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
    from . import AssistanceCondition

class AnswerOption(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AnswerOption - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'text': 'str',
            'value': 'int',
            'assistance_conditions': 'list[AssistanceCondition]'
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'value': 'value',
            'assistance_conditions': 'assistanceConditions'
        }

        self._id = None
        self._text = None
        self._value = None
        self._assistance_conditions = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AnswerOption.


        :return: The id of this AnswerOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AnswerOption.


        :param id: The id of this AnswerOption.
        :type: str
        """
        

        self._id = id

    @property
    def text(self) -> str:
        """
        Gets the text of this AnswerOption.


        :return: The text of this AnswerOption.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text of this AnswerOption.


        :param text: The text of this AnswerOption.
        :type: str
        """
        

        self._text = text

    @property
    def value(self) -> int:
        """
        Gets the value of this AnswerOption.


        :return: The value of this AnswerOption.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        """
        Sets the value of this AnswerOption.


        :param value: The value of this AnswerOption.
        :type: int
        """
        

        self._value = value

    @property
    def assistance_conditions(self) -> List['AssistanceCondition']:
        """
        Gets the assistance_conditions of this AnswerOption.
        List of assistance conditions which are combined together with a logical AND operator. Eg ( assistanceCondtion1 && assistanceCondition2 ) wherein assistanceCondition could be ( EXISTS topic1 || topic2 || ... ) or (NOTEXISTS topic3 || topic4 || ...).

        :return: The assistance_conditions of this AnswerOption.
        :rtype: list[AssistanceCondition]
        """
        return self._assistance_conditions

    @assistance_conditions.setter
    def assistance_conditions(self, assistance_conditions: List['AssistanceCondition']) -> None:
        """
        Sets the assistance_conditions of this AnswerOption.
        List of assistance conditions which are combined together with a logical AND operator. Eg ( assistanceCondtion1 && assistanceCondition2 ) wherein assistanceCondition could be ( EXISTS topic1 || topic2 || ... ) or (NOTEXISTS topic3 || topic4 || ...).

        :param assistance_conditions: The assistance_conditions of this AnswerOption.
        :type: list[AssistanceCondition]
        """
        

        self._assistance_conditions = assistance_conditions

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

