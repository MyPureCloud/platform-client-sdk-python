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


class TransferToAddressRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TransferToAddressRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'transfer_type': 'str',
            'keep_internal_message_alive': 'bool',
            'address': 'str'
        }

        self.attribute_map = {
            'transfer_type': 'transferType',
            'keep_internal_message_alive': 'keepInternalMessageAlive',
            'address': 'address'
        }

        self._transfer_type = None
        self._keep_internal_message_alive = None
        self._address = None

    @property
    def transfer_type(self) -> str:
        """
        Gets the transfer_type of this TransferToAddressRequest.
        The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended.

        :return: The transfer_type of this TransferToAddressRequest.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type: str) -> None:
        """
        Sets the transfer_type of this TransferToAddressRequest.
        The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended.

        :param transfer_type: The transfer_type of this TransferToAddressRequest.
        :type: str
        """
        if isinstance(transfer_type, int):
            transfer_type = str(transfer_type)
        allowed_values = ["Attended", "Unattended"]
        if transfer_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for transfer_type -> " + transfer_type)
            self._transfer_type = "outdated_sdk_version"
        else:
            self._transfer_type = transfer_type

    @property
    def keep_internal_message_alive(self) -> bool:
        """
        Gets the keep_internal_message_alive of this TransferToAddressRequest.
        If true, the digital internal message will NOT be terminated.

        :return: The keep_internal_message_alive of this TransferToAddressRequest.
        :rtype: bool
        """
        return self._keep_internal_message_alive

    @keep_internal_message_alive.setter
    def keep_internal_message_alive(self, keep_internal_message_alive: bool) -> None:
        """
        Sets the keep_internal_message_alive of this TransferToAddressRequest.
        If true, the digital internal message will NOT be terminated.

        :param keep_internal_message_alive: The keep_internal_message_alive of this TransferToAddressRequest.
        :type: bool
        """
        

        self._keep_internal_message_alive = keep_internal_message_alive

    @property
    def address(self) -> str:
        """
        Gets the address of this TransferToAddressRequest.
        User's name, queue's name, destination's address or phone number.

        :return: The address of this TransferToAddressRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this TransferToAddressRequest.
        User's name, queue's name, destination's address or phone number.

        :param address: The address of this TransferToAddressRequest.
        :type: str
        """
        

        self._address = address

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

