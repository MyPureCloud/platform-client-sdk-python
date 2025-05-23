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


class EntityChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EntityChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entity_id': 'str',
            'entity_name': 'str',
            'entity_type': 'str',
            'old_values': 'list[str]',
            'new_values': 'list[str]'
        }

        self.attribute_map = {
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'entity_type': 'entityType',
            'old_values': 'oldValues',
            'new_values': 'newValues'
        }

        self._entity_id = None
        self._entity_name = None
        self._entity_type = None
        self._old_values = None
        self._new_values = None

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this EntityChange.
        Id of the entity that was changed

        :return: The entity_id of this EntityChange.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this EntityChange.
        Id of the entity that was changed

        :param entity_id: The entity_id of this EntityChange.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def entity_name(self) -> str:
        """
        Gets the entity_name of this EntityChange.
        Name of the entity that was changed

        :return: The entity_name of this EntityChange.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name: str) -> None:
        """
        Sets the entity_name of this EntityChange.
        Name of the entity that was changed

        :param entity_name: The entity_name of this EntityChange.
        :type: str
        """
        

        self._entity_name = entity_name

    @property
    def entity_type(self) -> str:
        """
        Gets the entity_type of this EntityChange.
        Type of the entity that was changed

        :return: The entity_type of this EntityChange.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str) -> None:
        """
        Sets the entity_type of this EntityChange.
        Type of the entity that was changed

        :param entity_type: The entity_type of this EntityChange.
        :type: str
        """
        

        self._entity_type = entity_type

    @property
    def old_values(self) -> List[str]:
        """
        Gets the old_values of this EntityChange.
        Previous values for the entity.

        :return: The old_values of this EntityChange.
        :rtype: list[str]
        """
        return self._old_values

    @old_values.setter
    def old_values(self, old_values: List[str]) -> None:
        """
        Sets the old_values of this EntityChange.
        Previous values for the entity.

        :param old_values: The old_values of this EntityChange.
        :type: list[str]
        """
        

        self._old_values = old_values

    @property
    def new_values(self) -> List[str]:
        """
        Gets the new_values of this EntityChange.
        New values for the entity.

        :return: The new_values of this EntityChange.
        :rtype: list[str]
        """
        return self._new_values

    @new_values.setter
    def new_values(self, new_values: List[str]) -> None:
        """
        Sets the new_values of this EntityChange.
        New values for the entity.

        :param new_values: The new_values of this EntityChange.
        :type: list[str]
        """
        

        self._new_values = new_values

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

