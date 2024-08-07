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


class LimitCount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LimitCount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'estimated_count': 'int',
            'max': 'int',
            'entity_id': 'str',
            'user_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'estimated_count': 'estimatedCount',
            'max': 'max',
            'entity_id': 'entityId',
            'user_id': 'userId'
        }

        self._name = None
        self._estimated_count = None
        self._max = None
        self._entity_id = None
        self._user_id = None

    @property
    def name(self) -> str:
        """
        Gets the name of this LimitCount.
        The name of the limit.

        :return: The name of this LimitCount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this LimitCount.
        The name of the limit.

        :param name: The name of this LimitCount.
        :type: str
        """
        

        self._name = name

    @property
    def estimated_count(self) -> int:
        """
        Gets the estimated_count of this LimitCount.
        The total used count of the limit.

        :return: The estimated_count of this LimitCount.
        :rtype: int
        """
        return self._estimated_count

    @estimated_count.setter
    def estimated_count(self, estimated_count: int) -> None:
        """
        Sets the estimated_count of this LimitCount.
        The total used count of the limit.

        :param estimated_count: The estimated_count of this LimitCount.
        :type: int
        """
        

        self._estimated_count = estimated_count

    @property
    def max(self) -> int:
        """
        Gets the max of this LimitCount.
        The maximum value of the limit.

        :return: The max of this LimitCount.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max: int) -> None:
        """
        Sets the max of this LimitCount.
        The maximum value of the limit.

        :param max: The max of this LimitCount.
        :type: int
        """
        

        self._max = max

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this LimitCount.
        The entity which makes this count unique. The context of what the entity is would be dependant on the limit. May not be applicable for all limits.

        :return: The entity_id of this LimitCount.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this LimitCount.
        The entity which makes this count unique. The context of what the entity is would be dependant on the limit. May not be applicable for all limits.

        :param entity_id: The entity_id of this LimitCount.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this LimitCount.
        The user which makes this count unique. May not be applicable for all limits.

        :return: The user_id of this LimitCount.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this LimitCount.
        The user which makes this count unique. May not be applicable for all limits.

        :param user_id: The user_id of this LimitCount.
        :type: str
        """
        

        self._user_id = user_id

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

