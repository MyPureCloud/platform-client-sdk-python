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
    from . import GroupGreetingEventGreetingAudioFile
    from . import GroupGreetingEventGreetingOwner

class GroupGreetingEventGreeting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GroupGreetingEventGreeting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'owner_type': 'str',
            'owner': 'GroupGreetingEventGreetingOwner',
            'greeting_audio_file': 'GroupGreetingEventGreetingAudioFile',
            'audio_tts': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'owner_type': 'ownerType',
            'owner': 'owner',
            'greeting_audio_file': 'greetingAudioFile',
            'audio_tts': 'audioTTS'
        }

        self._id = None
        self._name = None
        self._type = None
        self._owner_type = None
        self._owner = None
        self._greeting_audio_file = None
        self._audio_tts = None

    @property
    def id(self) -> str:
        """
        Gets the id of this GroupGreetingEventGreeting.


        :return: The id of this GroupGreetingEventGreeting.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this GroupGreetingEventGreeting.


        :param id: The id of this GroupGreetingEventGreeting.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this GroupGreetingEventGreeting.


        :return: The name of this GroupGreetingEventGreeting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this GroupGreetingEventGreeting.


        :param name: The name of this GroupGreetingEventGreeting.
        :type: str
        """
        

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this GroupGreetingEventGreeting.


        :return: The type of this GroupGreetingEventGreeting.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this GroupGreetingEventGreeting.


        :param type: The type of this GroupGreetingEventGreeting.
        :type: str
        """
        

        self._type = type

    @property
    def owner_type(self) -> str:
        """
        Gets the owner_type of this GroupGreetingEventGreeting.


        :return: The owner_type of this GroupGreetingEventGreeting.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type: str) -> None:
        """
        Sets the owner_type of this GroupGreetingEventGreeting.


        :param owner_type: The owner_type of this GroupGreetingEventGreeting.
        :type: str
        """
        

        self._owner_type = owner_type

    @property
    def owner(self) -> 'GroupGreetingEventGreetingOwner':
        """
        Gets the owner of this GroupGreetingEventGreeting.


        :return: The owner of this GroupGreetingEventGreeting.
        :rtype: GroupGreetingEventGreetingOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner: 'GroupGreetingEventGreetingOwner') -> None:
        """
        Sets the owner of this GroupGreetingEventGreeting.


        :param owner: The owner of this GroupGreetingEventGreeting.
        :type: GroupGreetingEventGreetingOwner
        """
        

        self._owner = owner

    @property
    def greeting_audio_file(self) -> 'GroupGreetingEventGreetingAudioFile':
        """
        Gets the greeting_audio_file of this GroupGreetingEventGreeting.


        :return: The greeting_audio_file of this GroupGreetingEventGreeting.
        :rtype: GroupGreetingEventGreetingAudioFile
        """
        return self._greeting_audio_file

    @greeting_audio_file.setter
    def greeting_audio_file(self, greeting_audio_file: 'GroupGreetingEventGreetingAudioFile') -> None:
        """
        Sets the greeting_audio_file of this GroupGreetingEventGreeting.


        :param greeting_audio_file: The greeting_audio_file of this GroupGreetingEventGreeting.
        :type: GroupGreetingEventGreetingAudioFile
        """
        

        self._greeting_audio_file = greeting_audio_file

    @property
    def audio_tts(self) -> str:
        """
        Gets the audio_tts of this GroupGreetingEventGreeting.


        :return: The audio_tts of this GroupGreetingEventGreeting.
        :rtype: str
        """
        return self._audio_tts

    @audio_tts.setter
    def audio_tts(self, audio_tts: str) -> None:
        """
        Sets the audio_tts of this GroupGreetingEventGreeting.


        :param audio_tts: The audio_tts of this GroupGreetingEventGreeting.
        :type: str
        """
        

        self._audio_tts = audio_tts

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

