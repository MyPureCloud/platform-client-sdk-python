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
    from . import Detail
    from . import DomainEntityRef
    from . import User

class Operation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Operation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'complete': 'bool',
            'user': 'User',
            'client': 'DomainEntityRef',
            'error_message': 'str',
            'error_code': 'str',
            'error_details': 'list[Detail]',
            'error_message_params': 'dict(str, str)',
            'action_name': 'str',
            'action_status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'complete': 'complete',
            'user': 'user',
            'client': 'client',
            'error_message': 'errorMessage',
            'error_code': 'errorCode',
            'error_details': 'errorDetails',
            'error_message_params': 'errorMessageParams',
            'action_name': 'actionName',
            'action_status': 'actionStatus'
        }

        self._id = None
        self._complete = None
        self._user = None
        self._client = None
        self._error_message = None
        self._error_code = None
        self._error_details = None
        self._error_message_params = None
        self._action_name = None
        self._action_status = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Operation.


        :return: The id of this Operation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Operation.


        :param id: The id of this Operation.
        :type: str
        """
        

        self._id = id

    @property
    def complete(self) -> bool:
        """
        Gets the complete of this Operation.


        :return: The complete of this Operation.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete: bool) -> None:
        """
        Sets the complete of this Operation.


        :param complete: The complete of this Operation.
        :type: bool
        """
        

        self._complete = complete

    @property
    def user(self) -> 'User':
        """
        Gets the user of this Operation.


        :return: The user of this Operation.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: 'User') -> None:
        """
        Sets the user of this Operation.


        :param user: The user of this Operation.
        :type: User
        """
        

        self._user = user

    @property
    def client(self) -> 'DomainEntityRef':
        """
        Gets the client of this Operation.


        :return: The client of this Operation.
        :rtype: DomainEntityRef
        """
        return self._client

    @client.setter
    def client(self, client: 'DomainEntityRef') -> None:
        """
        Sets the client of this Operation.


        :param client: The client of this Operation.
        :type: DomainEntityRef
        """
        

        self._client = client

    @property
    def error_message(self) -> str:
        """
        Gets the error_message of this Operation.


        :return: The error_message of this Operation.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message: str) -> None:
        """
        Sets the error_message of this Operation.


        :param error_message: The error_message of this Operation.
        :type: str
        """
        

        self._error_message = error_message

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this Operation.


        :return: The error_code of this Operation.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this Operation.


        :param error_code: The error_code of this Operation.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def error_details(self) -> List['Detail']:
        """
        Gets the error_details of this Operation.


        :return: The error_details of this Operation.
        :rtype: list[Detail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details: List['Detail']) -> None:
        """
        Sets the error_details of this Operation.


        :param error_details: The error_details of this Operation.
        :type: list[Detail]
        """
        

        self._error_details = error_details

    @property
    def error_message_params(self) -> Dict[str, str]:
        """
        Gets the error_message_params of this Operation.


        :return: The error_message_params of this Operation.
        :rtype: dict(str, str)
        """
        return self._error_message_params

    @error_message_params.setter
    def error_message_params(self, error_message_params: Dict[str, str]) -> None:
        """
        Sets the error_message_params of this Operation.


        :param error_message_params: The error_message_params of this Operation.
        :type: dict(str, str)
        """
        

        self._error_message_params = error_message_params

    @property
    def action_name(self) -> str:
        """
        Gets the action_name of this Operation.
        Action name

        :return: The action_name of this Operation.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name: str) -> None:
        """
        Sets the action_name of this Operation.
        Action name

        :param action_name: The action_name of this Operation.
        :type: str
        """
        if isinstance(action_name, int):
            action_name = str(action_name)
        allowed_values = ["CREATE", "CHECKIN", "CHECKOUT", "DEBUG", "DELETE", "HISTORY", "PUBLISH", "REVERT", "SAVE", "STATE_CHANGE", "UPDATE", "VALIDATE"]
        if action_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action_name -> " + action_name)
            self._action_name = "outdated_sdk_version"
        else:
            self._action_name = action_name

    @property
    def action_status(self) -> str:
        """
        Gets the action_status of this Operation.
        Action status

        :return: The action_status of this Operation.
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status: str) -> None:
        """
        Sets the action_status of this Operation.
        Action status

        :param action_status: The action_status of this Operation.
        :type: str
        """
        if isinstance(action_status, int):
            action_status = str(action_status)
        allowed_values = ["LOCKED", "UNLOCKED", "STARTED", "PENDING_GENERATION", "PENDING_BACKEND_NOTIFICATION", "SUCCESS", "FAILURE"]
        if action_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action_status -> " + action_status)
            self._action_status = "outdated_sdk_version"
        else:
            self._action_status = action_status

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

