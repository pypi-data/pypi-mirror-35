# -*- coding: utf-8 -*-
"""
Copyright (c) 2017
Fraunhofer Institute for Manufacturing Engineering
and Automation (IPA)
Author: Daniel Stock
mailto: daniel DOT stock AT ipa DOT fraunhofer DOT com
See the file "LICENSE" for the full license governing this code.
"""

from msb_client.DataFormat import *
from msb_client.ComplexDataFormat import *
import json, copy


class Event:
    def __init__(
        self,
        eventId,
        event_name,
        event_description,
        event_dataFormat,
        priority=0,
        isArray=False,
    ):
        self.eventId = eventId
        self.name = event_name
        self.description = event_description
        if isinstance(event_dataFormat, DataFormat) or isinstance(
            event_dataFormat, ComplexDataFormat
        ):
            self.dataFormat = copy.deepcopy(event_dataFormat).getDataFormat()
            self.df = event_dataFormat
        elif isinstance(event_dataFormat, DataType):
            self.dataFormat = DataFormat(event_dataFormat, isArray).getDataFormat()
            self.df = convertDataType(event_dataFormat)
        elif type(event_dataFormat) == type(datetime):
            self.dataFormat = DataFormat(event_dataFormat, isArray).getDataFormat()
            self.df = datetime.datetime
        elif event_dataFormat is None:
            self.dataFormat = None
            self.df = None
        else:
            try:
                json_object = {"dataObject": json.loads(event_dataFormat)}
                self.dataFormat = json_object
            except:
                self.dataFormat = DataFormat(event_dataFormat, isArray).getDataFormat()
            self.df = event_dataFormat
        self.priority = priority
        self.isArray = isArray

    id = 0
    dataObject = 0
