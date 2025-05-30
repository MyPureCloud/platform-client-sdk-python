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
    from . import JourneyViewLinkTimeConstraint

class JourneyViewLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyViewLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'constraint_within': 'JourneyViewLinkTimeConstraint',
            'constraint_after': 'JourneyViewLinkTimeConstraint',
            'event_count_type': 'str',
            'join_attributes': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'constraint_within': 'constraintWithin',
            'constraint_after': 'constraintAfter',
            'event_count_type': 'eventCountType',
            'join_attributes': 'joinAttributes'
        }

        self._id = None
        self._constraint_within = None
        self._constraint_after = None
        self._event_count_type = None
        self._join_attributes = None

    @property
    def id(self) -> str:
        """
        Gets the id of this JourneyViewLink.
        The identifier of the element downstream

        :return: The id of this JourneyViewLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this JourneyViewLink.
        The identifier of the element downstream

        :param id: The id of this JourneyViewLink.
        :type: str
        """
        

        self._id = id

    @property
    def constraint_within(self) -> 'JourneyViewLinkTimeConstraint':
        """
        Gets the constraint_within of this JourneyViewLink.
        A time constraint on this link, which requires a customer to complete the downstream element within this amount of time to be counted.

        :return: The constraint_within of this JourneyViewLink.
        :rtype: JourneyViewLinkTimeConstraint
        """
        return self._constraint_within

    @constraint_within.setter
    def constraint_within(self, constraint_within: 'JourneyViewLinkTimeConstraint') -> None:
        """
        Sets the constraint_within of this JourneyViewLink.
        A time constraint on this link, which requires a customer to complete the downstream element within this amount of time to be counted.

        :param constraint_within: The constraint_within of this JourneyViewLink.
        :type: JourneyViewLinkTimeConstraint
        """
        

        self._constraint_within = constraint_within

    @property
    def constraint_after(self) -> 'JourneyViewLinkTimeConstraint':
        """
        Gets the constraint_after of this JourneyViewLink.
        A time constraint on this link, which requires a customer must complete the downstream element after this amount of time to be counted.

        :return: The constraint_after of this JourneyViewLink.
        :rtype: JourneyViewLinkTimeConstraint
        """
        return self._constraint_after

    @constraint_after.setter
    def constraint_after(self, constraint_after: 'JourneyViewLinkTimeConstraint') -> None:
        """
        Sets the constraint_after of this JourneyViewLink.
        A time constraint on this link, which requires a customer must complete the downstream element after this amount of time to be counted.

        :param constraint_after: The constraint_after of this JourneyViewLink.
        :type: JourneyViewLinkTimeConstraint
        """
        

        self._constraint_after = constraint_after

    @property
    def event_count_type(self) -> str:
        """
        Gets the event_count_type of this JourneyViewLink.
        The type of events that will be counted. Note: Concurrent will override any JourneyViewLinkTimeConstraint. Default is Sequential.

        :return: The event_count_type of this JourneyViewLink.
        :rtype: str
        """
        return self._event_count_type

    @event_count_type.setter
    def event_count_type(self, event_count_type: str) -> None:
        """
        Sets the event_count_type of this JourneyViewLink.
        The type of events that will be counted. Note: Concurrent will override any JourneyViewLinkTimeConstraint. Default is Sequential.

        :param event_count_type: The event_count_type of this JourneyViewLink.
        :type: str
        """
        if isinstance(event_count_type, int):
            event_count_type = str(event_count_type)
        allowed_values = ["All", "Concurrent", "Sequential"]
        if event_count_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for event_count_type -> " + event_count_type)
            self._event_count_type = "outdated_sdk_version"
        else:
            self._event_count_type = event_count_type

    @property
    def join_attributes(self) -> List[str]:
        """
        Gets the join_attributes of this JourneyViewLink.
        Other (secondary) attributes on which this link should join the customers being counted

        :return: The join_attributes of this JourneyViewLink.
        :rtype: list[str]
        """
        return self._join_attributes

    @join_attributes.setter
    def join_attributes(self, join_attributes: List[str]) -> None:
        """
        Sets the join_attributes of this JourneyViewLink.
        Other (secondary) attributes on which this link should join the customers being counted

        :param join_attributes: The join_attributes of this JourneyViewLink.
        :type: list[str]
        """
        

        self._join_attributes = join_attributes

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

