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


class SchedulingNoForecastOptionsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SchedulingNoForecastOptionsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'shift_length': 'str',
            'shift_start': 'str'
        }

        self.attribute_map = {
            'shift_length': 'shiftLength',
            'shift_start': 'shiftStart'
        }

        self._shift_length = None
        self._shift_start = None

    @property
    def shift_length(self) -> str:
        """
        Gets the shift_length of this SchedulingNoForecastOptionsRequest.
        The shift length option to apply if no forecast is supplied

        :return: The shift_length of this SchedulingNoForecastOptionsRequest.
        :rtype: str
        """
        return self._shift_length

    @shift_length.setter
    def shift_length(self, shift_length: str) -> None:
        """
        Sets the shift_length of this SchedulingNoForecastOptionsRequest.
        The shift length option to apply if no forecast is supplied

        :param shift_length: The shift_length of this SchedulingNoForecastOptionsRequest.
        :type: str
        """
        if isinstance(shift_length, int):
            shift_length = str(shift_length)
        allowed_values = ["Shortest", "Median", "Longest", "Random"]
        if shift_length.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for shift_length -> " + shift_length)
            self._shift_length = "outdated_sdk_version"
        else:
            self._shift_length = shift_length

    @property
    def shift_start(self) -> str:
        """
        Gets the shift_start of this SchedulingNoForecastOptionsRequest.
        The shift start option to apply if no forecast is supplied

        :return: The shift_start of this SchedulingNoForecastOptionsRequest.
        :rtype: str
        """
        return self._shift_start

    @shift_start.setter
    def shift_start(self, shift_start: str) -> None:
        """
        Sets the shift_start of this SchedulingNoForecastOptionsRequest.
        The shift start option to apply if no forecast is supplied

        :param shift_start: The shift_start of this SchedulingNoForecastOptionsRequest.
        :type: str
        """
        if isinstance(shift_start, int):
            shift_start = str(shift_start)
        allowed_values = ["Earliest", "Median", "Latest", "Random"]
        if shift_start.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for shift_start -> " + shift_start)
            self._shift_start = "outdated_sdk_version"
        else:
            self._shift_start = shift_start

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

