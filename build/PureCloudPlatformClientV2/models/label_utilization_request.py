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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict


class LabelUtilizationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LabelUtilizationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maximum_capacity': 'int',
            'interrupting_label_ids': 'list[str]'
        }

        self.attribute_map = {
            'maximum_capacity': 'maximumCapacity',
            'interrupting_label_ids': 'interruptingLabelIds'
        }

        self._maximum_capacity = None
        self._interrupting_label_ids = None

    @property
    def maximum_capacity(self) -> int:
        """
        Gets the maximum_capacity of this LabelUtilizationRequest.
        Defines the maximum number of interactions with this label that an agent can handle at one time.

        :return: The maximum_capacity of this LabelUtilizationRequest.
        :rtype: int
        """
        return self._maximum_capacity

    @maximum_capacity.setter
    def maximum_capacity(self, maximum_capacity: int) -> None:
        """
        Sets the maximum_capacity of this LabelUtilizationRequest.
        Defines the maximum number of interactions with this label that an agent can handle at one time.

        :param maximum_capacity: The maximum_capacity of this LabelUtilizationRequest.
        :type: int
        """
        

        self._maximum_capacity = maximum_capacity

    @property
    def interrupting_label_ids(self) -> List[str]:
        """
        Gets the interrupting_label_ids of this LabelUtilizationRequest.
        Defines other labels that can interrupt an interaction with this label.

        :return: The interrupting_label_ids of this LabelUtilizationRequest.
        :rtype: list[str]
        """
        return self._interrupting_label_ids

    @interrupting_label_ids.setter
    def interrupting_label_ids(self, interrupting_label_ids: List[str]) -> None:
        """
        Sets the interrupting_label_ids of this LabelUtilizationRequest.
        Defines other labels that can interrupt an interaction with this label.

        :param interrupting_label_ids: The interrupting_label_ids of this LabelUtilizationRequest.
        :type: list[str]
        """
        

        self._interrupting_label_ids = interrupting_label_ids

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
