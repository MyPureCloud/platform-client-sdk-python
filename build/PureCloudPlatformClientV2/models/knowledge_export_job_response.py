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
    from . import ErrorBody
    from . import KnowledgeBase
    from . import KnowledgeExportJobFilter
    from . import KnowledgeOperationSource
    from . import UserReference

class KnowledgeExportJobResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeExportJobResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'download_url': 'str',
            'file_type': 'str',
            'json_file_version': 'int',
            'count_document_processed': 'int',
            'export_filter': 'KnowledgeExportJobFilter',
            'status': 'str',
            'knowledge_base': 'KnowledgeBase',
            'created_by': 'UserReference',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'error_information': 'ErrorBody',
            'source': 'KnowledgeOperationSource',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'download_url': 'downloadURL',
            'file_type': 'fileType',
            'json_file_version': 'jsonFileVersion',
            'count_document_processed': 'countDocumentProcessed',
            'export_filter': 'exportFilter',
            'status': 'status',
            'knowledge_base': 'knowledgeBase',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'error_information': 'errorInformation',
            'source': 'source',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._download_url = None
        self._file_type = None
        self._json_file_version = None
        self._count_document_processed = None
        self._export_filter = None
        self._status = None
        self._knowledge_base = None
        self._created_by = None
        self._date_created = None
        self._date_modified = None
        self._error_information = None
        self._source = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this KnowledgeExportJobResponse.
        Id of the export job.

        :return: The id of this KnowledgeExportJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this KnowledgeExportJobResponse.
        Id of the export job.

        :param id: The id of this KnowledgeExportJobResponse.
        :type: str
        """
        

        self._id = id

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this KnowledgeExportJobResponse.
        The URL of the location at which the caller can download the export file, when available.

        :return: The download_url of this KnowledgeExportJobResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this KnowledgeExportJobResponse.
        The URL of the location at which the caller can download the export file, when available.

        :param download_url: The download_url of this KnowledgeExportJobResponse.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def file_type(self) -> str:
        """
        Gets the file_type of this KnowledgeExportJobResponse.
        File type of the document

        :return: The file_type of this KnowledgeExportJobResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type: str) -> None:
        """
        Sets the file_type of this KnowledgeExportJobResponse.
        File type of the document

        :param file_type: The file_type of this KnowledgeExportJobResponse.
        :type: str
        """
        if isinstance(file_type, int):
            file_type = str(file_type)
        allowed_values = ["Json", "Csv", "Xlsx"]
        if file_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for file_type -> " + file_type)
            self._file_type = "outdated_sdk_version"
        else:
            self._file_type = file_type

    @property
    def json_file_version(self) -> int:
        """
        Gets the json_file_version of this KnowledgeExportJobResponse.
        Requested version of the exported json file.

        :return: The json_file_version of this KnowledgeExportJobResponse.
        :rtype: int
        """
        return self._json_file_version

    @json_file_version.setter
    def json_file_version(self, json_file_version: int) -> None:
        """
        Sets the json_file_version of this KnowledgeExportJobResponse.
        Requested version of the exported json file.

        :param json_file_version: The json_file_version of this KnowledgeExportJobResponse.
        :type: int
        """
        

        self._json_file_version = json_file_version

    @property
    def count_document_processed(self) -> int:
        """
        Gets the count_document_processed of this KnowledgeExportJobResponse.
        The current count of the number of records processed.

        :return: The count_document_processed of this KnowledgeExportJobResponse.
        :rtype: int
        """
        return self._count_document_processed

    @count_document_processed.setter
    def count_document_processed(self, count_document_processed: int) -> None:
        """
        Sets the count_document_processed of this KnowledgeExportJobResponse.
        The current count of the number of records processed.

        :param count_document_processed: The count_document_processed of this KnowledgeExportJobResponse.
        :type: int
        """
        

        self._count_document_processed = count_document_processed

    @property
    def export_filter(self) -> 'KnowledgeExportJobFilter':
        """
        Gets the export_filter of this KnowledgeExportJobResponse.
        Filters to narrow down what to export.

        :return: The export_filter of this KnowledgeExportJobResponse.
        :rtype: KnowledgeExportJobFilter
        """
        return self._export_filter

    @export_filter.setter
    def export_filter(self, export_filter: 'KnowledgeExportJobFilter') -> None:
        """
        Sets the export_filter of this KnowledgeExportJobResponse.
        Filters to narrow down what to export.

        :param export_filter: The export_filter of this KnowledgeExportJobResponse.
        :type: KnowledgeExportJobFilter
        """
        

        self._export_filter = export_filter

    @property
    def status(self) -> str:
        """
        Gets the status of this KnowledgeExportJobResponse.
        The status of the export job.

        :return: The status of this KnowledgeExportJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this KnowledgeExportJobResponse.
        The status of the export job.

        :param status: The status of this KnowledgeExportJobResponse.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Created", "ValidationInProgress", "ValidationCompleted", "ValidationFailed", "Started", "InProgress", "Completed", "PartialCompleted", "Failed", "AbortRequested", "Aborted"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def knowledge_base(self) -> 'KnowledgeBase':
        """
        Gets the knowledge_base of this KnowledgeExportJobResponse.
        Knowledge base which document export belongs to.

        :return: The knowledge_base of this KnowledgeExportJobResponse.
        :rtype: KnowledgeBase
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base: 'KnowledgeBase') -> None:
        """
        Sets the knowledge_base of this KnowledgeExportJobResponse.
        Knowledge base which document export belongs to.

        :param knowledge_base: The knowledge_base of this KnowledgeExportJobResponse.
        :type: KnowledgeBase
        """
        

        self._knowledge_base = knowledge_base

    @property
    def created_by(self) -> 'UserReference':
        """
        Gets the created_by of this KnowledgeExportJobResponse.
        The user who created the operation

        :return: The created_by of this KnowledgeExportJobResponse.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'UserReference') -> None:
        """
        Sets the created_by of this KnowledgeExportJobResponse.
        The user who created the operation

        :param created_by: The created_by of this KnowledgeExportJobResponse.
        :type: UserReference
        """
        

        self._created_by = created_by

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this KnowledgeExportJobResponse.
        The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this KnowledgeExportJobResponse.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this KnowledgeExportJobResponse.
        The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this KnowledgeExportJobResponse.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this KnowledgeExportJobResponse.
        The timestamp of when the export stopped. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this KnowledgeExportJobResponse.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this KnowledgeExportJobResponse.
        The timestamp of when the export stopped. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this KnowledgeExportJobResponse.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def error_information(self) -> 'ErrorBody':
        """
        Gets the error_information of this KnowledgeExportJobResponse.
        Any error information, or null of the processing is not in failed state.

        :return: The error_information of this KnowledgeExportJobResponse.
        :rtype: ErrorBody
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information: 'ErrorBody') -> None:
        """
        Sets the error_information of this KnowledgeExportJobResponse.
        Any error information, or null of the processing is not in failed state.

        :param error_information: The error_information of this KnowledgeExportJobResponse.
        :type: ErrorBody
        """
        

        self._error_information = error_information

    @property
    def source(self) -> 'KnowledgeOperationSource':
        """
        Gets the source of this KnowledgeExportJobResponse.
        Source of the export job.

        :return: The source of this KnowledgeExportJobResponse.
        :rtype: KnowledgeOperationSource
        """
        return self._source

    @source.setter
    def source(self, source: 'KnowledgeOperationSource') -> None:
        """
        Sets the source of this KnowledgeExportJobResponse.
        Source of the export job.

        :param source: The source of this KnowledgeExportJobResponse.
        :type: KnowledgeOperationSource
        """
        

        self._source = source

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this KnowledgeExportJobResponse.
        The URI for this object

        :return: The self_uri of this KnowledgeExportJobResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this KnowledgeExportJobResponse.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeExportJobResponse.
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

