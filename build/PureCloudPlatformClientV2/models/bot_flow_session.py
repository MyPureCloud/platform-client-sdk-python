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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import AddressableEntityRef
    from . import BotChannel
    from . import Entity

class BotFlowSession(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BotFlowSession - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'flow': 'Entity',
            'channel': 'BotChannel',
            'language': 'str',
            'end_language': 'str',
            'bot_result': 'str',
            'bot_result_category': 'str',
            'date_created': 'datetime',
            'conversation': 'AddressableEntityRef'
        }

        self.attribute_map = {
            'id': 'id',
            'flow': 'flow',
            'channel': 'channel',
            'language': 'language',
            'end_language': 'endLanguage',
            'bot_result': 'botResult',
            'bot_result_category': 'botResultCategory',
            'date_created': 'dateCreated',
            'conversation': 'conversation'
        }

        self._id = None
        self._flow = None
        self._channel = None
        self._language = None
        self._end_language = None
        self._bot_result = None
        self._bot_result_category = None
        self._date_created = None
        self._conversation = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BotFlowSession.
        The ID of the bot session.

        :return: The id of this BotFlowSession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BotFlowSession.
        The ID of the bot session.

        :param id: The id of this BotFlowSession.
        :type: str
        """
        

        self._id = id

    @property
    def flow(self) -> 'Entity':
        """
        Gets the flow of this BotFlowSession.
        The flow associated to this bot session.

        :return: The flow of this BotFlowSession.
        :rtype: Entity
        """
        return self._flow

    @flow.setter
    def flow(self, flow: 'Entity') -> None:
        """
        Sets the flow of this BotFlowSession.
        The flow associated to this bot session.

        :param flow: The flow of this BotFlowSession.
        :type: Entity
        """
        

        self._flow = flow

    @property
    def channel(self) -> 'BotChannel':
        """
        Gets the channel of this BotFlowSession.
        Channel-specific information that describes the message channel/provider.

        :return: The channel of this BotFlowSession.
        :rtype: BotChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel: 'BotChannel') -> None:
        """
        Sets the channel of this BotFlowSession.
        Channel-specific information that describes the message channel/provider.

        :param channel: The channel of this BotFlowSession.
        :type: BotChannel
        """
        

        self._channel = channel

    @property
    def language(self) -> str:
        """
        Gets the language of this BotFlowSession.
        The initial language of operation for the session.

        :return: The language of this BotFlowSession.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this BotFlowSession.
        The initial language of operation for the session.

        :param language: The language of this BotFlowSession.
        :type: str
        """
        

        self._language = language

    @property
    def end_language(self) -> str:
        """
        Gets the end_language of this BotFlowSession.
        The language of the session at the time the session ended

        :return: The end_language of this BotFlowSession.
        :rtype: str
        """
        return self._end_language

    @end_language.setter
    def end_language(self, end_language: str) -> None:
        """
        Sets the end_language of this BotFlowSession.
        The language of the session at the time the session ended

        :param end_language: The end_language of this BotFlowSession.
        :type: str
        """
        

        self._end_language = end_language

    @property
    def bot_result(self) -> str:
        """
        Gets the bot_result of this BotFlowSession.
        The reason for session termination.

        :return: The bot_result of this BotFlowSession.
        :rtype: str
        """
        return self._bot_result

    @bot_result.setter
    def bot_result(self, bot_result: str) -> None:
        """
        Sets the bot_result of this BotFlowSession.
        The reason for session termination.

        :param bot_result: The bot_result of this BotFlowSession.
        :type: str
        """
        if isinstance(bot_result, int):
            bot_result = str(bot_result)
        allowed_values = ["Unknown", "ExitRequestedByUser", "ExitRequestedByBot", "ExitError", "ExitRecognitionFailure", "DisconnectRequestedByUser", "DisconnectRequestedByBot", "DisconnectSessionExpired", "DisconnectError", "DisconnectRecognitionFailure", "TransferToACD"]
        if bot_result.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for bot_result -> " + bot_result)
            self._bot_result = "outdated_sdk_version"
        else:
            self._bot_result = bot_result

    @property
    def bot_result_category(self) -> str:
        """
        Gets the bot_result_category of this BotFlowSession.
        The category of result for the session.

        :return: The bot_result_category of this BotFlowSession.
        :rtype: str
        """
        return self._bot_result_category

    @bot_result_category.setter
    def bot_result_category(self, bot_result_category: str) -> None:
        """
        Sets the bot_result_category of this BotFlowSession.
        The category of result for the session.

        :param bot_result_category: The bot_result_category of this BotFlowSession.
        :type: str
        """
        if isinstance(bot_result_category, int):
            bot_result_category = str(bot_result_category)
        allowed_values = ["Unknown", "UserExit", "BotExit", "Error", "RecognitionFailure", "UserDisconnect", "BotDisconnect", "SessionExpired", "Transfer"]
        if bot_result_category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for bot_result_category -> " + bot_result_category)
            self._bot_result_category = "outdated_sdk_version"
        else:
            self._bot_result_category = bot_result_category

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this BotFlowSession.
        Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this BotFlowSession.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this BotFlowSession.
        Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this BotFlowSession.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def conversation(self) -> 'AddressableEntityRef':
        """
        Gets the conversation of this BotFlowSession.
        The conversation details, across potentially multiple Bot Flow sessions.

        :return: The conversation of this BotFlowSession.
        :rtype: AddressableEntityRef
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'AddressableEntityRef') -> None:
        """
        Sets the conversation of this BotFlowSession.
        The conversation details, across potentially multiple Bot Flow sessions.

        :param conversation: The conversation of this BotFlowSession.
        :type: AddressableEntityRef
        """
        

        self._conversation = conversation

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
