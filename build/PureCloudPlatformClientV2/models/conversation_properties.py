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


class ConversationProperties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationProperties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_waiting': 'bool',
            'is_active': 'bool',
            'is_acd': 'bool',
            'is_preferred': 'bool',
            'is_screenshare': 'bool',
            'is_cobrowse': 'bool',
            'is_voicemail': 'bool',
            'is_flagged': 'bool',
            'is_monitored': 'bool',
            'is_screen_monitored': 'bool',
            'filter_wrap_up_notes': 'bool',
            'match_all': 'bool'
        }

        self.attribute_map = {
            'is_waiting': 'isWaiting',
            'is_active': 'isActive',
            'is_acd': 'isAcd',
            'is_preferred': 'isPreferred',
            'is_screenshare': 'isScreenshare',
            'is_cobrowse': 'isCobrowse',
            'is_voicemail': 'isVoicemail',
            'is_flagged': 'isFlagged',
            'is_monitored': 'isMonitored',
            'is_screen_monitored': 'isScreenMonitored',
            'filter_wrap_up_notes': 'filterWrapUpNotes',
            'match_all': 'matchAll'
        }

        self._is_waiting = None
        self._is_active = None
        self._is_acd = None
        self._is_preferred = None
        self._is_screenshare = None
        self._is_cobrowse = None
        self._is_voicemail = None
        self._is_flagged = None
        self._is_monitored = None
        self._is_screen_monitored = None
        self._filter_wrap_up_notes = None
        self._match_all = None

    @property
    def is_waiting(self) -> bool:
        """
        Gets the is_waiting of this ConversationProperties.
        Indicates filtering for waiting

        :return: The is_waiting of this ConversationProperties.
        :rtype: bool
        """
        return self._is_waiting

    @is_waiting.setter
    def is_waiting(self, is_waiting: bool) -> None:
        """
        Sets the is_waiting of this ConversationProperties.
        Indicates filtering for waiting

        :param is_waiting: The is_waiting of this ConversationProperties.
        :type: bool
        """
        

        self._is_waiting = is_waiting

    @property
    def is_active(self) -> bool:
        """
        Gets the is_active of this ConversationProperties.
        Indicates filtering for active

        :return: The is_active of this ConversationProperties.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool) -> None:
        """
        Sets the is_active of this ConversationProperties.
        Indicates filtering for active

        :param is_active: The is_active of this ConversationProperties.
        :type: bool
        """
        

        self._is_active = is_active

    @property
    def is_acd(self) -> bool:
        """
        Gets the is_acd of this ConversationProperties.
        Indicates filtering for Acd

        :return: The is_acd of this ConversationProperties.
        :rtype: bool
        """
        return self._is_acd

    @is_acd.setter
    def is_acd(self, is_acd: bool) -> None:
        """
        Sets the is_acd of this ConversationProperties.
        Indicates filtering for Acd

        :param is_acd: The is_acd of this ConversationProperties.
        :type: bool
        """
        

        self._is_acd = is_acd

    @property
    def is_preferred(self) -> bool:
        """
        Gets the is_preferred of this ConversationProperties.
        Indicates filtering for Preferred Agent Routing

        :return: The is_preferred of this ConversationProperties.
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred: bool) -> None:
        """
        Sets the is_preferred of this ConversationProperties.
        Indicates filtering for Preferred Agent Routing

        :param is_preferred: The is_preferred of this ConversationProperties.
        :type: bool
        """
        

        self._is_preferred = is_preferred

    @property
    def is_screenshare(self) -> bool:
        """
        Gets the is_screenshare of this ConversationProperties.
        Indicates filtering for screenshare

        :return: The is_screenshare of this ConversationProperties.
        :rtype: bool
        """
        return self._is_screenshare

    @is_screenshare.setter
    def is_screenshare(self, is_screenshare: bool) -> None:
        """
        Sets the is_screenshare of this ConversationProperties.
        Indicates filtering for screenshare

        :param is_screenshare: The is_screenshare of this ConversationProperties.
        :type: bool
        """
        

        self._is_screenshare = is_screenshare

    @property
    def is_cobrowse(self) -> bool:
        """
        Gets the is_cobrowse of this ConversationProperties.
        Indicates filtering for Cobrowse

        :return: The is_cobrowse of this ConversationProperties.
        :rtype: bool
        """
        return self._is_cobrowse

    @is_cobrowse.setter
    def is_cobrowse(self, is_cobrowse: bool) -> None:
        """
        Sets the is_cobrowse of this ConversationProperties.
        Indicates filtering for Cobrowse

        :param is_cobrowse: The is_cobrowse of this ConversationProperties.
        :type: bool
        """
        

        self._is_cobrowse = is_cobrowse

    @property
    def is_voicemail(self) -> bool:
        """
        Gets the is_voicemail of this ConversationProperties.
        Indicates filtering for Voice mail

        :return: The is_voicemail of this ConversationProperties.
        :rtype: bool
        """
        return self._is_voicemail

    @is_voicemail.setter
    def is_voicemail(self, is_voicemail: bool) -> None:
        """
        Sets the is_voicemail of this ConversationProperties.
        Indicates filtering for Voice mail

        :param is_voicemail: The is_voicemail of this ConversationProperties.
        :type: bool
        """
        

        self._is_voicemail = is_voicemail

    @property
    def is_flagged(self) -> bool:
        """
        Gets the is_flagged of this ConversationProperties.
        Indicates filtering for flagged

        :return: The is_flagged of this ConversationProperties.
        :rtype: bool
        """
        return self._is_flagged

    @is_flagged.setter
    def is_flagged(self, is_flagged: bool) -> None:
        """
        Sets the is_flagged of this ConversationProperties.
        Indicates filtering for flagged

        :param is_flagged: The is_flagged of this ConversationProperties.
        :type: bool
        """
        

        self._is_flagged = is_flagged

    @property
    def is_monitored(self) -> bool:
        """
        Gets the is_monitored of this ConversationProperties.
        Indicates filtering for monitored

        :return: The is_monitored of this ConversationProperties.
        :rtype: bool
        """
        return self._is_monitored

    @is_monitored.setter
    def is_monitored(self, is_monitored: bool) -> None:
        """
        Sets the is_monitored of this ConversationProperties.
        Indicates filtering for monitored

        :param is_monitored: The is_monitored of this ConversationProperties.
        :type: bool
        """
        

        self._is_monitored = is_monitored

    @property
    def is_screen_monitored(self) -> bool:
        """
        Gets the is_screen_monitored of this ConversationProperties.
        Indicates filtering for screenMonitored

        :return: The is_screen_monitored of this ConversationProperties.
        :rtype: bool
        """
        return self._is_screen_monitored

    @is_screen_monitored.setter
    def is_screen_monitored(self, is_screen_monitored: bool) -> None:
        """
        Sets the is_screen_monitored of this ConversationProperties.
        Indicates filtering for screenMonitored

        :param is_screen_monitored: The is_screen_monitored of this ConversationProperties.
        :type: bool
        """
        

        self._is_screen_monitored = is_screen_monitored

    @property
    def filter_wrap_up_notes(self) -> bool:
        """
        Gets the filter_wrap_up_notes of this ConversationProperties.
        Indicates filtering for WrapUpNotes

        :return: The filter_wrap_up_notes of this ConversationProperties.
        :rtype: bool
        """
        return self._filter_wrap_up_notes

    @filter_wrap_up_notes.setter
    def filter_wrap_up_notes(self, filter_wrap_up_notes: bool) -> None:
        """
        Sets the filter_wrap_up_notes of this ConversationProperties.
        Indicates filtering for WrapUpNotes

        :param filter_wrap_up_notes: The filter_wrap_up_notes of this ConversationProperties.
        :type: bool
        """
        

        self._filter_wrap_up_notes = filter_wrap_up_notes

    @property
    def match_all(self) -> bool:
        """
        Gets the match_all of this ConversationProperties.
        Indicates comparison operation, TRUE indicates filters will use AND logic, FALSE indicates OR logic

        :return: The match_all of this ConversationProperties.
        :rtype: bool
        """
        return self._match_all

    @match_all.setter
    def match_all(self, match_all: bool) -> None:
        """
        Sets the match_all of this ConversationProperties.
        Indicates comparison operation, TRUE indicates filters will use AND logic, FALSE indicates OR logic

        :param match_all: The match_all of this ConversationProperties.
        :type: bool
        """
        

        self._match_all = match_all

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

