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
    from . import QueueConversationEventTopicAfterCallWork
    from . import QueueConversationEventTopicDialerPreview
    from . import QueueConversationEventTopicQueueMediaSettings
    from . import QueueConversationEventTopicVoicemail
    from . import QueueConversationEventTopicWrapup

class QueueConversationEventTopicCallback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationEventTopicCallback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'initial_state': 'str',
            'id': 'str',
            'direction': 'str',
            'held': 'bool',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'dialer_preview': 'QueueConversationEventTopicDialerPreview',
            'voicemail': 'QueueConversationEventTopicVoicemail',
            'callback_numbers': 'list[str]',
            'callback_user_name': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'external_campaign': 'bool',
            'skip_enabled': 'bool',
            'provider': 'str',
            'timeout_seconds': 'int',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'callback_scheduled_time': 'datetime',
            'automated_callback_config_id': 'str',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'after_call_work': 'QueueConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'caller_id': 'str',
            'caller_id_name': 'str',
            'queue_media_settings': 'QueueConversationEventTopicQueueMediaSettings'
        }

        self.attribute_map = {
            'state': 'state',
            'initial_state': 'initialState',
            'id': 'id',
            'direction': 'direction',
            'held': 'held',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'dialer_preview': 'dialerPreview',
            'voicemail': 'voicemail',
            'callback_numbers': 'callbackNumbers',
            'callback_user_name': 'callbackUserName',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'external_campaign': 'externalCampaign',
            'skip_enabled': 'skipEnabled',
            'provider': 'provider',
            'timeout_seconds': 'timeoutSeconds',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'callback_scheduled_time': 'callbackScheduledTime',
            'automated_callback_config_id': 'automatedCallbackConfigId',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'caller_id': 'callerId',
            'caller_id_name': 'callerIdName',
            'queue_media_settings': 'queueMediaSettings'
        }

        self._state = None
        self._initial_state = None
        self._id = None
        self._direction = None
        self._held = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._dialer_preview = None
        self._voicemail = None
        self._callback_numbers = None
        self._callback_user_name = None
        self._script_id = None
        self._peer_id = None
        self._external_campaign = None
        self._skip_enabled = None
        self._provider = None
        self._timeout_seconds = None
        self._connected_time = None
        self._disconnected_time = None
        self._callback_scheduled_time = None
        self._automated_callback_config_id = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._caller_id = None
        self._caller_id_name = None
        self._queue_media_settings = None

    @property
    def state(self) -> str:
        """
        Gets the state of this QueueConversationEventTopicCallback.


        :return: The state of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this QueueConversationEventTopicCallback.


        :param state: The state of this QueueConversationEventTopicCallback.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "scheduled", "uploading", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def initial_state(self) -> str:
        """
        Gets the initial_state of this QueueConversationEventTopicCallback.


        :return: The initial_state of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this QueueConversationEventTopicCallback.


        :param initial_state: The initial_state of this QueueConversationEventTopicCallback.
        :type: str
        """
        if isinstance(initial_state, int):
            initial_state = str(initial_state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "scheduled", "uploading", "none"]
        if initial_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_state -> " + initial_state)
            self._initial_state = "outdated_sdk_version"
        else:
            self._initial_state = initial_state

    @property
    def id(self) -> str:
        """
        Gets the id of this QueueConversationEventTopicCallback.
        A globally unique identifier for this communication.

        :return: The id of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this QueueConversationEventTopicCallback.
        A globally unique identifier for this communication.

        :param id: The id of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._id = id

    @property
    def direction(self) -> str:
        """
        Gets the direction of this QueueConversationEventTopicCallback.
        The direction of the call

        :return: The direction of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this QueueConversationEventTopicCallback.
        The direction of the call

        :param direction: The direction of this QueueConversationEventTopicCallback.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def held(self) -> bool:
        """
        Gets the held of this QueueConversationEventTopicCallback.
        True if this call is held and the person on this side hears silence.

        :return: The held of this QueueConversationEventTopicCallback.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held: bool) -> None:
        """
        Sets the held of this QueueConversationEventTopicCallback.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this QueueConversationEventTopicCallback.
        :type: bool
        """
        

        self._held = held

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this QueueConversationEventTopicCallback.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this QueueConversationEventTopicCallback.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this QueueConversationEventTopicCallback.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "endpoint.dnd", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transfer.dnd", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self) -> datetime:
        """
        Gets the start_hold_time of this QueueConversationEventTopicCallback.
        The timestamp the callback was placed on hold in the cloud clock if the callback is currently on hold.

        :return: The start_hold_time of this QueueConversationEventTopicCallback.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time: datetime) -> None:
        """
        Sets the start_hold_time of this QueueConversationEventTopicCallback.
        The timestamp the callback was placed on hold in the cloud clock if the callback is currently on hold.

        :param start_hold_time: The start_hold_time of this QueueConversationEventTopicCallback.
        :type: datetime
        """
        

        self._start_hold_time = start_hold_time

    @property
    def dialer_preview(self) -> 'QueueConversationEventTopicDialerPreview':
        """
        Gets the dialer_preview of this QueueConversationEventTopicCallback.


        :return: The dialer_preview of this QueueConversationEventTopicCallback.
        :rtype: QueueConversationEventTopicDialerPreview
        """
        return self._dialer_preview

    @dialer_preview.setter
    def dialer_preview(self, dialer_preview: 'QueueConversationEventTopicDialerPreview') -> None:
        """
        Sets the dialer_preview of this QueueConversationEventTopicCallback.


        :param dialer_preview: The dialer_preview of this QueueConversationEventTopicCallback.
        :type: QueueConversationEventTopicDialerPreview
        """
        

        self._dialer_preview = dialer_preview

    @property
    def voicemail(self) -> 'QueueConversationEventTopicVoicemail':
        """
        Gets the voicemail of this QueueConversationEventTopicCallback.


        :return: The voicemail of this QueueConversationEventTopicCallback.
        :rtype: QueueConversationEventTopicVoicemail
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail: 'QueueConversationEventTopicVoicemail') -> None:
        """
        Sets the voicemail of this QueueConversationEventTopicCallback.


        :param voicemail: The voicemail of this QueueConversationEventTopicCallback.
        :type: QueueConversationEventTopicVoicemail
        """
        

        self._voicemail = voicemail

    @property
    def callback_numbers(self) -> List[str]:
        """
        Gets the callback_numbers of this QueueConversationEventTopicCallback.
        The phone number(s) to use to place the callback.

        :return: The callback_numbers of this QueueConversationEventTopicCallback.
        :rtype: list[str]
        """
        return self._callback_numbers

    @callback_numbers.setter
    def callback_numbers(self, callback_numbers: List[str]) -> None:
        """
        Sets the callback_numbers of this QueueConversationEventTopicCallback.
        The phone number(s) to use to place the callback.

        :param callback_numbers: The callback_numbers of this QueueConversationEventTopicCallback.
        :type: list[str]
        """
        

        self._callback_numbers = callback_numbers

    @property
    def callback_user_name(self) -> str:
        """
        Gets the callback_user_name of this QueueConversationEventTopicCallback.
        The name of the user requesting a callback.

        :return: The callback_user_name of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._callback_user_name

    @callback_user_name.setter
    def callback_user_name(self, callback_user_name: str) -> None:
        """
        Sets the callback_user_name of this QueueConversationEventTopicCallback.
        The name of the user requesting a callback.

        :param callback_user_name: The callback_user_name of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._callback_user_name = callback_user_name

    @property
    def script_id(self) -> str:
        """
        Gets the script_id of this QueueConversationEventTopicCallback.
        The UUID of the script to use.

        :return: The script_id of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: str) -> None:
        """
        Sets the script_id of this QueueConversationEventTopicCallback.
        The UUID of the script to use.

        :param script_id: The script_id of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._script_id = script_id

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this QueueConversationEventTopicCallback.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this QueueConversationEventTopicCallback.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def external_campaign(self) -> bool:
        """
        Gets the external_campaign of this QueueConversationEventTopicCallback.
        True if the call for the callback uses external dialing.

        :return: The external_campaign of this QueueConversationEventTopicCallback.
        :rtype: bool
        """
        return self._external_campaign

    @external_campaign.setter
    def external_campaign(self, external_campaign: bool) -> None:
        """
        Sets the external_campaign of this QueueConversationEventTopicCallback.
        True if the call for the callback uses external dialing.

        :param external_campaign: The external_campaign of this QueueConversationEventTopicCallback.
        :type: bool
        """
        

        self._external_campaign = external_campaign

    @property
    def skip_enabled(self) -> bool:
        """
        Gets the skip_enabled of this QueueConversationEventTopicCallback.
        True if the ability to skip a callback should be enabled.

        :return: The skip_enabled of this QueueConversationEventTopicCallback.
        :rtype: bool
        """
        return self._skip_enabled

    @skip_enabled.setter
    def skip_enabled(self, skip_enabled: bool) -> None:
        """
        Sets the skip_enabled of this QueueConversationEventTopicCallback.
        True if the ability to skip a callback should be enabled.

        :param skip_enabled: The skip_enabled of this QueueConversationEventTopicCallback.
        :type: bool
        """
        

        self._skip_enabled = skip_enabled

    @property
    def provider(self) -> str:
        """
        Gets the provider of this QueueConversationEventTopicCallback.
        The source provider of the callback.

        :return: The provider of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this QueueConversationEventTopicCallback.
        The source provider of the callback.

        :param provider: The provider of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._provider = provider

    @property
    def timeout_seconds(self) -> int:
        """
        Gets the timeout_seconds of this QueueConversationEventTopicCallback.
        The number of seconds before the system automatically places a call for a callback.  0 means the automatic placement is disabled.

        :return: The timeout_seconds of this QueueConversationEventTopicCallback.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds: int) -> None:
        """
        Sets the timeout_seconds of this QueueConversationEventTopicCallback.
        The number of seconds before the system automatically places a call for a callback.  0 means the automatic placement is disabled.

        :param timeout_seconds: The timeout_seconds of this QueueConversationEventTopicCallback.
        :type: int
        """
        

        self._timeout_seconds = timeout_seconds

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication was connected in the cloud clock.

        :return: The connected_time of this QueueConversationEventTopicCallback.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication was connected in the cloud clock.

        :param connected_time: The connected_time of this QueueConversationEventTopicCallback.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :return: The disconnected_time of this QueueConversationEventTopicCallback.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :param disconnected_time: The disconnected_time of this QueueConversationEventTopicCallback.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def callback_scheduled_time(self) -> datetime:
        """
        Gets the callback_scheduled_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication is scheduled in the provider clock. If this value is missing it indicates the callback will be placed immediately.

        :return: The callback_scheduled_time of this QueueConversationEventTopicCallback.
        :rtype: datetime
        """
        return self._callback_scheduled_time

    @callback_scheduled_time.setter
    def callback_scheduled_time(self, callback_scheduled_time: datetime) -> None:
        """
        Sets the callback_scheduled_time of this QueueConversationEventTopicCallback.
        The timestamp when this communication is scheduled in the provider clock. If this value is missing it indicates the callback will be placed immediately.

        :param callback_scheduled_time: The callback_scheduled_time of this QueueConversationEventTopicCallback.
        :type: datetime
        """
        

        self._callback_scheduled_time = callback_scheduled_time

    @property
    def automated_callback_config_id(self) -> str:
        """
        Gets the automated_callback_config_id of this QueueConversationEventTopicCallback.
        The id of the config for automatically placing the callback (and handling the disposition). If null, the callback will not be placed automatically but routed to an agent as per normal.

        :return: The automated_callback_config_id of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._automated_callback_config_id

    @automated_callback_config_id.setter
    def automated_callback_config_id(self, automated_callback_config_id: str) -> None:
        """
        Sets the automated_callback_config_id of this QueueConversationEventTopicCallback.
        The id of the config for automatically placing the callback (and handling the disposition). If null, the callback will not be placed automatically but routed to an agent as per normal.

        :param automated_callback_config_id: The automated_callback_config_id of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._automated_callback_config_id = automated_callback_config_id

    @property
    def wrapup(self) -> 'QueueConversationEventTopicWrapup':
        """
        Gets the wrapup of this QueueConversationEventTopicCallback.
        Call wrap up or disposition data.

        :return: The wrapup of this QueueConversationEventTopicCallback.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'QueueConversationEventTopicWrapup') -> None:
        """
        Sets the wrapup of this QueueConversationEventTopicCallback.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this QueueConversationEventTopicCallback.
        :type: QueueConversationEventTopicWrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'QueueConversationEventTopicAfterCallWork':
        """
        Gets the after_call_work of this QueueConversationEventTopicCallback.
        A communication's after-call work data.

        :return: The after_call_work of this QueueConversationEventTopicCallback.
        :rtype: QueueConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'QueueConversationEventTopicAfterCallWork') -> None:
        """
        Sets the after_call_work of this QueueConversationEventTopicCallback.
        A communication's after-call work data.

        :param after_call_work: The after_call_work of this QueueConversationEventTopicCallback.
        :type: QueueConversationEventTopicAfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this QueueConversationEventTopicCallback.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this QueueConversationEventTopicCallback.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this QueueConversationEventTopicCallback.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this QueueConversationEventTopicCallback.
        :type: bool
        """
        

        self._after_call_work_required = after_call_work_required

    @property
    def caller_id(self) -> str:
        """
        Gets the caller_id of this QueueConversationEventTopicCallback.
        The phone number displayed to recipients of the phone call. The value should conform to the E164 format.

        :return: The caller_id of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id: str) -> None:
        """
        Sets the caller_id of this QueueConversationEventTopicCallback.
        The phone number displayed to recipients of the phone call. The value should conform to the E164 format.

        :param caller_id: The caller_id of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._caller_id = caller_id

    @property
    def caller_id_name(self) -> str:
        """
        Gets the caller_id_name of this QueueConversationEventTopicCallback.
        The name displayed to recipients of the phone call.

        :return: The caller_id_name of this QueueConversationEventTopicCallback.
        :rtype: str
        """
        return self._caller_id_name

    @caller_id_name.setter
    def caller_id_name(self, caller_id_name: str) -> None:
        """
        Sets the caller_id_name of this QueueConversationEventTopicCallback.
        The name displayed to recipients of the phone call.

        :param caller_id_name: The caller_id_name of this QueueConversationEventTopicCallback.
        :type: str
        """
        

        self._caller_id_name = caller_id_name

    @property
    def queue_media_settings(self) -> 'QueueConversationEventTopicQueueMediaSettings':
        """
        Gets the queue_media_settings of this QueueConversationEventTopicCallback.
        Represents the queue setting for this media.

        :return: The queue_media_settings of this QueueConversationEventTopicCallback.
        :rtype: QueueConversationEventTopicQueueMediaSettings
        """
        return self._queue_media_settings

    @queue_media_settings.setter
    def queue_media_settings(self, queue_media_settings: 'QueueConversationEventTopicQueueMediaSettings') -> None:
        """
        Sets the queue_media_settings of this QueueConversationEventTopicCallback.
        Represents the queue setting for this media.

        :param queue_media_settings: The queue_media_settings of this QueueConversationEventTopicCallback.
        :type: QueueConversationEventTopicQueueMediaSettings
        """
        

        self._queue_media_settings = queue_media_settings

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

