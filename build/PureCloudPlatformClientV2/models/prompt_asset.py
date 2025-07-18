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


class PromptAsset(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PromptAsset - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'prompt_id': 'str',
            'language': 'str',
            'media_uri': 'str',
            'tts_string': 'str',
            'text': 'str',
            'upload_status': 'str',
            'upload_uri': 'str',
            'language_default': 'bool',
            'tags': 'dict(str, list[str])',
            'duration_seconds': 'float',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'prompt_id': 'promptId',
            'language': 'language',
            'media_uri': 'mediaUri',
            'tts_string': 'ttsString',
            'text': 'text',
            'upload_status': 'uploadStatus',
            'upload_uri': 'uploadUri',
            'language_default': 'languageDefault',
            'tags': 'tags',
            'duration_seconds': 'durationSeconds',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._prompt_id = None
        self._language = None
        self._media_uri = None
        self._tts_string = None
        self._text = None
        self._upload_status = None
        self._upload_uri = None
        self._language_default = None
        self._tags = None
        self._duration_seconds = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this PromptAsset.
        The globally unique identifier for the object.

        :return: The id of this PromptAsset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this PromptAsset.
        The globally unique identifier for the object.

        :param id: The id of this PromptAsset.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this PromptAsset.


        :return: The name of this PromptAsset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this PromptAsset.


        :param name: The name of this PromptAsset.
        :type: str
        """
        

        self._name = name

    @property
    def prompt_id(self) -> str:
        """
        Gets the prompt_id of this PromptAsset.
        Associated prompt ID

        :return: The prompt_id of this PromptAsset.
        :rtype: str
        """
        return self._prompt_id

    @prompt_id.setter
    def prompt_id(self, prompt_id: str) -> None:
        """
        Sets the prompt_id of this PromptAsset.
        Associated prompt ID

        :param prompt_id: The prompt_id of this PromptAsset.
        :type: str
        """
        

        self._prompt_id = prompt_id

    @property
    def language(self) -> str:
        """
        Gets the language of this PromptAsset.
        Prompt resource language

        :return: The language of this PromptAsset.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this PromptAsset.
        Prompt resource language

        :param language: The language of this PromptAsset.
        :type: str
        """
        

        self._language = language

    @property
    def media_uri(self) -> str:
        """
        Gets the media_uri of this PromptAsset.
        URI of the resource audio

        :return: The media_uri of this PromptAsset.
        :rtype: str
        """
        return self._media_uri

    @media_uri.setter
    def media_uri(self, media_uri: str) -> None:
        """
        Sets the media_uri of this PromptAsset.
        URI of the resource audio

        :param media_uri: The media_uri of this PromptAsset.
        :type: str
        """
        

        self._media_uri = media_uri

    @property
    def tts_string(self) -> str:
        """
        Gets the tts_string of this PromptAsset.
        Text to speech of the resource

        :return: The tts_string of this PromptAsset.
        :rtype: str
        """
        return self._tts_string

    @tts_string.setter
    def tts_string(self, tts_string: str) -> None:
        """
        Sets the tts_string of this PromptAsset.
        Text to speech of the resource

        :param tts_string: The tts_string of this PromptAsset.
        :type: str
        """
        

        self._tts_string = tts_string

    @property
    def text(self) -> str:
        """
        Gets the text of this PromptAsset.
        Text of the resource

        :return: The text of this PromptAsset.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text of this PromptAsset.
        Text of the resource

        :param text: The text of this PromptAsset.
        :type: str
        """
        

        self._text = text

    @property
    def upload_status(self) -> str:
        """
        Gets the upload_status of this PromptAsset.
        Audio upload status

        :return: The upload_status of this PromptAsset.
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status: str) -> None:
        """
        Sets the upload_status of this PromptAsset.
        Audio upload status

        :param upload_status: The upload_status of this PromptAsset.
        :type: str
        """
        if isinstance(upload_status, int):
            upload_status = str(upload_status)
        allowed_values = ["created", "uploaded", "transcoded", "transcodeFailed"]
        if upload_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for upload_status -> " + upload_status)
            self._upload_status = "outdated_sdk_version"
        else:
            self._upload_status = upload_status

    @property
    def upload_uri(self) -> str:
        """
        Gets the upload_uri of this PromptAsset.
        Deprecated. This was use for uploading the resource audio.

        :return: The upload_uri of this PromptAsset.
        :rtype: str
        """
        return self._upload_uri

    @upload_uri.setter
    def upload_uri(self, upload_uri: str) -> None:
        """
        Sets the upload_uri of this PromptAsset.
        Deprecated. This was use for uploading the resource audio.

        :param upload_uri: The upload_uri of this PromptAsset.
        :type: str
        """
        

        self._upload_uri = upload_uri

    @property
    def language_default(self) -> bool:
        """
        Gets the language_default of this PromptAsset.
        Whether or not this resource locale is the default for the language

        :return: The language_default of this PromptAsset.
        :rtype: bool
        """
        return self._language_default

    @language_default.setter
    def language_default(self, language_default: bool) -> None:
        """
        Sets the language_default of this PromptAsset.
        Whether or not this resource locale is the default for the language

        :param language_default: The language_default of this PromptAsset.
        :type: bool
        """
        

        self._language_default = language_default

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of this PromptAsset.


        :return: The tags of this PromptAsset.
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]) -> None:
        """
        Sets the tags of this PromptAsset.


        :param tags: The tags of this PromptAsset.
        :type: dict(str, list[str])
        """
        

        self._tags = tags

    @property
    def duration_seconds(self) -> float:
        """
        Gets the duration_seconds of this PromptAsset.


        :return: The duration_seconds of this PromptAsset.
        :rtype: float
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds: float) -> None:
        """
        Sets the duration_seconds of this PromptAsset.


        :param duration_seconds: The duration_seconds of this PromptAsset.
        :type: float
        """
        

        self._duration_seconds = duration_seconds

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this PromptAsset.
        The URI for this object

        :return: The self_uri of this PromptAsset.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this PromptAsset.
        The URI for this object

        :param self_uri: The self_uri of this PromptAsset.
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

