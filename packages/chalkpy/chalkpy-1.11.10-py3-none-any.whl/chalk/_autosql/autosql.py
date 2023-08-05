from typing import Iterable, List, Mapping, Optional, Union

import polars as pl
import pyarrow as pa

from chalk.client.client_impl import ChalkConfigurationException
from chalk.features.dataframe import DataFrame

try:
    import duckdb
    import sqlglot
except ModuleNotFoundError:
    duckdb = None
    sqlglot = None

from chalk.utils.string import normalize_string_for_matching


def _resolve_implicit_col_feature_mappings_str(
    explicit_mappings: Mapping[str, str],
    expected_features: Iterable[str],
    row_column_names: List[str],
) -> List[Optional[str]]:
    implicit_mappings = {normalize_string_for_matching(f): f for f in expected_features}
    return [
        explicit_mappings.get(col)
        if col in explicit_mappings
        else implicit_mappings.get(normalize_string_for_matching(col), None)
        for col in row_column_names
    ]


def query_arrow_table(query: str, table: pa.Table) -> pa.Table:
    if duckdb is None or sqlglot is None:
        raise ChalkConfigurationException.missing_dependency("chalkpy[sql]")
    t: sqlglot.exp.Table
    table_names = list({t.name for t in sqlglot.parse_one(query).find_all(sqlglot.exp.Table)})
    con = duckdb.connect(database=":memory:")
    if len(table_names) > 1:
        raise ValueError(f"Query should target only one table. Found: {', '.join(table_names)}")
    if len(table_names) == 1:
        con.register(table_names[0], table)
    result_table = con.execute(query).fetch_arrow_table()
    return result_table


def query_as_features(
    query: str,
    fqn_to_name: Mapping[str, str],
    table: pa.Table,
) -> pl.DataFrame:
    res = query_arrow_table(query, table)
    col_feature_mappings = _resolve_implicit_col_feature_mappings_str(
        # Note: snowflake by default capitalizes all table and column names, although it's
        # technically possible to disable this behavior by quoting things when creating your schema
        # explicit_mappings={k.upper(): v for k, v in self._fields_normalized().items()},
        explicit_mappings={},
        row_column_names=res.column_names,
        expected_features=fqn_to_name.values(),
    )
    name_to_fqn = {v: k for k, v in fqn_to_name.items()}
    renamed = (
        pl.from_arrow(res)
        .drop([col for col, f in zip(res.column_names, col_feature_mappings) if f is None])
        .rename({col: name_to_fqn[f] for col, f in zip(res.column_names, col_feature_mappings) if f is not None})
    )
    return renamed


def query_as_feature_formatted(
    formatted_query: str,
    fqn_to_name: Mapping[str, str],
    table: Union[pa.Table, DataFrame, pl.DataFrame, pl.LazyFrame],
) -> pl.DataFrame:
    # We're going to string replace whatever was there before
    unformatted = formatted_query.replace(str(table), "__chalk_table__")
    pa_table = table
    if isinstance(table, DataFrame):
        pa_table = table.to_polars().collect().to_arrow()
    elif isinstance(table, pl.DataFrame):
        pa_table = table.to_arrow()
    elif isinstance(table, pl.LazyFrame):
        pa_table = table.collect().to_arrow()

    if not isinstance(pa_table, pa.Table):
        raise ValueError(f"Unexpected table type: {type(pa_table)}")

    return query_as_features(unformatted, fqn_to_name, pa_table)
