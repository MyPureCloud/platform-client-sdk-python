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


class QueueConversationCallEventTopicQueueMediaSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationCallEventTopicQueueMediaSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alerting_timeout_seconds': 'int',
            'auto_answer_alert_tone_seconds': 'float',
            'manual_answer_alert_tone_seconds': 'float',
            'enable_auto_answer': 'bool'
        }

        self.attribute_map = {
            'alerting_timeout_seconds': 'alertingTimeoutSeconds',
            'auto_answer_alert_tone_seconds': 'autoAnswerAlertToneSeconds',
            'manual_answer_alert_tone_seconds': 'manualAnswerAlertToneSeconds',
            'enable_auto_answer': 'enableAutoAnswer'
        }

        self._alerting_timeout_seconds = None
        self._auto_answer_alert_tone_seconds = None
        self._manual_answer_alert_tone_seconds = None
        self._enable_auto_answer = None

    @property
    def alerting_timeout_seconds(self) -> int:
        """
        Gets the alerting_timeout_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies how long the agent has to answer an interaction before being marked as not responding.

        :return: The alerting_timeout_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :rtype: int
        """
        return self._alerting_timeout_seconds

    @alerting_timeout_seconds.setter
    def alerting_timeout_seconds(self, alerting_timeout_seconds: int) -> None:
        """
        Sets the alerting_timeout_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies how long the agent has to answer an interaction before being marked as not responding.

        :param alerting_timeout_seconds: The alerting_timeout_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :type: int
        """
        

        self._alerting_timeout_seconds = alerting_timeout_seconds

    @property
    def auto_answer_alert_tone_seconds(self) -> float:
        """
        Gets the auto_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies the duration of the alerting sound to be played for auto answered interactions.

        :return: The auto_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :rtype: float
        """
        return self._auto_answer_alert_tone_seconds

    @auto_answer_alert_tone_seconds.setter
    def auto_answer_alert_tone_seconds(self, auto_answer_alert_tone_seconds: float) -> None:
        """
        Sets the auto_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies the duration of the alerting sound to be played for auto answered interactions.

        :param auto_answer_alert_tone_seconds: The auto_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :type: float
        """
        

        self._auto_answer_alert_tone_seconds = auto_answer_alert_tone_seconds

    @property
    def manual_answer_alert_tone_seconds(self) -> float:
        """
        Gets the manual_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies the duration of the alerting sound to be played for manually answered interactions

        :return: The manual_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :rtype: float
        """
        return self._manual_answer_alert_tone_seconds

    @manual_answer_alert_tone_seconds.setter
    def manual_answer_alert_tone_seconds(self, manual_answer_alert_tone_seconds: float) -> None:
        """
        Sets the manual_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        Specifies the duration of the alerting sound to be played for manually answered interactions

        :param manual_answer_alert_tone_seconds: The manual_answer_alert_tone_seconds of this QueueConversationCallEventTopicQueueMediaSettings.
        :type: float
        """
        

        self._manual_answer_alert_tone_seconds = manual_answer_alert_tone_seconds

    @property
    def enable_auto_answer(self) -> bool:
        """
        Gets the enable_auto_answer of this QueueConversationCallEventTopicQueueMediaSettings.
        Flag to indicate if auto answer is enabled for the given media type or media subtype.

        :return: The enable_auto_answer of this QueueConversationCallEventTopicQueueMediaSettings.
        :rtype: bool
        """
        return self._enable_auto_answer

    @enable_auto_answer.setter
    def enable_auto_answer(self, enable_auto_answer: bool) -> None:
        """
        Sets the enable_auto_answer of this QueueConversationCallEventTopicQueueMediaSettings.
        Flag to indicate if auto answer is enabled for the given media type or media subtype.

        :param enable_auto_answer: The enable_auto_answer of this QueueConversationCallEventTopicQueueMediaSettings.
        :type: bool
        """
        

        self._enable_auto_answer = enable_auto_answer

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

