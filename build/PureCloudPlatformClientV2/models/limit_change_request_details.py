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

class LimitChangeRequestDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LimitChangeRequestDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'key': 'str',
            'namespace': 'str',
            'requested_value': 'float',
            'description': 'str',
            'support_case_url': 'str',
            'created_by': 'str',
            'status': 'str',
            'current_value': 'float',
            'date_created': 'datetime',
            'status_history': 'list[StatusChange]',
            'date_completed': 'datetime',
            'last_changed_by': 'str',
            'reject_reason': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'key': 'key',
            'namespace': 'namespace',
            'requested_value': 'requestedValue',
            'description': 'description',
            'support_case_url': 'supportCaseUrl',
            'created_by': 'createdBy',
            'status': 'status',
            'current_value': 'currentValue',
            'date_created': 'dateCreated',
            'status_history': 'statusHistory',
            'date_completed': 'dateCompleted',
            'last_changed_by': 'lastChangedBy',
            'reject_reason': 'rejectReason',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._key = None
        self._namespace = None
        self._requested_value = None
        self._description = None
        self._support_case_url = None
        self._created_by = None
        self._status = None
        self._current_value = None
        self._date_created = None
        self._status_history = None
        self._date_completed = None
        self._last_changed_by = None
        self._reject_reason = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this LimitChangeRequestDetails.
        The globally unique identifier for the object.

        :return: The id of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LimitChangeRequestDetails.
        The globally unique identifier for the object.

        :param id: The id of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._id = id

    @property
    def key(self):
        """
        Gets the key of this LimitChangeRequestDetails.
        Limit key to be overridden (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits)

        :return: The key of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this LimitChangeRequestDetails.
        Limit key to be overridden (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits)

        :param key: The key of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._key = key

    @property
    def namespace(self):
        """
        Gets the namespace of this LimitChangeRequestDetails.
        Namespace the key belongs to (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits)

        :return: The namespace of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this LimitChangeRequestDetails.
        Namespace the key belongs to (see https://developer.mypurecloud.com/api/rest/v2/organization/limits.html#available_limits)

        :param namespace: The namespace of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._namespace = namespace

    @property
    def requested_value(self):
        """
        Gets the requested_value of this LimitChangeRequestDetails.
        Requested limit value for a given key

        :return: The requested_value of this LimitChangeRequestDetails.
        :rtype: float
        """
        return self._requested_value

    @requested_value.setter
    def requested_value(self, requested_value):
        """
        Sets the requested_value of this LimitChangeRequestDetails.
        Requested limit value for a given key

        :param requested_value: The requested_value of this LimitChangeRequestDetails.
        :type: float
        """
        
        self._requested_value = requested_value

    @property
    def description(self):
        """
        Gets the description of this LimitChangeRequestDetails.
        Description of the need for the limit change request

        :return: The description of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LimitChangeRequestDetails.
        Description of the need for the limit change request

        :param description: The description of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._description = description

    @property
    def support_case_url(self):
        """
        Gets the support_case_url of this LimitChangeRequestDetails.
        The support case url created by Care

        :return: The support_case_url of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._support_case_url

    @support_case_url.setter
    def support_case_url(self, support_case_url):
        """
        Sets the support_case_url of this LimitChangeRequestDetails.
        The support case url created by Care

        :param support_case_url: The support_case_url of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._support_case_url = support_case_url

    @property
    def created_by(self):
        """
        Gets the created_by of this LimitChangeRequestDetails.
        The user who created the change request

        :return: The created_by of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this LimitChangeRequestDetails.
        The user who created the change request

        :param created_by: The created_by of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._created_by = created_by

    @property
    def status(self):
        """
        Gets the status of this LimitChangeRequestDetails.
        Current status of the limit change request

        :return: The status of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LimitChangeRequestDetails.
        Current status of the limit change request

        :param status: The status of this LimitChangeRequestDetails.
        :type: str
        """
        allowed_values = ["Open", "Approved", "ImplementingChange", "ChangeImplemented", "Rejected", "Rollback", "ImplementingRollback", "RollbackImplemented"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def current_value(self):
        """
        Gets the current_value of this LimitChangeRequestDetails.
        Current limit value for a given key

        :return: The current_value of this LimitChangeRequestDetails.
        :rtype: float
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """
        Sets the current_value of this LimitChangeRequestDetails.
        Current limit value for a given key

        :param current_value: The current_value of this LimitChangeRequestDetails.
        :type: float
        """
        
        self._current_value = current_value

    @property
    def date_created(self):
        """
        Gets the date_created of this LimitChangeRequestDetails.
        The date of the limit change request creation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this LimitChangeRequestDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this LimitChangeRequestDetails.
        The date of the limit change request creation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this LimitChangeRequestDetails.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def status_history(self):
        """
        Gets the status_history of this LimitChangeRequestDetails.
        List of statuses that a limit change request has gone through

        :return: The status_history of this LimitChangeRequestDetails.
        :rtype: list[StatusChange]
        """
        return self._status_history

    @status_history.setter
    def status_history(self, status_history):
        """
        Sets the status_history of this LimitChangeRequestDetails.
        List of statuses that a limit change request has gone through

        :param status_history: The status_history of this LimitChangeRequestDetails.
        :type: list[StatusChange]
        """
        
        self._status_history = status_history

    @property
    def date_completed(self):
        """
        Gets the date_completed of this LimitChangeRequestDetails.
        The date of the limit change request completion (ChangeImplemented, Rejected, or RollbackImplemented. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_completed of this LimitChangeRequestDetails.
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """
        Sets the date_completed of this LimitChangeRequestDetails.
        The date of the limit change request completion (ChangeImplemented, Rejected, or RollbackImplemented. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_completed: The date_completed of this LimitChangeRequestDetails.
        :type: datetime
        """
        
        self._date_completed = date_completed

    @property
    def last_changed_by(self):
        """
        Gets the last_changed_by of this LimitChangeRequestDetails.
        The user who last updated the status of the limit change request

        :return: The last_changed_by of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._last_changed_by

    @last_changed_by.setter
    def last_changed_by(self, last_changed_by):
        """
        Sets the last_changed_by of this LimitChangeRequestDetails.
        The user who last updated the status of the limit change request

        :param last_changed_by: The last_changed_by of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._last_changed_by = last_changed_by

    @property
    def reject_reason(self):
        """
        Gets the reject_reason of this LimitChangeRequestDetails.
        The reason for rejecting the limit override request

        :return: The reject_reason of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """
        Sets the reject_reason of this LimitChangeRequestDetails.
        The reason for rejecting the limit override request

        :param reject_reason: The reject_reason of this LimitChangeRequestDetails.
        :type: str
        """
        allowed_values = ["AlternativeExists", "IncreaseNotRequired", "PlatformMisuse", "PlatformStability", "OtherReason"]
        if reject_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for reject_reason -> " + reject_reason)
            self._reject_reason = "outdated_sdk_version"
        else:
            self._reject_reason = reject_reason

    @property
    def self_uri(self):
        """
        Gets the self_uri of this LimitChangeRequestDetails.
        The URI for this object

        :return: The self_uri of this LimitChangeRequestDetails.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this LimitChangeRequestDetails.
        The URI for this object

        :param self_uri: The self_uri of this LimitChangeRequestDetails.
        :type: str
        """
        
        self._self_uri = self_uri

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

