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
    from . import ConversationDivisionMembership
    from . import Participant
    from . import TransferResponse

class Conversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Conversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'external_tag': 'str',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'address': 'str',
            'participants': 'list[Participant]',
            'conversation_ids': 'list[str]',
            'max_participants': 'int',
            'recording_state': 'str',
            'state': 'str',
            'divisions': 'list[ConversationDivisionMembership]',
            'recent_transfers': 'list[TransferResponse]',
            'secure_pause': 'bool',
            'utilization_label_id': 'str',
            'inactivity_timeout': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'external_tag': 'externalTag',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'address': 'address',
            'participants': 'participants',
            'conversation_ids': 'conversationIds',
            'max_participants': 'maxParticipants',
            'recording_state': 'recordingState',
            'state': 'state',
            'divisions': 'divisions',
            'recent_transfers': 'recentTransfers',
            'secure_pause': 'securePause',
            'utilization_label_id': 'utilizationLabelId',
            'inactivity_timeout': 'inactivityTimeout',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._external_tag = None
        self._start_time = None
        self._end_time = None
        self._address = None
        self._participants = None
        self._conversation_ids = None
        self._max_participants = None
        self._recording_state = None
        self._state = None
        self._divisions = None
        self._recent_transfers = None
        self._secure_pause = None
        self._utilization_label_id = None
        self._inactivity_timeout = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Conversation.
        The globally unique identifier for the object.

        :return: The id of this Conversation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Conversation.
        The globally unique identifier for the object.

        :param id: The id of this Conversation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Conversation.


        :return: The name of this Conversation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Conversation.


        :param name: The name of this Conversation.
        :type: str
        """
        

        self._name = name

    @property
    def external_tag(self) -> str:
        """
        Gets the external_tag of this Conversation.
        The external tag associated with the conversation.

        :return: The external_tag of this Conversation.
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag: str) -> None:
        """
        Sets the external_tag of this Conversation.
        The external tag associated with the conversation.

        :param external_tag: The external_tag of this Conversation.
        :type: str
        """
        

        self._external_tag = external_tag

    @property
    def start_time(self) -> datetime:
        """
        Gets the start_time of this Conversation.
        The time when the conversation started. This will be the time when the first participant joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_time of this Conversation.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime) -> None:
        """
        Sets the start_time of this Conversation.
        The time when the conversation started. This will be the time when the first participant joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_time: The start_time of this Conversation.
        :type: datetime
        """
        

        self._start_time = start_time

    @property
    def end_time(self) -> datetime:
        """
        Gets the end_time of this Conversation.
        The time when the conversation ended. This will be the time when the last participant left the conversation, or null when the conversation is still active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_time of this Conversation.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime) -> None:
        """
        Sets the end_time of this Conversation.
        The time when the conversation ended. This will be the time when the last participant left the conversation, or null when the conversation is still active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_time: The end_time of this Conversation.
        :type: datetime
        """
        

        self._end_time = end_time

    @property
    def address(self) -> str:
        """
        Gets the address of this Conversation.
        The address of the conversation as seen from an external participant. For phone calls this will be the DNIS for inbound calls and the ANI for outbound calls. For other media types this will be the address of the destination participant for inbound and the address of the initiating participant for outbound.

        :return: The address of this Conversation.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this Conversation.
        The address of the conversation as seen from an external participant. For phone calls this will be the DNIS for inbound calls and the ANI for outbound calls. For other media types this will be the address of the destination participant for inbound and the address of the initiating participant for outbound.

        :param address: The address of this Conversation.
        :type: str
        """
        

        self._address = address

    @property
    def participants(self) -> List['Participant']:
        """
        Gets the participants of this Conversation.
        The list of all participants in the conversation.

        :return: The participants of this Conversation.
        :rtype: list[Participant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants: List['Participant']) -> None:
        """
        Sets the participants of this Conversation.
        The list of all participants in the conversation.

        :param participants: The participants of this Conversation.
        :type: list[Participant]
        """
        

        self._participants = participants

    @property
    def conversation_ids(self) -> List[str]:
        """
        Gets the conversation_ids of this Conversation.
        A list of conversations to merge into this conversation to create a conference. This field is null except when being used to create a conference.

        :return: The conversation_ids of this Conversation.
        :rtype: list[str]
        """
        return self._conversation_ids

    @conversation_ids.setter
    def conversation_ids(self, conversation_ids: List[str]) -> None:
        """
        Sets the conversation_ids of this Conversation.
        A list of conversations to merge into this conversation to create a conference. This field is null except when being used to create a conference.

        :param conversation_ids: The conversation_ids of this Conversation.
        :type: list[str]
        """
        

        self._conversation_ids = conversation_ids

    @property
    def max_participants(self) -> int:
        """
        Gets the max_participants of this Conversation.
        If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference.

        :return: The max_participants of this Conversation.
        :rtype: int
        """
        return self._max_participants

    @max_participants.setter
    def max_participants(self, max_participants: int) -> None:
        """
        Sets the max_participants of this Conversation.
        If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference.

        :param max_participants: The max_participants of this Conversation.
        :type: int
        """
        

        self._max_participants = max_participants

    @property
    def recording_state(self) -> str:
        """
        Gets the recording_state of this Conversation.
        On update, 'paused' initiates a secure pause, 'active' resumes any paused recordings; otherwise indicates state of conversation recording.

        :return: The recording_state of this Conversation.
        :rtype: str
        """
        return self._recording_state

    @recording_state.setter
    def recording_state(self, recording_state: str) -> None:
        """
        Sets the recording_state of this Conversation.
        On update, 'paused' initiates a secure pause, 'active' resumes any paused recordings; otherwise indicates state of conversation recording.

        :param recording_state: The recording_state of this Conversation.
        :type: str
        """
        if isinstance(recording_state, int):
            recording_state = str(recording_state)
        allowed_values = ["ACTIVE", "PAUSED", "NONE"]
        if recording_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for recording_state -> " + recording_state)
            self._recording_state = "outdated_sdk_version"
        else:
            self._recording_state = recording_state

    @property
    def state(self) -> str:
        """
        Gets the state of this Conversation.
        On update, 'disconnected' will disconnect the conversation. No other values are valid. When reading conversations, this field will never have a value present.

        :return: The state of this Conversation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Conversation.
        On update, 'disconnected' will disconnect the conversation. No other values are valid. When reading conversations, this field will never have a value present.

        :param state: The state of this Conversation.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "converting", "uploading", "transmitting", "parked", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def divisions(self) -> List['ConversationDivisionMembership']:
        """
        Gets the divisions of this Conversation.
        Identifiers of divisions associated with this conversation

        :return: The divisions of this Conversation.
        :rtype: list[ConversationDivisionMembership]
        """
        return self._divisions

    @divisions.setter
    def divisions(self, divisions: List['ConversationDivisionMembership']) -> None:
        """
        Sets the divisions of this Conversation.
        Identifiers of divisions associated with this conversation

        :param divisions: The divisions of this Conversation.
        :type: list[ConversationDivisionMembership]
        """
        

        self._divisions = divisions

    @property
    def recent_transfers(self) -> List['TransferResponse']:
        """
        Gets the recent_transfers of this Conversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :return: The recent_transfers of this Conversation.
        :rtype: list[TransferResponse]
        """
        return self._recent_transfers

    @recent_transfers.setter
    def recent_transfers(self, recent_transfers: List['TransferResponse']) -> None:
        """
        Sets the recent_transfers of this Conversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :param recent_transfers: The recent_transfers of this Conversation.
        :type: list[TransferResponse]
        """
        

        self._recent_transfers = recent_transfers

    @property
    def secure_pause(self) -> bool:
        """
        Gets the secure_pause of this Conversation.
        True when the recording of this conversation is in secure pause status.

        :return: The secure_pause of this Conversation.
        :rtype: bool
        """
        return self._secure_pause

    @secure_pause.setter
    def secure_pause(self, secure_pause: bool) -> None:
        """
        Sets the secure_pause of this Conversation.
        True when the recording of this conversation is in secure pause status.

        :param secure_pause: The secure_pause of this Conversation.
        :type: bool
        """
        

        self._secure_pause = secure_pause

    @property
    def utilization_label_id(self) -> str:
        """
        Gets the utilization_label_id of this Conversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :return: The utilization_label_id of this Conversation.
        :rtype: str
        """
        return self._utilization_label_id

    @utilization_label_id.setter
    def utilization_label_id(self, utilization_label_id: str) -> None:
        """
        Sets the utilization_label_id of this Conversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :param utilization_label_id: The utilization_label_id of this Conversation.
        :type: str
        """
        

        self._utilization_label_id = utilization_label_id

    @property
    def inactivity_timeout(self) -> datetime:
        """
        Gets the inactivity_timeout of this Conversation.
        The time in the future, after which this conversation would be considered inactive. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The inactivity_timeout of this Conversation.
        :rtype: datetime
        """
        return self._inactivity_timeout

    @inactivity_timeout.setter
    def inactivity_timeout(self, inactivity_timeout: datetime) -> None:
        """
        Sets the inactivity_timeout of this Conversation.
        The time in the future, after which this conversation would be considered inactive. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param inactivity_timeout: The inactivity_timeout of this Conversation.
        :type: datetime
        """
        

        self._inactivity_timeout = inactivity_timeout

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Conversation.
        The URI for this object

        :return: The self_uri of this Conversation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Conversation.
        The URI for this object

        :param self_uri: The self_uri of this Conversation.
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

