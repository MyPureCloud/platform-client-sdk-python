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

class SmsProvisioningStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SmsProvisioningStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'state': 'str',
            'error': 'ErrorBody',
            'version': 'int'
        }

        self.attribute_map = {
            'action': 'action',
            'state': 'state',
            'error': 'error',
            'version': 'version'
        }

        self._action = None
        self._state = None
        self._error = None
        self._version = None

    @property
    def action(self):
        """
        Gets the action of this SmsProvisioningStatus.
        Provisioning action

        :return: The action of this SmsProvisioningStatus.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this SmsProvisioningStatus.
        Provisioning action

        :param action: The action of this SmsProvisioningStatus.
        :type: str
        """
        allowed_values = ["Unknown", "Create", "Update", "Delete"]
        if action.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action -> " + action)
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def state(self):
        """
        Gets the state of this SmsProvisioningStatus.
        Provisioning state

        :return: The state of this SmsProvisioningStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this SmsProvisioningStatus.
        Provisioning state

        :param state: The state of this SmsProvisioningStatus.
        :type: str
        """
        allowed_values = ["Running", "Completed", "Failed"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def error(self):
        """
        Gets the error of this SmsProvisioningStatus.
        Any error associated with a Failed state

        :return: The error of this SmsProvisioningStatus.
        :rtype: ErrorBody
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this SmsProvisioningStatus.
        Any error associated with a Failed state

        :param error: The error of this SmsProvisioningStatus.
        :type: ErrorBody
        """
        
        self._error = error

    @property
    def version(self):
        """
        Gets the version of this SmsProvisioningStatus.
        The phone number version associated with the provisioning action

        :return: The version of this SmsProvisioningStatus.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SmsProvisioningStatus.
        The phone number version associated with the provisioning action

        :param version: The version of this SmsProvisioningStatus.
        :type: int
        """
        
        self._version = version

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
