import abc
from dataclasses import dataclass
from typing import Optional


class DataSource(abc.ABC):
    """
    Generic data source for connecting extrenal data sources to clickhouse.
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def definition_sql(self):
        """
        Returns the SQL definition of the data source.
        """


class PostgresqlSource(DataSource):
    def __init__(
        self,
        database,
        table,
        host="localhost",
        port=5432,
        user="postgres",
        password="",
        invalidate_query=None,
    ):
        super().__init__()
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.table = table
        self.invalidate_query = invalidate_query

    def definition_sql(self):
        invalidate_query = ""
        if self.invalidate_query:
            invalidate_query = f"invalidate_query '{self.invalidate_query}'"
        return f"""SOURCE(POSTGRESQL(
            port {self.port}
            host '{self.host}'
            user '{self.user}'
            password '{self.password}'
            db '{self.database}'
            table '{self.table}'
            {invalidate_query}
        ))"""


class ClickhouseSource(DataSource):
    def __init__(self, database, table, host="localhost", port=9000, user="default", password=""):
        super().__init__()
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.table = table

    def definition_sql(self):
        return f"""SOURCE(CLICKHOUSE(
            port {self.port}
            host '{self.host}'
            user '{self.user}'
            password '{self.password}'
            db '{self.database}'
            table '{self.table}'
        ))"""


@dataclass
class DictionaryAttr:
    name: str
    type: str
    expression: Optional[str] = None
    null_value: str = "NULL"
    injective: bool = False

    def definition_sql(self):
        expression = f"EXPRESSION {self.expression}" if self.expression else ""
        return (
            f"{self.name} {self.type} DEFAULT {self.null_value} {expression} "
            f"{'INJECTIVE' if self.injective else ''}"
        )


class DictionaryDefinition:
    def __init__(
        self,
        name: str,
        source: DataSource,
        key: str,
        layout: str,
        attrs: [DictionaryAttr],
        lifetime_min: int = 600,
        lifetime_max: int = 720,
    ):
        self.name = name
        self.key = key
        self.source = source
        self.layout = layout
        self.attrs = attrs
        self.lifetime_min = lifetime_min
        self.lifetime_max = lifetime_max

    def definition_sql(self):
        attrs = ",\n".join([attr.definition_sql() for attr in self.attrs])
        return (
            f"CREATE DICTIONARY {self.name} ("
            f"{self.key} UInt64,\n"
            f"{attrs}"
            f") "
            f"PRIMARY KEY {self.key} "
            f"{self.source.definition_sql()} "
            f"LAYOUT ({self.layout.upper()}()) "
            f"LIFETIME(MIN {self.lifetime_min} MAX {self.lifetime_max})"
        )
