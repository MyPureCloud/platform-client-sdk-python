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


class RoomUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        RoomUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'subject': 'str',
            'pinned_message_ids': 'list[str]',
            'owner_ids': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'subject': 'subject',
            'pinned_message_ids': 'pinnedMessageIds',
            'owner_ids': 'ownerIds'
        }

        self._description = None
        self._subject = None
        self._pinned_message_ids = None
        self._owner_ids = None

    @property
    def description(self) -> str:
        """
        Gets the description of this RoomUpdateRequest.
        Room's description

        :return: The description of this RoomUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this RoomUpdateRequest.
        Room's description

        :param description: The description of this RoomUpdateRequest.
        :type: str
        """
        

        self._description = description

    @property
    def subject(self) -> str:
        """
        Gets the subject of this RoomUpdateRequest.
        Room's subject

        :return: The subject of this RoomUpdateRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this RoomUpdateRequest.
        Room's subject

        :param subject: The subject of this RoomUpdateRequest.
        :type: str
        """
        

        self._subject = subject

    @property
    def pinned_message_ids(self) -> List[str]:
        """
        Gets the pinned_message_ids of this RoomUpdateRequest.
        Room's pinned messages

        :return: The pinned_message_ids of this RoomUpdateRequest.
        :rtype: list[str]
        """
        return self._pinned_message_ids

    @pinned_message_ids.setter
    def pinned_message_ids(self, pinned_message_ids: List[str]) -> None:
        """
        Sets the pinned_message_ids of this RoomUpdateRequest.
        Room's pinned messages

        :param pinned_message_ids: The pinned_message_ids of this RoomUpdateRequest.
        :type: list[str]
        """
        

        self._pinned_message_ids = pinned_message_ids

    @property
    def owner_ids(self) -> List[str]:
        """
        Gets the owner_ids of this RoomUpdateRequest.
        Room's owners

        :return: The owner_ids of this RoomUpdateRequest.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids: List[str]) -> None:
        """
        Sets the owner_ids of this RoomUpdateRequest.
        Room's owners

        :param owner_ids: The owner_ids of this RoomUpdateRequest.
        :type: list[str]
        """
        

        self._owner_ids = owner_ids

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

