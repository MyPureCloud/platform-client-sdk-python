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


class AgentBidWorkPlanOverrideRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentBidWorkPlanOverrideRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agent_id': 'str',
            'override_work_plan_id': 'str',
            'override_reason': 'str'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'override_work_plan_id': 'overrideWorkPlanId',
            'override_reason': 'overrideReason'
        }

        self._agent_id = None
        self._override_work_plan_id = None
        self._override_reason = None

    @property
    def agent_id(self) -> str:
        """
        Gets the agent_id of this AgentBidWorkPlanOverrideRequest.
        The ID of agent

        :return: The agent_id of this AgentBidWorkPlanOverrideRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id: str) -> None:
        """
        Sets the agent_id of this AgentBidWorkPlanOverrideRequest.
        The ID of agent

        :param agent_id: The agent_id of this AgentBidWorkPlanOverrideRequest.
        :type: str
        """
        

        self._agent_id = agent_id

    @property
    def override_work_plan_id(self) -> str:
        """
        Gets the override_work_plan_id of this AgentBidWorkPlanOverrideRequest.
        The ID of the work plan that overrides the assigned work plan for the agent

        :return: The override_work_plan_id of this AgentBidWorkPlanOverrideRequest.
        :rtype: str
        """
        return self._override_work_plan_id

    @override_work_plan_id.setter
    def override_work_plan_id(self, override_work_plan_id: str) -> None:
        """
        Sets the override_work_plan_id of this AgentBidWorkPlanOverrideRequest.
        The ID of the work plan that overrides the assigned work plan for the agent

        :param override_work_plan_id: The override_work_plan_id of this AgentBidWorkPlanOverrideRequest.
        :type: str
        """
        

        self._override_work_plan_id = override_work_plan_id

    @property
    def override_reason(self) -> str:
        """
        Gets the override_reason of this AgentBidWorkPlanOverrideRequest.
        The reason for overriding the assigned work plan. This must be null if overrideWorkPlanId is not specified

        :return: The override_reason of this AgentBidWorkPlanOverrideRequest.
        :rtype: str
        """
        return self._override_reason

    @override_reason.setter
    def override_reason(self, override_reason: str) -> None:
        """
        Sets the override_reason of this AgentBidWorkPlanOverrideRequest.
        The reason for overriding the assigned work plan. This must be null if overrideWorkPlanId is not specified

        :param override_reason: The override_reason of this AgentBidWorkPlanOverrideRequest.
        :type: str
        """
        if isinstance(override_reason, int):
            override_reason = str(override_reason)
        allowed_values = ["UnableToBid", "ChangeOfCircumstance", "NewHire", "EmployeeMove"]
        if override_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for override_reason -> " + override_reason)
            self._override_reason = "outdated_sdk_version"
        else:
            self._override_reason = override_reason

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

