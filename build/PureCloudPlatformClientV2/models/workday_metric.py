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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class WorkdayMetric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WorkdayMetric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metric': 'Metric',
            'objective': 'Objective',
            'points': 'int',
            'value': 'float',
            'punctuality_events': 'list[PunctualityEvent]'
        }

        self.attribute_map = {
            'metric': 'metric',
            'objective': 'objective',
            'points': 'points',
            'value': 'value',
            'punctuality_events': 'punctualityEvents'
        }

        self._metric = None
        self._objective = None
        self._points = None
        self._value = None
        self._punctuality_events = None

    @property
    def metric(self):
        """
        Gets the metric of this WorkdayMetric.
        Gamification metric

        :return: The metric of this WorkdayMetric.
        :rtype: Metric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this WorkdayMetric.
        Gamification metric

        :param metric: The metric of this WorkdayMetric.
        :type: Metric
        """
        
        self._metric = metric

    @property
    def objective(self):
        """
        Gets the objective of this WorkdayMetric.
        Current objective for this metric

        :return: The objective of this WorkdayMetric.
        :rtype: Objective
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """
        Sets the objective of this WorkdayMetric.
        Current objective for this metric

        :param objective: The objective of this WorkdayMetric.
        :type: Objective
        """
        
        self._objective = objective

    @property
    def points(self):
        """
        Gets the points of this WorkdayMetric.
        Gamification points earned for this metric

        :return: The points of this WorkdayMetric.
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """
        Sets the points of this WorkdayMetric.
        Gamification points earned for this metric

        :param points: The points of this WorkdayMetric.
        :type: int
        """
        
        self._points = points

    @property
    def value(self):
        """
        Gets the value of this WorkdayMetric.
        Value of this metric

        :return: The value of this WorkdayMetric.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this WorkdayMetric.
        Value of this metric

        :param value: The value of this WorkdayMetric.
        :type: float
        """
        
        self._value = value

    @property
    def punctuality_events(self):
        """
        Gets the punctuality_events of this WorkdayMetric.
        List of schedule activity events for punctuality metrics

        :return: The punctuality_events of this WorkdayMetric.
        :rtype: list[PunctualityEvent]
        """
        return self._punctuality_events

    @punctuality_events.setter
    def punctuality_events(self, punctuality_events):
        """
        Sets the punctuality_events of this WorkdayMetric.
        List of schedule activity events for punctuality metrics

        :param punctuality_events: The punctuality_events of this WorkdayMetric.
        :type: list[PunctualityEvent]
        """
        
        self._punctuality_events = punctuality_events

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

