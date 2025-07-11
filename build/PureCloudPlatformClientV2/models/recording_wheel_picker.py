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
    from . import RecordingWheelPickerItem

class RecordingWheelPicker(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        RecordingWheelPicker - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'items': 'list[RecordingWheelPickerItem]'
        }

        self.attribute_map = {
            'id': 'id',
            'items': 'items'
        }

        self._id = None
        self._items = None

    @property
    def id(self) -> str:
        """
        Gets the id of this RecordingWheelPicker.
        Optional unique identifier to help map component replies to form messages where multiple Wheel Pickers can be present.

        :return: The id of this RecordingWheelPicker.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this RecordingWheelPicker.
        Optional unique identifier to help map component replies to form messages where multiple Wheel Pickers can be present.

        :param id: The id of this RecordingWheelPicker.
        :type: str
        """
        

        self._id = id

    @property
    def items(self) -> List['RecordingWheelPickerItem']:
        """
        Gets the items of this RecordingWheelPicker.
        An array of options in the Wheel Picker.

        :return: The items of this RecordingWheelPicker.
        :rtype: list[RecordingWheelPickerItem]
        """
        return self._items

    @items.setter
    def items(self, items: List['RecordingWheelPickerItem']) -> None:
        """
        Sets the items of this RecordingWheelPicker.
        An array of options in the Wheel Picker.

        :param items: The items of this RecordingWheelPicker.
        :type: list[RecordingWheelPickerItem]
        """
        

        self._items = items

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

