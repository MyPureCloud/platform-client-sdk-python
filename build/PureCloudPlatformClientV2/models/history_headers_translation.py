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


class HistoryHeadersTranslation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        HistoryHeadersTranslation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pcFrom': 'str',
            'to': 'str',
            'cc': 'str',
            'subject': 'str',
            'reply_prefix': 'str',
            'forward_prefix': 'str',
            'sent': 'str',
            'language': 'str',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'pcFrom': 'from',
            'to': 'to',
            'cc': 'cc',
            'subject': 'subject',
            'reply_prefix': 'replyPrefix',
            'forward_prefix': 'forwardPrefix',
            'sent': 'sent',
            'language': 'language',
            'time_zone': 'timeZone'
        }

        self._pcFrom = None
        self._to = None
        self._cc = None
        self._subject = None
        self._reply_prefix = None
        self._forward_prefix = None
        self._sent = None
        self._language = None
        self._time_zone = None

    @property
    def pcFrom(self) -> str:
        """
        Gets the pcFrom of this HistoryHeadersTranslation.
        A translation for the word \"from\", for the expected language

        :return: The pcFrom of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._pcFrom

    @pcFrom.setter
    def pcFrom(self, pcFrom: str) -> None:
        """
        Sets the pcFrom of this HistoryHeadersTranslation.
        A translation for the word \"from\", for the expected language

        :param pcFrom: The pcFrom of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._pcFrom = pcFrom

    @property
    def to(self) -> str:
        """
        Gets the to of this HistoryHeadersTranslation.
        A translation for the word \"to\", for the expected language

        :return: The to of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to: str) -> None:
        """
        Sets the to of this HistoryHeadersTranslation.
        A translation for the word \"to\", for the expected language

        :param to: The to of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._to = to

    @property
    def cc(self) -> str:
        """
        Gets the cc of this HistoryHeadersTranslation.
        A translation for the word \"cc\", for the expected language

        :return: The cc of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc: str) -> None:
        """
        Sets the cc of this HistoryHeadersTranslation.
        A translation for the word \"cc\", for the expected language

        :param cc: The cc of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._cc = cc

    @property
    def subject(self) -> str:
        """
        Gets the subject of this HistoryHeadersTranslation.
        A translation for the word \"subject\", for the expected language

        :return: The subject of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this HistoryHeadersTranslation.
        A translation for the word \"subject\", for the expected language

        :param subject: The subject of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._subject = subject

    @property
    def reply_prefix(self) -> str:
        """
        Gets the reply_prefix of this HistoryHeadersTranslation.
        A translation for the subject prefix \"Reply\", for the expected language

        :return: The reply_prefix of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._reply_prefix

    @reply_prefix.setter
    def reply_prefix(self, reply_prefix: str) -> None:
        """
        Sets the reply_prefix of this HistoryHeadersTranslation.
        A translation for the subject prefix \"Reply\", for the expected language

        :param reply_prefix: The reply_prefix of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._reply_prefix = reply_prefix

    @property
    def forward_prefix(self) -> str:
        """
        Gets the forward_prefix of this HistoryHeadersTranslation.
        A translation for the subject prefix \"Forward\", for the expected language

        :return: The forward_prefix of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._forward_prefix

    @forward_prefix.setter
    def forward_prefix(self, forward_prefix: str) -> None:
        """
        Sets the forward_prefix of this HistoryHeadersTranslation.
        A translation for the subject prefix \"Forward\", for the expected language

        :param forward_prefix: The forward_prefix of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._forward_prefix = forward_prefix

    @property
    def sent(self) -> str:
        """
        Gets the sent of this HistoryHeadersTranslation.
        A translation for the word \"sent\", for the expected language

        :return: The sent of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent: str) -> None:
        """
        Sets the sent of this HistoryHeadersTranslation.
        A translation for the word \"sent\", for the expected language

        :param sent: The sent of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._sent = sent

    @property
    def language(self) -> str:
        """
        Gets the language of this HistoryHeadersTranslation.
        The code of the expected language

        :return: The language of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this HistoryHeadersTranslation.
        The code of the expected language

        :param language: The language of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._language = language

    @property
    def time_zone(self) -> str:
        """
        Gets the time_zone of this HistoryHeadersTranslation.
        Timezone used by the agent, used to format the sent email date and time. If not defined, will default to UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :return: The time_zone of this HistoryHeadersTranslation.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str) -> None:
        """
        Sets the time_zone of this HistoryHeadersTranslation.
        Timezone used by the agent, used to format the sent email date and time. If not defined, will default to UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :param time_zone: The time_zone of this HistoryHeadersTranslation.
        :type: str
        """
        

        self._time_zone = time_zone

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

