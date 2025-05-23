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
    from . import FlowPathsElement

class FlowPaths(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowPaths - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'date_start': 'datetime',
            'date_end': 'datetime',
            'elements': 'dict(str, FlowPathsElement)'
        }

        self.attribute_map = {
            'category': 'category',
            'date_start': 'dateStart',
            'date_end': 'dateEnd',
            'elements': 'elements'
        }

        self._category = None
        self._date_start = None
        self._date_end = None
        self._elements = None

    @property
    def category(self) -> str:
        """
        Gets the category of this FlowPaths.
        Category (use case) of the paths within a given domain.

        :return: The category of this FlowPaths.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Sets the category of this FlowPaths.
        Category (use case) of the paths within a given domain.

        :param category: The category of this FlowPaths.
        :type: str
        """
        if isinstance(category, int):
            category = str(category)
        allowed_values = ["All", "Abandoned", "AgentEscalation", "Complete", "Disconnect", "Error", "RecognitionFailure", "Transfer"]
        if category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for category -> " + category)
            self._category = "outdated_sdk_version"
        else:
            self._category = category

    @property
    def date_start(self) -> datetime:
        """
        Gets the date_start of this FlowPaths.
        Start date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_start of this FlowPaths.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: datetime) -> None:
        """
        Sets the date_start of this FlowPaths.
        Start date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_start: The date_start of this FlowPaths.
        :type: datetime
        """
        

        self._date_start = date_start

    @property
    def date_end(self) -> datetime:
        """
        Gets the date_end of this FlowPaths.
        End date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_end of this FlowPaths.
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end: datetime) -> None:
        """
        Sets the date_end of this FlowPaths.
        End date of the date range included in the flow paths data. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_end: The date_end of this FlowPaths.
        :type: datetime
        """
        

        self._date_end = date_end

    @property
    def elements(self) -> Dict[str, 'FlowPathsElement']:
        """
        Gets the elements of this FlowPaths.
        Unique element identifiers and their corresponding elements in the trie data structure representing the paths.

        :return: The elements of this FlowPaths.
        :rtype: dict(str, FlowPathsElement)
        """
        return self._elements

    @elements.setter
    def elements(self, elements: Dict[str, 'FlowPathsElement']) -> None:
        """
        Sets the elements of this FlowPaths.
        Unique element identifiers and their corresponding elements in the trie data structure representing the paths.

        :param elements: The elements of this FlowPaths.
        :type: dict(str, FlowPathsElement)
        """
        

        self._elements = elements

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

