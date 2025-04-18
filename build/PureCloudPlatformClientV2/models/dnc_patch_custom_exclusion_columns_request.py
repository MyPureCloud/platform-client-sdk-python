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


class DncPatchCustomExclusionColumnsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DncPatchCustomExclusionColumnsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'custom_exclusion_column_entries': 'list[str]',
            'expiration_date_time': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'custom_exclusion_column_entries': 'customExclusionColumnEntries',
            'expiration_date_time': 'expirationDateTime'
        }

        self._action = None
        self._custom_exclusion_column_entries = None
        self._expiration_date_time = None

    @property
    def action(self) -> str:
        """
        Gets the action of this DncPatchCustomExclusionColumnsRequest.
        The action to perform

        :return: The action of this DncPatchCustomExclusionColumnsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        """
        Sets the action of this DncPatchCustomExclusionColumnsRequest.
        The action to perform

        :param action: The action of this DncPatchCustomExclusionColumnsRequest.
        :type: str
        """
        if isinstance(action, int):
            action = str(action)
        allowed_values = ["Add", "Remove"]
        if action.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action -> " + action)
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def custom_exclusion_column_entries(self) -> List[str]:
        """
        Gets the custom_exclusion_column_entries of this DncPatchCustomExclusionColumnsRequest.
        The list of custom exclusion column entries to Add to / Remove from the DNC list 

        :return: The custom_exclusion_column_entries of this DncPatchCustomExclusionColumnsRequest.
        :rtype: list[str]
        """
        return self._custom_exclusion_column_entries

    @custom_exclusion_column_entries.setter
    def custom_exclusion_column_entries(self, custom_exclusion_column_entries: List[str]) -> None:
        """
        Sets the custom_exclusion_column_entries of this DncPatchCustomExclusionColumnsRequest.
        The list of custom exclusion column entries to Add to / Remove from the DNC list 

        :param custom_exclusion_column_entries: The custom_exclusion_column_entries of this DncPatchCustomExclusionColumnsRequest.
        :type: list[str]
        """
        

        self._custom_exclusion_column_entries = custom_exclusion_column_entries

    @property
    def expiration_date_time(self) -> str:
        """
        Gets the expiration_date_time of this DncPatchCustomExclusionColumnsRequest.
        Expiration date for DNC customExclusionColumnEntries in yyyy-MM-ddTHH:mmZ format

        :return: The expiration_date_time of this DncPatchCustomExclusionColumnsRequest.
        :rtype: str
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time: str) -> None:
        """
        Sets the expiration_date_time of this DncPatchCustomExclusionColumnsRequest.
        Expiration date for DNC customExclusionColumnEntries in yyyy-MM-ddTHH:mmZ format

        :param expiration_date_time: The expiration_date_time of this DncPatchCustomExclusionColumnsRequest.
        :type: str
        """
        

        self._expiration_date_time = expiration_date_time

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

