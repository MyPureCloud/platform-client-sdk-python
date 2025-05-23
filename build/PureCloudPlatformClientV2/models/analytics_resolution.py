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


class AnalyticsResolution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AnalyticsResolution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_time': 'datetime',
            'queue_id': 'str',
            'user_id': 'str',
            'n_next_contact_avoided': 'int'
        }

        self.attribute_map = {
            'event_time': 'eventTime',
            'queue_id': 'queueId',
            'user_id': 'userId',
            'n_next_contact_avoided': 'nNextContactAvoided'
        }

        self._event_time = None
        self._queue_id = None
        self._user_id = None
        self._n_next_contact_avoided = None

    @property
    def event_time(self) -> datetime:
        """
        Gets the event_time of this AnalyticsResolution.
        Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_time of this AnalyticsResolution.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: datetime) -> None:
        """
        Sets the event_time of this AnalyticsResolution.
        Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_time: The event_time of this AnalyticsResolution.
        :type: datetime
        """
        

        self._event_time = event_time

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this AnalyticsResolution.
        The ID of the last queue on which the conversation was handled.

        :return: The queue_id of this AnalyticsResolution.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this AnalyticsResolution.
        The ID of the last queue on which the conversation was handled.

        :param queue_id: The queue_id of this AnalyticsResolution.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this AnalyticsResolution.
        The ID of the last user who handled the conversation.

        :return: The user_id of this AnalyticsResolution.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this AnalyticsResolution.
        The ID of the last user who handled the conversation.

        :param user_id: The user_id of this AnalyticsResolution.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def n_next_contact_avoided(self) -> int:
        """
        Gets the n_next_contact_avoided of this AnalyticsResolution.


        :return: The n_next_contact_avoided of this AnalyticsResolution.
        :rtype: int
        """
        return self._n_next_contact_avoided

    @n_next_contact_avoided.setter
    def n_next_contact_avoided(self, n_next_contact_avoided: int) -> None:
        """
        Sets the n_next_contact_avoided of this AnalyticsResolution.


        :param n_next_contact_avoided: The n_next_contact_avoided of this AnalyticsResolution.
        :type: int
        """
        

        self._n_next_contact_avoided = n_next_contact_avoided

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

