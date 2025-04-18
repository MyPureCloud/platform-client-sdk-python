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
    from . import ConversationBasic
    from . import DomainEntityRef

class CampaignInteraction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignInteraction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'campaign': 'DomainEntityRef',
            'agent': 'DomainEntityRef',
            'contact': 'DomainEntityRef',
            'destination_address': 'str',
            'active_preview_call': 'bool',
            'last_active_preview_wrapup_time': 'datetime',
            'creation_time': 'datetime',
            'call_placed_time': 'datetime',
            'call_routed_time': 'datetime',
            'preview_connected_time': 'datetime',
            'queue': 'DomainEntityRef',
            'script': 'DomainEntityRef',
            'disposition': 'str',
            'caller_name': 'str',
            'caller_address': 'str',
            'preview_pop_delivered_time': 'datetime',
            'conversation': 'ConversationBasic',
            'dialer_system_participant_id': 'str',
            'dialing_mode': 'str',
            'skills': 'list[DomainEntityRef]'
        }

        self.attribute_map = {
            'id': 'id',
            'campaign': 'campaign',
            'agent': 'agent',
            'contact': 'contact',
            'destination_address': 'destinationAddress',
            'active_preview_call': 'activePreviewCall',
            'last_active_preview_wrapup_time': 'lastActivePreviewWrapupTime',
            'creation_time': 'creationTime',
            'call_placed_time': 'callPlacedTime',
            'call_routed_time': 'callRoutedTime',
            'preview_connected_time': 'previewConnectedTime',
            'queue': 'queue',
            'script': 'script',
            'disposition': 'disposition',
            'caller_name': 'callerName',
            'caller_address': 'callerAddress',
            'preview_pop_delivered_time': 'previewPopDeliveredTime',
            'conversation': 'conversation',
            'dialer_system_participant_id': 'dialerSystemParticipantId',
            'dialing_mode': 'dialingMode',
            'skills': 'skills'
        }

        self._id = None
        self._campaign = None
        self._agent = None
        self._contact = None
        self._destination_address = None
        self._active_preview_call = None
        self._last_active_preview_wrapup_time = None
        self._creation_time = None
        self._call_placed_time = None
        self._call_routed_time = None
        self._preview_connected_time = None
        self._queue = None
        self._script = None
        self._disposition = None
        self._caller_name = None
        self._caller_address = None
        self._preview_pop_delivered_time = None
        self._conversation = None
        self._dialer_system_participant_id = None
        self._dialing_mode = None
        self._skills = None

    @property
    def id(self) -> str:
        """
        Gets the id of this CampaignInteraction.


        :return: The id of this CampaignInteraction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CampaignInteraction.


        :param id: The id of this CampaignInteraction.
        :type: str
        """
        

        self._id = id

    @property
    def campaign(self) -> 'DomainEntityRef':
        """
        Gets the campaign of this CampaignInteraction.


        :return: The campaign of this CampaignInteraction.
        :rtype: DomainEntityRef
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign: 'DomainEntityRef') -> None:
        """
        Sets the campaign of this CampaignInteraction.


        :param campaign: The campaign of this CampaignInteraction.
        :type: DomainEntityRef
        """
        

        self._campaign = campaign

    @property
    def agent(self) -> 'DomainEntityRef':
        """
        Gets the agent of this CampaignInteraction.


        :return: The agent of this CampaignInteraction.
        :rtype: DomainEntityRef
        """
        return self._agent

    @agent.setter
    def agent(self, agent: 'DomainEntityRef') -> None:
        """
        Sets the agent of this CampaignInteraction.


        :param agent: The agent of this CampaignInteraction.
        :type: DomainEntityRef
        """
        

        self._agent = agent

    @property
    def contact(self) -> 'DomainEntityRef':
        """
        Gets the contact of this CampaignInteraction.


        :return: The contact of this CampaignInteraction.
        :rtype: DomainEntityRef
        """
        return self._contact

    @contact.setter
    def contact(self, contact: 'DomainEntityRef') -> None:
        """
        Sets the contact of this CampaignInteraction.


        :param contact: The contact of this CampaignInteraction.
        :type: DomainEntityRef
        """
        

        self._contact = contact

    @property
    def destination_address(self) -> str:
        """
        Gets the destination_address of this CampaignInteraction.


        :return: The destination_address of this CampaignInteraction.
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address: str) -> None:
        """
        Sets the destination_address of this CampaignInteraction.


        :param destination_address: The destination_address of this CampaignInteraction.
        :type: str
        """
        

        self._destination_address = destination_address

    @property
    def active_preview_call(self) -> bool:
        """
        Gets the active_preview_call of this CampaignInteraction.
        Boolean value if there is an active preview call on the interaction

        :return: The active_preview_call of this CampaignInteraction.
        :rtype: bool
        """
        return self._active_preview_call

    @active_preview_call.setter
    def active_preview_call(self, active_preview_call: bool) -> None:
        """
        Sets the active_preview_call of this CampaignInteraction.
        Boolean value if there is an active preview call on the interaction

        :param active_preview_call: The active_preview_call of this CampaignInteraction.
        :type: bool
        """
        

        self._active_preview_call = active_preview_call

    @property
    def last_active_preview_wrapup_time(self) -> datetime:
        """
        Gets the last_active_preview_wrapup_time of this CampaignInteraction.
        The time when the last preview of the interaction was wrapped up. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The last_active_preview_wrapup_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._last_active_preview_wrapup_time

    @last_active_preview_wrapup_time.setter
    def last_active_preview_wrapup_time(self, last_active_preview_wrapup_time: datetime) -> None:
        """
        Sets the last_active_preview_wrapup_time of this CampaignInteraction.
        The time when the last preview of the interaction was wrapped up. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param last_active_preview_wrapup_time: The last_active_preview_wrapup_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._last_active_preview_wrapup_time = last_active_preview_wrapup_time

    @property
    def creation_time(self) -> datetime:
        """
        Gets the creation_time of this CampaignInteraction.
        The time when dialer created the interaction. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The creation_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time: datetime) -> None:
        """
        Sets the creation_time of this CampaignInteraction.
        The time when dialer created the interaction. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param creation_time: The creation_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._creation_time = creation_time

    @property
    def call_placed_time(self) -> datetime:
        """
        Gets the call_placed_time of this CampaignInteraction.
        The time when the agent or system places the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The call_placed_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._call_placed_time

    @call_placed_time.setter
    def call_placed_time(self, call_placed_time: datetime) -> None:
        """
        Sets the call_placed_time of this CampaignInteraction.
        The time when the agent or system places the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param call_placed_time: The call_placed_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._call_placed_time = call_placed_time

    @property
    def call_routed_time(self) -> datetime:
        """
        Gets the call_routed_time of this CampaignInteraction.
        The time when the agent was connected to the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The call_routed_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._call_routed_time

    @call_routed_time.setter
    def call_routed_time(self, call_routed_time: datetime) -> None:
        """
        Sets the call_routed_time of this CampaignInteraction.
        The time when the agent was connected to the call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param call_routed_time: The call_routed_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._call_routed_time = call_routed_time

    @property
    def preview_connected_time(self) -> datetime:
        """
        Gets the preview_connected_time of this CampaignInteraction.
        The time when the customer and routing participant are connected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The preview_connected_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._preview_connected_time

    @preview_connected_time.setter
    def preview_connected_time(self, preview_connected_time: datetime) -> None:
        """
        Sets the preview_connected_time of this CampaignInteraction.
        The time when the customer and routing participant are connected. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param preview_connected_time: The preview_connected_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._preview_connected_time = preview_connected_time

    @property
    def queue(self) -> 'DomainEntityRef':
        """
        Gets the queue of this CampaignInteraction.


        :return: The queue of this CampaignInteraction.
        :rtype: DomainEntityRef
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'DomainEntityRef') -> None:
        """
        Sets the queue of this CampaignInteraction.


        :param queue: The queue of this CampaignInteraction.
        :type: DomainEntityRef
        """
        

        self._queue = queue

    @property
    def script(self) -> 'DomainEntityRef':
        """
        Gets the script of this CampaignInteraction.


        :return: The script of this CampaignInteraction.
        :rtype: DomainEntityRef
        """
        return self._script

    @script.setter
    def script(self, script: 'DomainEntityRef') -> None:
        """
        Sets the script of this CampaignInteraction.


        :param script: The script of this CampaignInteraction.
        :type: DomainEntityRef
        """
        

        self._script = script

    @property
    def disposition(self) -> str:
        """
        Gets the disposition of this CampaignInteraction.
        Describes what happened with call analysis for instance: disposition.classification.callable.person, disposition.classification.callable.noanswer

        :return: The disposition of this CampaignInteraction.
        :rtype: str
        """
        return self._disposition

    @disposition.setter
    def disposition(self, disposition: str) -> None:
        """
        Sets the disposition of this CampaignInteraction.
        Describes what happened with call analysis for instance: disposition.classification.callable.person, disposition.classification.callable.noanswer

        :param disposition: The disposition of this CampaignInteraction.
        :type: str
        """
        if isinstance(disposition, int):
            disposition = str(disposition)
        allowed_values = ["DISCONNECT", "LIVE_VOICE", "BUSY", "MACHINE", "NO_ANSWER", "SIT_CALLABLE", "SIT_UNCALLABLE", "FAX"]
        if disposition.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disposition -> " + disposition)
            self._disposition = "outdated_sdk_version"
        else:
            self._disposition = disposition

    @property
    def caller_name(self) -> str:
        """
        Gets the caller_name of this CampaignInteraction.


        :return: The caller_name of this CampaignInteraction.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name: str) -> None:
        """
        Sets the caller_name of this CampaignInteraction.


        :param caller_name: The caller_name of this CampaignInteraction.
        :type: str
        """
        

        self._caller_name = caller_name

    @property
    def caller_address(self) -> str:
        """
        Gets the caller_address of this CampaignInteraction.


        :return: The caller_address of this CampaignInteraction.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address: str) -> None:
        """
        Sets the caller_address of this CampaignInteraction.


        :param caller_address: The caller_address of this CampaignInteraction.
        :type: str
        """
        

        self._caller_address = caller_address

    @property
    def preview_pop_delivered_time(self) -> datetime:
        """
        Gets the preview_pop_delivered_time of this CampaignInteraction.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The preview_pop_delivered_time of this CampaignInteraction.
        :rtype: datetime
        """
        return self._preview_pop_delivered_time

    @preview_pop_delivered_time.setter
    def preview_pop_delivered_time(self, preview_pop_delivered_time: datetime) -> None:
        """
        Sets the preview_pop_delivered_time of this CampaignInteraction.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param preview_pop_delivered_time: The preview_pop_delivered_time of this CampaignInteraction.
        :type: datetime
        """
        

        self._preview_pop_delivered_time = preview_pop_delivered_time

    @property
    def conversation(self) -> 'ConversationBasic':
        """
        Gets the conversation of this CampaignInteraction.


        :return: The conversation of this CampaignInteraction.
        :rtype: ConversationBasic
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'ConversationBasic') -> None:
        """
        Sets the conversation of this CampaignInteraction.


        :param conversation: The conversation of this CampaignInteraction.
        :type: ConversationBasic
        """
        

        self._conversation = conversation

    @property
    def dialer_system_participant_id(self) -> str:
        """
        Gets the dialer_system_participant_id of this CampaignInteraction.
        conversation participant id that is the dialer system participant to monitor the call from dialer perspective

        :return: The dialer_system_participant_id of this CampaignInteraction.
        :rtype: str
        """
        return self._dialer_system_participant_id

    @dialer_system_participant_id.setter
    def dialer_system_participant_id(self, dialer_system_participant_id: str) -> None:
        """
        Sets the dialer_system_participant_id of this CampaignInteraction.
        conversation participant id that is the dialer system participant to monitor the call from dialer perspective

        :param dialer_system_participant_id: The dialer_system_participant_id of this CampaignInteraction.
        :type: str
        """
        

        self._dialer_system_participant_id = dialer_system_participant_id

    @property
    def dialing_mode(self) -> str:
        """
        Gets the dialing_mode of this CampaignInteraction.


        :return: The dialing_mode of this CampaignInteraction.
        :rtype: str
        """
        return self._dialing_mode

    @dialing_mode.setter
    def dialing_mode(self, dialing_mode: str) -> None:
        """
        Sets the dialing_mode of this CampaignInteraction.


        :param dialing_mode: The dialing_mode of this CampaignInteraction.
        :type: str
        """
        

        self._dialing_mode = dialing_mode

    @property
    def skills(self) -> List['DomainEntityRef']:
        """
        Gets the skills of this CampaignInteraction.
        Any skills that are attached to the call for routing

        :return: The skills of this CampaignInteraction.
        :rtype: list[DomainEntityRef]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List['DomainEntityRef']) -> None:
        """
        Sets the skills of this CampaignInteraction.
        Any skills that are attached to the call for routing

        :param skills: The skills of this CampaignInteraction.
        :type: list[DomainEntityRef]
        """
        

        self._skills = skills

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

