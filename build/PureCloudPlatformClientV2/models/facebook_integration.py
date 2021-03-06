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

class FacebookIntegration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FacebookIntegration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'app_id': 'str',
            'page_id': 'str',
            'status': 'str',
            'recipient': 'DomainEntityRef',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'DomainEntityRef',
            'modified_by': 'DomainEntityRef',
            'version': 'int',
            'create_status': 'str',
            'create_error': 'ErrorBody',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'app_id': 'appId',
            'page_id': 'pageId',
            'status': 'status',
            'recipient': 'recipient',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'version': 'version',
            'create_status': 'createStatus',
            'create_error': 'createError',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._app_id = None
        self._page_id = None
        self._status = None
        self._recipient = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._version = None
        self._create_status = None
        self._create_error = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this FacebookIntegration.
        A unique Integration Id.

        :return: The id of this FacebookIntegration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FacebookIntegration.
        A unique Integration Id.

        :param id: The id of this FacebookIntegration.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FacebookIntegration.
        The name of the Facebook Integration

        :return: The name of this FacebookIntegration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FacebookIntegration.
        The name of the Facebook Integration

        :param name: The name of this FacebookIntegration.
        :type: str
        """
        
        self._name = name

    @property
    def app_id(self):
        """
        Gets the app_id of this FacebookIntegration.
        The App Id from Facebook messenger

        :return: The app_id of this FacebookIntegration.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this FacebookIntegration.
        The App Id from Facebook messenger

        :param app_id: The app_id of this FacebookIntegration.
        :type: str
        """
        
        self._app_id = app_id

    @property
    def page_id(self):
        """
        Gets the page_id of this FacebookIntegration.
        The Page Id from Facebook messenger

        :return: The page_id of this FacebookIntegration.
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """
        Sets the page_id of this FacebookIntegration.
        The Page Id from Facebook messenger

        :param page_id: The page_id of this FacebookIntegration.
        :type: str
        """
        
        self._page_id = page_id

    @property
    def status(self):
        """
        Gets the status of this FacebookIntegration.
        The status of the Facebook Integration

        :return: The status of this FacebookIntegration.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FacebookIntegration.
        The status of the Facebook Integration

        :param status: The status of this FacebookIntegration.
        :type: str
        """
        
        self._status = status

    @property
    def recipient(self):
        """
        Gets the recipient of this FacebookIntegration.
        The recipient reference associated to the Facebook Integration. This recipient is used to associate a flow to an integration

        :return: The recipient of this FacebookIntegration.
        :rtype: DomainEntityRef
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this FacebookIntegration.
        The recipient reference associated to the Facebook Integration. This recipient is used to associate a flow to an integration

        :param recipient: The recipient of this FacebookIntegration.
        :type: DomainEntityRef
        """
        
        self._recipient = recipient

    @property
    def date_created(self):
        """
        Gets the date_created of this FacebookIntegration.
        Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this FacebookIntegration.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this FacebookIntegration.
        Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this FacebookIntegration.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this FacebookIntegration.
        Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this FacebookIntegration.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this FacebookIntegration.
        Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this FacebookIntegration.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def created_by(self):
        """
        Gets the created_by of this FacebookIntegration.
        User reference that created this Integration

        :return: The created_by of this FacebookIntegration.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this FacebookIntegration.
        User reference that created this Integration

        :param created_by: The created_by of this FacebookIntegration.
        :type: DomainEntityRef
        """
        
        self._created_by = created_by

    @property
    def modified_by(self):
        """
        Gets the modified_by of this FacebookIntegration.
        User reference that last modified this Integration

        :return: The modified_by of this FacebookIntegration.
        :rtype: DomainEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this FacebookIntegration.
        User reference that last modified this Integration

        :param modified_by: The modified_by of this FacebookIntegration.
        :type: DomainEntityRef
        """
        
        self._modified_by = modified_by

    @property
    def version(self):
        """
        Gets the version of this FacebookIntegration.
        Version number required for updates.

        :return: The version of this FacebookIntegration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FacebookIntegration.
        Version number required for updates.

        :param version: The version of this FacebookIntegration.
        :type: int
        """
        
        self._version = version

    @property
    def create_status(self):
        """
        Gets the create_status of this FacebookIntegration.
        Status of asynchronous create operation

        :return: The create_status of this FacebookIntegration.
        :rtype: str
        """
        return self._create_status

    @create_status.setter
    def create_status(self, create_status):
        """
        Sets the create_status of this FacebookIntegration.
        Status of asynchronous create operation

        :param create_status: The create_status of this FacebookIntegration.
        :type: str
        """
        allowed_values = ["Initiated", "Completed", "Error"]
        if create_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for create_status -> " + create_status)
            self._create_status = "outdated_sdk_version"
        else:
            self._create_status = create_status

    @property
    def create_error(self):
        """
        Gets the create_error of this FacebookIntegration.
        Error information returned, if createStatus is set to Error

        :return: The create_error of this FacebookIntegration.
        :rtype: ErrorBody
        """
        return self._create_error

    @create_error.setter
    def create_error(self, create_error):
        """
        Sets the create_error of this FacebookIntegration.
        Error information returned, if createStatus is set to Error

        :param create_error: The create_error of this FacebookIntegration.
        :type: ErrorBody
        """
        
        self._create_error = create_error

    @property
    def self_uri(self):
        """
        Gets the self_uri of this FacebookIntegration.
        The URI for this object

        :return: The self_uri of this FacebookIntegration.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this FacebookIntegration.
        The URI for this object

        :param self_uri: The self_uri of this FacebookIntegration.
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

