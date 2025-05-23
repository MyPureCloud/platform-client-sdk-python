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
    from . import MetadataDocumentation
    from . import MetadataPresentation
    from . import MetadataResults

class AcceleratorSpecification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AcceleratorSpecification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'origin': 'str',
            'type': 'str',
            'classification': 'str',
            'tags': 'list[str]',
            'permissions': 'list[str]',
            'products': 'list[str]',
            'documentation': 'list[MetadataDocumentation]',
            'presentation': 'list[MetadataPresentation]',
            'results': 'MetadataResults',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'origin': 'origin',
            'type': 'type',
            'classification': 'classification',
            'tags': 'tags',
            'permissions': 'permissions',
            'products': 'products',
            'documentation': 'documentation',
            'presentation': 'presentation',
            'results': 'results',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._origin = None
        self._type = None
        self._classification = None
        self._tags = None
        self._permissions = None
        self._products = None
        self._documentation = None
        self._presentation = None
        self._results = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AcceleratorSpecification.
        The globally unique identifier for the object.

        :return: The id of this AcceleratorSpecification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AcceleratorSpecification.
        The globally unique identifier for the object.

        :param id: The id of this AcceleratorSpecification.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this AcceleratorSpecification.
        name of this accelerator

        :return: The name of this AcceleratorSpecification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this AcceleratorSpecification.
        name of this accelerator

        :param name: The name of this AcceleratorSpecification.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this AcceleratorSpecification.
        a description of the general purpose of this accelerator

        :return: The description of this AcceleratorSpecification.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this AcceleratorSpecification.
        a description of the general purpose of this accelerator

        :param description: The description of this AcceleratorSpecification.
        :type: str
        """
        

        self._description = description

    @property
    def origin(self) -> str:
        """
        Gets the origin of this AcceleratorSpecification.
        where the accelerator originated

        :return: The origin of this AcceleratorSpecification.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin: str) -> None:
        """
        Sets the origin of this AcceleratorSpecification.
        where the accelerator originated

        :param origin: The origin of this AcceleratorSpecification.
        :type: str
        """
        if isinstance(origin, int):
            origin = str(origin)
        allowed_values = ["Community", "Partner", "Genesys"]
        if origin.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for origin -> " + origin)
            self._origin = "outdated_sdk_version"
        else:
            self._origin = origin

    @property
    def type(self) -> str:
        """
        Gets the type of this AcceleratorSpecification.
        type of the artifact

        :return: The type of this AcceleratorSpecification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this AcceleratorSpecification.
        type of the artifact

        :param type: The type of this AcceleratorSpecification.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Module", "Accelerator", "Blueprint"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def classification(self) -> str:
        """
        Gets the classification of this AcceleratorSpecification.
        architectural classification into which the accelerator belongs

        :return: The classification of this AcceleratorSpecification.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification: str) -> None:
        """
        Sets the classification of this AcceleratorSpecification.
        architectural classification into which the accelerator belongs

        :param classification: The classification of this AcceleratorSpecification.
        :type: str
        """
        

        self._classification = classification

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of this AcceleratorSpecification.
        tags

        :return: The tags of this AcceleratorSpecification.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]) -> None:
        """
        Sets the tags of this AcceleratorSpecification.
        tags

        :param tags: The tags of this AcceleratorSpecification.
        :type: list[str]
        """
        

        self._tags = tags

    @property
    def permissions(self) -> List[str]:
        """
        Gets the permissions of this AcceleratorSpecification.
        Genesys Cloud permissions required to install the accelerator

        :return: The permissions of this AcceleratorSpecification.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions: List[str]) -> None:
        """
        Sets the permissions of this AcceleratorSpecification.
        Genesys Cloud permissions required to install the accelerator

        :param permissions: The permissions of this AcceleratorSpecification.
        :type: list[str]
        """
        

        self._permissions = permissions

    @property
    def products(self) -> List[str]:
        """
        Gets the products of this AcceleratorSpecification.
        Genesys Cloud products required to install the accelerator

        :return: The products of this AcceleratorSpecification.
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products: List[str]) -> None:
        """
        Sets the products of this AcceleratorSpecification.
        Genesys Cloud products required to install the accelerator

        :param products: The products of this AcceleratorSpecification.
        :type: list[str]
        """
        

        self._products = products

    @property
    def documentation(self) -> List['MetadataDocumentation']:
        """
        Gets the documentation of this AcceleratorSpecification.
        additional documentation about the artifact

        :return: The documentation of this AcceleratorSpecification.
        :rtype: list[MetadataDocumentation]
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation: List['MetadataDocumentation']) -> None:
        """
        Sets the documentation of this AcceleratorSpecification.
        additional documentation about the artifact

        :param documentation: The documentation of this AcceleratorSpecification.
        :type: list[MetadataDocumentation]
        """
        

        self._documentation = documentation

    @property
    def presentation(self) -> List['MetadataPresentation']:
        """
        Gets the presentation of this AcceleratorSpecification.
        presentation of data fields to be gathered for the accelerator

        :return: The presentation of this AcceleratorSpecification.
        :rtype: list[MetadataPresentation]
        """
        return self._presentation

    @presentation.setter
    def presentation(self, presentation: List['MetadataPresentation']) -> None:
        """
        Sets the presentation of this AcceleratorSpecification.
        presentation of data fields to be gathered for the accelerator

        :param presentation: The presentation of this AcceleratorSpecification.
        :type: list[MetadataPresentation]
        """
        

        self._presentation = presentation

    @property
    def results(self) -> 'MetadataResults':
        """
        Gets the results of this AcceleratorSpecification.
        resources created or modified as a result of running the accelerator

        :return: The results of this AcceleratorSpecification.
        :rtype: MetadataResults
        """
        return self._results

    @results.setter
    def results(self, results: 'MetadataResults') -> None:
        """
        Sets the results of this AcceleratorSpecification.
        resources created or modified as a result of running the accelerator

        :param results: The results of this AcceleratorSpecification.
        :type: MetadataResults
        """
        

        self._results = results

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this AcceleratorSpecification.
        The URI for this object

        :return: The self_uri of this AcceleratorSpecification.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this AcceleratorSpecification.
        The URI for this object

        :param self_uri: The self_uri of this AcceleratorSpecification.
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

