# -*- coding: utf-8 -*-
"""
Copyright (c) 2017
Fraunhofer Institute for Manufacturing Engineering
and Automation (IPA)
Author: Daniel Stock
mailto: daniel DOT stock AT ipa DOT fraunhofer DOT com
See the file "LICENSE" for the full license governing this code.
"""

import datetime
from enum import Enum


class DataType(Enum):
    STRING = "string"
    INT32 = "int32"
    INT64 = "int64"
    DOUBLE = "double"
    FLOAT = "float"
    DATETIME = "date-time"
    BOOLEAN = "boolean"
    BYTE = "byte"


def getDataType(format):
    dataType = {}
    if format == "string" or format == DataType.STRING or format == str:
        dataType["type"] = "string"
    elif format == "int32" or format == DataType.INT32:
        dataType["type"] = "integer"
        dataType["format"] = "int32"
    elif (
        format == "int64"
        or format == DataType.INT64
        or format == int
        or format == "integer"
    ):
        dataType["type"] = "integer"
        dataType["format"] = "int64"
    elif format == "float" or format == DataType.FLOAT:
        dataType["type"] = "number"
        dataType["format"] = "float"
    elif (
        format == "double"
        or format == DataType.DOUBLE
        or format == float
        or format == "number"
    ):
        dataType["type"] = "number"
        dataType["format"] = "double"
    elif (
        format == "date-time"
        or format == DataType.DATETIME
        or format == datetime
        or format == datetime.datetime
    ):
        dataType["type"] = "string"
        dataType["format"] = "date-time"
    elif format == "boolean" or format == DataType.BOOLEAN or format == bool:
        dataType["type"] = "boolean"
    elif format == "byte" or format == DataType.BYTE:
        dataType["type"] = "string"
        dataType["format"] = "byte"
    else:
        print("Unknown dataType: " + str(format))
    return dataType


def convertDataType(format):
    dataType = {}
    if format == DataType.STRING:
        return str
    elif format == DataType.INT32:
        return int
    elif format == DataType.INT64:
        return int
    elif format == DataType.FLOAT:
        return float
    elif format == DataType.DOUBLE:
        return float
    elif format == DataType.DATETIME:
        return datetime.datetime
    elif DataType.BOOLEAN:
        return bool
    elif format == DataType.BYTE:
        return bytes
    else:
        print("Unknown dataType: " + str(format))
    return dataType
