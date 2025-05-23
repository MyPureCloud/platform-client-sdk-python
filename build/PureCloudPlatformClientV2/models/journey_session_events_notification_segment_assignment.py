# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import JourneySessionEventsNotificationSegment

class JourneySessionEventsNotificationSegmentAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneySessionEventsNotificationSegmentAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'segment': 'JourneySessionEventsNotificationSegment',
            'assigned_date': 'datetime'
        }

        self.attribute_map = {
            'segment': 'segment',
            'assigned_date': 'assignedDate'
        }

        self._segment = None
        self._assigned_date = None

    @property
    def segment(self) -> 'JourneySessionEventsNotificationSegment':
        """
        Gets the segment of this JourneySessionEventsNotificationSegmentAssignment.


        :return: The segment of this JourneySessionEventsNotificationSegmentAssignment.
        :rtype: JourneySessionEventsNotificationSegment
        """
        return self._segment

    @segment.setter
    def segment(self, segment: 'JourneySessionEventsNotificationSegment') -> None:
        """
        Sets the segment of this JourneySessionEventsNotificationSegmentAssignment.


        :param segment: The segment of this JourneySessionEventsNotificationSegmentAssignment.
        :type: JourneySessionEventsNotificationSegment
        """
        

        self._segment = segment

    @property
    def assigned_date(self) -> datetime:
        """
        Gets the assigned_date of this JourneySessionEventsNotificationSegmentAssignment.


        :return: The assigned_date of this JourneySessionEventsNotificationSegmentAssignment.
        :rtype: datetime
        """
        return self._assigned_date

    @assigned_date.setter
    def assigned_date(self, assigned_date: datetime) -> None:
        """
        Sets the assigned_date of this JourneySessionEventsNotificationSegmentAssignment.


        :param assigned_date: The assigned_date of this JourneySessionEventsNotificationSegmentAssignment.
        :type: datetime
        """
        

        self._assigned_date = assigned_date

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

