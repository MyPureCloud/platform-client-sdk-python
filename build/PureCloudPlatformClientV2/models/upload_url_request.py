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


class UploadUrlRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UploadUrlRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file_name': 'str',
            'content_md5': 'str',
            'signed_url_timeout_seconds': 'int',
            'content_type': 'str',
            'server_side_encryption': 'str'
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'content_md5': 'contentMd5',
            'signed_url_timeout_seconds': 'signedUrlTimeoutSeconds',
            'content_type': 'contentType',
            'server_side_encryption': 'serverSideEncryption'
        }

        self._file_name = None
        self._content_md5 = None
        self._signed_url_timeout_seconds = None
        self._content_type = None
        self._server_side_encryption = None

    @property
    def file_name(self) -> str:
        """
        Gets the file_name of this UploadUrlRequest.
        Name of the file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%`]\">[~<#|

        :return: The file_name of this UploadUrlRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str) -> None:
        """
        Sets the file_name of this UploadUrlRequest.
        Name of the file to upload. It must not start with a dot and not end with a forward slash. Whitespace and the following characters are not allowed: \\{^}%`]\">[~<#|

        :param file_name: The file_name of this UploadUrlRequest.
        :type: str
        """
        

        self._file_name = file_name

    @property
    def content_md5(self) -> str:
        """
        Gets the content_md5 of this UploadUrlRequest.
        Content MD5 of the file to upload

        :return: The content_md5 of this UploadUrlRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5: str) -> None:
        """
        Sets the content_md5 of this UploadUrlRequest.
        Content MD5 of the file to upload

        :param content_md5: The content_md5 of this UploadUrlRequest.
        :type: str
        """
        

        self._content_md5 = content_md5

    @property
    def signed_url_timeout_seconds(self) -> int:
        """
        Gets the signed_url_timeout_seconds of this UploadUrlRequest.
        The number of seconds the presigned URL is valid for (from 1 to 604800 seconds). If none provided, defaults to 600 seconds

        :return: The signed_url_timeout_seconds of this UploadUrlRequest.
        :rtype: int
        """
        return self._signed_url_timeout_seconds

    @signed_url_timeout_seconds.setter
    def signed_url_timeout_seconds(self, signed_url_timeout_seconds: int) -> None:
        """
        Sets the signed_url_timeout_seconds of this UploadUrlRequest.
        The number of seconds the presigned URL is valid for (from 1 to 604800 seconds). If none provided, defaults to 600 seconds

        :param signed_url_timeout_seconds: The signed_url_timeout_seconds of this UploadUrlRequest.
        :type: int
        """
        

        self._signed_url_timeout_seconds = signed_url_timeout_seconds

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this UploadUrlRequest.
        The content type of the file to upload. Allows all MIME types

        :return: The content_type of this UploadUrlRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this UploadUrlRequest.
        The content type of the file to upload. Allows all MIME types

        :param content_type: The content_type of this UploadUrlRequest.
        :type: str
        """
        

        self._content_type = content_type

    @property
    def server_side_encryption(self) -> str:
        """
        Gets the server_side_encryption of this UploadUrlRequest.


        :return: The server_side_encryption of this UploadUrlRequest.
        :rtype: str
        """
        return self._server_side_encryption

    @server_side_encryption.setter
    def server_side_encryption(self, server_side_encryption: str) -> None:
        """
        Sets the server_side_encryption of this UploadUrlRequest.


        :param server_side_encryption: The server_side_encryption of this UploadUrlRequest.
        :type: str
        """
        if isinstance(server_side_encryption, int):
            server_side_encryption = str(server_side_encryption)
        allowed_values = ["AES256"]
        if server_side_encryption.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for server_side_encryption -> " + server_side_encryption)
            self._server_side_encryption = "outdated_sdk_version"
        else:
            self._server_side_encryption = server_side_encryption

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

