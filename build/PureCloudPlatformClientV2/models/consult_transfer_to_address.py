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


class ConsultTransferToAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConsultTransferToAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'speak_to': 'str',
            'consulting_user_id': 'str',
            'address': 'str'
        }

        self.attribute_map = {
            'speak_to': 'speakTo',
            'consulting_user_id': 'consultingUserId',
            'address': 'address'
        }

        self._speak_to = None
        self._consulting_user_id = None
        self._address = None

    @property
    def speak_to(self) -> str:
        """
        Gets the speak_to of this ConsultTransferToAddress.
        Determines to whom the initiating participant is requesting to speak. Defaults to DESTINATION

        :return: The speak_to of this ConsultTransferToAddress.
        :rtype: str
        """
        return self._speak_to

    @speak_to.setter
    def speak_to(self, speak_to: str) -> None:
        """
        Sets the speak_to of this ConsultTransferToAddress.
        Determines to whom the initiating participant is requesting to speak. Defaults to DESTINATION

        :param speak_to: The speak_to of this ConsultTransferToAddress.
        :type: str
        """
        if isinstance(speak_to, int):
            speak_to = str(speak_to)
        allowed_values = ["DESTINATION", "OBJECT", "BOTH", "CONFERENCE"]
        if speak_to.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for speak_to -> " + speak_to)
            self._speak_to = "outdated_sdk_version"
        else:
            self._speak_to = speak_to

    @property
    def consulting_user_id(self) -> str:
        """
        Gets the consulting_user_id of this ConsultTransferToAddress.
        The user ID of the person who wants to talk before completing the transfer. Could be the same of the context user ID

        :return: The consulting_user_id of this ConsultTransferToAddress.
        :rtype: str
        """
        return self._consulting_user_id

    @consulting_user_id.setter
    def consulting_user_id(self, consulting_user_id: str) -> None:
        """
        Sets the consulting_user_id of this ConsultTransferToAddress.
        The user ID of the person who wants to talk before completing the transfer. Could be the same of the context user ID

        :param consulting_user_id: The consulting_user_id of this ConsultTransferToAddress.
        :type: str
        """
        

        self._consulting_user_id = consulting_user_id

    @property
    def address(self) -> str:
        """
        Gets the address of this ConsultTransferToAddress.
        Destination's address or phone number.

        :return: The address of this ConsultTransferToAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this ConsultTransferToAddress.
        Destination's address or phone number.

        :param address: The address of this ConsultTransferToAddress.
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

