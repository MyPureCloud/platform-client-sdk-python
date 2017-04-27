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


class ContactListFilterNotificationRange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContactListFilterNotificationRange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gt': 'str',
            'gte': 'str',
            'lt': 'str',
            'lte': 'str',
            'in_set': 'list[str]',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'gt': 'gt',
            'gte': 'gte',
            'lt': 'lt',
            'lte': 'lte',
            'in_set': 'inSet',
            'additional_properties': 'additionalProperties'
        }

        self._gt = None
        self._gte = None
        self._lt = None
        self._lte = None
        self._in_set = None
        self._additional_properties = None

    @property
    def gt(self):
        """
        Gets the gt of this ContactListFilterNotificationRange.


        :return: The gt of this ContactListFilterNotificationRange.
        :rtype: str
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """
        Sets the gt of this ContactListFilterNotificationRange.


        :param gt: The gt of this ContactListFilterNotificationRange.
        :type: str
        """
        
        self._gt = gt

    @property
    def gte(self):
        """
        Gets the gte of this ContactListFilterNotificationRange.


        :return: The gte of this ContactListFilterNotificationRange.
        :rtype: str
        """
        return self._gte

    @gte.setter
    def gte(self, gte):
        """
        Sets the gte of this ContactListFilterNotificationRange.


        :param gte: The gte of this ContactListFilterNotificationRange.
        :type: str
        """
        
        self._gte = gte

    @property
    def lt(self):
        """
        Gets the lt of this ContactListFilterNotificationRange.


        :return: The lt of this ContactListFilterNotificationRange.
        :rtype: str
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """
        Sets the lt of this ContactListFilterNotificationRange.


        :param lt: The lt of this ContactListFilterNotificationRange.
        :type: str
        """
        
        self._lt = lt

    @property
    def lte(self):
        """
        Gets the lte of this ContactListFilterNotificationRange.


        :return: The lte of this ContactListFilterNotificationRange.
        :rtype: str
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """
        Sets the lte of this ContactListFilterNotificationRange.


        :param lte: The lte of this ContactListFilterNotificationRange.
        :type: str
        """
        
        self._lte = lte

    @property
    def in_set(self):
        """
        Gets the in_set of this ContactListFilterNotificationRange.


        :return: The in_set of this ContactListFilterNotificationRange.
        :rtype: list[str]
        """
        return self._in_set

    @in_set.setter
    def in_set(self, in_set):
        """
        Sets the in_set of this ContactListFilterNotificationRange.


        :param in_set: The in_set of this ContactListFilterNotificationRange.
        :type: list[str]
        """
        
        self._in_set = in_set

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ContactListFilterNotificationRange.


        :return: The additional_properties of this ContactListFilterNotificationRange.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ContactListFilterNotificationRange.


        :param additional_properties: The additional_properties of this ContactListFilterNotificationRange.
        :type: object
        """
        
        self._additional_properties = additional_properties

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
