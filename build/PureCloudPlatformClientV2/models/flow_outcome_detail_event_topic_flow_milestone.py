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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict


class FlowOutcomeDetailEventTopicFlowMilestone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowOutcomeDetailEventTopicFlowMilestone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'milestone_id': 'str',
            'milestone_time': 'int'
        }

        self.attribute_map = {
            'milestone_id': 'milestoneId',
            'milestone_time': 'milestoneTime'
        }

        self._milestone_id = None
        self._milestone_time = None

    @property
    def milestone_id(self) -> str:
        """
        Gets the milestone_id of this FlowOutcomeDetailEventTopicFlowMilestone.


        :return: The milestone_id of this FlowOutcomeDetailEventTopicFlowMilestone.
        :rtype: str
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id: str) -> None:
        """
        Sets the milestone_id of this FlowOutcomeDetailEventTopicFlowMilestone.


        :param milestone_id: The milestone_id of this FlowOutcomeDetailEventTopicFlowMilestone.
        :type: str
        """
        

        self._milestone_id = milestone_id

    @property
    def milestone_time(self) -> int:
        """
        Gets the milestone_time of this FlowOutcomeDetailEventTopicFlowMilestone.


        :return: The milestone_time of this FlowOutcomeDetailEventTopicFlowMilestone.
        :rtype: int
        """
        return self._milestone_time

    @milestone_time.setter
    def milestone_time(self, milestone_time: int) -> None:
        """
        Sets the milestone_time of this FlowOutcomeDetailEventTopicFlowMilestone.


        :param milestone_time: The milestone_time of this FlowOutcomeDetailEventTopicFlowMilestone.
        :type: int
        """
        

        self._milestone_time = milestone_time

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
