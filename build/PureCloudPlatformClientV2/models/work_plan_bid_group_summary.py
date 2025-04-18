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
    from . import ManagementUnitReference

class WorkPlanBidGroupSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkPlanBidGroupSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'management_unit': 'ManagementUnitReference',
            'agent_count': 'int',
            'work_plan_count': 'int',
            'planning_group_count': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'management_unit': 'managementUnit',
            'agent_count': 'agentCount',
            'work_plan_count': 'workPlanCount',
            'planning_group_count': 'planningGroupCount',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._management_unit = None
        self._agent_count = None
        self._work_plan_count = None
        self._planning_group_count = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WorkPlanBidGroupSummary.
        The globally unique identifier for the object.

        :return: The id of this WorkPlanBidGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WorkPlanBidGroupSummary.
        The globally unique identifier for the object.

        :param id: The id of this WorkPlanBidGroupSummary.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this WorkPlanBidGroupSummary.
        The name assigned to this bid group

        :return: The name of this WorkPlanBidGroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WorkPlanBidGroupSummary.
        The name assigned to this bid group

        :param name: The name of this WorkPlanBidGroupSummary.
        :type: str
        """
        

        self._name = name

    @property
    def management_unit(self) -> 'ManagementUnitReference':
        """
        Gets the management_unit of this WorkPlanBidGroupSummary.
        The management unit this bid group belongs to

        :return: The management_unit of this WorkPlanBidGroupSummary.
        :rtype: ManagementUnitReference
        """
        return self._management_unit

    @management_unit.setter
    def management_unit(self, management_unit: 'ManagementUnitReference') -> None:
        """
        Sets the management_unit of this WorkPlanBidGroupSummary.
        The management unit this bid group belongs to

        :param management_unit: The management_unit of this WorkPlanBidGroupSummary.
        :type: ManagementUnitReference
        """
        

        self._management_unit = management_unit

    @property
    def agent_count(self) -> int:
        """
        Gets the agent_count of this WorkPlanBidGroupSummary.
        The number of agents in this bid group

        :return: The agent_count of this WorkPlanBidGroupSummary.
        :rtype: int
        """
        return self._agent_count

    @agent_count.setter
    def agent_count(self, agent_count: int) -> None:
        """
        Sets the agent_count of this WorkPlanBidGroupSummary.
        The number of agents in this bid group

        :param agent_count: The agent_count of this WorkPlanBidGroupSummary.
        :type: int
        """
        

        self._agent_count = agent_count

    @property
    def work_plan_count(self) -> int:
        """
        Gets the work_plan_count of this WorkPlanBidGroupSummary.
        The number of work plans in this bid group

        :return: The work_plan_count of this WorkPlanBidGroupSummary.
        :rtype: int
        """
        return self._work_plan_count

    @work_plan_count.setter
    def work_plan_count(self, work_plan_count: int) -> None:
        """
        Sets the work_plan_count of this WorkPlanBidGroupSummary.
        The number of work plans in this bid group

        :param work_plan_count: The work_plan_count of this WorkPlanBidGroupSummary.
        :type: int
        """
        

        self._work_plan_count = work_plan_count

    @property
    def planning_group_count(self) -> int:
        """
        Gets the planning_group_count of this WorkPlanBidGroupSummary.
        The number of planning groups in this bid group

        :return: The planning_group_count of this WorkPlanBidGroupSummary.
        :rtype: int
        """
        return self._planning_group_count

    @planning_group_count.setter
    def planning_group_count(self, planning_group_count: int) -> None:
        """
        Sets the planning_group_count of this WorkPlanBidGroupSummary.
        The number of planning groups in this bid group

        :param planning_group_count: The planning_group_count of this WorkPlanBidGroupSummary.
        :type: int
        """
        

        self._planning_group_count = planning_group_count

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this WorkPlanBidGroupSummary.
        The URI for this object

        :return: The self_uri of this WorkPlanBidGroupSummary.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this WorkPlanBidGroupSummary.
        The URI for this object

        :param self_uri: The self_uri of this WorkPlanBidGroupSummary.
        :type: str
        """
        

        self._self_uri = self_uri

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

