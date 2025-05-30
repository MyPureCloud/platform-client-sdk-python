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
    from . import LocalDateRange

class TimeOffBalanceRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TimeOffBalanceRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_code_ids': 'list[str]',
            'date_ranges': 'list[LocalDateRange]'
        }

        self.attribute_map = {
            'activity_code_ids': 'activityCodeIds',
            'date_ranges': 'dateRanges'
        }

        self._activity_code_ids = None
        self._date_ranges = None

    @property
    def activity_code_ids(self) -> List[str]:
        """
        Gets the activity_code_ids of this TimeOffBalanceRequest.
        The set of activity code IDs for which to query available time off balances

        :return: The activity_code_ids of this TimeOffBalanceRequest.
        :rtype: list[str]
        """
        return self._activity_code_ids

    @activity_code_ids.setter
    def activity_code_ids(self, activity_code_ids: List[str]) -> None:
        """
        Sets the activity_code_ids of this TimeOffBalanceRequest.
        The set of activity code IDs for which to query available time off balances

        :param activity_code_ids: The activity_code_ids of this TimeOffBalanceRequest.
        :type: list[str]
        """
        

        self._activity_code_ids = activity_code_ids

    @property
    def date_ranges(self) -> List['LocalDateRange']:
        """
        Gets the date_ranges of this TimeOffBalanceRequest.
        The list of date ranges for which to query time off balance

        :return: The date_ranges of this TimeOffBalanceRequest.
        :rtype: list[LocalDateRange]
        """
        return self._date_ranges

    @date_ranges.setter
    def date_ranges(self, date_ranges: List['LocalDateRange']) -> None:
        """
        Sets the date_ranges of this TimeOffBalanceRequest.
        The list of date ranges for which to query time off balance

        :param date_ranges: The date_ranges of this TimeOffBalanceRequest.
        :type: list[LocalDateRange]
        """
        

        self._date_ranges = date_ranges

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

