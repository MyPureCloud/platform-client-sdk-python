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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class StatusChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatusChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date_status_changed': 'datetime',
            'status': 'str',
            'previous_status': 'str',
            'message': 'str',
            'changed_by': 'str',
            'reject_reason': 'str'
        }

        self.attribute_map = {
            'date_status_changed': 'dateStatusChanged',
            'status': 'status',
            'previous_status': 'previousStatus',
            'message': 'message',
            'changed_by': 'changedBy',
            'reject_reason': 'rejectReason'
        }

        self._date_status_changed = None
        self._status = None
        self._previous_status = None
        self._message = None
        self._changed_by = None
        self._reject_reason = None

    @property
    def date_status_changed(self):
        """
        Gets the date_status_changed of this StatusChange.
        The date of this status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_status_changed of this StatusChange.
        :rtype: datetime
        """
        return self._date_status_changed

    @date_status_changed.setter
    def date_status_changed(self, date_status_changed):
        """
        Sets the date_status_changed of this StatusChange.
        The date of this status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_status_changed: The date_status_changed of this StatusChange.
        :type: datetime
        """
        
        self._date_status_changed = date_status_changed

    @property
    def status(self):
        """
        Gets the status of this StatusChange.
        The status the change request transitioned to

        :return: The status of this StatusChange.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StatusChange.
        The status the change request transitioned to

        :param status: The status of this StatusChange.
        :type: str
        """
        allowed_values = ["Open", "Approved", "ImplementingChange", "ChangeImplemented", "Rejected", "Rollback", "ImplementingRollback", "RollbackImplemented"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def previous_status(self):
        """
        Gets the previous_status of this StatusChange.
        The status the change request transitioned from

        :return: The previous_status of this StatusChange.
        :rtype: str
        """
        return self._previous_status

    @previous_status.setter
    def previous_status(self, previous_status):
        """
        Sets the previous_status of this StatusChange.
        The status the change request transitioned from

        :param previous_status: The previous_status of this StatusChange.
        :type: str
        """
        allowed_values = ["Open", "Approved", "ImplementingChange", "ChangeImplemented", "Rejected", "Rollback", "ImplementingRollback", "RollbackImplemented"]
        if previous_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for previous_status -> " + previous_status)
            self._previous_status = "outdated_sdk_version"
        else:
            self._previous_status = previous_status

    @property
    def message(self):
        """
        Gets the message of this StatusChange.
        A short message describing the status change

        :return: The message of this StatusChange.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this StatusChange.
        A short message describing the status change

        :param message: The message of this StatusChange.
        :type: str
        """
        
        self._message = message

    @property
    def changed_by(self):
        """
        Gets the changed_by of this StatusChange.
        If applicable, the user who updated the change request to this status

        :return: The changed_by of this StatusChange.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this StatusChange.
        If applicable, the user who updated the change request to this status

        :param changed_by: The changed_by of this StatusChange.
        :type: str
        """
        
        self._changed_by = changed_by

    @property
    def reject_reason(self):
        """
        Gets the reject_reason of this StatusChange.
        The reason for rejecting the limit override request

        :return: The reject_reason of this StatusChange.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """
        Sets the reject_reason of this StatusChange.
        The reason for rejecting the limit override request

        :param reject_reason: The reject_reason of this StatusChange.
        :type: str
        """
        allowed_values = ["AlternativeExists", "IncreaseNotRequired", "PlatformMisuse", "PlatformStability", "OtherReason"]
        if reject_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for reject_reason -> " + reject_reason)
            self._reject_reason = "outdated_sdk_version"
        else:
            self._reject_reason = reject_reason

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

