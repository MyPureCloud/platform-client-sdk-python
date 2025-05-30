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


class PhraseTranslation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PhraseTranslation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_time_ms': 'int',
            'participant_purpose': 'str',
            'translated_text': 'str'
        }

        self.attribute_map = {
            'start_time_ms': 'startTimeMs',
            'participant_purpose': 'participantPurpose',
            'translated_text': 'translatedText'
        }

        self._start_time_ms = None
        self._participant_purpose = None
        self._translated_text = None

    @property
    def start_time_ms(self) -> int:
        """
        Gets the start_time_ms of this PhraseTranslation.
        Epoch start time of the phrase

        :return: The start_time_ms of this PhraseTranslation.
        :rtype: int
        """
        return self._start_time_ms

    @start_time_ms.setter
    def start_time_ms(self, start_time_ms: int) -> None:
        """
        Sets the start_time_ms of this PhraseTranslation.
        Epoch start time of the phrase

        :param start_time_ms: The start_time_ms of this PhraseTranslation.
        :type: int
        """
        

        self._start_time_ms = start_time_ms

    @property
    def participant_purpose(self) -> str:
        """
        Gets the participant_purpose of this PhraseTranslation.
        Purpose of the participant associated with the phrase

        :return: The participant_purpose of this PhraseTranslation.
        :rtype: str
        """
        return self._participant_purpose

    @participant_purpose.setter
    def participant_purpose(self, participant_purpose: str) -> None:
        """
        Sets the participant_purpose of this PhraseTranslation.
        Purpose of the participant associated with the phrase

        :param participant_purpose: The participant_purpose of this PhraseTranslation.
        :type: str
        """
        

        self._participant_purpose = participant_purpose

    @property
    def translated_text(self) -> str:
        """
        Gets the translated_text of this PhraseTranslation.
        Translation of the phrase

        :return: The translated_text of this PhraseTranslation.
        :rtype: str
        """
        return self._translated_text

    @translated_text.setter
    def translated_text(self, translated_text: str) -> None:
        """
        Sets the translated_text of this PhraseTranslation.
        Translation of the phrase

        :param translated_text: The translated_text of this PhraseTranslation.
        :type: str
        """
        

        self._translated_text = translated_text

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

