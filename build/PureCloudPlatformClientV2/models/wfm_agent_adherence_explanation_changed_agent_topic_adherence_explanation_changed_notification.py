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
    from . import WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit
    from . import WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit
    from . import WfmAgentAdherenceExplanationChangedAgentTopicUserReference

class WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'agent': 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference',
            'management_unit': 'WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit',
            'business_unit': 'WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit',
            'type': 'str',
            'status': 'str',
            'start_date': 'datetime',
            'length_minutes': 'int',
            'notes': 'str',
            'reviewed_by': 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference',
            'reviewed_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'agent': 'agent',
            'management_unit': 'managementUnit',
            'business_unit': 'businessUnit',
            'type': 'type',
            'status': 'status',
            'start_date': 'startDate',
            'length_minutes': 'lengthMinutes',
            'notes': 'notes',
            'reviewed_by': 'reviewedBy',
            'reviewed_date': 'reviewedDate'
        }

        self._id = None
        self._agent = None
        self._management_unit = None
        self._business_unit = None
        self._type = None
        self._status = None
        self._start_date = None
        self._length_minutes = None
        self._notes = None
        self._reviewed_by = None
        self._reviewed_date = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The id of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param id: The id of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: str
        """
        

        self._id = id

    @property
    def agent(self) -> 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference':
        """
        Gets the agent of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The agent of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: WfmAgentAdherenceExplanationChangedAgentTopicUserReference
        """
        return self._agent

    @agent.setter
    def agent(self, agent: 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference') -> None:
        """
        Sets the agent of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param agent: The agent of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: WfmAgentAdherenceExplanationChangedAgentTopicUserReference
        """
        

        self._agent = agent

    @property
    def management_unit(self) -> 'WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit':
        """
        Gets the management_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The management_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit
        """
        return self._management_unit

    @management_unit.setter
    def management_unit(self, management_unit: 'WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit') -> None:
        """
        Sets the management_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param management_unit: The management_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: WfmAgentAdherenceExplanationChangedAgentTopicManagementUnit
        """
        

        self._management_unit = management_unit

    @property
    def business_unit(self) -> 'WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit':
        """
        Gets the business_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The business_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit: 'WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit') -> None:
        """
        Sets the business_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param business_unit: The business_unit of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: WfmAgentAdherenceExplanationChangedAgentTopicBusinessUnit
        """
        

        self._business_unit = business_unit

    @property
    def type(self) -> str:
        """
        Gets the type of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The type of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param type: The type of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Late"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def status(self) -> str:
        """
        Gets the status of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The status of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param status: The status of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Pending", "Approved", "Denied"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The start_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param start_date: The start_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def length_minutes(self) -> int:
        """
        Gets the length_minutes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The length_minutes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: int
        """
        return self._length_minutes

    @length_minutes.setter
    def length_minutes(self, length_minutes: int) -> None:
        """
        Sets the length_minutes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param length_minutes: The length_minutes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: int
        """
        

        self._length_minutes = length_minutes

    @property
    def notes(self) -> str:
        """
        Gets the notes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The notes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str) -> None:
        """
        Sets the notes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param notes: The notes of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: str
        """
        

        self._notes = notes

    @property
    def reviewed_by(self) -> 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference':
        """
        Gets the reviewed_by of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The reviewed_by of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: WfmAgentAdherenceExplanationChangedAgentTopicUserReference
        """
        return self._reviewed_by

    @reviewed_by.setter
    def reviewed_by(self, reviewed_by: 'WfmAgentAdherenceExplanationChangedAgentTopicUserReference') -> None:
        """
        Sets the reviewed_by of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param reviewed_by: The reviewed_by of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: WfmAgentAdherenceExplanationChangedAgentTopicUserReference
        """
        

        self._reviewed_by = reviewed_by

    @property
    def reviewed_date(self) -> datetime:
        """
        Gets the reviewed_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :return: The reviewed_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :rtype: datetime
        """
        return self._reviewed_date

    @reviewed_date.setter
    def reviewed_date(self, reviewed_date: datetime) -> None:
        """
        Sets the reviewed_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.


        :param reviewed_date: The reviewed_date of this WfmAgentAdherenceExplanationChangedAgentTopicAdherenceExplanationChangedNotification.
        :type: datetime
        """
        

        self._reviewed_date = reviewed_date

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

