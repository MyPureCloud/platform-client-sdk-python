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


class KnowledgeBaseReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeBaseReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'language_code': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'language_code': 'languageCode',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._language_code = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this KnowledgeBaseReference.
        The globally unique identifier for the knowledge base.

        :return: The id of this KnowledgeBaseReference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this KnowledgeBaseReference.
        The globally unique identifier for the knowledge base.

        :param id: The id of this KnowledgeBaseReference.
        :type: str
        """
        

        self._id = id

    @property
    def language_code(self) -> str:
        """
        Gets the language_code of this KnowledgeBaseReference.
        Language of the knowledge base

        :return: The language_code of this KnowledgeBaseReference.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code: str) -> None:
        """
        Sets the language_code of this KnowledgeBaseReference.
        Language of the knowledge base

        :param language_code: The language_code of this KnowledgeBaseReference.
        :type: str
        """
        if isinstance(language_code, int):
            language_code = str(language_code)
        allowed_values = ["en-US", "en-UK", "en-AU", "en-CA", "en-HK", "en-IN", "en-IE", "en-NZ", "en-PH", "en-SG", "en-ZA", "de-DE", "de-AT", "de-CH", "es-AR", "es-CO", "es-MX", "es-US", "es-ES", "fr-FR", "fr-BE", "fr-CA", "fr-CH", "pt-BR", "pt-PT", "nl-NL", "nl-BE", "it-IT", "ca-ES", "tr-TR", "sv-SE", "fi-FI", "nb-NO", "da-DK", "ja-JP", "ar-AE", "zh-CN", "zh-TW", "zh-HK", "ko-KR", "pl-PL", "hi-IN", "th-TH", "hu-HU", "vi-VN", "uk-UA", "cs-CZ"]
        if language_code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language_code -> " + language_code)
            self._language_code = "outdated_sdk_version"
        else:
            self._language_code = language_code

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this KnowledgeBaseReference.
        The URI for this object

        :return: The self_uri of this KnowledgeBaseReference.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this KnowledgeBaseReference.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeBaseReference.
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

