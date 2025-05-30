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
    from . import FlowHealthErrorInfo
    from . import FlowHealthIntentUtterance

class HealthInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        HealthInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'error_info': 'FlowHealthErrorInfo',
            'overall_score': 'float',
            'issue_count': 'int',
            'static_validation_results': 'list[str]',
            'utterances': 'list[FlowHealthIntentUtterance]'
        }

        self.attribute_map = {
            'status': 'status',
            'error_info': 'errorInfo',
            'overall_score': 'overallScore',
            'issue_count': 'issueCount',
            'static_validation_results': 'staticValidationResults',
            'utterances': 'utterances'
        }

        self._status = None
        self._error_info = None
        self._overall_score = None
        self._issue_count = None
        self._static_validation_results = None
        self._utterances = None

    @property
    def status(self) -> str:
        """
        Gets the status of this HealthInfo.
        Status of health computation for this intent.

        :return: The status of this HealthInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this HealthInfo.
        Status of health computation for this intent.

        :param status: The status of this HealthInfo.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["InProgress", "Completed", "Error"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def error_info(self) -> 'FlowHealthErrorInfo':
        """
        Gets the error_info of this HealthInfo.
        Error details for the intent, if any.

        :return: The error_info of this HealthInfo.
        :rtype: FlowHealthErrorInfo
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info: 'FlowHealthErrorInfo') -> None:
        """
        Sets the error_info of this HealthInfo.
        Error details for the intent, if any.

        :param error_info: The error_info of this HealthInfo.
        :type: FlowHealthErrorInfo
        """
        

        self._error_info = error_info

    @property
    def overall_score(self) -> float:
        """
        Gets the overall_score of this HealthInfo.
        Overall health score for the intent ranged between 0 and 100 as 100 is the perfect health score.

        :return: The overall_score of this HealthInfo.
        :rtype: float
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score: float) -> None:
        """
        Sets the overall_score of this HealthInfo.
        Overall health score for the intent ranged between 0 and 100 as 100 is the perfect health score.

        :param overall_score: The overall_score of this HealthInfo.
        :type: float
        """
        

        self._overall_score = overall_score

    @property
    def issue_count(self) -> int:
        """
        Gets the issue_count of this HealthInfo.
        Number of issues found in the intent.

        :return: The issue_count of this HealthInfo.
        :rtype: int
        """
        return self._issue_count

    @issue_count.setter
    def issue_count(self, issue_count: int) -> None:
        """
        Sets the issue_count of this HealthInfo.
        Number of issues found in the intent.

        :param issue_count: The issue_count of this HealthInfo.
        :type: int
        """
        

        self._issue_count = issue_count

    @property
    def static_validation_results(self) -> List[str]:
        """
        Gets the static_validation_results of this HealthInfo.
        Validation results for the intent.

        :return: The static_validation_results of this HealthInfo.
        :rtype: list[str]
        """
        return self._static_validation_results

    @static_validation_results.setter
    def static_validation_results(self, static_validation_results: List[str]) -> None:
        """
        Sets the static_validation_results of this HealthInfo.
        Validation results for the intent.

        :param static_validation_results: The static_validation_results of this HealthInfo.
        :type: list[str]
        """
        

        self._static_validation_results = static_validation_results

    @property
    def utterances(self) -> List['FlowHealthIntentUtterance']:
        """
        Gets the utterances of this HealthInfo.
        Utterances for this intent.

        :return: The utterances of this HealthInfo.
        :rtype: list[FlowHealthIntentUtterance]
        """
        return self._utterances

    @utterances.setter
    def utterances(self, utterances: List['FlowHealthIntentUtterance']) -> None:
        """
        Sets the utterances of this HealthInfo.
        Utterances for this intent.

        :param utterances: The utterances of this HealthInfo.
        :type: list[FlowHealthIntentUtterance]
        """
        

        self._utterances = utterances

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

