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


class RoutingRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        RoutingRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operator': 'str',
            'threshold': 'int',
            'wait_seconds': 'float'
        }

        self.attribute_map = {
            'operator': 'operator',
            'threshold': 'threshold',
            'wait_seconds': 'waitSeconds'
        }

        self._operator = None
        self._threshold = None
        self._wait_seconds = None

    @property
    def operator(self) -> str:
        """
        Gets the operator of this RoutingRule.
        matching operator.  MEETS_THRESHOLD matches any agent with a score at or above the rule's threshold.  ANY matches all specified agents, regardless of score.

        :return: The operator of this RoutingRule.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this RoutingRule.
        matching operator.  MEETS_THRESHOLD matches any agent with a score at or above the rule's threshold.  ANY matches all specified agents, regardless of score.

        :param operator: The operator of this RoutingRule.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["MEETS_THRESHOLD", "ANY"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def threshold(self) -> int:
        """
        Gets the threshold of this RoutingRule.
        threshold required for routing attempt (generally an agent score).  may be null for operator ANY.

        :return: The threshold of this RoutingRule.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold: int) -> None:
        """
        Sets the threshold of this RoutingRule.
        threshold required for routing attempt (generally an agent score).  may be null for operator ANY.

        :param threshold: The threshold of this RoutingRule.
        :type: int
        """
        

        self._threshold = threshold

    @property
    def wait_seconds(self) -> float:
        """
        Gets the wait_seconds of this RoutingRule.
        seconds to wait in this rule before moving to the next

        :return: The wait_seconds of this RoutingRule.
        :rtype: float
        """
        return self._wait_seconds

    @wait_seconds.setter
    def wait_seconds(self, wait_seconds: float) -> None:
        """
        Sets the wait_seconds of this RoutingRule.
        seconds to wait in this rule before moving to the next

        :param wait_seconds: The wait_seconds of this RoutingRule.
        :type: float
        """
        

        self._wait_seconds = wait_seconds

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

