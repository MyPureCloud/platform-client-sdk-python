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
    from . import GrammarLanguageFileMetadata

class GrammarLanguage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GrammarLanguage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'grammar_id': 'str',
            'language': 'str',
            'voice_file_url': 'str',
            'dtmf_file_url': 'str',
            'voice_file_metadata': 'GrammarLanguageFileMetadata',
            'dtmf_file_metadata': 'GrammarLanguageFileMetadata',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'grammar_id': 'grammarId',
            'language': 'language',
            'voice_file_url': 'voiceFileUrl',
            'dtmf_file_url': 'dtmfFileUrl',
            'voice_file_metadata': 'voiceFileMetadata',
            'dtmf_file_metadata': 'dtmfFileMetadata',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._grammar_id = None
        self._language = None
        self._voice_file_url = None
        self._dtmf_file_url = None
        self._voice_file_metadata = None
        self._dtmf_file_metadata = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this GrammarLanguage.
        The globally unique identifier for the object.

        :return: The id of this GrammarLanguage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this GrammarLanguage.
        The globally unique identifier for the object.

        :param id: The id of this GrammarLanguage.
        :type: str
        """
        

        self._id = id

    @property
    def grammar_id(self) -> str:
        """
        Gets the grammar_id of this GrammarLanguage.
        The ID of the grammar associated with this grammar language

        :return: The grammar_id of this GrammarLanguage.
        :rtype: str
        """
        return self._grammar_id

    @grammar_id.setter
    def grammar_id(self, grammar_id: str) -> None:
        """
        Sets the grammar_id of this GrammarLanguage.
        The ID of the grammar associated with this grammar language

        :param grammar_id: The grammar_id of this GrammarLanguage.
        :type: str
        """
        

        self._grammar_id = grammar_id

    @property
    def language(self) -> str:
        """
        Gets the language of this GrammarLanguage.


        :return: The language of this GrammarLanguage.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this GrammarLanguage.


        :param language: The language of this GrammarLanguage.
        :type: str
        """
        

        self._language = language

    @property
    def voice_file_url(self) -> str:
        """
        Gets the voice_file_url of this GrammarLanguage.
        The URL to the voice mode file associated with this grammar language

        :return: The voice_file_url of this GrammarLanguage.
        :rtype: str
        """
        return self._voice_file_url

    @voice_file_url.setter
    def voice_file_url(self, voice_file_url: str) -> None:
        """
        Sets the voice_file_url of this GrammarLanguage.
        The URL to the voice mode file associated with this grammar language

        :param voice_file_url: The voice_file_url of this GrammarLanguage.
        :type: str
        """
        

        self._voice_file_url = voice_file_url

    @property
    def dtmf_file_url(self) -> str:
        """
        Gets the dtmf_file_url of this GrammarLanguage.
        The URL to the DTMF mode file associated with this grammar language

        :return: The dtmf_file_url of this GrammarLanguage.
        :rtype: str
        """
        return self._dtmf_file_url

    @dtmf_file_url.setter
    def dtmf_file_url(self, dtmf_file_url: str) -> None:
        """
        Sets the dtmf_file_url of this GrammarLanguage.
        The URL to the DTMF mode file associated with this grammar language

        :param dtmf_file_url: The dtmf_file_url of this GrammarLanguage.
        :type: str
        """
        

        self._dtmf_file_url = dtmf_file_url

    @property
    def voice_file_metadata(self) -> 'GrammarLanguageFileMetadata':
        """
        Gets the voice_file_metadata of this GrammarLanguage.
        Additional information about the associated voice file

        :return: The voice_file_metadata of this GrammarLanguage.
        :rtype: GrammarLanguageFileMetadata
        """
        return self._voice_file_metadata

    @voice_file_metadata.setter
    def voice_file_metadata(self, voice_file_metadata: 'GrammarLanguageFileMetadata') -> None:
        """
        Sets the voice_file_metadata of this GrammarLanguage.
        Additional information about the associated voice file

        :param voice_file_metadata: The voice_file_metadata of this GrammarLanguage.
        :type: GrammarLanguageFileMetadata
        """
        

        self._voice_file_metadata = voice_file_metadata

    @property
    def dtmf_file_metadata(self) -> 'GrammarLanguageFileMetadata':
        """
        Gets the dtmf_file_metadata of this GrammarLanguage.
        Additional information about the associated dtmf file

        :return: The dtmf_file_metadata of this GrammarLanguage.
        :rtype: GrammarLanguageFileMetadata
        """
        return self._dtmf_file_metadata

    @dtmf_file_metadata.setter
    def dtmf_file_metadata(self, dtmf_file_metadata: 'GrammarLanguageFileMetadata') -> None:
        """
        Sets the dtmf_file_metadata of this GrammarLanguage.
        Additional information about the associated dtmf file

        :param dtmf_file_metadata: The dtmf_file_metadata of this GrammarLanguage.
        :type: GrammarLanguageFileMetadata
        """
        

        self._dtmf_file_metadata = dtmf_file_metadata

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this GrammarLanguage.
        The URI for this object

        :return: The self_uri of this GrammarLanguage.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this GrammarLanguage.
        The URI for this object

        :param self_uri: The self_uri of this GrammarLanguage.
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

