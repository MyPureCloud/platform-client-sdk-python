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


class FacetStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FacetStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count': 'int',
            'min': 'float',
            'max': 'float',
            'mean': 'float',
            'std_deviation': 'float',
            'date_min': 'datetime',
            'date_max': 'datetime'
        }

        self.attribute_map = {
            'count': 'count',
            'min': 'min',
            'max': 'max',
            'mean': 'mean',
            'std_deviation': 'stdDeviation',
            'date_min': 'dateMin',
            'date_max': 'dateMax'
        }

        self._count = None
        self._min = None
        self._max = None
        self._mean = None
        self._std_deviation = None
        self._date_min = None
        self._date_max = None

    @property
    def count(self) -> int:
        """
        Gets the count of this FacetStatistics.


        :return: The count of this FacetStatistics.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int) -> None:
        """
        Sets the count of this FacetStatistics.


        :param count: The count of this FacetStatistics.
        :type: int
        """
        

        self._count = count

    @property
    def min(self) -> float:
        """
        Gets the min of this FacetStatistics.


        :return: The min of this FacetStatistics.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min: float) -> None:
        """
        Sets the min of this FacetStatistics.


        :param min: The min of this FacetStatistics.
        :type: float
        """
        

        self._min = min

    @property
    def max(self) -> float:
        """
        Gets the max of this FacetStatistics.


        :return: The max of this FacetStatistics.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max: float) -> None:
        """
        Sets the max of this FacetStatistics.


        :param max: The max of this FacetStatistics.
        :type: float
        """
        

        self._max = max

    @property
    def mean(self) -> float:
        """
        Gets the mean of this FacetStatistics.


        :return: The mean of this FacetStatistics.
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean: float) -> None:
        """
        Sets the mean of this FacetStatistics.


        :param mean: The mean of this FacetStatistics.
        :type: float
        """
        

        self._mean = mean

    @property
    def std_deviation(self) -> float:
        """
        Gets the std_deviation of this FacetStatistics.


        :return: The std_deviation of this FacetStatistics.
        :rtype: float
        """
        return self._std_deviation

    @std_deviation.setter
    def std_deviation(self, std_deviation: float) -> None:
        """
        Sets the std_deviation of this FacetStatistics.


        :param std_deviation: The std_deviation of this FacetStatistics.
        :type: float
        """
        

        self._std_deviation = std_deviation

    @property
    def date_min(self) -> datetime:
        """
        Gets the date_min of this FacetStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_min of this FacetStatistics.
        :rtype: datetime
        """
        return self._date_min

    @date_min.setter
    def date_min(self, date_min: datetime) -> None:
        """
        Sets the date_min of this FacetStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_min: The date_min of this FacetStatistics.
        :type: datetime
        """
        

        self._date_min = date_min

    @property
    def date_max(self) -> datetime:
        """
        Gets the date_max of this FacetStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_max of this FacetStatistics.
        :rtype: datetime
        """
        return self._date_max

    @date_max.setter
    def date_max(self, date_max: datetime) -> None:
        """
        Sets the date_max of this FacetStatistics.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_max: The date_max of this FacetStatistics.
        :type: datetime
        """
        

        self._date_max = date_max

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

