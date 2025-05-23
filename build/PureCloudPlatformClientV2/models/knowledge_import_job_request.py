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
    from . import KnowledgeImportJobSettings

class KnowledgeImportJobRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeImportJobRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'upload_key': 'str',
            'file_type': 'str',
            'settings': 'KnowledgeImportJobSettings',
            'skip_confirmation_step': 'bool'
        }

        self.attribute_map = {
            'upload_key': 'uploadKey',
            'file_type': 'fileType',
            'settings': 'settings',
            'skip_confirmation_step': 'skipConfirmationStep'
        }

        self._upload_key = None
        self._file_type = None
        self._settings = None
        self._skip_confirmation_step = None

    @property
    def upload_key(self) -> str:
        """
        Gets the upload_key of this KnowledgeImportJobRequest.
        Upload key

        :return: The upload_key of this KnowledgeImportJobRequest.
        :rtype: str
        """
        return self._upload_key

    @upload_key.setter
    def upload_key(self, upload_key: str) -> None:
        """
        Sets the upload_key of this KnowledgeImportJobRequest.
        Upload key

        :param upload_key: The upload_key of this KnowledgeImportJobRequest.
        :type: str
        """
        

        self._upload_key = upload_key

    @property
    def file_type(self) -> str:
        """
        Gets the file_type of this KnowledgeImportJobRequest.
        File type of the document

        :return: The file_type of this KnowledgeImportJobRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type: str) -> None:
        """
        Sets the file_type of this KnowledgeImportJobRequest.
        File type of the document

        :param file_type: The file_type of this KnowledgeImportJobRequest.
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
    def settings(self) -> 'KnowledgeImportJobSettings':
        """
        Gets the settings of this KnowledgeImportJobRequest.
        Additional optional settings

        :return: The settings of this KnowledgeImportJobRequest.
        :rtype: KnowledgeImportJobSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings: 'KnowledgeImportJobSettings') -> None:
        """
        Sets the settings of this KnowledgeImportJobRequest.
        Additional optional settings

        :param settings: The settings of this KnowledgeImportJobRequest.
        :type: KnowledgeImportJobSettings
        """
        

        self._settings = settings

    @property
    def skip_confirmation_step(self) -> bool:
        """
        Gets the skip_confirmation_step of this KnowledgeImportJobRequest.
        If enabled pre-validation step will be skipped.

        :return: The skip_confirmation_step of this KnowledgeImportJobRequest.
        :rtype: bool
        """
        return self._skip_confirmation_step

    @skip_confirmation_step.setter
    def skip_confirmation_step(self, skip_confirmation_step: bool) -> None:
        """
        Sets the skip_confirmation_step of this KnowledgeImportJobRequest.
        If enabled pre-validation step will be skipped.

        :param skip_confirmation_step: The skip_confirmation_step of this KnowledgeImportJobRequest.
        :type: bool
        """
        

        self._skip_confirmation_step = skip_confirmation_step

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

