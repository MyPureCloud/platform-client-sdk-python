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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import AvailabilityRange
    from . import RequiredLocalDateRange

class FixedAvailability(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FixedAvailability - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'availability_range': 'AvailabilityRange',
            'date_range': 'RequiredLocalDateRange',
            'days_of_week': 'list[str]'
        }

        self.attribute_map = {
            'availability_range': 'availabilityRange',
            'date_range': 'dateRange',
            'days_of_week': 'daysOfWeek'
        }

        self._availability_range = None
        self._date_range = None
        self._days_of_week = None

    @property
    def availability_range(self) -> 'AvailabilityRange':
        """
        Gets the availability_range of this FixedAvailability.
        The range of time of day the activity can be scheduled

        :return: The availability_range of this FixedAvailability.
        :rtype: AvailabilityRange
        """
        return self._availability_range

    @availability_range.setter
    def availability_range(self, availability_range: 'AvailabilityRange') -> None:
        """
        Sets the availability_range of this FixedAvailability.
        The range of time of day the activity can be scheduled

        :param availability_range: The availability_range of this FixedAvailability.
        :type: AvailabilityRange
        """
        

        self._availability_range = availability_range

    @property
    def date_range(self) -> 'RequiredLocalDateRange':
        """
        Gets the date_range of this FixedAvailability.
        The range of date for which the activity plan could be scheduled

        :return: The date_range of this FixedAvailability.
        :rtype: RequiredLocalDateRange
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range: 'RequiredLocalDateRange') -> None:
        """
        Sets the date_range of this FixedAvailability.
        The range of date for which the activity plan could be scheduled

        :param date_range: The date_range of this FixedAvailability.
        :type: RequiredLocalDateRange
        """
        

        self._date_range = date_range

    @property
    def days_of_week(self) -> List[str]:
        """
        Gets the days_of_week of this FixedAvailability.
        The days of week available for scheduling. Empty list or null means daysOfWeek is not considered

        :return: The days_of_week of this FixedAvailability.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week: List[str]) -> None:
        """
        Sets the days_of_week of this FixedAvailability.
        The days of week available for scheduling. Empty list or null means daysOfWeek is not considered

        :param days_of_week: The days_of_week of this FixedAvailability.
        :type: list[str]
        """
        

        self._days_of_week = days_of_week

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
