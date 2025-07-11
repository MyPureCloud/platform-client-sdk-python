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


class DecisionTableRowExecutionOutput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DecisionTableRowExecutionOutput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'row_id': 'str',
            'row_index': 'int',
            'outputs': 'dict(str, object)'
        }

        self.attribute_map = {
            'row_id': 'rowId',
            'row_index': 'rowIndex',
            'outputs': 'outputs'
        }

        self._row_id = None
        self._row_index = None
        self._outputs = None

    @property
    def row_id(self) -> str:
        """
        Gets the row_id of this DecisionTableRowExecutionOutput.
        Unique rule identifier.

        :return: The row_id of this DecisionTableRowExecutionOutput.
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id: str) -> None:
        """
        Sets the row_id of this DecisionTableRowExecutionOutput.
        Unique rule identifier.

        :param row_id: The row_id of this DecisionTableRowExecutionOutput.
        :type: str
        """
        

        self._row_id = row_id

    @property
    def row_index(self) -> int:
        """
        Gets the row_index of this DecisionTableRowExecutionOutput.
        Unique rule identifier.

        :return: The row_index of this DecisionTableRowExecutionOutput.
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index: int) -> None:
        """
        Sets the row_index of this DecisionTableRowExecutionOutput.
        Unique rule identifier.

        :param row_index: The row_index of this DecisionTableRowExecutionOutput.
        :type: int
        """
        

        self._row_index = row_index

    @property
    def outputs(self) -> Dict[str, object]:
        """
        Gets the outputs of this DecisionTableRowExecutionOutput.
        The JSON output produced by this rule. Valid according to the execution output contract. In the case of enum decision table output columns, the enum options key will be provided as the value, not the enum options label as this can be changed. For business rules queue columns both “queue” and “id” keys will always be returned  regardless of the business rules queue attribute key and these do not change.

        :return: The outputs of this DecisionTableRowExecutionOutput.
        :rtype: dict(str, object)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs: Dict[str, object]) -> None:
        """
        Sets the outputs of this DecisionTableRowExecutionOutput.
        The JSON output produced by this rule. Valid according to the execution output contract. In the case of enum decision table output columns, the enum options key will be provided as the value, not the enum options label as this can be changed. For business rules queue columns both “queue” and “id” keys will always be returned  regardless of the business rules queue attribute key and these do not change.

        :param outputs: The outputs of this DecisionTableRowExecutionOutput.
        :type: dict(str, object)
        """
        

        self._outputs = outputs

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

