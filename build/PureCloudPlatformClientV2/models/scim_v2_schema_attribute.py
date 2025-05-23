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


class ScimV2SchemaAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScimV2SchemaAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'sub_attributes': 'list[ScimV2SchemaAttribute]',
            'multi_valued': 'bool',
            'description': 'str',
            'required': 'bool',
            'canonical_values': 'list[str]',
            'case_exact': 'bool',
            'mutability': 'str',
            'returned': 'str',
            'uniqueness': 'str',
            'reference_types': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'sub_attributes': 'subAttributes',
            'multi_valued': 'multiValued',
            'description': 'description',
            'required': 'required',
            'canonical_values': 'canonicalValues',
            'case_exact': 'caseExact',
            'mutability': 'mutability',
            'returned': 'returned',
            'uniqueness': 'uniqueness',
            'reference_types': 'referenceTypes'
        }

        self._name = None
        self._type = None
        self._sub_attributes = None
        self._multi_valued = None
        self._description = None
        self._required = None
        self._canonical_values = None
        self._case_exact = None
        self._mutability = None
        self._returned = None
        self._uniqueness = None
        self._reference_types = None

    @property
    def name(self) -> str:
        """
        Gets the name of this ScimV2SchemaAttribute.
        The name of the attribute.

        :return: The name of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ScimV2SchemaAttribute.
        The name of the attribute.

        :param name: The name of this ScimV2SchemaAttribute.
        :type: str
        """
        

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this ScimV2SchemaAttribute.
        The data type of the attribute.

        :return: The type of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this ScimV2SchemaAttribute.
        The data type of the attribute.

        :param type: The type of this ScimV2SchemaAttribute.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["string", "boolean", "decimal", "integer", "dateTime", "reference", "complex"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def sub_attributes(self) -> List['ScimV2SchemaAttribute']:
        """
        Gets the sub_attributes of this ScimV2SchemaAttribute.
        The list of subattributes for an attribute of the type \"complex\". Uses the same schema as \"attributes\".

        :return: The sub_attributes of this ScimV2SchemaAttribute.
        :rtype: list[ScimV2SchemaAttribute]
        """
        return self._sub_attributes

    @sub_attributes.setter
    def sub_attributes(self, sub_attributes: List['ScimV2SchemaAttribute']) -> None:
        """
        Sets the sub_attributes of this ScimV2SchemaAttribute.
        The list of subattributes for an attribute of the type \"complex\". Uses the same schema as \"attributes\".

        :param sub_attributes: The sub_attributes of this ScimV2SchemaAttribute.
        :type: list[ScimV2SchemaAttribute]
        """
        

        self._sub_attributes = sub_attributes

    @property
    def multi_valued(self) -> bool:
        """
        Gets the multi_valued of this ScimV2SchemaAttribute.
        Indicates whether an attribute contains multiple values.

        :return: The multi_valued of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._multi_valued

    @multi_valued.setter
    def multi_valued(self, multi_valued: bool) -> None:
        """
        Sets the multi_valued of this ScimV2SchemaAttribute.
        Indicates whether an attribute contains multiple values.

        :param multi_valued: The multi_valued of this ScimV2SchemaAttribute.
        :type: bool
        """
        

        self._multi_valued = multi_valued

    @property
    def description(self) -> str:
        """
        Gets the description of this ScimV2SchemaAttribute.
        The description of the attribute.

        :return: The description of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this ScimV2SchemaAttribute.
        The description of the attribute.

        :param description: The description of this ScimV2SchemaAttribute.
        :type: str
        """
        

        self._description = description

    @property
    def required(self) -> bool:
        """
        Gets the required of this ScimV2SchemaAttribute.
        Indicates whether an attribute is required.

        :return: The required of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required: bool) -> None:
        """
        Sets the required of this ScimV2SchemaAttribute.
        Indicates whether an attribute is required.

        :param required: The required of this ScimV2SchemaAttribute.
        :type: bool
        """
        

        self._required = required

    @property
    def canonical_values(self) -> List[str]:
        """
        Gets the canonical_values of this ScimV2SchemaAttribute.
        The list of standard values that service providers may use. Service providers may ignore unsupported values.

        :return: The canonical_values of this ScimV2SchemaAttribute.
        :rtype: list[str]
        """
        return self._canonical_values

    @canonical_values.setter
    def canonical_values(self, canonical_values: List[str]) -> None:
        """
        Sets the canonical_values of this ScimV2SchemaAttribute.
        The list of standard values that service providers may use. Service providers may ignore unsupported values.

        :param canonical_values: The canonical_values of this ScimV2SchemaAttribute.
        :type: list[str]
        """
        

        self._canonical_values = canonical_values

    @property
    def case_exact(self) -> bool:
        """
        Gets the case_exact of this ScimV2SchemaAttribute.
        Indicates whether a string attribute is case-sensitive. If set to \"true\", the server preserves case sensitivity. If set to \"false\", the server may change the case. The server also uses case sensitivity when evaluating filters. See section 3.4.2.2 \"Filtering\" in RFC 7644 for details.

        :return: The case_exact of this ScimV2SchemaAttribute.
        :rtype: bool
        """
        return self._case_exact

    @case_exact.setter
    def case_exact(self, case_exact: bool) -> None:
        """
        Sets the case_exact of this ScimV2SchemaAttribute.
        Indicates whether a string attribute is case-sensitive. If set to \"true\", the server preserves case sensitivity. If set to \"false\", the server may change the case. The server also uses case sensitivity when evaluating filters. See section 3.4.2.2 \"Filtering\" in RFC 7644 for details.

        :param case_exact: The case_exact of this ScimV2SchemaAttribute.
        :type: bool
        """
        

        self._case_exact = case_exact

    @property
    def mutability(self) -> str:
        """
        Gets the mutability of this ScimV2SchemaAttribute.
        The circumstances under which an attribute can be defined or redefined. The default is \"readWrite\".

        :return: The mutability of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._mutability

    @mutability.setter
    def mutability(self, mutability: str) -> None:
        """
        Sets the mutability of this ScimV2SchemaAttribute.
        The circumstances under which an attribute can be defined or redefined. The default is \"readWrite\".

        :param mutability: The mutability of this ScimV2SchemaAttribute.
        :type: str
        """
        if isinstance(mutability, int):
            mutability = str(mutability)
        allowed_values = ["readWrite", "readOnly", "immutable", "writeOnly"]
        if mutability.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for mutability -> " + mutability)
            self._mutability = "outdated_sdk_version"
        else:
            self._mutability = mutability

    @property
    def returned(self) -> str:
        """
        Gets the returned of this ScimV2SchemaAttribute.
        The circumstances under which an attribute and its values are returned in response to a GET, PUT, POST, or PATCH request.

        :return: The returned of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._returned

    @returned.setter
    def returned(self, returned: str) -> None:
        """
        Sets the returned of this ScimV2SchemaAttribute.
        The circumstances under which an attribute and its values are returned in response to a GET, PUT, POST, or PATCH request.

        :param returned: The returned of this ScimV2SchemaAttribute.
        :type: str
        """
        if isinstance(returned, int):
            returned = str(returned)
        allowed_values = ["always", "never", "default", "request"]
        if returned.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for returned -> " + returned)
            self._returned = "outdated_sdk_version"
        else:
            self._returned = returned

    @property
    def uniqueness(self) -> str:
        """
        Gets the uniqueness of this ScimV2SchemaAttribute.
        The method by which the service provider enforces the uniqueness of an attribute value. A server can reject a value by returning the HTTP response code 400 (Bad Request). A client can enforce uniqueness to a greater degree than the server provider enforces. For example, a client could make a value unique even though the server has \"uniqueness\" set to \"none\".

        :return: The uniqueness of this ScimV2SchemaAttribute.
        :rtype: str
        """
        return self._uniqueness

    @uniqueness.setter
    def uniqueness(self, uniqueness: str) -> None:
        """
        Sets the uniqueness of this ScimV2SchemaAttribute.
        The method by which the service provider enforces the uniqueness of an attribute value. A server can reject a value by returning the HTTP response code 400 (Bad Request). A client can enforce uniqueness to a greater degree than the server provider enforces. For example, a client could make a value unique even though the server has \"uniqueness\" set to \"none\".

        :param uniqueness: The uniqueness of this ScimV2SchemaAttribute.
        :type: str
        """
        if isinstance(uniqueness, int):
            uniqueness = str(uniqueness)
        allowed_values = ["none", "server", "global"]
        if uniqueness.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for uniqueness -> " + uniqueness)
            self._uniqueness = "outdated_sdk_version"
        else:
            self._uniqueness = uniqueness

    @property
    def reference_types(self) -> List[str]:
        """
        Gets the reference_types of this ScimV2SchemaAttribute.
        The list of SCIM resource types that may be referenced. Only applies when \"type\" is set to \"reference\".

        :return: The reference_types of this ScimV2SchemaAttribute.
        :rtype: list[str]
        """
        return self._reference_types

    @reference_types.setter
    def reference_types(self, reference_types: List[str]) -> None:
        """
        Sets the reference_types of this ScimV2SchemaAttribute.
        The list of SCIM resource types that may be referenced. Only applies when \"type\" is set to \"reference\".

        :param reference_types: The reference_types of this ScimV2SchemaAttribute.
        :type: list[str]
        """
        

        self._reference_types = reference_types

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

