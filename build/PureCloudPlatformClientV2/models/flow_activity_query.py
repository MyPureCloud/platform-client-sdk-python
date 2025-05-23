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
    from . import FlowActivityQueryFilter
    from . import FlowActivityQueryMetric

class FlowActivityQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowActivityQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metrics': 'list[FlowActivityQueryMetric]',
            'group_by': 'list[str]',
            'filter': 'FlowActivityQueryFilter',
            'order': 'str'
        }

        self.attribute_map = {
            'metrics': 'metrics',
            'group_by': 'groupBy',
            'filter': 'filter',
            'order': 'order'
        }

        self._metrics = None
        self._group_by = None
        self._filter = None
        self._order = None

    @property
    def metrics(self) -> List['FlowActivityQueryMetric']:
        """
        Gets the metrics of this FlowActivityQuery.
        List of requested metrics

        :return: The metrics of this FlowActivityQuery.
        :rtype: list[FlowActivityQueryMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List['FlowActivityQueryMetric']) -> None:
        """
        Sets the metrics of this FlowActivityQuery.
        List of requested metrics

        :param metrics: The metrics of this FlowActivityQuery.
        :type: list[FlowActivityQueryMetric]
        """
        

        self._metrics = metrics

    @property
    def group_by(self) -> List[str]:
        """
        Gets the group_by of this FlowActivityQuery.
        Dimension(s) to group by

        :return: The group_by of this FlowActivityQuery.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by: List[str]) -> None:
        """
        Sets the group_by of this FlowActivityQuery.
        Dimension(s) to group by

        :param group_by: The group_by of this FlowActivityQuery.
        :type: list[str]
        """
        

        self._group_by = group_by

    @property
    def filter(self) -> 'FlowActivityQueryFilter':
        """
        Gets the filter of this FlowActivityQuery.
        Filter to return a subset of observations. Expresses boolean logical predicates as well as dimensional filters

        :return: The filter of this FlowActivityQuery.
        :rtype: FlowActivityQueryFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter: 'FlowActivityQueryFilter') -> None:
        """
        Sets the filter of this FlowActivityQuery.
        Filter to return a subset of observations. Expresses boolean logical predicates as well as dimensional filters

        :param filter: The filter of this FlowActivityQuery.
        :type: FlowActivityQueryFilter
        """
        

        self._filter = filter

    @property
    def order(self) -> str:
        """
        Gets the order of this FlowActivityQuery.
        Sort the result set in ascending/descending order. Default is ascending

        :return: The order of this FlowActivityQuery.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order: str) -> None:
        """
        Sets the order of this FlowActivityQuery.
        Sort the result set in ascending/descending order. Default is ascending

        :param order: The order of this FlowActivityQuery.
        :type: str
        """
        if isinstance(order, int):
            order = str(order)
        allowed_values = ["asc", "desc", "unordered"]
        if order.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for order -> " + order)
            self._order = "outdated_sdk_version"
        else:
            self._order = order

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

