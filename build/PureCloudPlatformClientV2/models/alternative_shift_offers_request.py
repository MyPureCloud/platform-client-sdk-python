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
    from . import AlternativeShiftScheduleLookup

class AlternativeShiftOffersRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AlternativeShiftOffersRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'schedule': 'AlternativeShiftScheduleLookup',
            'query_week_date': 'date'
        }

        self.attribute_map = {
            'schedule': 'schedule',
            'query_week_date': 'queryWeekDate'
        }

        self._schedule = None
        self._query_week_date = None

    @property
    def schedule(self) -> 'AlternativeShiftScheduleLookup':
        """
        Gets the schedule of this AlternativeShiftOffersRequest.
        The existing schedule being used to find alternative shift offers

        :return: The schedule of this AlternativeShiftOffersRequest.
        :rtype: AlternativeShiftScheduleLookup
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: 'AlternativeShiftScheduleLookup') -> None:
        """
        Sets the schedule of this AlternativeShiftOffersRequest.
        The existing schedule being used to find alternative shift offers

        :param schedule: The schedule of this AlternativeShiftOffersRequest.
        :type: AlternativeShiftScheduleLookup
        """
        

        self._schedule = schedule

    @property
    def query_week_date(self) -> date:
        """
        Gets the query_week_date of this AlternativeShiftOffersRequest.
        The start date for the week in this schedule in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The query_week_date of this AlternativeShiftOffersRequest.
        :rtype: date
        """
        return self._query_week_date

    @query_week_date.setter
    def query_week_date(self, query_week_date: date) -> None:
        """
        Sets the query_week_date of this AlternativeShiftOffersRequest.
        The start date for the week in this schedule in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param query_week_date: The query_week_date of this AlternativeShiftOffersRequest.
        :type: date
        """
        

        self._query_week_date = query_week_date

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
