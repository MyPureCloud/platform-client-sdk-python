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
    from . import PerformancePredictionRecalculationCompleteEventTopicErrorBody

class PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operation_id': 'str',
            'download_url': 'str',
            'state': 'str',
            'error': 'PerformancePredictionRecalculationCompleteEventTopicErrorBody'
        }

        self.attribute_map = {
            'operation_id': 'operationId',
            'download_url': 'downloadUrl',
            'state': 'state',
            'error': 'error'
        }

        self._operation_id = None
        self._download_url = None
        self._state = None
        self._error = None

    @property
    def operation_id(self) -> str:
        """
        Gets the operation_id of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :return: The operation_id of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id: str) -> None:
        """
        Sets the operation_id of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :param operation_id: The operation_id of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :type: str
        """
        

        self._operation_id = operation_id

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :return: The download_url of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :param download_url: The download_url of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def state(self) -> str:
        """
        Gets the state of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :return: The state of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :param state: The state of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Processing", "Complete", "Canceled", "Error"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def error(self) -> 'PerformancePredictionRecalculationCompleteEventTopicErrorBody':
        """
        Gets the error of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :return: The error of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :rtype: PerformancePredictionRecalculationCompleteEventTopicErrorBody
        """
        return self._error

    @error.setter
    def error(self, error: 'PerformancePredictionRecalculationCompleteEventTopicErrorBody') -> None:
        """
        Sets the error of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.


        :param error: The error of this PerformancePredictionRecalculationCompleteEventTopicPerformancePredictionUserRecalculationNotification.
        :type: PerformancePredictionRecalculationCompleteEventTopicErrorBody
        """
        

        self._error = error

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

