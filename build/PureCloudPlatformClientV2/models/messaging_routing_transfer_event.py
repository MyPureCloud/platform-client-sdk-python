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


class MessagingRoutingTransferEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessagingRoutingTransferEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_id': 'str',
            'event_date_time': 'datetime',
            'conversation_id': 'str',
            'transfer_type': 'str',
            'command_id': 'str',
            'initiating_communication_id': 'str',
            'target_communication_id': 'str',
            'object_communication_id': 'str',
            'destination_queue_id': 'str',
            'language_id': 'str',
            'skill_ids': 'list[str]'
        }

        self.attribute_map = {
            'event_id': 'eventId',
            'event_date_time': 'eventDateTime',
            'conversation_id': 'conversationId',
            'transfer_type': 'transferType',
            'command_id': 'commandId',
            'initiating_communication_id': 'initiatingCommunicationId',
            'target_communication_id': 'targetCommunicationId',
            'object_communication_id': 'objectCommunicationId',
            'destination_queue_id': 'destinationQueueId',
            'language_id': 'languageId',
            'skill_ids': 'skillIds'
        }

        self._event_id = None
        self._event_date_time = None
        self._conversation_id = None
        self._transfer_type = None
        self._command_id = None
        self._initiating_communication_id = None
        self._target_communication_id = None
        self._object_communication_id = None
        self._destination_queue_id = None
        self._language_id = None
        self._skill_ids = None

    @property
    def event_id(self) -> str:
        """
        Gets the event_id of this MessagingRoutingTransferEvent.
        A unique (V4 UUID) eventId for this event

        :return: The event_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str) -> None:
        """
        Sets the event_id of this MessagingRoutingTransferEvent.
        A unique (V4 UUID) eventId for this event

        :param event_id: The event_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._event_id = event_id

    @property
    def event_date_time(self) -> datetime:
        """
        Gets the event_date_time of this MessagingRoutingTransferEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_date_time of this MessagingRoutingTransferEvent.
        :rtype: datetime
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time: datetime) -> None:
        """
        Sets the event_date_time of this MessagingRoutingTransferEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_date_time: The event_date_time of this MessagingRoutingTransferEvent.
        :type: datetime
        """
        

        self._event_date_time = event_date_time

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this MessagingRoutingTransferEvent.
        A unique Id (V4 UUID) identifying this conversation

        :return: The conversation_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this MessagingRoutingTransferEvent.
        A unique Id (V4 UUID) identifying this conversation

        :param conversation_id: The conversation_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def transfer_type(self) -> str:
        """
        Gets the transfer_type of this MessagingRoutingTransferEvent.
        Indicates the desired type of transfer.

        :return: The transfer_type of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type: str) -> None:
        """
        Sets the transfer_type of this MessagingRoutingTransferEvent.
        Indicates the desired type of transfer.

        :param transfer_type: The transfer_type of this MessagingRoutingTransferEvent.
        :type: str
        """
        if isinstance(transfer_type, int):
            transfer_type = str(transfer_type)
        allowed_values = ["Attended", "Unattended"]
        if transfer_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for transfer_type -> " + transfer_type)
            self._transfer_type = "outdated_sdk_version"
        else:
            self._transfer_type = transfer_type

    @property
    def command_id(self) -> str:
        """
        Gets the command_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) used by the external platform to refer to the transfer in subsequent *Transfer events.

        :return: The command_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id: str) -> None:
        """
        Sets the command_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) used by the external platform to refer to the transfer in subsequent *Transfer events.

        :param command_id: The command_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._command_id = command_id

    @property
    def initiating_communication_id(self) -> str:
        """
        Gets the initiating_communication_id of this MessagingRoutingTransferEvent.
        Indicates the desired type of transfer.

        :return: The initiating_communication_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._initiating_communication_id

    @initiating_communication_id.setter
    def initiating_communication_id(self, initiating_communication_id: str) -> None:
        """
        Sets the initiating_communication_id of this MessagingRoutingTransferEvent.
        Indicates the desired type of transfer.

        :param initiating_communication_id: The initiating_communication_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._initiating_communication_id = initiating_communication_id

    @property
    def target_communication_id(self) -> str:
        """
        Gets the target_communication_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the communication that is being transferred away from. In many cases this will be the same as the `initiatingCommunicationId`.

        :return: The target_communication_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._target_communication_id

    @target_communication_id.setter
    def target_communication_id(self, target_communication_id: str) -> None:
        """
        Sets the target_communication_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the communication that is being transferred away from. In many cases this will be the same as the `initiatingCommunicationId`.

        :param target_communication_id: The target_communication_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._target_communication_id = target_communication_id

    @property
    def object_communication_id(self) -> str:
        """
        Gets the object_communication_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the communication that is being transferred.

        :return: The object_communication_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._object_communication_id

    @object_communication_id.setter
    def object_communication_id(self, object_communication_id: str) -> None:
        """
        Sets the object_communication_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the communication that is being transferred.

        :param object_communication_id: The object_communication_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._object_communication_id = object_communication_id

    @property
    def destination_queue_id(self) -> str:
        """
        Gets the destination_queue_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the desired destination queue that the object communication should be transferred to.

        :return: The destination_queue_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._destination_queue_id

    @destination_queue_id.setter
    def destination_queue_id(self, destination_queue_id: str) -> None:
        """
        Sets the destination_queue_id of this MessagingRoutingTransferEvent.
        The id (V4 UUID) of the desired destination queue that the object communication should be transferred to.

        :param destination_queue_id: The destination_queue_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._destination_queue_id = destination_queue_id

    @property
    def language_id(self) -> str:
        """
        Gets the language_id of this MessagingRoutingTransferEvent.
        The unique identifier (V4 UUID) for the language that should be used to determine the destination for the conversation.

        :return: The language_id of this MessagingRoutingTransferEvent.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id: str) -> None:
        """
        Sets the language_id of this MessagingRoutingTransferEvent.
        The unique identifier (V4 UUID) for the language that should be used to determine the destination for the conversation.

        :param language_id: The language_id of this MessagingRoutingTransferEvent.
        :type: str
        """
        

        self._language_id = language_id

    @property
    def skill_ids(self) -> List[str]:
        """
        Gets the skill_ids of this MessagingRoutingTransferEvent.
        The unique identifiers (V4 UUID) for the skills that should be used to determine the destination for the conversation.

        :return: The skill_ids of this MessagingRoutingTransferEvent.
        :rtype: list[str]
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids: List[str]) -> None:
        """
        Sets the skill_ids of this MessagingRoutingTransferEvent.
        The unique identifiers (V4 UUID) for the skills that should be used to determine the destination for the conversation.

        :param skill_ids: The skill_ids of this MessagingRoutingTransferEvent.
        :type: list[str]
        """
        

        self._skill_ids = skill_ids

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

