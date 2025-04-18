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


class Contact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Contact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'display': 'str',
            'media_type': 'str',
            'type': 'str',
            'extension': 'str',
            'country_code': 'str',
            'integration': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'display': 'display',
            'media_type': 'mediaType',
            'type': 'type',
            'extension': 'extension',
            'country_code': 'countryCode',
            'integration': 'integration'
        }

        self._address = None
        self._display = None
        self._media_type = None
        self._type = None
        self._extension = None
        self._country_code = None
        self._integration = None

    @property
    def address(self) -> str:
        """
        Gets the address of this Contact.
        Email address or phone number for this contact type

        :return: The address of this Contact.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this Contact.
        Email address or phone number for this contact type

        :param address: The address of this Contact.
        :type: str
        """
        

        self._address = address

    @property
    def display(self) -> str:
        """
        Gets the display of this Contact.
        Formatted version of the address property

        :return: The display of this Contact.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display: str) -> None:
        """
        Sets the display of this Contact.
        Formatted version of the address property

        :param display: The display of this Contact.
        :type: str
        """
        

        self._display = display

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this Contact.


        :return: The media_type of this Contact.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this Contact.


        :param media_type: The media_type of this Contact.
        :type: str
        """
        if isinstance(media_type, int):
            media_type = str(media_type)
        allowed_values = ["PHONE", "EMAIL", "SMS"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def type(self) -> str:
        """
        Gets the type of this Contact.


        :return: The type of this Contact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Contact.


        :param type: The type of this Contact.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["PRIMARY", "WORK", "WORK2", "WORK3", "WORK4", "HOME", "MOBILE", "MAIN", "OTHER"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def extension(self) -> str:
        """
        Gets the extension of this Contact.
        Use internal extension instead of address. Mutually exclusive with the address field.

        :return: The extension of this Contact.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension: str) -> None:
        """
        Sets the extension of this Contact.
        Use internal extension instead of address. Mutually exclusive with the address field.

        :param extension: The extension of this Contact.
        :type: str
        """
        

        self._extension = extension

    @property
    def country_code(self) -> str:
        """
        Gets the country_code of this Contact.


        :return: The country_code of this Contact.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str) -> None:
        """
        Sets the country_code of this Contact.


        :param country_code: The country_code of this Contact.
        :type: str
        """
        

        self._country_code = country_code

    @property
    def integration(self) -> str:
        """
        Gets the integration of this Contact.
        Integration tag value if this number is associated with an external integration.

        :return: The integration of this Contact.
        :rtype: str
        """
        return self._integration

    @integration.setter
    def integration(self, integration: str) -> None:
        """
        Sets the integration of this Contact.
        Integration tag value if this number is associated with an external integration.

        :param integration: The integration of this Contact.
        :type: str
        """
        

        self._integration = integration

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

