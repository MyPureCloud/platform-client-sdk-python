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


class BuSearchAgentSchedulesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuSearchAgentSchedulesRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'user_ids': 'list[str]'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'user_ids': 'userIds'
        }

        self._start_date = None
        self._end_date = None
        self._user_ids = None

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this BuSearchAgentSchedulesRequest.
        Start date of the range to search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_date of this BuSearchAgentSchedulesRequest.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this BuSearchAgentSchedulesRequest.
        Start date of the range to search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_date: The start_date of this BuSearchAgentSchedulesRequest.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def end_date(self) -> datetime:
        """
        Gets the end_date of this BuSearchAgentSchedulesRequest.
        End date of the range to search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_date of this BuSearchAgentSchedulesRequest.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime) -> None:
        """
        Sets the end_date of this BuSearchAgentSchedulesRequest.
        End date of the range to search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_date: The end_date of this BuSearchAgentSchedulesRequest.
        :type: datetime
        """
        

        self._end_date = end_date

    @property
    def user_ids(self) -> List[str]:
        """
        Gets the user_ids of this BuSearchAgentSchedulesRequest.
        IDs of the users for whose schedules to search

        :return: The user_ids of this BuSearchAgentSchedulesRequest.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: List[str]) -> None:
        """
        Sets the user_ids of this BuSearchAgentSchedulesRequest.
        IDs of the users for whose schedules to search

        :param user_ids: The user_ids of this BuSearchAgentSchedulesRequest.
        :type: list[str]
        """
        

        self._user_ids = user_ids

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

