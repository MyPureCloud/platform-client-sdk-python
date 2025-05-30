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
    from . import AddressableEntityRef
    from . import UserReference

class Room(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Room - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'room_type': 'str',
            'description': 'str',
            'subject': 'str',
            'participant_limit': 'int',
            'owners': 'list[UserReference]',
            'pinned_messages': 'list[AddressableEntityRef]',
            'jid': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'room_type': 'roomType',
            'description': 'description',
            'subject': 'subject',
            'participant_limit': 'participantLimit',
            'owners': 'owners',
            'pinned_messages': 'pinnedMessages',
            'jid': 'jid',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._room_type = None
        self._description = None
        self._subject = None
        self._participant_limit = None
        self._owners = None
        self._pinned_messages = None
        self._jid = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Room.
        The jid of the room if adhoc, the id of the group for group rooms

        :return: The id of this Room.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Room.
        The jid of the room if adhoc, the id of the group for group rooms

        :param id: The id of this Room.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Room.


        :return: The name of this Room.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Room.


        :param name: The name of this Room.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Room.
        Room's created time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Room.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Room.
        Room's created time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Room.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def room_type(self) -> str:
        """
        Gets the room_type of this Room.
        The type of room

        :return: The room_type of this Room.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type: str) -> None:
        """
        Sets the room_type of this Room.
        The type of room

        :param room_type: The room_type of this Room.
        :type: str
        """
        if isinstance(room_type, int):
            room_type = str(room_type)
        allowed_values = ["adhoc", "acd", "group", "oneOnOne", "supervisorAssistance"]
        if room_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for room_type -> " + room_type)
            self._room_type = "outdated_sdk_version"
        else:
            self._room_type = room_type

    @property
    def description(self) -> str:
        """
        Gets the description of this Room.
        Room's description

        :return: The description of this Room.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this Room.
        Room's description

        :param description: The description of this Room.
        :type: str
        """
        

        self._description = description

    @property
    def subject(self) -> str:
        """
        Gets the subject of this Room.
        Room's subject

        :return: The subject of this Room.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this Room.
        Room's subject

        :param subject: The subject of this Room.
        :type: str
        """
        

        self._subject = subject

    @property
    def participant_limit(self) -> int:
        """
        Gets the participant_limit of this Room.
        Room's size limit

        :return: The participant_limit of this Room.
        :rtype: int
        """
        return self._participant_limit

    @participant_limit.setter
    def participant_limit(self, participant_limit: int) -> None:
        """
        Sets the participant_limit of this Room.
        Room's size limit

        :param participant_limit: The participant_limit of this Room.
        :type: int
        """
        

        self._participant_limit = participant_limit

    @property
    def owners(self) -> List['UserReference']:
        """
        Gets the owners of this Room.
        Room's owners

        :return: The owners of this Room.
        :rtype: list[UserReference]
        """
        return self._owners

    @owners.setter
    def owners(self, owners: List['UserReference']) -> None:
        """
        Sets the owners of this Room.
        Room's owners

        :param owners: The owners of this Room.
        :type: list[UserReference]
        """
        

        self._owners = owners

    @property
    def pinned_messages(self) -> List['AddressableEntityRef']:
        """
        Gets the pinned_messages of this Room.
        Room's pinned messages

        :return: The pinned_messages of this Room.
        :rtype: list[AddressableEntityRef]
        """
        return self._pinned_messages

    @pinned_messages.setter
    def pinned_messages(self, pinned_messages: List['AddressableEntityRef']) -> None:
        """
        Sets the pinned_messages of this Room.
        Room's pinned messages

        :param pinned_messages: The pinned_messages of this Room.
        :type: list[AddressableEntityRef]
        """
        

        self._pinned_messages = pinned_messages

    @property
    def jid(self) -> str:
        """
        Gets the jid of this Room.
        The jid of the room

        :return: The jid of this Room.
        :rtype: str
        """
        return self._jid

    @jid.setter
    def jid(self, jid: str) -> None:
        """
        Sets the jid of this Room.
        The jid of the room

        :param jid: The jid of this Room.
        :type: str
        """
        

        self._jid = jid

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Room.
        The URI for this object

        :return: The self_uri of this Room.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Room.
        The URI for this object

        :param self_uri: The self_uri of this Room.
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

