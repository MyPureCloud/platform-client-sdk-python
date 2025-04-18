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
    from . import WfmVersionedEntityMetadata

class BuShortTermForecastListItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuShortTermForecastListItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'week_date': 'date',
            'week_count': 'int',
            'creation_method': 'str',
            'description': 'str',
            'legacy': 'bool',
            'metadata': 'WfmVersionedEntityMetadata',
            'can_use_for_scheduling': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'week_date': 'weekDate',
            'week_count': 'weekCount',
            'creation_method': 'creationMethod',
            'description': 'description',
            'legacy': 'legacy',
            'metadata': 'metadata',
            'can_use_for_scheduling': 'canUseForScheduling',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._week_date = None
        self._week_count = None
        self._creation_method = None
        self._description = None
        self._legacy = None
        self._metadata = None
        self._can_use_for_scheduling = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BuShortTermForecastListItem.
        The globally unique identifier for the object.

        :return: The id of this BuShortTermForecastListItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BuShortTermForecastListItem.
        The globally unique identifier for the object.

        :param id: The id of this BuShortTermForecastListItem.
        :type: str
        """
        

        self._id = id

    @property
    def week_date(self) -> date:
        """
        Gets the week_date of this BuShortTermForecastListItem.
        The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The week_date of this BuShortTermForecastListItem.
        :rtype: date
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date: date) -> None:
        """
        Sets the week_date of this BuShortTermForecastListItem.
        The start week date of this forecast in yyyy-MM-dd.  Must fall on the start day of week for the associated business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param week_date: The week_date of this BuShortTermForecastListItem.
        :type: date
        """
        

        self._week_date = week_date

    @property
    def week_count(self) -> int:
        """
        Gets the week_count of this BuShortTermForecastListItem.
        The number of weeks this forecast covers

        :return: The week_count of this BuShortTermForecastListItem.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count: int) -> None:
        """
        Sets the week_count of this BuShortTermForecastListItem.
        The number of weeks this forecast covers

        :param week_count: The week_count of this BuShortTermForecastListItem.
        :type: int
        """
        

        self._week_count = week_count

    @property
    def creation_method(self) -> str:
        """
        Gets the creation_method of this BuShortTermForecastListItem.
        The method by which this forecast was created

        :return: The creation_method of this BuShortTermForecastListItem.
        :rtype: str
        """
        return self._creation_method

    @creation_method.setter
    def creation_method(self, creation_method: str) -> None:
        """
        Sets the creation_method of this BuShortTermForecastListItem.
        The method by which this forecast was created

        :param creation_method: The creation_method of this BuShortTermForecastListItem.
        :type: str
        """
        if isinstance(creation_method, int):
            creation_method = str(creation_method)
        allowed_values = ["Import", "ImportedHistoricalWeightedAverage", "HistoricalWeightedAverage", "Advanced"]
        if creation_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for creation_method -> " + creation_method)
            self._creation_method = "outdated_sdk_version"
        else:
            self._creation_method = creation_method

    @property
    def description(self) -> str:
        """
        Gets the description of this BuShortTermForecastListItem.
        The description of this forecast

        :return: The description of this BuShortTermForecastListItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this BuShortTermForecastListItem.
        The description of this forecast

        :param description: The description of this BuShortTermForecastListItem.
        :type: str
        """
        

        self._description = description

    @property
    def legacy(self) -> bool:
        """
        Gets the legacy of this BuShortTermForecastListItem.
        Whether this forecast contains modifications on legacy metrics

        :return: The legacy of this BuShortTermForecastListItem.
        :rtype: bool
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy: bool) -> None:
        """
        Sets the legacy of this BuShortTermForecastListItem.
        Whether this forecast contains modifications on legacy metrics

        :param legacy: The legacy of this BuShortTermForecastListItem.
        :type: bool
        """
        

        self._legacy = legacy

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this BuShortTermForecastListItem.
        Metadata for this forecast

        :return: The metadata of this BuShortTermForecastListItem.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this BuShortTermForecastListItem.
        Metadata for this forecast

        :param metadata: The metadata of this BuShortTermForecastListItem.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

    @property
    def can_use_for_scheduling(self) -> bool:
        """
        Gets the can_use_for_scheduling of this BuShortTermForecastListItem.
        Whether this forecast can be used for scheduling

        :return: The can_use_for_scheduling of this BuShortTermForecastListItem.
        :rtype: bool
        """
        return self._can_use_for_scheduling

    @can_use_for_scheduling.setter
    def can_use_for_scheduling(self, can_use_for_scheduling: bool) -> None:
        """
        Sets the can_use_for_scheduling of this BuShortTermForecastListItem.
        Whether this forecast can be used for scheduling

        :param can_use_for_scheduling: The can_use_for_scheduling of this BuShortTermForecastListItem.
        :type: bool
        """
        

        self._can_use_for_scheduling = can_use_for_scheduling

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this BuShortTermForecastListItem.
        The URI for this object

        :return: The self_uri of this BuShortTermForecastListItem.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this BuShortTermForecastListItem.
        The URI for this object

        :param self_uri: The self_uri of this BuShortTermForecastListItem.
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

