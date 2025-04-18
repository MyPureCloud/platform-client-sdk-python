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


class HistoricalShrinkageAggregateResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        HistoricalShrinkageAggregateResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'scheduled_shrinkage_seconds': 'int',
            'scheduled_shrinkage_percent': 'float',
            'actual_shrinkage_seconds': 'int',
            'actual_shrinkage_percent': 'float',
            'paid_shrinkage_seconds': 'int',
            'unpaid_shrinkage_seconds': 'int',
            'planned_shrinkage_seconds': 'int',
            'unplanned_shrinkage_seconds': 'int'
        }

        self.attribute_map = {
            'scheduled_shrinkage_seconds': 'scheduledShrinkageSeconds',
            'scheduled_shrinkage_percent': 'scheduledShrinkagePercent',
            'actual_shrinkage_seconds': 'actualShrinkageSeconds',
            'actual_shrinkage_percent': 'actualShrinkagePercent',
            'paid_shrinkage_seconds': 'paidShrinkageSeconds',
            'unpaid_shrinkage_seconds': 'unpaidShrinkageSeconds',
            'planned_shrinkage_seconds': 'plannedShrinkageSeconds',
            'unplanned_shrinkage_seconds': 'unplannedShrinkageSeconds'
        }

        self._scheduled_shrinkage_seconds = None
        self._scheduled_shrinkage_percent = None
        self._actual_shrinkage_seconds = None
        self._actual_shrinkage_percent = None
        self._paid_shrinkage_seconds = None
        self._unpaid_shrinkage_seconds = None
        self._planned_shrinkage_seconds = None
        self._unplanned_shrinkage_seconds = None

    @property
    def scheduled_shrinkage_seconds(self) -> int:
        """
        Gets the scheduled_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for scheduled activities

        :return: The scheduled_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._scheduled_shrinkage_seconds

    @scheduled_shrinkage_seconds.setter
    def scheduled_shrinkage_seconds(self, scheduled_shrinkage_seconds: int) -> None:
        """
        Sets the scheduled_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for scheduled activities

        :param scheduled_shrinkage_seconds: The scheduled_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._scheduled_shrinkage_seconds = scheduled_shrinkage_seconds

    @property
    def scheduled_shrinkage_percent(self) -> float:
        """
        Gets the scheduled_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in percent from 0.0 to 100.0 for scheduled activities

        :return: The scheduled_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        :rtype: float
        """
        return self._scheduled_shrinkage_percent

    @scheduled_shrinkage_percent.setter
    def scheduled_shrinkage_percent(self, scheduled_shrinkage_percent: float) -> None:
        """
        Sets the scheduled_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in percent from 0.0 to 100.0 for scheduled activities

        :param scheduled_shrinkage_percent: The scheduled_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        :type: float
        """
        

        self._scheduled_shrinkage_percent = scheduled_shrinkage_percent

    @property
    def actual_shrinkage_seconds(self) -> int:
        """
        Gets the actual_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated actual value in seconds for scheduled activities

        :return: The actual_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._actual_shrinkage_seconds

    @actual_shrinkage_seconds.setter
    def actual_shrinkage_seconds(self, actual_shrinkage_seconds: int) -> None:
        """
        Sets the actual_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated actual value in seconds for scheduled activities

        :param actual_shrinkage_seconds: The actual_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._actual_shrinkage_seconds = actual_shrinkage_seconds

    @property
    def actual_shrinkage_percent(self) -> float:
        """
        Gets the actual_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        Aggregated actual value in percent from 0.0 to 100.0 for scheduled activities

        :return: The actual_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        :rtype: float
        """
        return self._actual_shrinkage_percent

    @actual_shrinkage_percent.setter
    def actual_shrinkage_percent(self, actual_shrinkage_percent: float) -> None:
        """
        Sets the actual_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        Aggregated actual value in percent from 0.0 to 100.0 for scheduled activities

        :param actual_shrinkage_percent: The actual_shrinkage_percent of this HistoricalShrinkageAggregateResponse.
        :type: float
        """
        

        self._actual_shrinkage_percent = actual_shrinkage_percent

    @property
    def paid_shrinkage_seconds(self) -> int:
        """
        Gets the paid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for paid activities

        :return: The paid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._paid_shrinkage_seconds

    @paid_shrinkage_seconds.setter
    def paid_shrinkage_seconds(self, paid_shrinkage_seconds: int) -> None:
        """
        Sets the paid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for paid activities

        :param paid_shrinkage_seconds: The paid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._paid_shrinkage_seconds = paid_shrinkage_seconds

    @property
    def unpaid_shrinkage_seconds(self) -> int:
        """
        Gets the unpaid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for unpaid activities

        :return: The unpaid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._unpaid_shrinkage_seconds

    @unpaid_shrinkage_seconds.setter
    def unpaid_shrinkage_seconds(self, unpaid_shrinkage_seconds: int) -> None:
        """
        Sets the unpaid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for unpaid activities

        :param unpaid_shrinkage_seconds: The unpaid_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._unpaid_shrinkage_seconds = unpaid_shrinkage_seconds

    @property
    def planned_shrinkage_seconds(self) -> int:
        """
        Gets the planned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for planned activities

        :return: The planned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._planned_shrinkage_seconds

    @planned_shrinkage_seconds.setter
    def planned_shrinkage_seconds(self, planned_shrinkage_seconds: int) -> None:
        """
        Sets the planned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for planned activities

        :param planned_shrinkage_seconds: The planned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._planned_shrinkage_seconds = planned_shrinkage_seconds

    @property
    def unplanned_shrinkage_seconds(self) -> int:
        """
        Gets the unplanned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for unplanned activities

        :return: The unplanned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :rtype: int
        """
        return self._unplanned_shrinkage_seconds

    @unplanned_shrinkage_seconds.setter
    def unplanned_shrinkage_seconds(self, unplanned_shrinkage_seconds: int) -> None:
        """
        Sets the unplanned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        Aggregated shrinkage value in seconds for unplanned activities

        :param unplanned_shrinkage_seconds: The unplanned_shrinkage_seconds of this HistoricalShrinkageAggregateResponse.
        :type: int
        """
        

        self._unplanned_shrinkage_seconds = unplanned_shrinkage_seconds

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

