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


class EmailThreadingSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EmailThreadingSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_new_conversation_on_subject_change': 'bool',
            'timeout_in_minutes': 'int'
        }

        self.attribute_map = {
            'start_new_conversation_on_subject_change': 'startNewConversationOnSubjectChange',
            'timeout_in_minutes': 'timeoutInMinutes'
        }

        self._start_new_conversation_on_subject_change = None
        self._timeout_in_minutes = None

    @property
    def start_new_conversation_on_subject_change(self) -> bool:
        """
        Gets the start_new_conversation_on_subject_change of this EmailThreadingSettings.
        This setting controls whether a new conversation is started if the subject of an inbound email is different from the subject of the current conversation. RE: and FWD: prefixes in any language are ignored.

        :return: The start_new_conversation_on_subject_change of this EmailThreadingSettings.
        :rtype: bool
        """
        return self._start_new_conversation_on_subject_change

    @start_new_conversation_on_subject_change.setter
    def start_new_conversation_on_subject_change(self, start_new_conversation_on_subject_change: bool) -> None:
        """
        Sets the start_new_conversation_on_subject_change of this EmailThreadingSettings.
        This setting controls whether a new conversation is started if the subject of an inbound email is different from the subject of the current conversation. RE: and FWD: prefixes in any language are ignored.

        :param start_new_conversation_on_subject_change: The start_new_conversation_on_subject_change of this EmailThreadingSettings.
        :type: bool
        """
        

        self._start_new_conversation_on_subject_change = start_new_conversation_on_subject_change

    @property
    def timeout_in_minutes(self) -> int:
        """
        Gets the timeout_in_minutes of this EmailThreadingSettings.
        In minutes, how long an email conversation should keep being threaded after being disconnected.

        :return: The timeout_in_minutes of this EmailThreadingSettings.
        :rtype: int
        """
        return self._timeout_in_minutes

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, timeout_in_minutes: int) -> None:
        """
        Sets the timeout_in_minutes of this EmailThreadingSettings.
        In minutes, how long an email conversation should keep being threaded after being disconnected.

        :param timeout_in_minutes: The timeout_in_minutes of this EmailThreadingSettings.
        :type: int
        """
        

        self._timeout_in_minutes = timeout_in_minutes

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

