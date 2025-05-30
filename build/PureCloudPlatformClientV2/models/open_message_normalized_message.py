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
    from . import OpenMessageContent
    from . import OpenMessagingChannel

class OpenMessageNormalizedMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OpenMessageNormalizedMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'channel': 'OpenMessagingChannel',
            'type': 'str',
            'text': 'str',
            'content': 'list[OpenMessageContent]',
            'metadata': 'dict(str, str)',
            'conversation_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'channel': 'channel',
            'type': 'type',
            'text': 'text',
            'content': 'content',
            'metadata': 'metadata',
            'conversation_id': 'conversationId'
        }

        self._id = None
        self._channel = None
        self._type = None
        self._text = None
        self._content = None
        self._metadata = None
        self._conversation_id = None

    @property
    def id(self) -> str:
        """
        Gets the id of this OpenMessageNormalizedMessage.
        Unique ID of the message generated by Messaging Platform.

        :return: The id of this OpenMessageNormalizedMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this OpenMessageNormalizedMessage.
        Unique ID of the message generated by Messaging Platform.

        :param id: The id of this OpenMessageNormalizedMessage.
        :type: str
        """
        

        self._id = id

    @property
    def channel(self) -> 'OpenMessagingChannel':
        """
        Gets the channel of this OpenMessageNormalizedMessage.
        Channel-specific information that describes the message and the message channel/provider.

        :return: The channel of this OpenMessageNormalizedMessage.
        :rtype: OpenMessagingChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel: 'OpenMessagingChannel') -> None:
        """
        Sets the channel of this OpenMessageNormalizedMessage.
        Channel-specific information that describes the message and the message channel/provider.

        :param channel: The channel of this OpenMessageNormalizedMessage.
        :type: OpenMessagingChannel
        """
        

        self._channel = channel

    @property
    def type(self) -> str:
        """
        Gets the type of this OpenMessageNormalizedMessage.
        Message type.

        :return: The type of this OpenMessageNormalizedMessage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this OpenMessageNormalizedMessage.
        Message type.

        :param type: The type of this OpenMessageNormalizedMessage.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Text"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def text(self) -> str:
        """
        Gets the text of this OpenMessageNormalizedMessage.
        Message text.

        :return: The text of this OpenMessageNormalizedMessage.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text of this OpenMessageNormalizedMessage.
        Message text.

        :param text: The text of this OpenMessageNormalizedMessage.
        :type: str
        """
        

        self._text = text

    @property
    def content(self) -> List['OpenMessageContent']:
        """
        Gets the content of this OpenMessageNormalizedMessage.
        List of content elements.

        :return: The content of this OpenMessageNormalizedMessage.
        :rtype: list[OpenMessageContent]
        """
        return self._content

    @content.setter
    def content(self, content: List['OpenMessageContent']) -> None:
        """
        Sets the content of this OpenMessageNormalizedMessage.
        List of content elements.

        :param content: The content of this OpenMessageNormalizedMessage.
        :type: list[OpenMessageContent]
        """
        

        self._content = content

    @property
    def metadata(self) -> Dict[str, str]:
        """
        Gets the metadata of this OpenMessageNormalizedMessage.
        Additional metadata about this message.

        :return: The metadata of this OpenMessageNormalizedMessage.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Dict[str, str]) -> None:
        """
        Sets the metadata of this OpenMessageNormalizedMessage.
        Additional metadata about this message.

        :param metadata: The metadata of this OpenMessageNormalizedMessage.
        :type: dict(str, str)
        """
        

        self._metadata = metadata

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this OpenMessageNormalizedMessage.
        The conversationId context for the message

        :return: The conversation_id of this OpenMessageNormalizedMessage.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this OpenMessageNormalizedMessage.
        The conversationId context for the message

        :param conversation_id: The conversation_id of this OpenMessageNormalizedMessage.
        :type: str
        """
        

        self._conversation_id = conversation_id

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

