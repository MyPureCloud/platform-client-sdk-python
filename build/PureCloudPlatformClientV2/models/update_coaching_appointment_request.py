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
    from . import WfmScheduleReference

class UpdateCoachingAppointmentRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UpdateCoachingAppointmentRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'date_start': 'datetime',
            'length_in_minutes': 'int',
            'conversation_ids': 'list[str]',
            'document_ids': 'list[str]',
            'status': 'str',
            'wfm_schedule': 'WfmScheduleReference',
            'external_links': 'list[str]',
            'location': 'str',
            'share_insights_data': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'date_start': 'dateStart',
            'length_in_minutes': 'lengthInMinutes',
            'conversation_ids': 'conversationIds',
            'document_ids': 'documentIds',
            'status': 'status',
            'wfm_schedule': 'wfmSchedule',
            'external_links': 'externalLinks',
            'location': 'location',
            'share_insights_data': 'shareInsightsData'
        }

        self._name = None
        self._description = None
        self._date_start = None
        self._length_in_minutes = None
        self._conversation_ids = None
        self._document_ids = None
        self._status = None
        self._wfm_schedule = None
        self._external_links = None
        self._location = None
        self._share_insights_data = None

    @property
    def name(self) -> str:
        """
        Gets the name of this UpdateCoachingAppointmentRequest.
        The name of coaching appointment.

        :return: The name of this UpdateCoachingAppointmentRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this UpdateCoachingAppointmentRequest.
        The name of coaching appointment.

        :param name: The name of this UpdateCoachingAppointmentRequest.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this UpdateCoachingAppointmentRequest.
        The description of coaching appointment.

        :return: The description of this UpdateCoachingAppointmentRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this UpdateCoachingAppointmentRequest.
        The description of coaching appointment.

        :param description: The description of this UpdateCoachingAppointmentRequest.
        :type: str
        """
        

        self._description = description

    @property
    def date_start(self) -> datetime:
        """
        Gets the date_start of this UpdateCoachingAppointmentRequest.
        The date/time the coaching appointment starts. Times will be rounded down to the minute. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_start of this UpdateCoachingAppointmentRequest.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: datetime) -> None:
        """
        Sets the date_start of this UpdateCoachingAppointmentRequest.
        The date/time the coaching appointment starts. Times will be rounded down to the minute. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_start: The date_start of this UpdateCoachingAppointmentRequest.
        :type: datetime
        """
        

        self._date_start = date_start

    @property
    def length_in_minutes(self) -> int:
        """
        Gets the length_in_minutes of this UpdateCoachingAppointmentRequest.
        The duration of coaching appointment in minutes.

        :return: The length_in_minutes of this UpdateCoachingAppointmentRequest.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes: int) -> None:
        """
        Sets the length_in_minutes of this UpdateCoachingAppointmentRequest.
        The duration of coaching appointment in minutes.

        :param length_in_minutes: The length_in_minutes of this UpdateCoachingAppointmentRequest.
        :type: int
        """
        

        self._length_in_minutes = length_in_minutes

    @property
    def conversation_ids(self) -> List[str]:
        """
        Gets the conversation_ids of this UpdateCoachingAppointmentRequest.
        IDs of conversations associated with this coaching appointment.

        :return: The conversation_ids of this UpdateCoachingAppointmentRequest.
        :rtype: list[str]
        """
        return self._conversation_ids

    @conversation_ids.setter
    def conversation_ids(self, conversation_ids: List[str]) -> None:
        """
        Sets the conversation_ids of this UpdateCoachingAppointmentRequest.
        IDs of conversations associated with this coaching appointment.

        :param conversation_ids: The conversation_ids of this UpdateCoachingAppointmentRequest.
        :type: list[str]
        """
        

        self._conversation_ids = conversation_ids

    @property
    def document_ids(self) -> List[str]:
        """
        Gets the document_ids of this UpdateCoachingAppointmentRequest.
        IDs of documents associated with this coaching appointment.

        :return: The document_ids of this UpdateCoachingAppointmentRequest.
        :rtype: list[str]
        """
        return self._document_ids

    @document_ids.setter
    def document_ids(self, document_ids: List[str]) -> None:
        """
        Sets the document_ids of this UpdateCoachingAppointmentRequest.
        IDs of documents associated with this coaching appointment.

        :param document_ids: The document_ids of this UpdateCoachingAppointmentRequest.
        :type: list[str]
        """
        

        self._document_ids = document_ids

    @property
    def status(self) -> str:
        """
        Gets the status of this UpdateCoachingAppointmentRequest.
        The status of the coaching appointment.

        :return: The status of this UpdateCoachingAppointmentRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this UpdateCoachingAppointmentRequest.
        The status of the coaching appointment.

        :param status: The status of this UpdateCoachingAppointmentRequest.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Scheduled", "InProgress", "Completed"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def wfm_schedule(self) -> 'WfmScheduleReference':
        """
        Gets the wfm_schedule of this UpdateCoachingAppointmentRequest.
        The Workforce Management schedule the appointment is associated with.

        :return: The wfm_schedule of this UpdateCoachingAppointmentRequest.
        :rtype: WfmScheduleReference
        """
        return self._wfm_schedule

    @wfm_schedule.setter
    def wfm_schedule(self, wfm_schedule: 'WfmScheduleReference') -> None:
        """
        Sets the wfm_schedule of this UpdateCoachingAppointmentRequest.
        The Workforce Management schedule the appointment is associated with.

        :param wfm_schedule: The wfm_schedule of this UpdateCoachingAppointmentRequest.
        :type: WfmScheduleReference
        """
        

        self._wfm_schedule = wfm_schedule

    @property
    def external_links(self) -> List[str]:
        """
        Gets the external_links of this UpdateCoachingAppointmentRequest.
        The list of external links related to the appointment

        :return: The external_links of this UpdateCoachingAppointmentRequest.
        :rtype: list[str]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links: List[str]) -> None:
        """
        Sets the external_links of this UpdateCoachingAppointmentRequest.
        The list of external links related to the appointment

        :param external_links: The external_links of this UpdateCoachingAppointmentRequest.
        :type: list[str]
        """
        

        self._external_links = external_links

    @property
    def location(self) -> str:
        """
        Gets the location of this UpdateCoachingAppointmentRequest.
        The location of the appointment

        :return: The location of this UpdateCoachingAppointmentRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str) -> None:
        """
        Sets the location of this UpdateCoachingAppointmentRequest.
        The location of the appointment

        :param location: The location of this UpdateCoachingAppointmentRequest.
        :type: str
        """
        

        self._location = location

    @property
    def share_insights_data(self) -> bool:
        """
        Gets the share_insights_data of this UpdateCoachingAppointmentRequest.
        Whether to share the insight data

        :return: The share_insights_data of this UpdateCoachingAppointmentRequest.
        :rtype: bool
        """
        return self._share_insights_data

    @share_insights_data.setter
    def share_insights_data(self, share_insights_data: bool) -> None:
        """
        Sets the share_insights_data of this UpdateCoachingAppointmentRequest.
        Whether to share the insight data

        :param share_insights_data: The share_insights_data of this UpdateCoachingAppointmentRequest.
        :type: bool
        """
        

        self._share_insights_data = share_insights_data

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

