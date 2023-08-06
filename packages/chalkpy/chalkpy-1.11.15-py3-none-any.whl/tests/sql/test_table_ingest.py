from typing import cast

import pytest

from chalk.features import features
from chalk.sql import PostgreSQLSource
from chalk.sql.integrations.postgres import PostgreSQLSourceImpl

try:
    import psycopg2
except ImportError:
    psycopg2 = None


@features
class UserFeatures:
    id: str


@features
class LibraryFeatures:
    id: str


@pytest.mark.skipif(psycopg2 is None, reason="psycopg2 is not installed")
def test_table_builder():
    source: PostgreSQLSourceImpl = cast(
        PostgreSQLSourceImpl,
        PostgreSQLSource()
        .with_table(name="users", features=UserFeatures)
        .with_table(name="libraries", features=LibraryFeatures),
    )
    assert len(source.ingested_tables) == 2
