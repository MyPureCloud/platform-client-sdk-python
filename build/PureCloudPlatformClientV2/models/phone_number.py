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


class PhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'display': 'str',
            'extension': 'int',
            'accepts_sms': 'bool',
            'normalization_country_code': 'str',
            'user_input': 'str',
            'e164': 'str',
            'country_code': 'str'
        }

        self.attribute_map = {
            'display': 'display',
            'extension': 'extension',
            'accepts_sms': 'acceptsSMS',
            'normalization_country_code': 'normalizationCountryCode',
            'user_input': 'userInput',
            'e164': 'e164',
            'country_code': 'countryCode'
        }

        self._display = None
        self._extension = None
        self._accepts_sms = None
        self._normalization_country_code = None
        self._user_input = None
        self._e164 = None
        self._country_code = None

    @property
    def display(self) -> str:
        """
        Gets the display of this PhoneNumber.
        The displayed form of the phone number string. Users should input the phone number in this field, but it will be altered by the API on write. If the phone number can be read as E164, the value will be replaced with international formatted-version of the number. If the number cannot be read as E164, the value will be preserved as-is. In both cases, the provided input string will be copied to the userInput field.

        :return: The display of this PhoneNumber.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display: str) -> None:
        """
        Sets the display of this PhoneNumber.
        The displayed form of the phone number string. Users should input the phone number in this field, but it will be altered by the API on write. If the phone number can be read as E164, the value will be replaced with international formatted-version of the number. If the number cannot be read as E164, the value will be preserved as-is. In both cases, the provided input string will be copied to the userInput field.

        :param display: The display of this PhoneNumber.
        :type: str
        """
        

        self._display = display

    @property
    def extension(self) -> int:
        """
        Gets the extension of this PhoneNumber.
        An optional extension for the provided phone number.

        :return: The extension of this PhoneNumber.
        :rtype: int
        """
        return self._extension

    @extension.setter
    def extension(self, extension: int) -> None:
        """
        Sets the extension of this PhoneNumber.
        An optional extension for the provided phone number.

        :param extension: The extension of this PhoneNumber.
        :type: int
        """
        

        self._extension = extension

    @property
    def accepts_sms(self) -> bool:
        """
        Gets the accepts_sms of this PhoneNumber.
        Whether this phone number can accept SMS messages.

        :return: The accepts_sms of this PhoneNumber.
        :rtype: bool
        """
        return self._accepts_sms

    @accepts_sms.setter
    def accepts_sms(self, accepts_sms: bool) -> None:
        """
        Sets the accepts_sms of this PhoneNumber.
        Whether this phone number can accept SMS messages.

        :param accepts_sms: The accepts_sms of this PhoneNumber.
        :type: bool
        """
        

        self._accepts_sms = accepts_sms

    @property
    def normalization_country_code(self) -> str:
        """
        Gets the normalization_country_code of this PhoneNumber.
        The country code that will be used for E164 conversion of a provided phone number. If the country code is omitted from the provided phone number, the country code provided in this field will be used during the E164 conversion attempt. If this field is left empty, the default country code for any provided phone number that does not explicitly include a country code is assumed to be +1 (North America).

        :return: The normalization_country_code of this PhoneNumber.
        :rtype: str
        """
        return self._normalization_country_code

    @normalization_country_code.setter
    def normalization_country_code(self, normalization_country_code: str) -> None:
        """
        Sets the normalization_country_code of this PhoneNumber.
        The country code that will be used for E164 conversion of a provided phone number. If the country code is omitted from the provided phone number, the country code provided in this field will be used during the E164 conversion attempt. If this field is left empty, the default country code for any provided phone number that does not explicitly include a country code is assumed to be +1 (North America).

        :param normalization_country_code: The normalization_country_code of this PhoneNumber.
        :type: str
        """
        

        self._normalization_country_code = normalization_country_code

    @property
    def user_input(self) -> str:
        """
        Gets the user_input of this PhoneNumber.
        The user-inputted phone number string that was provided to the display field on write. This field is not user-writeable and will always be set by the system.

        :return: The user_input of this PhoneNumber.
        :rtype: str
        """
        return self._user_input

    @user_input.setter
    def user_input(self, user_input: str) -> None:
        """
        Sets the user_input of this PhoneNumber.
        The user-inputted phone number string that was provided to the display field on write. This field is not user-writeable and will always be set by the system.

        :param user_input: The user_input of this PhoneNumber.
        :type: str
        """
        

        self._user_input = user_input

    @property
    def e164(self) -> str:
        """
        Gets the e164 of this PhoneNumber.
        The E164-formatted form of the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164.

        :return: The e164 of this PhoneNumber.
        :rtype: str
        """
        return self._e164

    @e164.setter
    def e164(self, e164: str) -> None:
        """
        Sets the e164 of this PhoneNumber.
        The E164-formatted form of the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164.

        :param e164: The e164 of this PhoneNumber.
        :type: str
        """
        

        self._e164 = e164

    @property
    def country_code(self) -> str:
        """
        Gets the country_code of this PhoneNumber.
        The detected country code from the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164.

        :return: The country_code of this PhoneNumber.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str) -> None:
        """
        Sets the country_code of this PhoneNumber.
        The detected country code from the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164.

        :param country_code: The country_code of this PhoneNumber.
        :type: str
        """
        

        self._country_code = country_code

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

