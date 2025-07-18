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
    from . import LogCaptureUserConfiguration

class LogCaptureUserConfigurationListing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LogCaptureUserConfigurationListing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int',
            'entities': 'list[LogCaptureUserConfiguration]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'total': 'total',
            'entities': 'entities',
            'self_uri': 'selfUri'
        }

        self._total = None
        self._entities = None
        self._self_uri = None

    @property
    def total(self) -> int:
        """
        Gets the total of this LogCaptureUserConfigurationListing.


        :return: The total of this LogCaptureUserConfigurationListing.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int) -> None:
        """
        Sets the total of this LogCaptureUserConfigurationListing.


        :param total: The total of this LogCaptureUserConfigurationListing.
        :type: int
        """
        

        self._total = total

    @property
    def entities(self) -> List['LogCaptureUserConfiguration']:
        """
        Gets the entities of this LogCaptureUserConfigurationListing.


        :return: The entities of this LogCaptureUserConfigurationListing.
        :rtype: list[LogCaptureUserConfiguration]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['LogCaptureUserConfiguration']) -> None:
        """
        Sets the entities of this LogCaptureUserConfigurationListing.


        :param entities: The entities of this LogCaptureUserConfigurationListing.
        :type: list[LogCaptureUserConfiguration]
        """
        

        self._entities = entities

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this LogCaptureUserConfigurationListing.


        :return: The self_uri of this LogCaptureUserConfigurationListing.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this LogCaptureUserConfigurationListing.


        :param self_uri: The self_uri of this LogCaptureUserConfigurationListing.
        :type: str
        """
        

        self._self_uri = self_uri

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

