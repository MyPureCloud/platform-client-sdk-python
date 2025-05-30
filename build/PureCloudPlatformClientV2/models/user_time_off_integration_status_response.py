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
    from . import TimeOffRequestReference
    from . import UserReference

class UserTimeOffIntegrationStatusResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UserTimeOffIntegrationStatusResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time_off_request': 'TimeOffRequestReference',
            'integration_status': 'str',
            'user': 'UserReference'
        }

        self.attribute_map = {
            'time_off_request': 'timeOffRequest',
            'integration_status': 'integrationStatus',
            'user': 'user'
        }

        self._time_off_request = None
        self._integration_status = None
        self._user = None

    @property
    def time_off_request(self) -> 'TimeOffRequestReference':
        """
        Gets the time_off_request of this UserTimeOffIntegrationStatusResponse.
        The time off request associated with this integration status

        :return: The time_off_request of this UserTimeOffIntegrationStatusResponse.
        :rtype: TimeOffRequestReference
        """
        return self._time_off_request

    @time_off_request.setter
    def time_off_request(self, time_off_request: 'TimeOffRequestReference') -> None:
        """
        Sets the time_off_request of this UserTimeOffIntegrationStatusResponse.
        The time off request associated with this integration status

        :param time_off_request: The time_off_request of this UserTimeOffIntegrationStatusResponse.
        :type: TimeOffRequestReference
        """
        

        self._time_off_request = time_off_request

    @property
    def integration_status(self) -> str:
        """
        Gets the integration_status of this UserTimeOffIntegrationStatusResponse.
        The value of integration status for the time off request

        :return: The integration_status of this UserTimeOffIntegrationStatusResponse.
        :rtype: str
        """
        return self._integration_status

    @integration_status.setter
    def integration_status(self, integration_status: str) -> None:
        """
        Sets the integration_status of this UserTimeOffIntegrationStatusResponse.
        The value of integration status for the time off request

        :param integration_status: The integration_status of this UserTimeOffIntegrationStatusResponse.
        :type: str
        """
        if isinstance(integration_status, int):
            integration_status = str(integration_status)
        allowed_values = ["Processing", "Error", "AutomaticallyComplete", "ManuallyComplete"]
        if integration_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for integration_status -> " + integration_status)
            self._integration_status = "outdated_sdk_version"
        else:
            self._integration_status = integration_status

    @property
    def user(self) -> 'UserReference':
        """
        Gets the user of this UserTimeOffIntegrationStatusResponse.
        The user to whom the time off request belongs

        :return: The user of this UserTimeOffIntegrationStatusResponse.
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user: 'UserReference') -> None:
        """
        Sets the user of this UserTimeOffIntegrationStatusResponse.
        The user to whom the time off request belongs

        :param user: The user of this UserTimeOffIntegrationStatusResponse.
        :type: UserReference
        """
        

        self._user = user

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

