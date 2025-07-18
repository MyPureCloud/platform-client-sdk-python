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
    from . import BusinessUnitReference

class BuScheduleReferenceForMuRoute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuScheduleReferenceForMuRoute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'week_date': 'date',
            'business_unit': 'BusinessUnitReference',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'week_date': 'weekDate',
            'business_unit': 'businessUnit',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._week_date = None
        self._business_unit = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BuScheduleReferenceForMuRoute.
        The ID of the schedule

        :return: The id of this BuScheduleReferenceForMuRoute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BuScheduleReferenceForMuRoute.
        The ID of the schedule

        :param id: The id of this BuScheduleReferenceForMuRoute.
        :type: str
        """
        

        self._id = id

    @property
    def week_date(self) -> date:
        """
        Gets the week_date of this BuScheduleReferenceForMuRoute.
        The start week date for this schedule. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The week_date of this BuScheduleReferenceForMuRoute.
        :rtype: date
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date: date) -> None:
        """
        Sets the week_date of this BuScheduleReferenceForMuRoute.
        The start week date for this schedule. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param week_date: The week_date of this BuScheduleReferenceForMuRoute.
        :type: date
        """
        

        self._week_date = week_date

    @property
    def business_unit(self) -> 'BusinessUnitReference':
        """
        Gets the business_unit of this BuScheduleReferenceForMuRoute.
        The start week date for this schedule

        :return: The business_unit of this BuScheduleReferenceForMuRoute.
        :rtype: BusinessUnitReference
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit: 'BusinessUnitReference') -> None:
        """
        Sets the business_unit of this BuScheduleReferenceForMuRoute.
        The start week date for this schedule

        :param business_unit: The business_unit of this BuScheduleReferenceForMuRoute.
        :type: BusinessUnitReference
        """
        

        self._business_unit = business_unit

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this BuScheduleReferenceForMuRoute.
        The URI for this object

        :return: The self_uri of this BuScheduleReferenceForMuRoute.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this BuScheduleReferenceForMuRoute.
        The URI for this object

        :param self_uri: The self_uri of this BuScheduleReferenceForMuRoute.
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

