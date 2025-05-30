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


class MeetingIdRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MeetingIdRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'ephemeral': 'bool',
            'conference_id': 'str',
            'date_expired': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'ephemeral': 'ephemeral',
            'conference_id': 'conferenceId',
            'date_expired': 'dateExpired',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._ephemeral = None
        self._conference_id = None
        self._date_expired = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this MeetingIdRecord.
        The globally unique identifier for the object.

        :return: The id of this MeetingIdRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this MeetingIdRecord.
        The globally unique identifier for the object.

        :param id: The id of this MeetingIdRecord.
        :type: str
        """
        

        self._id = id

    @property
    def ephemeral(self) -> bool:
        """
        Gets the ephemeral of this MeetingIdRecord.
        Boolean flag for ephemeral status of the created record

        :return: The ephemeral of this MeetingIdRecord.
        :rtype: bool
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral: bool) -> None:
        """
        Sets the ephemeral of this MeetingIdRecord.
        Boolean flag for ephemeral status of the created record

        :param ephemeral: The ephemeral of this MeetingIdRecord.
        :type: bool
        """
        

        self._ephemeral = ephemeral

    @property
    def conference_id(self) -> str:
        """
        Gets the conference_id of this MeetingIdRecord.
        The conferenceId used to generate a meetingId

        :return: The conference_id of this MeetingIdRecord.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id: str) -> None:
        """
        Sets the conference_id of this MeetingIdRecord.
        The conferenceId used to generate a meetingId

        :param conference_id: The conference_id of this MeetingIdRecord.
        :type: str
        """
        

        self._conference_id = conference_id

    @property
    def date_expired(self) -> datetime:
        """
        Gets the date_expired of this MeetingIdRecord.
        Instant at which the meetingId record will no longer be considered active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_expired of this MeetingIdRecord.
        :rtype: datetime
        """
        return self._date_expired

    @date_expired.setter
    def date_expired(self, date_expired: datetime) -> None:
        """
        Sets the date_expired of this MeetingIdRecord.
        Instant at which the meetingId record will no longer be considered active. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_expired: The date_expired of this MeetingIdRecord.
        :type: datetime
        """
        

        self._date_expired = date_expired

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this MeetingIdRecord.
        The URI for this object

        :return: The self_uri of this MeetingIdRecord.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this MeetingIdRecord.
        The URI for this object

        :param self_uri: The self_uri of this MeetingIdRecord.
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

