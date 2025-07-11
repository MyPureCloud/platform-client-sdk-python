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
    from . import Campaign
    from . import ExternalContact
    from . import ExternalOrganization
    from . import Group
    from . import Queue
    from . import User

class CallHistoryParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CallHistoryParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'address': 'str',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'purpose': 'str',
            'direction': 'str',
            'ani': 'str',
            'dnis': 'str',
            'user': 'User',
            'queue': 'Queue',
            'group': 'Group',
            'disconnect_type': 'str',
            'external_contact': 'ExternalContact',
            'external_organization': 'ExternalOrganization',
            'did_interact': 'bool',
            'sip_response_codes': 'list[int]',
            'flagged_reason': 'str',
            'outbound_campaign': 'Campaign'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'purpose': 'purpose',
            'direction': 'direction',
            'ani': 'ani',
            'dnis': 'dnis',
            'user': 'user',
            'queue': 'queue',
            'group': 'group',
            'disconnect_type': 'disconnectType',
            'external_contact': 'externalContact',
            'external_organization': 'externalOrganization',
            'did_interact': 'didInteract',
            'sip_response_codes': 'sipResponseCodes',
            'flagged_reason': 'flaggedReason',
            'outbound_campaign': 'outboundCampaign'
        }

        self._id = None
        self._name = None
        self._address = None
        self._start_time = None
        self._end_time = None
        self._purpose = None
        self._direction = None
        self._ani = None
        self._dnis = None
        self._user = None
        self._queue = None
        self._group = None
        self._disconnect_type = None
        self._external_contact = None
        self._external_organization = None
        self._did_interact = None
        self._sip_response_codes = None
        self._flagged_reason = None
        self._outbound_campaign = None

    @property
    def id(self) -> str:
        """
        Gets the id of this CallHistoryParticipant.
        The unique participant ID.

        :return: The id of this CallHistoryParticipant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CallHistoryParticipant.
        The unique participant ID.

        :param id: The id of this CallHistoryParticipant.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this CallHistoryParticipant.
        The display friendly name of the participant.

        :return: The name of this CallHistoryParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this CallHistoryParticipant.
        The display friendly name of the participant.

        :param name: The name of this CallHistoryParticipant.
        :type: str
        """
        

        self._name = name

    @property
    def address(self) -> str:
        """
        Gets the address of this CallHistoryParticipant.
        The participant address.

        :return: The address of this CallHistoryParticipant.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this CallHistoryParticipant.
        The participant address.

        :param address: The address of this CallHistoryParticipant.
        :type: str
        """
        

        self._address = address

    @property
    def start_time(self) -> datetime:
        """
        Gets the start_time of this CallHistoryParticipant.
        The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_time of this CallHistoryParticipant.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime) -> None:
        """
        Sets the start_time of this CallHistoryParticipant.
        The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_time: The start_time of this CallHistoryParticipant.
        :type: datetime
        """
        

        self._start_time = start_time

    @property
    def end_time(self) -> datetime:
        """
        Gets the end_time of this CallHistoryParticipant.
        The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_time of this CallHistoryParticipant.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime) -> None:
        """
        Sets the end_time of this CallHistoryParticipant.
        The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_time: The end_time of this CallHistoryParticipant.
        :type: datetime
        """
        

        self._end_time = end_time

    @property
    def purpose(self) -> str:
        """
        Gets the purpose of this CallHistoryParticipant.
        The participant's purpose.  Values can be: 'agent', 'user', 'customer', 'external', 'acd', 'ivr

        :return: The purpose of this CallHistoryParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose: str) -> None:
        """
        Sets the purpose of this CallHistoryParticipant.
        The participant's purpose.  Values can be: 'agent', 'user', 'customer', 'external', 'acd', 'ivr

        :param purpose: The purpose of this CallHistoryParticipant.
        :type: str
        """
        

        self._purpose = purpose

    @property
    def direction(self) -> str:
        """
        Gets the direction of this CallHistoryParticipant.
        The participant's direction.  Values can be: 'inbound' or 'outbound'

        :return: The direction of this CallHistoryParticipant.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this CallHistoryParticipant.
        The participant's direction.  Values can be: 'inbound' or 'outbound'

        :param direction: The direction of this CallHistoryParticipant.
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
    def ani(self) -> str:
        """
        Gets the ani of this CallHistoryParticipant.
        The call ANI.

        :return: The ani of this CallHistoryParticipant.
        :rtype: str
        """
        return self._ani

    @ani.setter
    def ani(self, ani: str) -> None:
        """
        Sets the ani of this CallHistoryParticipant.
        The call ANI.

        :param ani: The ani of this CallHistoryParticipant.
        :type: str
        """
        

        self._ani = ani

    @property
    def dnis(self) -> str:
        """
        Gets the dnis of this CallHistoryParticipant.
        The call DNIS.

        :return: The dnis of this CallHistoryParticipant.
        :rtype: str
        """
        return self._dnis

    @dnis.setter
    def dnis(self, dnis: str) -> None:
        """
        Sets the dnis of this CallHistoryParticipant.
        The call DNIS.

        :param dnis: The dnis of this CallHistoryParticipant.
        :type: str
        """
        

        self._dnis = dnis

    @property
    def user(self) -> 'User':
        """
        Gets the user of this CallHistoryParticipant.
        The PureCloud user for this participant.

        :return: The user of this CallHistoryParticipant.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: 'User') -> None:
        """
        Sets the user of this CallHistoryParticipant.
        The PureCloud user for this participant.

        :param user: The user of this CallHistoryParticipant.
        :type: User
        """
        

        self._user = user

    @property
    def queue(self) -> 'Queue':
        """
        Gets the queue of this CallHistoryParticipant.
        The PureCloud queue for this participant.

        :return: The queue of this CallHistoryParticipant.
        :rtype: Queue
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'Queue') -> None:
        """
        Sets the queue of this CallHistoryParticipant.
        The PureCloud queue for this participant.

        :param queue: The queue of this CallHistoryParticipant.
        :type: Queue
        """
        

        self._queue = queue

    @property
    def group(self) -> 'Group':
        """
        Gets the group of this CallHistoryParticipant.
        The group involved in the group ring call.

        :return: The group of this CallHistoryParticipant.
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group: 'Group') -> None:
        """
        Sets the group of this CallHistoryParticipant.
        The group involved in the group ring call.

        :param group: The group of this CallHistoryParticipant.
        :type: Group
        """
        

        self._group = group

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this CallHistoryParticipant.
        The reason the participant was disconnected from the conversation.

        :return: The disconnect_type of this CallHistoryParticipant.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this CallHistoryParticipant.
        The reason the participant was disconnected from the conversation.

        :param disconnect_type: The disconnect_type of this CallHistoryParticipant.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "endpoint.donotdisturb", "client", "system", "transfer", "transfer.conference", "transfer.consult", "transfer.donotdisturb", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transport.failure", "error", "peer", "other", "spam", "inactivity"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def external_contact(self) -> 'ExternalContact':
        """
        Gets the external_contact of this CallHistoryParticipant.
        The PureCloud external contact

        :return: The external_contact of this CallHistoryParticipant.
        :rtype: ExternalContact
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact: 'ExternalContact') -> None:
        """
        Sets the external_contact of this CallHistoryParticipant.
        The PureCloud external contact

        :param external_contact: The external_contact of this CallHistoryParticipant.
        :type: ExternalContact
        """
        

        self._external_contact = external_contact

    @property
    def external_organization(self) -> 'ExternalOrganization':
        """
        Gets the external_organization of this CallHistoryParticipant.
        The PureCloud external organization

        :return: The external_organization of this CallHistoryParticipant.
        :rtype: ExternalOrganization
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization: 'ExternalOrganization') -> None:
        """
        Sets the external_organization of this CallHistoryParticipant.
        The PureCloud external organization

        :param external_organization: The external_organization of this CallHistoryParticipant.
        :type: ExternalOrganization
        """
        

        self._external_organization = external_organization

    @property
    def did_interact(self) -> bool:
        """
        Gets the did_interact of this CallHistoryParticipant.
        Indicates whether the contact ever connected

        :return: The did_interact of this CallHistoryParticipant.
        :rtype: bool
        """
        return self._did_interact

    @did_interact.setter
    def did_interact(self, did_interact: bool) -> None:
        """
        Sets the did_interact of this CallHistoryParticipant.
        Indicates whether the contact ever connected

        :param did_interact: The did_interact of this CallHistoryParticipant.
        :type: bool
        """
        

        self._did_interact = did_interact

    @property
    def sip_response_codes(self) -> List[int]:
        """
        Gets the sip_response_codes of this CallHistoryParticipant.
        Indicates SIP Response codes associated with the participant

        :return: The sip_response_codes of this CallHistoryParticipant.
        :rtype: list[int]
        """
        return self._sip_response_codes

    @sip_response_codes.setter
    def sip_response_codes(self, sip_response_codes: List[int]) -> None:
        """
        Sets the sip_response_codes of this CallHistoryParticipant.
        Indicates SIP Response codes associated with the participant

        :param sip_response_codes: The sip_response_codes of this CallHistoryParticipant.
        :type: list[int]
        """
        

        self._sip_response_codes = sip_response_codes

    @property
    def flagged_reason(self) -> str:
        """
        Gets the flagged_reason of this CallHistoryParticipant.
        The reason specifying why participant flagged the conversation.

        :return: The flagged_reason of this CallHistoryParticipant.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason: str) -> None:
        """
        Sets the flagged_reason of this CallHistoryParticipant.
        The reason specifying why participant flagged the conversation.

        :param flagged_reason: The flagged_reason of this CallHistoryParticipant.
        :type: str
        """
        if isinstance(flagged_reason, int):
            flagged_reason = str(flagged_reason)
        allowed_values = ["general"]
        if flagged_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for flagged_reason -> " + flagged_reason)
            self._flagged_reason = "outdated_sdk_version"
        else:
            self._flagged_reason = flagged_reason

    @property
    def outbound_campaign(self) -> 'Campaign':
        """
        Gets the outbound_campaign of this CallHistoryParticipant.
        The outbound campaign associated with the participant

        :return: The outbound_campaign of this CallHistoryParticipant.
        :rtype: Campaign
        """
        return self._outbound_campaign

    @outbound_campaign.setter
    def outbound_campaign(self, outbound_campaign: 'Campaign') -> None:
        """
        Sets the outbound_campaign of this CallHistoryParticipant.
        The outbound campaign associated with the participant

        :param outbound_campaign: The outbound_campaign of this CallHistoryParticipant.
        :type: Campaign
        """
        

        self._outbound_campaign = outbound_campaign

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

