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
    from . import Referrer

class AppEventResponseSession(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AppEventResponseSession - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'duration_in_seconds': 'int',
            'event_count': 'int',
            'screenview_count': 'int',
            'referrer': 'Referrer',
            'self_uri': 'str',
            'created_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'duration_in_seconds': 'durationInSeconds',
            'event_count': 'eventCount',
            'screenview_count': 'screenviewCount',
            'referrer': 'referrer',
            'self_uri': 'selfUri',
            'created_date': 'createdDate'
        }

        self._id = None
        self._duration_in_seconds = None
        self._event_count = None
        self._screenview_count = None
        self._referrer = None
        self._self_uri = None
        self._created_date = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AppEventResponseSession.
        ID of the app session.

        :return: The id of this AppEventResponseSession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AppEventResponseSession.
        ID of the app session.

        :param id: The id of this AppEventResponseSession.
        :type: str
        """
        

        self._id = id

    @property
    def duration_in_seconds(self) -> int:
        """
        Gets the duration_in_seconds of this AppEventResponseSession.
        Indicates how long the customer has been in the app within this session.

        :return: The duration_in_seconds of this AppEventResponseSession.
        :rtype: int
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds: int) -> None:
        """
        Sets the duration_in_seconds of this AppEventResponseSession.
        Indicates how long the customer has been in the app within this session.

        :param duration_in_seconds: The duration_in_seconds of this AppEventResponseSession.
        :type: int
        """
        

        self._duration_in_seconds = duration_in_seconds

    @property
    def event_count(self) -> int:
        """
        Gets the event_count of this AppEventResponseSession.
        The count of all events recorded during this session.

        :return: The event_count of this AppEventResponseSession.
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count: int) -> None:
        """
        Sets the event_count of this AppEventResponseSession.
        The count of all events recorded during this session.

        :param event_count: The event_count of this AppEventResponseSession.
        :type: int
        """
        

        self._event_count = event_count

    @property
    def screenview_count(self) -> int:
        """
        Gets the screenview_count of this AppEventResponseSession.
        The count of all screen views recorded during this session.

        :return: The screenview_count of this AppEventResponseSession.
        :rtype: int
        """
        return self._screenview_count

    @screenview_count.setter
    def screenview_count(self, screenview_count: int) -> None:
        """
        Sets the screenview_count of this AppEventResponseSession.
        The count of all screen views recorded during this session.

        :param screenview_count: The screenview_count of this AppEventResponseSession.
        :type: int
        """
        

        self._screenview_count = screenview_count

    @property
    def referrer(self) -> 'Referrer':
        """
        Gets the referrer of this AppEventResponseSession.
        The referrer of the first event in the app session.

        :return: The referrer of this AppEventResponseSession.
        :rtype: Referrer
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer: 'Referrer') -> None:
        """
        Sets the referrer of this AppEventResponseSession.
        The referrer of the first event in the app session.

        :param referrer: The referrer of this AppEventResponseSession.
        :type: Referrer
        """
        

        self._referrer = referrer

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this AppEventResponseSession.
        The URI for this object

        :return: The self_uri of this AppEventResponseSession.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this AppEventResponseSession.
        The URI for this object

        :param self_uri: The self_uri of this AppEventResponseSession.
        :type: str
        """
        

        self._self_uri = self_uri

    @property
    def created_date(self) -> datetime:
        """
        Gets the created_date of this AppEventResponseSession.
        UTC timestamp of the session's first event, that is when the session starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this AppEventResponseSession.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime) -> None:
        """
        Sets the created_date of this AppEventResponseSession.
        UTC timestamp of the session's first event, that is when the session starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this AppEventResponseSession.
        :type: datetime
        """
        

        self._created_date = created_date

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

