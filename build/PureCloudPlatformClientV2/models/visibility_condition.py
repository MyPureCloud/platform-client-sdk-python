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


class VisibilityCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        VisibilityCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'combining_operation': 'str',
            'predicates': 'list[object]'
        }

        self.attribute_map = {
            'combining_operation': 'combiningOperation',
            'predicates': 'predicates'
        }

        self._combining_operation = None
        self._predicates = None

    @property
    def combining_operation(self) -> str:
        """
        Gets the combining_operation of this VisibilityCondition.


        :return: The combining_operation of this VisibilityCondition.
        :rtype: str
        """
        return self._combining_operation

    @combining_operation.setter
    def combining_operation(self, combining_operation: str) -> None:
        """
        Sets the combining_operation of this VisibilityCondition.


        :param combining_operation: The combining_operation of this VisibilityCondition.
        :type: str
        """
        if isinstance(combining_operation, int):
            combining_operation = str(combining_operation)
        allowed_values = ["AND", "OR"]
        if combining_operation.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for combining_operation -> " + combining_operation)
            self._combining_operation = "outdated_sdk_version"
        else:
            self._combining_operation = combining_operation

    @property
    def predicates(self) -> List[object]:
        """
        Gets the predicates of this VisibilityCondition.
        A list of strings, each representing the location in the form of the Answer Option to depend on. In the format of \"/form/questionGroup/{questionGroupIndex}/question/{questionIndex}/answer/{answerIndex}\" or, to assume the current question group, \"../question/{questionIndex}/answer/{answerIndex}\". Note: Indexes are zero-based

        :return: The predicates of this VisibilityCondition.
        :rtype: list[object]
        """
        return self._predicates

    @predicates.setter
    def predicates(self, predicates: List[object]) -> None:
        """
        Sets the predicates of this VisibilityCondition.
        A list of strings, each representing the location in the form of the Answer Option to depend on. In the format of \"/form/questionGroup/{questionGroupIndex}/question/{questionIndex}/answer/{answerIndex}\" or, to assume the current question group, \"../question/{questionIndex}/answer/{answerIndex}\". Note: Indexes are zero-based

        :param predicates: The predicates of this VisibilityCondition.
        :type: list[object]
        """
        

        self._predicates = predicates

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

