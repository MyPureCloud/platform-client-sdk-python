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


class FreeSeatingConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FreeSeatingConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'ttl_minutes': 'int'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'ttl_minutes': 'ttlMinutes'
        }

        self._enabled = None
        self._ttl_minutes = None

    @property
    def enabled(self):
        """
        Gets the enabled of this FreeSeatingConfiguration.
        Whether or not free-seating is enabled for the organization

        :return: The enabled of this FreeSeatingConfiguration.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this FreeSeatingConfiguration.
        Whether or not free-seating is enabled for the organization

        :param enabled: The enabled of this FreeSeatingConfiguration.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def ttl_minutes(self):
        """
        Gets the ttl_minutes of this FreeSeatingConfiguration.
        The amount of time in minutes until an offline user is disassociated from their station

        :return: The ttl_minutes of this FreeSeatingConfiguration.
        :rtype: int
        """
        return self._ttl_minutes

    @ttl_minutes.setter
    def ttl_minutes(self, ttl_minutes):
        """
        Sets the ttl_minutes of this FreeSeatingConfiguration.
        The amount of time in minutes until an offline user is disassociated from their station

        :param ttl_minutes: The ttl_minutes of this FreeSeatingConfiguration.
        :type: int
        """
        
        self._ttl_minutes = ttl_minutes

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
