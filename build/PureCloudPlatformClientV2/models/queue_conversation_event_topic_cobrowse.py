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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class QueueConversationEventTopicCobrowse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationEventTopicCobrowse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'disconnect_type': 'str',
            'id': 'str',
            'pcSelf': 'QueueConversationEventTopicAddress',
            'room_id': 'str',
            'cobrowse_session_id': 'str',
            'cobrowse_role': 'str',
            'controlling': 'list[str]',
            'viewer_url': 'str',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'provider_event_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'after_call_work': 'QueueConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'state': 'state',
            'disconnect_type': 'disconnectType',
            'id': 'id',
            'pcSelf': 'self',
            'room_id': 'roomId',
            'cobrowse_session_id': 'cobrowseSessionId',
            'cobrowse_role': 'cobrowseRole',
            'controlling': 'controlling',
            'viewer_url': 'viewerUrl',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'provider_event_time': 'providerEventTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'additional_properties': 'additionalProperties'
        }

        self._state = None
        self._disconnect_type = None
        self._id = None
        self._pcSelf = None
        self._room_id = None
        self._cobrowse_session_id = None
        self._cobrowse_role = None
        self._controlling = None
        self._viewer_url = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._provider_event_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._additional_properties = None

    @property
    def state(self):
        """
        Gets the state of this QueueConversationEventTopicCobrowse.


        :return: The state of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this QueueConversationEventTopicCobrowse.


        :param state: The state of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        allowed_values = ["ALERTING", "DIALING", "CONTACTING", "OFFERING", "CONNECTED", "DISCONNECTED", "TERMINATED", "NONE"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def disconnect_type(self):
        """
        Gets the disconnect_type of this QueueConversationEventTopicCobrowse.


        :return: The disconnect_type of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type):
        """
        Sets the disconnect_type of this QueueConversationEventTopicCobrowse.


        :param disconnect_type: The disconnect_type of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        allowed_values = ["ENDPOINT", "CLIENT", "SYSTEM", "TIMEOUT", "TRANSFER", "TRANSFER_CONFERENCE", "TRANSFER_CONSULT", "TRANSFER_FORWARD", "TRANSPORT_FAILURE", "ERROR", "PEER", "OTHER", "SPAM", "UNCALLABLE"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def id(self):
        """
        Gets the id of this QueueConversationEventTopicCobrowse.


        :return: The id of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationEventTopicCobrowse.


        :param id: The id of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._id = id

    @property
    def pcSelf(self):
        """
        Gets the pcSelf of this QueueConversationEventTopicCobrowse.


        :return: The pcSelf of this QueueConversationEventTopicCobrowse.
        :rtype: QueueConversationEventTopicAddress
        """
        return self._pcSelf

    @pcSelf.setter
    def pcSelf(self, pcSelf):
        """
        Sets the pcSelf of this QueueConversationEventTopicCobrowse.


        :param pcSelf: The pcSelf of this QueueConversationEventTopicCobrowse.
        :type: QueueConversationEventTopicAddress
        """
        
        self._pcSelf = pcSelf

    @property
    def room_id(self):
        """
        Gets the room_id of this QueueConversationEventTopicCobrowse.


        :return: The room_id of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this QueueConversationEventTopicCobrowse.


        :param room_id: The room_id of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._room_id = room_id

    @property
    def cobrowse_session_id(self):
        """
        Gets the cobrowse_session_id of this QueueConversationEventTopicCobrowse.


        :return: The cobrowse_session_id of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._cobrowse_session_id

    @cobrowse_session_id.setter
    def cobrowse_session_id(self, cobrowse_session_id):
        """
        Sets the cobrowse_session_id of this QueueConversationEventTopicCobrowse.


        :param cobrowse_session_id: The cobrowse_session_id of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._cobrowse_session_id = cobrowse_session_id

    @property
    def cobrowse_role(self):
        """
        Gets the cobrowse_role of this QueueConversationEventTopicCobrowse.


        :return: The cobrowse_role of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._cobrowse_role

    @cobrowse_role.setter
    def cobrowse_role(self, cobrowse_role):
        """
        Sets the cobrowse_role of this QueueConversationEventTopicCobrowse.


        :param cobrowse_role: The cobrowse_role of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._cobrowse_role = cobrowse_role

    @property
    def controlling(self):
        """
        Gets the controlling of this QueueConversationEventTopicCobrowse.


        :return: The controlling of this QueueConversationEventTopicCobrowse.
        :rtype: list[str]
        """
        return self._controlling

    @controlling.setter
    def controlling(self, controlling):
        """
        Sets the controlling of this QueueConversationEventTopicCobrowse.


        :param controlling: The controlling of this QueueConversationEventTopicCobrowse.
        :type: list[str]
        """
        
        self._controlling = controlling

    @property
    def viewer_url(self):
        """
        Gets the viewer_url of this QueueConversationEventTopicCobrowse.


        :return: The viewer_url of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._viewer_url

    @viewer_url.setter
    def viewer_url(self, viewer_url):
        """
        Sets the viewer_url of this QueueConversationEventTopicCobrowse.


        :param viewer_url: The viewer_url of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._viewer_url = viewer_url

    @property
    def provider(self):
        """
        Gets the provider of this QueueConversationEventTopicCobrowse.


        :return: The provider of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this QueueConversationEventTopicCobrowse.


        :param provider: The provider of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._provider = provider

    @property
    def script_id(self):
        """
        Gets the script_id of this QueueConversationEventTopicCobrowse.


        :return: The script_id of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """
        Sets the script_id of this QueueConversationEventTopicCobrowse.


        :param script_id: The script_id of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._script_id = script_id

    @property
    def peer_id(self):
        """
        Gets the peer_id of this QueueConversationEventTopicCobrowse.


        :return: The peer_id of this QueueConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this QueueConversationEventTopicCobrowse.


        :param peer_id: The peer_id of this QueueConversationEventTopicCobrowse.
        :type: str
        """
        
        self._peer_id = peer_id

    @property
    def provider_event_time(self):
        """
        Gets the provider_event_time of this QueueConversationEventTopicCobrowse.


        :return: The provider_event_time of this QueueConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._provider_event_time

    @provider_event_time.setter
    def provider_event_time(self, provider_event_time):
        """
        Sets the provider_event_time of this QueueConversationEventTopicCobrowse.


        :param provider_event_time: The provider_event_time of this QueueConversationEventTopicCobrowse.
        :type: datetime
        """
        
        self._provider_event_time = provider_event_time

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationEventTopicCobrowse.


        :return: The connected_time of this QueueConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationEventTopicCobrowse.


        :param connected_time: The connected_time of this QueueConversationEventTopicCobrowse.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def disconnected_time(self):
        """
        Gets the disconnected_time of this QueueConversationEventTopicCobrowse.


        :return: The disconnected_time of this QueueConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time):
        """
        Sets the disconnected_time of this QueueConversationEventTopicCobrowse.


        :param disconnected_time: The disconnected_time of this QueueConversationEventTopicCobrowse.
        :type: datetime
        """
        
        self._disconnected_time = disconnected_time

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationEventTopicCobrowse.


        :return: The wrapup of this QueueConversationEventTopicCobrowse.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationEventTopicCobrowse.


        :param wrapup: The wrapup of this QueueConversationEventTopicCobrowse.
        :type: QueueConversationEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def after_call_work(self):
        """
        Gets the after_call_work of this QueueConversationEventTopicCobrowse.


        :return: The after_call_work of this QueueConversationEventTopicCobrowse.
        :rtype: QueueConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work):
        """
        Sets the after_call_work of this QueueConversationEventTopicCobrowse.


        :param after_call_work: The after_call_work of this QueueConversationEventTopicCobrowse.
        :type: QueueConversationEventTopicAfterCallWork
        """
        
        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self):
        """
        Gets the after_call_work_required of this QueueConversationEventTopicCobrowse.


        :return: The after_call_work_required of this QueueConversationEventTopicCobrowse.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required):
        """
        Sets the after_call_work_required of this QueueConversationEventTopicCobrowse.


        :param after_call_work_required: The after_call_work_required of this QueueConversationEventTopicCobrowse.
        :type: bool
        """
        
        self._after_call_work_required = after_call_work_required

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationEventTopicCobrowse.


        :return: The additional_properties of this QueueConversationEventTopicCobrowse.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationEventTopicCobrowse.


        :param additional_properties: The additional_properties of this QueueConversationEventTopicCobrowse.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

