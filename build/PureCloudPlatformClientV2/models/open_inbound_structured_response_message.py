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
    from . import ContentButtonResponse
    from . import OpenInboundMessageMessagingChannel

class OpenInboundStructuredResponseMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OpenInboundStructuredResponseMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel': 'OpenInboundMessageMessagingChannel',
            'button_response': 'ContentButtonResponse',
            'originating_message_id': 'str'
        }

        self.attribute_map = {
            'channel': 'channel',
            'button_response': 'buttonResponse',
            'originating_message_id': 'originatingMessageId'
        }

        self._channel = None
        self._button_response = None
        self._originating_message_id = None

    @property
    def channel(self) -> 'OpenInboundMessageMessagingChannel':
        """
        Gets the channel of this OpenInboundStructuredResponseMessage.
        Channel-specific information that describes the message and the message channel/provider.

        :return: The channel of this OpenInboundStructuredResponseMessage.
        :rtype: OpenInboundMessageMessagingChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel: 'OpenInboundMessageMessagingChannel') -> None:
        """
        Sets the channel of this OpenInboundStructuredResponseMessage.
        Channel-specific information that describes the message and the message channel/provider.

        :param channel: The channel of this OpenInboundStructuredResponseMessage.
        :type: OpenInboundMessageMessagingChannel
        """
        

        self._channel = channel

    @property
    def button_response(self) -> 'ContentButtonResponse':
        """
        Gets the button_response of this OpenInboundStructuredResponseMessage.
        Button response element.

        :return: The button_response of this OpenInboundStructuredResponseMessage.
        :rtype: ContentButtonResponse
        """
        return self._button_response

    @button_response.setter
    def button_response(self, button_response: 'ContentButtonResponse') -> None:
        """
        Sets the button_response of this OpenInboundStructuredResponseMessage.
        Button response element.

        :param button_response: The button_response of this OpenInboundStructuredResponseMessage.
        :type: ContentButtonResponse
        """
        

        self._button_response = button_response

    @property
    def originating_message_id(self) -> str:
        """
        Gets the originating_message_id of this OpenInboundStructuredResponseMessage.
        Id of original structured message that this messages responds to.

        :return: The originating_message_id of this OpenInboundStructuredResponseMessage.
        :rtype: str
        """
        return self._originating_message_id

    @originating_message_id.setter
    def originating_message_id(self, originating_message_id: str) -> None:
        """
        Sets the originating_message_id of this OpenInboundStructuredResponseMessage.
        Id of original structured message that this messages responds to.

        :param originating_message_id: The originating_message_id of this OpenInboundStructuredResponseMessage.
        :type: str
        """
        

        self._originating_message_id = originating_message_id

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

