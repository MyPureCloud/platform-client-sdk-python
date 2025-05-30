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
    from . import KnowledgeOperationSource
    from . import UserReference

class OperationResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OperationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'type': 'str',
            'created_by': 'UserReference',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'source': 'KnowledgeOperationSource',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'type': 'type',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'source': 'source',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._status = None
        self._type = None
        self._created_by = None
        self._date_created = None
        self._date_modified = None
        self._source = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this OperationResponse.
        The globally unique identifier for the object.

        :return: The id of this OperationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this OperationResponse.
        The globally unique identifier for the object.

        :param id: The id of this OperationResponse.
        :type: str
        """
        

        self._id = id

    @property
    def status(self) -> str:
        """
        Gets the status of this OperationResponse.
        Status of the operation.

        :return: The status of this OperationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this OperationResponse.
        Status of the operation.

        :param status: The status of this OperationResponse.
        :type: str
        """
        

        self._status = status

    @property
    def type(self) -> str:
        """
        Gets the type of this OperationResponse.
        Type of the operation.

        :return: The type of this OperationResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this OperationResponse.
        Type of the operation.

        :param type: The type of this OperationResponse.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Import", "Export", "Parse", "Sync"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def created_by(self) -> 'UserReference':
        """
        Gets the created_by of this OperationResponse.
        The user who created the operation.

        :return: The created_by of this OperationResponse.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'UserReference') -> None:
        """
        Sets the created_by of this OperationResponse.
        The user who created the operation.

        :param created_by: The created_by of this OperationResponse.
        :type: UserReference
        """
        

        self._created_by = created_by

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this OperationResponse.
        Operation creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this OperationResponse.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this OperationResponse.
        Operation creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this OperationResponse.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this OperationResponse.
        Operation last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this OperationResponse.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this OperationResponse.
        Operation last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this OperationResponse.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def source(self) -> 'KnowledgeOperationSource':
        """
        Gets the source of this OperationResponse.
        Source of the operation.

        :return: The source of this OperationResponse.
        :rtype: KnowledgeOperationSource
        """
        return self._source

    @source.setter
    def source(self, source: 'KnowledgeOperationSource') -> None:
        """
        Sets the source of this OperationResponse.
        Source of the operation.

        :param source: The source of this OperationResponse.
        :type: KnowledgeOperationSource
        """
        

        self._source = source

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this OperationResponse.
        The URI for this object

        :return: The self_uri of this OperationResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this OperationResponse.
        The URI for this object

        :param self_uri: The self_uri of this OperationResponse.
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

