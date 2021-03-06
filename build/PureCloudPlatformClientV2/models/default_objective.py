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

class DefaultObjective(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DefaultObjective - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'template_id': 'str',
            'zones': 'list[ObjectiveZone]',
            'enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'template_id': 'templateId',
            'zones': 'zones',
            'enabled': 'enabled'
        }

        self._id = None
        self._template_id = None
        self._zones = None
        self._enabled = None

    @property
    def id(self):
        """
        Gets the id of this DefaultObjective.
        The globally unique identifier for the object.

        :return: The id of this DefaultObjective.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DefaultObjective.
        The globally unique identifier for the object.

        :param id: The id of this DefaultObjective.
        :type: str
        """
        
        self._id = id

    @property
    def template_id(self):
        """
        Gets the template_id of this DefaultObjective.
        The id of this objective's base template

        :return: The template_id of this DefaultObjective.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this DefaultObjective.
        The id of this objective's base template

        :param template_id: The template_id of this DefaultObjective.
        :type: str
        """
        
        self._template_id = template_id

    @property
    def zones(self):
        """
        Gets the zones of this DefaultObjective.
        Objective zone specifies min,max points and values for the associated metric

        :return: The zones of this DefaultObjective.
        :rtype: list[ObjectiveZone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """
        Sets the zones of this DefaultObjective.
        Objective zone specifies min,max points and values for the associated metric

        :param zones: The zones of this DefaultObjective.
        :type: list[ObjectiveZone]
        """
        
        self._zones = zones

    @property
    def enabled(self):
        """
        Gets the enabled of this DefaultObjective.
        A flag for whether this objective is enabled for the related metric

        :return: The enabled of this DefaultObjective.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DefaultObjective.
        A flag for whether this objective is enabled for the related metric

        :param enabled: The enabled of this DefaultObjective.
        :type: bool
        """
        
        self._enabled = enabled

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

