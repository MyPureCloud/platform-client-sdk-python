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


class AiScoring(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AiScoring - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failure_type': 'str',
            'pending': 'bool',
            'date_last_changed': 'datetime'
        }

        self.attribute_map = {
            'failure_type': 'failureType',
            'pending': 'pending',
            'date_last_changed': 'dateLastChanged'
        }

        self._failure_type = None
        self._pending = None
        self._date_last_changed = None

    @property
    def failure_type(self) -> str:
        """
        Gets the failure_type of this AiScoring.
        The type of error that occurred while processing AI scores. It is null where there is no error.

        :return: The failure_type of this AiScoring.
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type: str) -> None:
        """
        Sets the failure_type of this AiScoring.
        The type of error that occurred while processing AI scores. It is null where there is no error.

        :param failure_type: The failure_type of this AiScoring.
        :type: str
        """
        if isinstance(failure_type, int):
            failure_type = str(failure_type)
        allowed_values = ["QuotaReached", "ParsingError", "ServiceError", "InvalidRequest", "DuplicateFormSameAgent", "Unauthorized"]
        if failure_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for failure_type -> " + failure_type)
            self._failure_type = "outdated_sdk_version"
        else:
            self._failure_type = failure_type

    @property
    def pending(self) -> bool:
        """
        Gets the pending of this AiScoring.
        Indicates whether AI scoring is currently processing the evaluation.

        :return: The pending of this AiScoring.
        :rtype: bool
        """
        return self._pending

    @pending.setter
    def pending(self, pending: bool) -> None:
        """
        Sets the pending of this AiScoring.
        Indicates whether AI scoring is currently processing the evaluation.

        :param pending: The pending of this AiScoring.
        :type: bool
        """
        

        self._pending = pending

    @property
    def date_last_changed(self) -> datetime:
        """
        Gets the date_last_changed of this AiScoring.
        The date when the AI scores were last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_last_changed of this AiScoring.
        :rtype: datetime
        """
        return self._date_last_changed

    @date_last_changed.setter
    def date_last_changed(self, date_last_changed: datetime) -> None:
        """
        Sets the date_last_changed of this AiScoring.
        The date when the AI scores were last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_last_changed: The date_last_changed of this AiScoring.
        :type: datetime
        """
        

        self._date_last_changed = date_last_changed

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

