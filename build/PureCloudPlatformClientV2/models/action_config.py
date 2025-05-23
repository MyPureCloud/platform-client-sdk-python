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
    from . import RequestConfig
    from . import ResponseConfig

class ActionConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ActionConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timeout_seconds': 'int',
            'request': 'RequestConfig',
            'response': 'ResponseConfig'
        }

        self.attribute_map = {
            'timeout_seconds': 'timeoutSeconds',
            'request': 'request',
            'response': 'response'
        }

        self._timeout_seconds = None
        self._request = None
        self._response = None

    @property
    def timeout_seconds(self) -> int:
        """
        Gets the timeout_seconds of this ActionConfig.
        Optional 1-60 second timeout enforced on the execution or test of this action. This setting is invalid for Custom Authentication Actions.

        :return: The timeout_seconds of this ActionConfig.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds: int) -> None:
        """
        Sets the timeout_seconds of this ActionConfig.
        Optional 1-60 second timeout enforced on the execution or test of this action. This setting is invalid for Custom Authentication Actions.

        :param timeout_seconds: The timeout_seconds of this ActionConfig.
        :type: int
        """
        

        self._timeout_seconds = timeout_seconds

    @property
    def request(self) -> 'RequestConfig':
        """
        Gets the request of this ActionConfig.
        Configuration of outbound request.

        :return: The request of this ActionConfig.
        :rtype: RequestConfig
        """
        return self._request

    @request.setter
    def request(self, request: 'RequestConfig') -> None:
        """
        Sets the request of this ActionConfig.
        Configuration of outbound request.

        :param request: The request of this ActionConfig.
        :type: RequestConfig
        """
        

        self._request = request

    @property
    def response(self) -> 'ResponseConfig':
        """
        Gets the response of this ActionConfig.
        Configuration of response processing.

        :return: The response of this ActionConfig.
        :rtype: ResponseConfig
        """
        return self._response

    @response.setter
    def response(self, response: 'ResponseConfig') -> None:
        """
        Sets the response of this ActionConfig.
        Configuration of response processing.

        :param response: The response of this ActionConfig.
        :type: ResponseConfig
        """
        

        self._response = response

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

