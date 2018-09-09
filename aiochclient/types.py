from datetime import datetime as dt
from enum import Enum


__all__ = ["what_type", "convert"]


def date(string):
    return dt.strptime(string, "%Y-%m-%d").date()


def datetime(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")


class Types(Enum):
    INT = int
    FLOAT = float
    STRING = str
    DATE = date
    DATETIME = datetime


TYPES_MAPPING = {
    "UInt8": Types.INT,
    "UInt16": Types.INT,
    "UInt32": Types.INT,
    "UInt64": Types.INT,
    "Int8": Types.INT,
    "Int16": Types.INT,
    "Int32": Types.INT,
    "Int64": Types.INT,
    "Float32": Types.FLOAT,
    "Float64": Types.FLOAT,
    "String": Types.STRING,
    "FixedString": Types.STRING,
    "Date": Types.DATE,
    "DateTime": Types.DATETIME,
    "Enum8": Types.STRING,
    "Enum16": Types.STRING,
}


def what_type(name: str) -> type:
    """ Returns python type from clickhouse type name """
    return TYPES_MAPPING[name].value


def convert(typ, val):
    if val == r'\N':
        return None
    return typ(val)
