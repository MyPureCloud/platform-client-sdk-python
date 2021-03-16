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

class ObjectiveZone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ObjectiveZone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'label': 'str',
            'direction_type': 'str',
            'zone_type': 'str',
            'upper_limit_points': 'int',
            'lower_limit_points': 'int',
            'upper_limit_value': 'int',
            'lower_limit_value': 'int'
        }

        self.attribute_map = {
            'label': 'label',
            'direction_type': 'directionType',
            'zone_type': 'zoneType',
            'upper_limit_points': 'upperLimitPoints',
            'lower_limit_points': 'lowerLimitPoints',
            'upper_limit_value': 'upperLimitValue',
            'lower_limit_value': 'lowerLimitValue'
        }

        self._label = None
        self._direction_type = None
        self._zone_type = None
        self._upper_limit_points = None
        self._lower_limit_points = None
        self._upper_limit_value = None
        self._lower_limit_value = None

    @property
    def label(self):
        """
        Gets the label of this ObjectiveZone.
        label

        :return: The label of this ObjectiveZone.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ObjectiveZone.
        label

        :param label: The label of this ObjectiveZone.
        :type: str
        """
        
        self._label = label

    @property
    def direction_type(self):
        """
        Gets the direction_type of this ObjectiveZone.
        direction type

        :return: The direction_type of this ObjectiveZone.
        :rtype: str
        """
        return self._direction_type

    @direction_type.setter
    def direction_type(self, direction_type):
        """
        Sets the direction_type of this ObjectiveZone.
        direction type

        :param direction_type: The direction_type of this ObjectiveZone.
        :type: str
        """
        allowed_values = ["Up", "Down", "Flat"]
        if direction_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction_type -> " + direction_type)
            self._direction_type = "outdated_sdk_version"
        else:
            self._direction_type = direction_type

    @property
    def zone_type(self):
        """
        Gets the zone_type of this ObjectiveZone.
        zone type

        :return: The zone_type of this ObjectiveZone.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """
        Sets the zone_type of this ObjectiveZone.
        zone type

        :param zone_type: The zone_type of this ObjectiveZone.
        :type: str
        """
        allowed_values = ["Good", "Target", "Great", "Out"]
        if zone_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for zone_type -> " + zone_type)
            self._zone_type = "outdated_sdk_version"
        else:
            self._zone_type = zone_type

    @property
    def upper_limit_points(self):
        """
        Gets the upper_limit_points of this ObjectiveZone.
        upper limit points

        :return: The upper_limit_points of this ObjectiveZone.
        :rtype: int
        """
        return self._upper_limit_points

    @upper_limit_points.setter
    def upper_limit_points(self, upper_limit_points):
        """
        Sets the upper_limit_points of this ObjectiveZone.
        upper limit points

        :param upper_limit_points: The upper_limit_points of this ObjectiveZone.
        :type: int
        """
        
        self._upper_limit_points = upper_limit_points

    @property
    def lower_limit_points(self):
        """
        Gets the lower_limit_points of this ObjectiveZone.
        lower limit points

        :return: The lower_limit_points of this ObjectiveZone.
        :rtype: int
        """
        return self._lower_limit_points

    @lower_limit_points.setter
    def lower_limit_points(self, lower_limit_points):
        """
        Sets the lower_limit_points of this ObjectiveZone.
        lower limit points

        :param lower_limit_points: The lower_limit_points of this ObjectiveZone.
        :type: int
        """
        
        self._lower_limit_points = lower_limit_points

    @property
    def upper_limit_value(self):
        """
        Gets the upper_limit_value of this ObjectiveZone.
        upper limit value

        :return: The upper_limit_value of this ObjectiveZone.
        :rtype: int
        """
        return self._upper_limit_value

    @upper_limit_value.setter
    def upper_limit_value(self, upper_limit_value):
        """
        Sets the upper_limit_value of this ObjectiveZone.
        upper limit value

        :param upper_limit_value: The upper_limit_value of this ObjectiveZone.
        :type: int
        """
        
        self._upper_limit_value = upper_limit_value

    @property
    def lower_limit_value(self):
        """
        Gets the lower_limit_value of this ObjectiveZone.
        lower limit value

        :return: The lower_limit_value of this ObjectiveZone.
        :rtype: int
        """
        return self._lower_limit_value

    @lower_limit_value.setter
    def lower_limit_value(self, lower_limit_value):
        """
        Sets the lower_limit_value of this ObjectiveZone.
        lower limit value

        :param lower_limit_value: The lower_limit_value of this ObjectiveZone.
        :type: int
        """
        
        self._lower_limit_value = lower_limit_value

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
