# -*- coding: utf-8 -*-
"""
Copyright (c) 2017
Fraunhofer Institute for Manufacturing Engineering
and Automation (IPA)
Author: Daniel Stock
mailto: daniel DOT stock AT ipa DOT fraunhofer DOT com
See the file "LICENSE" for the full license governing this code.
"""

from msb_client.DataType import getDataType


class DataFormat:
    def __init__(self, dataType=None, isArray=None):
        self.isArray = isArray
        dataFormat = {}
        dataObject = {}
        if isArray:
            dataObject["type"] = "array"
            dataObject["items"] = getDataType(dataType)
            dataFormat["dataObject"] = dataObject
        else:
            dataObject = getDataType(dataType)
            dataFormat["dataObject"] = dataObject
        self.dataFormat = dataFormat

    def getDataFormat(self):
        return self.dataFormat
