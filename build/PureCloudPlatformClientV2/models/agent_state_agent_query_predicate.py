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


class AgentStateAgentQueryPredicate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentStateAgentQueryPredicate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dimension': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'dimension': 'dimension',
            'value': 'value'
        }

        self._dimension = None
        self._value = None

    @property
    def dimension(self) -> str:
        """
        Gets the dimension of this AgentStateAgentQueryPredicate.
        Left hand side for dimension predicates

        :return: The dimension of this AgentStateAgentQueryPredicate.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: str) -> None:
        """
        Sets the dimension of this AgentStateAgentQueryPredicate.
        Left hand side for dimension predicates

        :param dimension: The dimension of this AgentStateAgentQueryPredicate.
        :type: str
        """
        if isinstance(dimension, int):
            dimension = str(dimension)
        allowed_values = ["activeQueueId", "assignedSkillId", "assignedLanguageId", "divisionId", "userId", "managerId", "systemPresence", "organizationPresenceId", "routingStatus", "isOutOfOffice", "online"]
        if dimension.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for dimension -> " + dimension)
            self._dimension = "outdated_sdk_version"
        else:
            self._dimension = dimension

    @property
    def value(self) -> str:
        """
        Gets the value of this AgentStateAgentQueryPredicate.
        Right hand side for dimension predicates

        :return: The value of this AgentStateAgentQueryPredicate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this AgentStateAgentQueryPredicate.
        Right hand side for dimension predicates

        :param value: The value of this AgentStateAgentQueryPredicate.
        :type: str
        """
        

        self._value = value

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

