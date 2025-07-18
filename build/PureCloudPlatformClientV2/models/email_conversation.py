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
    from . import EmailMediaParticipant
    from . import TransferResponse

class EmailConversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EmailConversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'participants': 'list[EmailMediaParticipant]',
            'other_media_uris': 'list[str]',
            'recent_transfers': 'list[TransferResponse]',
            'utilization_label_id': 'str',
            'inactivity_timeout': 'datetime',
            'divisions': 'list[ConversationDivisionMembership]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'participants': 'participants',
            'other_media_uris': 'otherMediaUris',
            'recent_transfers': 'recentTransfers',
            'utilization_label_id': 'utilizationLabelId',
            'inactivity_timeout': 'inactivityTimeout',
            'divisions': 'divisions',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._participants = None
        self._other_media_uris = None
        self._recent_transfers = None
        self._utilization_label_id = None
        self._inactivity_timeout = None
        self._divisions = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this EmailConversation.
        The globally unique identifier for the object.

        :return: The id of this EmailConversation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this EmailConversation.
        The globally unique identifier for the object.

        :param id: The id of this EmailConversation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EmailConversation.


        :return: The name of this EmailConversation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EmailConversation.


        :param name: The name of this EmailConversation.
        :type: str
        """
        

        self._name = name

    @property
    def participants(self) -> List['EmailMediaParticipant']:
        """
        Gets the participants of this EmailConversation.
        The list of participants involved in the conversation.

        :return: The participants of this EmailConversation.
        :rtype: list[EmailMediaParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants: List['EmailMediaParticipant']) -> None:
        """
        Sets the participants of this EmailConversation.
        The list of participants involved in the conversation.

        :param participants: The participants of this EmailConversation.
        :type: list[EmailMediaParticipant]
        """
        

        self._participants = participants

    @property
    def other_media_uris(self) -> List[str]:
        """
        Gets the other_media_uris of this EmailConversation.
        The list of other media channels involved in the conversation.

        :return: The other_media_uris of this EmailConversation.
        :rtype: list[str]
        """
        return self._other_media_uris

    @other_media_uris.setter
    def other_media_uris(self, other_media_uris: List[str]) -> None:
        """
        Sets the other_media_uris of this EmailConversation.
        The list of other media channels involved in the conversation.

        :param other_media_uris: The other_media_uris of this EmailConversation.
        :type: list[str]
        """
        

        self._other_media_uris = other_media_uris

    @property
    def recent_transfers(self) -> List['TransferResponse']:
        """
        Gets the recent_transfers of this EmailConversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :return: The recent_transfers of this EmailConversation.
        :rtype: list[TransferResponse]
        """
        return self._recent_transfers

    @recent_transfers.setter
    def recent_transfers(self, recent_transfers: List['TransferResponse']) -> None:
        """
        Sets the recent_transfers of this EmailConversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :param recent_transfers: The recent_transfers of this EmailConversation.
        :type: list[TransferResponse]
        """
        

        self._recent_transfers = recent_transfers

    @property
    def utilization_label_id(self) -> str:
        """
        Gets the utilization_label_id of this EmailConversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :return: The utilization_label_id of this EmailConversation.
        :rtype: str
        """
        return self._utilization_label_id

    @utilization_label_id.setter
    def utilization_label_id(self, utilization_label_id: str) -> None:
        """
        Sets the utilization_label_id of this EmailConversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :param utilization_label_id: The utilization_label_id of this EmailConversation.
        :type: str
        """
        

        self._utilization_label_id = utilization_label_id

    @property
    def inactivity_timeout(self) -> datetime:
        """
        Gets the inactivity_timeout of this EmailConversation.
        The time in the future, after which this conversation would be considered inactive. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The inactivity_timeout of this EmailConversation.
        :rtype: datetime
        """
        return self._inactivity_timeout

    @inactivity_timeout.setter
    def inactivity_timeout(self, inactivity_timeout: datetime) -> None:
        """
        Sets the inactivity_timeout of this EmailConversation.
        The time in the future, after which this conversation would be considered inactive. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param inactivity_timeout: The inactivity_timeout of this EmailConversation.
        :type: datetime
        """
        

        self._inactivity_timeout = inactivity_timeout

    @property
    def divisions(self) -> List['ConversationDivisionMembership']:
        """
        Gets the divisions of this EmailConversation.
        Identifiers of divisions associated with this conversation.

        :return: The divisions of this EmailConversation.
        :rtype: list[ConversationDivisionMembership]
        """
        return self._divisions

    @divisions.setter
    def divisions(self, divisions: List['ConversationDivisionMembership']) -> None:
        """
        Sets the divisions of this EmailConversation.
        Identifiers of divisions associated with this conversation.

        :param divisions: The divisions of this EmailConversation.
        :type: list[ConversationDivisionMembership]
        """
        

        self._divisions = divisions

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this EmailConversation.
        The URI for this object

        :return: The self_uri of this EmailConversation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this EmailConversation.
        The URI for this object

        :param self_uri: The self_uri of this EmailConversation.
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

