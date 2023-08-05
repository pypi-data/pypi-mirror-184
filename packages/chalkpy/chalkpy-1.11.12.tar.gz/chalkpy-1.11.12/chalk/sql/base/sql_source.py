import inspect
import os.path
from dataclasses import dataclass
from os import PathLike
from typing import Any, ClassVar, Dict, List, Mapping, Optional, Set, Type, TypeVar, Union

import sqlalchemy.sql.functions
from sqlalchemy.orm import InstrumentedAttribute, Session

from chalk.features import Feature, Features, FeatureWrapper, unwrap_feature
from chalk.sql.base.protocols import (
    BaseSQLSourceProtocol,
    ChalkQueryProtocol,
    DBSessionMakerProtocol,
    IncrementalSettings,
    StringChalkQueryProtocol,
    TableIngestProtocol,
)
from chalk.sql.base.session import DBSessionMaker
from chalk.sql.integrations.chalk_query import ChalkQuery
from chalk.sql.integrations.string_chalk_query import StringChalkQuery

TTableIngestMixIn = TypeVar("TTableIngestMixIn", bound="TableIngestMixIn")


@dataclass
class TableIngestionPreferences:
    features: Type[Features]
    ignore_columns: Set[str]
    ignore_features: Set[str]
    require_columns: Set[str]
    require_features: Set[str]
    column_to_feature: Dict[str, str]
    cdc: Optional[Union[bool, IncrementalSettings]]


def _force_set_str(x: Optional[List[Any]]) -> Set[str]:
    return set() if x is None else set(map(str, x))


class TableIngestMixIn(TableIngestProtocol):
    ingested_tables: Dict[str, TableIngestionPreferences]

    def with_table(
        self: Type[TTableIngestMixIn],
        *,
        name: str,
        features: Type[Union[Features, Any]],
        ignore_columns: Optional[List[str]] = None,
        ignore_features: Optional[List[Union[str, Any]]] = None,
        require_columns: Optional[List[str]] = None,
        require_features: Optional[List[Union[str, Any]]] = None,
        column_to_feature: Optional[Dict[str, Any]] = None,
        cdc: Optional[Union[bool, IncrementalSettings]] = None,
    ) -> TTableIngestMixIn:
        if name in self.ingested_tables:
            raise ValueError(f"The table {name} is ingested twice.")
        self.ingested_tables[name] = TableIngestionPreferences(
            features=features,
            ignore_columns=_force_set_str(ignore_columns),
            ignore_features=_force_set_str(ignore_features),
            require_columns=_force_set_str(require_columns),
            require_features=_force_set_str(require_features),
            column_to_feature={k: str(v) for k, v in (column_to_feature or {}).items()},
            cdc=cdc,
        )
        return self


class BaseSQLSource(BaseSQLSourceProtocol):
    registry: ClassVar[List["BaseSQLSource"]] = []

    def __init__(self, session_maker: Optional[DBSessionMaker] = None):
        self._session_maker = session_maker or DBSessionMaker()
        self._incremental_settings = None
        self.registry.append(self)

    def set_session_maker(self, maker: DBSessionMakerProtocol) -> None:
        self._session_maker = maker

    def query_sql_file(
        self,
        path: Union[str, bytes, PathLike],
        fields: Optional[Mapping[str, Union[Feature, Any]]] = None,
        args: Optional[Mapping[str, str]] = None,
    ) -> StringChalkQueryProtocol:
        sql_string = None
        if os.path.isfile(path):
            with open(path) as f:
                sql_string = f.read()
        else:
            caller_filename = inspect.stack()[1].filename
            dir_path = os.path.dirname(os.path.realpath(caller_filename))
            if isinstance(path, bytes):
                path = path.decode("utf-8")
            relative_path = os.path.join(dir_path, path)
            if os.path.isfile(relative_path):
                with open(relative_path) as f:
                    sql_string = f.read()
        if sql_string is None:
            raise FileNotFoundError(f"No such file: '{str(path)}'")
        return self.query_string(
            query=sql_string,
            fields=fields,
            args=args,
        )

    def query_string(
        self,
        query: str,
        fields: Optional[Mapping[str, Union[Feature, Any]]] = None,
        args: Optional[Mapping[str, str]] = None,
    ) -> StringChalkQueryProtocol:
        fields = fields or {}
        session = self._session_maker.get_session(self)
        fields = {f: unwrap_feature(v) if isinstance(v, FeatureWrapper) else v for (f, v) in fields.items()}
        return StringChalkQuery(session=session, source=self, query=query, fields=fields, args=args)

    def raw_session(self) -> Session:
        return self._session_maker.get_session(self)._raw_session

    def query(self, *entities, **kwargs) -> ChalkQueryProtocol:
        targets = []
        features = []
        for e in entities:
            if isinstance(e, Features):
                for f in e.features:
                    assert isinstance(f, Feature), f"Feature {f} must inherit from Feature"
                    assert f.attribute_name is not None
                    try:
                        feature_value = getattr(e, f.attribute_name)
                    except AttributeError:
                        continue
                    if isinstance(feature_value, InstrumentedAttribute):
                        features.append(f)
                        targets.append(feature_value.label(f.fqn))
                    elif isinstance(feature_value, sqlalchemy.sql.functions.GenericFunction):
                        features.append(f)
                        targets.append(feature_value.label(f.fqn))
            else:
                targets.append(e)
        session = self._session_maker.get_session(self)
        session.update_query(lambda x: x.query(*targets, **kwargs))

        return ChalkQuery(
            features=features,
            session=session,
            source=self,
        )
