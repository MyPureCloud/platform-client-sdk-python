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
    from . import PostInputContract
    from . import PostOutputContract

class ActionContractInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ActionContractInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'input': 'PostInputContract',
            'output': 'PostOutputContract'
        }

        self.attribute_map = {
            'input': 'input',
            'output': 'output'
        }

        self._input = None
        self._output = None

    @property
    def input(self) -> 'PostInputContract':
        """
        Gets the input of this ActionContractInput.
        Execution input contract

        :return: The input of this ActionContractInput.
        :rtype: PostInputContract
        """
        return self._input

    @input.setter
    def input(self, input: 'PostInputContract') -> None:
        """
        Sets the input of this ActionContractInput.
        Execution input contract

        :param input: The input of this ActionContractInput.
        :type: PostInputContract
        """
        

        self._input = input

    @property
    def output(self) -> 'PostOutputContract':
        """
        Gets the output of this ActionContractInput.
        Execution output contract

        :return: The output of this ActionContractInput.
        :rtype: PostOutputContract
        """
        return self._output

    @output.setter
    def output(self, output: 'PostOutputContract') -> None:
        """
        Sets the output of this ActionContractInput.
        Execution output contract

        :param output: The output of this ActionContractInput.
        :type: PostOutputContract
        """
        

        self._output = output

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

