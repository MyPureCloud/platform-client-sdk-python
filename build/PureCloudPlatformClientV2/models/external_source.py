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
    from . import LinkConfiguration

class ExternalSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'active': 'bool',
            'link_configuration': 'LinkConfiguration',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'active': 'active',
            'link_configuration': 'linkConfiguration',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._active = None
        self._link_configuration = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ExternalSource.
        The globally unique identifier for the object.

        :return: The id of this ExternalSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ExternalSource.
        The globally unique identifier for the object.

        :param id: The id of this ExternalSource.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ExternalSource.
        The name of the external source.

        :return: The name of this ExternalSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ExternalSource.
        The name of the external source.

        :param name: The name of this ExternalSource.
        :type: str
        """
        

        self._name = name

    @property
    def active(self) -> bool:
        """
        Gets the active of this ExternalSource.


        :return: The active of this ExternalSource.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool) -> None:
        """
        Sets the active of this ExternalSource.


        :param active: The active of this ExternalSource.
        :type: bool
        """
        

        self._active = active

    @property
    def link_configuration(self) -> 'LinkConfiguration':
        """
        Gets the link_configuration of this ExternalSource.


        :return: The link_configuration of this ExternalSource.
        :rtype: LinkConfiguration
        """
        return self._link_configuration

    @link_configuration.setter
    def link_configuration(self, link_configuration: 'LinkConfiguration') -> None:
        """
        Sets the link_configuration of this ExternalSource.


        :param link_configuration: The link_configuration of this ExternalSource.
        :type: LinkConfiguration
        """
        

        self._link_configuration = link_configuration

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ExternalSource.
        The URI for this object

        :return: The self_uri of this ExternalSource.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ExternalSource.
        The URI for this object

        :param self_uri: The self_uri of this ExternalSource.
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

