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


class MediaStatisticsClientInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MediaStatisticsClientInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'origin_app_name': 'str',
            'origin_app_id': 'str',
            'origin_app_version': 'str'
        }

        self.attribute_map = {
            'origin_app_name': 'originAppName',
            'origin_app_id': 'originAppId',
            'origin_app_version': 'originAppVersion'
        }

        self._origin_app_name = None
        self._origin_app_id = None
        self._origin_app_version = None

    @property
    def origin_app_name(self) -> str:
        """
        Gets the origin_app_name of this MediaStatisticsClientInfo.
        The name of the application that created the media session.

        :return: The origin_app_name of this MediaStatisticsClientInfo.
        :rtype: str
        """
        return self._origin_app_name

    @origin_app_name.setter
    def origin_app_name(self, origin_app_name: str) -> None:
        """
        Sets the origin_app_name of this MediaStatisticsClientInfo.
        The name of the application that created the media session.

        :param origin_app_name: The origin_app_name of this MediaStatisticsClientInfo.
        :type: str
        """
        

        self._origin_app_name = origin_app_name

    @property
    def origin_app_id(self) -> str:
        """
        Gets the origin_app_id of this MediaStatisticsClientInfo.
        The ID of the application that created the media session.

        :return: The origin_app_id of this MediaStatisticsClientInfo.
        :rtype: str
        """
        return self._origin_app_id

    @origin_app_id.setter
    def origin_app_id(self, origin_app_id: str) -> None:
        """
        Sets the origin_app_id of this MediaStatisticsClientInfo.
        The ID of the application that created the media session.

        :param origin_app_id: The origin_app_id of this MediaStatisticsClientInfo.
        :type: str
        """
        

        self._origin_app_id = origin_app_id

    @property
    def origin_app_version(self) -> str:
        """
        Gets the origin_app_version of this MediaStatisticsClientInfo.
        The version of the application that created the media session.

        :return: The origin_app_version of this MediaStatisticsClientInfo.
        :rtype: str
        """
        return self._origin_app_version

    @origin_app_version.setter
    def origin_app_version(self, origin_app_version: str) -> None:
        """
        Sets the origin_app_version of this MediaStatisticsClientInfo.
        The version of the application that created the media session.

        :param origin_app_version: The origin_app_version of this MediaStatisticsClientInfo.
        :type: str
        """
        

        self._origin_app_version = origin_app_version

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

