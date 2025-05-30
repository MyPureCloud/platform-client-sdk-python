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
    from . import Reaction

class ResponseSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ResponseSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'responses': 'dict(str, Reaction)',
            'beep_detection_enabled': 'bool',
            'amd_speech_distinguish_enabled': 'bool',
            'live_speaker_detection_mode': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'responses': 'responses',
            'beep_detection_enabled': 'beepDetectionEnabled',
            'amd_speech_distinguish_enabled': 'amdSpeechDistinguishEnabled',
            'live_speaker_detection_mode': 'liveSpeakerDetectionMode',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._responses = None
        self._beep_detection_enabled = None
        self._amd_speech_distinguish_enabled = None
        self._live_speaker_detection_mode = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ResponseSet.
        The globally unique identifier for the object.

        :return: The id of this ResponseSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ResponseSet.
        The globally unique identifier for the object.

        :param id: The id of this ResponseSet.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ResponseSet.
        The name of the ResponseSet.

        :return: The name of this ResponseSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ResponseSet.
        The name of the ResponseSet.

        :param name: The name of this ResponseSet.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this ResponseSet.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this ResponseSet.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this ResponseSet.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this ResponseSet.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this ResponseSet.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this ResponseSet.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this ResponseSet.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this ResponseSet.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this ResponseSet.
        Required for updates, must match the version number of the most recent update

        :return: The version of this ResponseSet.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this ResponseSet.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this ResponseSet.
        :type: int
        """
        

        self._version = version

    @property
    def responses(self) -> Dict[str, 'Reaction']:
        """
        Gets the responses of this ResponseSet.
        Map of disposition identifiers to reactions. For example: {\"disposition.classification.callable.person\": {\"reactionType\": \"transfer\"}}.

        :return: The responses of this ResponseSet.
        :rtype: dict(str, Reaction)
        """
        return self._responses

    @responses.setter
    def responses(self, responses: Dict[str, 'Reaction']) -> None:
        """
        Sets the responses of this ResponseSet.
        Map of disposition identifiers to reactions. For example: {\"disposition.classification.callable.person\": {\"reactionType\": \"transfer\"}}.

        :param responses: The responses of this ResponseSet.
        :type: dict(str, Reaction)
        """
        

        self._responses = responses

    @property
    def beep_detection_enabled(self) -> bool:
        """
        Gets the beep_detection_enabled of this ResponseSet.
        Whether to enable answering machine beep detection

        :return: The beep_detection_enabled of this ResponseSet.
        :rtype: bool
        """
        return self._beep_detection_enabled

    @beep_detection_enabled.setter
    def beep_detection_enabled(self, beep_detection_enabled: bool) -> None:
        """
        Sets the beep_detection_enabled of this ResponseSet.
        Whether to enable answering machine beep detection

        :param beep_detection_enabled: The beep_detection_enabled of this ResponseSet.
        :type: bool
        """
        

        self._beep_detection_enabled = beep_detection_enabled

    @property
    def amd_speech_distinguish_enabled(self) -> bool:
        """
        Gets the amd_speech_distinguish_enabled of this ResponseSet.
        Whether to enable answering machine detection

        :return: The amd_speech_distinguish_enabled of this ResponseSet.
        :rtype: bool
        """
        return self._amd_speech_distinguish_enabled

    @amd_speech_distinguish_enabled.setter
    def amd_speech_distinguish_enabled(self, amd_speech_distinguish_enabled: bool) -> None:
        """
        Sets the amd_speech_distinguish_enabled of this ResponseSet.
        Whether to enable answering machine detection

        :param amd_speech_distinguish_enabled: The amd_speech_distinguish_enabled of this ResponseSet.
        :type: bool
        """
        

        self._amd_speech_distinguish_enabled = amd_speech_distinguish_enabled

    @property
    def live_speaker_detection_mode(self) -> str:
        """
        Gets the live_speaker_detection_mode of this ResponseSet.
        Setting level of live speaker detection based on ringbacks

        :return: The live_speaker_detection_mode of this ResponseSet.
        :rtype: str
        """
        return self._live_speaker_detection_mode

    @live_speaker_detection_mode.setter
    def live_speaker_detection_mode(self, live_speaker_detection_mode: str) -> None:
        """
        Sets the live_speaker_detection_mode of this ResponseSet.
        Setting level of live speaker detection based on ringbacks

        :param live_speaker_detection_mode: The live_speaker_detection_mode of this ResponseSet.
        :type: str
        """
        if isinstance(live_speaker_detection_mode, int):
            live_speaker_detection_mode = str(live_speaker_detection_mode)
        allowed_values = ["Disabled", "Low", "Medium", "High"]
        if live_speaker_detection_mode.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for live_speaker_detection_mode -> " + live_speaker_detection_mode)
            self._live_speaker_detection_mode = "outdated_sdk_version"
        else:
            self._live_speaker_detection_mode = live_speaker_detection_mode

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ResponseSet.
        The URI for this object

        :return: The self_uri of this ResponseSet.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ResponseSet.
        The URI for this object

        :param self_uri: The self_uri of this ResponseSet.
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

