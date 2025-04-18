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
    from . import MediaEndpointStatistics

class MediaStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MediaStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'communication_id': 'str',
            'date_start': 'datetime',
            'creation_milliseconds': 'int',
            'preferred_region': 'str',
            'effective_region': 'str',
            'media_statistics': 'list[MediaEndpointStatistics]'
        }

        self.attribute_map = {
            'communication_id': 'communicationId',
            'date_start': 'dateStart',
            'creation_milliseconds': 'creationMilliseconds',
            'preferred_region': 'preferredRegion',
            'effective_region': 'effectiveRegion',
            'media_statistics': 'mediaStatistics'
        }

        self._communication_id = None
        self._date_start = None
        self._creation_milliseconds = None
        self._preferred_region = None
        self._effective_region = None
        self._media_statistics = None

    @property
    def communication_id(self) -> str:
        """
        Gets the communication_id of this MediaStatistics.


        :return: The communication_id of this MediaStatistics.
        :rtype: str
        """
        return self._communication_id

    @communication_id.setter
    def communication_id(self, communication_id: str) -> None:
        """
        Sets the communication_id of this MediaStatistics.


        :param communication_id: The communication_id of this MediaStatistics.
        :type: str
        """
        

        self._communication_id = communication_id

    @property
    def date_start(self) -> datetime:
        """
        Gets the date_start of this MediaStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_start of this MediaStatistics.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: datetime) -> None:
        """
        Sets the date_start of this MediaStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_start: The date_start of this MediaStatistics.
        :type: datetime
        """
        

        self._date_start = date_start

    @property
    def creation_milliseconds(self) -> int:
        """
        Gets the creation_milliseconds of this MediaStatistics.
        Relative milliseconds to create media session

        :return: The creation_milliseconds of this MediaStatistics.
        :rtype: int
        """
        return self._creation_milliseconds

    @creation_milliseconds.setter
    def creation_milliseconds(self, creation_milliseconds: int) -> None:
        """
        Sets the creation_milliseconds of this MediaStatistics.
        Relative milliseconds to create media session

        :param creation_milliseconds: The creation_milliseconds of this MediaStatistics.
        :type: int
        """
        

        self._creation_milliseconds = creation_milliseconds

    @property
    def preferred_region(self) -> str:
        """
        Gets the preferred_region of this MediaStatistics.
        Preferred media region

        :return: The preferred_region of this MediaStatistics.
        :rtype: str
        """
        return self._preferred_region

    @preferred_region.setter
    def preferred_region(self, preferred_region: str) -> None:
        """
        Sets the preferred_region of this MediaStatistics.
        Preferred media region

        :param preferred_region: The preferred_region of this MediaStatistics.
        :type: str
        """
        

        self._preferred_region = preferred_region

    @property
    def effective_region(self) -> str:
        """
        Gets the effective_region of this MediaStatistics.
        Actual media region

        :return: The effective_region of this MediaStatistics.
        :rtype: str
        """
        return self._effective_region

    @effective_region.setter
    def effective_region(self, effective_region: str) -> None:
        """
        Sets the effective_region of this MediaStatistics.
        Actual media region

        :param effective_region: The effective_region of this MediaStatistics.
        :type: str
        """
        

        self._effective_region = effective_region

    @property
    def media_statistics(self) -> List['MediaEndpointStatistics']:
        """
        Gets the media_statistics of this MediaStatistics.
        Media statistics for each media endpoint

        :return: The media_statistics of this MediaStatistics.
        :rtype: list[MediaEndpointStatistics]
        """
        return self._media_statistics

    @media_statistics.setter
    def media_statistics(self, media_statistics: List['MediaEndpointStatistics']) -> None:
        """
        Sets the media_statistics of this MediaStatistics.
        Media statistics for each media endpoint

        :param media_statistics: The media_statistics of this MediaStatistics.
        :type: list[MediaEndpointStatistics]
        """
        

        self._media_statistics = media_statistics

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

