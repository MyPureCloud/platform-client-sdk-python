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

class WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'request_id': 'str',
            'date_import_started': 'WfmHistoricalDataUploadRequestStatusTopicDateTime',
            'date_import_ended': 'WfmHistoricalDataUploadRequestStatusTopicDateTime',
            'date_created': 'WfmHistoricalDataUploadRequestStatusTopicDateTime',
            'date_modified': 'WfmHistoricalDataUploadRequestStatusTopicDateTime',
            'status': 'str',
            'error': 'str',
            'active': 'bool'
        }

        self.attribute_map = {
            'request_id': 'requestId',
            'date_import_started': 'dateImportStarted',
            'date_import_ended': 'dateImportEnded',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'status': 'status',
            'error': 'error',
            'active': 'active'
        }

        self._request_id = None
        self._date_import_started = None
        self._date_import_ended = None
        self._date_created = None
        self._date_modified = None
        self._status = None
        self._error = None
        self._active = None

    @property
    def request_id(self):
        """
        Gets the request_id of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The request_id of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param request_id: The request_id of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: str
        """
        
        self._request_id = request_id

    @property
    def date_import_started(self):
        """
        Gets the date_import_started of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The date_import_started of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        return self._date_import_started

    @date_import_started.setter
    def date_import_started(self, date_import_started):
        """
        Sets the date_import_started of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param date_import_started: The date_import_started of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        
        self._date_import_started = date_import_started

    @property
    def date_import_ended(self):
        """
        Gets the date_import_ended of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The date_import_ended of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        return self._date_import_ended

    @date_import_ended.setter
    def date_import_ended(self, date_import_ended):
        """
        Sets the date_import_ended of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param date_import_ended: The date_import_ended of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        
        self._date_import_ended = date_import_ended

    @property
    def date_created(self):
        """
        Gets the date_created of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The date_created of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param date_created: The date_created of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The date_modified of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param date_modified: The date_modified of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: WfmHistoricalDataUploadRequestStatusTopicDateTime
        """
        
        self._date_modified = date_modified

    @property
    def status(self):
        """
        Gets the status of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The status of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param status: The status of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: str
        """
        allowed_values = ["Initiated", "InProgress", "Pending", "Success", "Failed", "Cancelled", "Purged"]
        if status.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for status -> " + status
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def error(self):
        """
        Gets the error of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The error of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param error: The error of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: str
        """
        
        self._error = error

    @property
    def active(self):
        """
        Gets the active of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :return: The active of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.


        :param active: The active of this WfmHistoricalDataUploadRequestStatusTopicHistoricalDataUploadRequestUpdate.
        :type: bool
        """
        
        self._active = active

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
