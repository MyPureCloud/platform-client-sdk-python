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


class CoverSheet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CoverSheet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'notes': 'str',
            'locale': 'str'
        }

        self.attribute_map = {
            'notes': 'notes',
            'locale': 'locale'
        }

        self._notes = None
        self._locale = None

    @property
    def notes(self) -> str:
        """
        Gets the notes of this CoverSheet.
        Text to be added to the coversheet

        :return: The notes of this CoverSheet.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str) -> None:
        """
        Sets the notes of this CoverSheet.
        Text to be added to the coversheet

        :param notes: The notes of this CoverSheet.
        :type: str
        """
        

        self._notes = notes

    @property
    def locale(self) -> str:
        """
        Gets the locale of this CoverSheet.
        Locale, e.g. = en-US

        :return: The locale of this CoverSheet.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale: str) -> None:
        """
        Sets the locale of this CoverSheet.
        Locale, e.g. = en-US

        :param locale: The locale of this CoverSheet.
        :type: str
        """
        

        self._locale = locale

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

