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


class BuAgentScheduleActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuAgentScheduleActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'length_minutes': 'int',
            'description': 'str',
            'activity_code_id': 'str',
            'paid': 'bool',
            'payable_minutes': 'int',
            'time_off_request_id': 'str',
            'time_off_request_sync_version': 'int',
            'external_activity_id': 'str',
            'external_activity_type': 'str'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'length_minutes': 'lengthMinutes',
            'description': 'description',
            'activity_code_id': 'activityCodeId',
            'paid': 'paid',
            'payable_minutes': 'payableMinutes',
            'time_off_request_id': 'timeOffRequestId',
            'time_off_request_sync_version': 'timeOffRequestSyncVersion',
            'external_activity_id': 'externalActivityId',
            'external_activity_type': 'externalActivityType'
        }

        self._start_date = None
        self._length_minutes = None
        self._description = None
        self._activity_code_id = None
        self._paid = None
        self._payable_minutes = None
        self._time_off_request_id = None
        self._time_off_request_sync_version = None
        self._external_activity_id = None
        self._external_activity_type = None

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this BuAgentScheduleActivity.
        The start date/time of this activity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_date of this BuAgentScheduleActivity.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this BuAgentScheduleActivity.
        The start date/time of this activity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_date: The start_date of this BuAgentScheduleActivity.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def length_minutes(self) -> int:
        """
        Gets the length_minutes of this BuAgentScheduleActivity.
        The length of this activity in minutes

        :return: The length_minutes of this BuAgentScheduleActivity.
        :rtype: int
        """
        return self._length_minutes

    @length_minutes.setter
    def length_minutes(self, length_minutes: int) -> None:
        """
        Sets the length_minutes of this BuAgentScheduleActivity.
        The length of this activity in minutes

        :param length_minutes: The length_minutes of this BuAgentScheduleActivity.
        :type: int
        """
        

        self._length_minutes = length_minutes

    @property
    def description(self) -> str:
        """
        Gets the description of this BuAgentScheduleActivity.
        The description of this activity

        :return: The description of this BuAgentScheduleActivity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this BuAgentScheduleActivity.
        The description of this activity

        :param description: The description of this BuAgentScheduleActivity.
        :type: str
        """
        

        self._description = description

    @property
    def activity_code_id(self) -> str:
        """
        Gets the activity_code_id of this BuAgentScheduleActivity.
        The ID of the activity code associated with this activity

        :return: The activity_code_id of this BuAgentScheduleActivity.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id: str) -> None:
        """
        Sets the activity_code_id of this BuAgentScheduleActivity.
        The ID of the activity code associated with this activity

        :param activity_code_id: The activity_code_id of this BuAgentScheduleActivity.
        :type: str
        """
        

        self._activity_code_id = activity_code_id

    @property
    def paid(self) -> bool:
        """
        Gets the paid of this BuAgentScheduleActivity.
        Whether this activity is paid

        :return: The paid of this BuAgentScheduleActivity.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid: bool) -> None:
        """
        Sets the paid of this BuAgentScheduleActivity.
        Whether this activity is paid

        :param paid: The paid of this BuAgentScheduleActivity.
        :type: bool
        """
        

        self._paid = paid

    @property
    def payable_minutes(self) -> int:
        """
        Gets the payable_minutes of this BuAgentScheduleActivity.
        Payable minutes for this activity

        :return: The payable_minutes of this BuAgentScheduleActivity.
        :rtype: int
        """
        return self._payable_minutes

    @payable_minutes.setter
    def payable_minutes(self, payable_minutes: int) -> None:
        """
        Sets the payable_minutes of this BuAgentScheduleActivity.
        Payable minutes for this activity

        :param payable_minutes: The payable_minutes of this BuAgentScheduleActivity.
        :type: int
        """
        

        self._payable_minutes = payable_minutes

    @property
    def time_off_request_id(self) -> str:
        """
        Gets the time_off_request_id of this BuAgentScheduleActivity.
        The ID of the time off request associated with this activity, if applicable

        :return: The time_off_request_id of this BuAgentScheduleActivity.
        :rtype: str
        """
        return self._time_off_request_id

    @time_off_request_id.setter
    def time_off_request_id(self, time_off_request_id: str) -> None:
        """
        Sets the time_off_request_id of this BuAgentScheduleActivity.
        The ID of the time off request associated with this activity, if applicable

        :param time_off_request_id: The time_off_request_id of this BuAgentScheduleActivity.
        :type: str
        """
        

        self._time_off_request_id = time_off_request_id

    @property
    def time_off_request_sync_version(self) -> int:
        """
        Gets the time_off_request_sync_version of this BuAgentScheduleActivity.
        The sync version of the partial day time off request for which the scheduled activity is associated, if applicable

        :return: The time_off_request_sync_version of this BuAgentScheduleActivity.
        :rtype: int
        """
        return self._time_off_request_sync_version

    @time_off_request_sync_version.setter
    def time_off_request_sync_version(self, time_off_request_sync_version: int) -> None:
        """
        Sets the time_off_request_sync_version of this BuAgentScheduleActivity.
        The sync version of the partial day time off request for which the scheduled activity is associated, if applicable

        :param time_off_request_sync_version: The time_off_request_sync_version of this BuAgentScheduleActivity.
        :type: int
        """
        

        self._time_off_request_sync_version = time_off_request_sync_version

    @property
    def external_activity_id(self) -> str:
        """
        Gets the external_activity_id of this BuAgentScheduleActivity.
        The ID of the external activity associated with this activity, if applicable

        :return: The external_activity_id of this BuAgentScheduleActivity.
        :rtype: str
        """
        return self._external_activity_id

    @external_activity_id.setter
    def external_activity_id(self, external_activity_id: str) -> None:
        """
        Sets the external_activity_id of this BuAgentScheduleActivity.
        The ID of the external activity associated with this activity, if applicable

        :param external_activity_id: The external_activity_id of this BuAgentScheduleActivity.
        :type: str
        """
        

        self._external_activity_id = external_activity_id

    @property
    def external_activity_type(self) -> str:
        """
        Gets the external_activity_type of this BuAgentScheduleActivity.
        The type of the external activity associated with this activity, if applicable

        :return: The external_activity_type of this BuAgentScheduleActivity.
        :rtype: str
        """
        return self._external_activity_type

    @external_activity_type.setter
    def external_activity_type(self, external_activity_type: str) -> None:
        """
        Sets the external_activity_type of this BuAgentScheduleActivity.
        The type of the external activity associated with this activity, if applicable

        :param external_activity_type: The external_activity_type of this BuAgentScheduleActivity.
        :type: str
        """
        if isinstance(external_activity_type, int):
            external_activity_type = str(external_activity_type)
        allowed_values = ["ActivityPlan", "Coaching", "Learning"]
        if external_activity_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for external_activity_type -> " + external_activity_type)
            self._external_activity_type = "outdated_sdk_version"
        else:
            self._external_activity_type = external_activity_type

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

