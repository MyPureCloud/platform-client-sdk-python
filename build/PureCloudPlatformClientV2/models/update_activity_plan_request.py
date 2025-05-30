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
    from . import ListWrapperFixedAvailability
    from . import ValueWrapperActivityPlanServiceGoalImpactOverrides
    from . import ValueWrapperGroupSettings
    from . import ValueWrapperUserSearchRule

class UpdateActivityPlanRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UpdateActivityPlanRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'group_settings': 'ValueWrapperGroupSettings',
            'attendees_search_rule': 'ValueWrapperUserSearchRule',
            'facilitators_search_rule': 'ValueWrapperUserSearchRule',
            'transition_time_minutes': 'int',
            'service_goal_impact_overrides': 'ValueWrapperActivityPlanServiceGoalImpactOverrides',
            'optimization_objective': 'str',
            'state': 'str',
            'fixed_availability': 'ListWrapperFixedAvailability'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'group_settings': 'groupSettings',
            'attendees_search_rule': 'attendeesSearchRule',
            'facilitators_search_rule': 'facilitatorsSearchRule',
            'transition_time_minutes': 'transitionTimeMinutes',
            'service_goal_impact_overrides': 'serviceGoalImpactOverrides',
            'optimization_objective': 'optimizationObjective',
            'state': 'state',
            'fixed_availability': 'fixedAvailability'
        }

        self._name = None
        self._description = None
        self._group_settings = None
        self._attendees_search_rule = None
        self._facilitators_search_rule = None
        self._transition_time_minutes = None
        self._service_goal_impact_overrides = None
        self._optimization_objective = None
        self._state = None
        self._fixed_availability = None

    @property
    def name(self) -> str:
        """
        Gets the name of this UpdateActivityPlanRequest.
        The name of the activity plan

        :return: The name of this UpdateActivityPlanRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this UpdateActivityPlanRequest.
        The name of the activity plan

        :param name: The name of this UpdateActivityPlanRequest.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this UpdateActivityPlanRequest.
        The description of the activity plan

        :return: The description of this UpdateActivityPlanRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this UpdateActivityPlanRequest.
        The description of the activity plan

        :param description: The description of this UpdateActivityPlanRequest.
        :type: str
        """
        

        self._description = description

    @property
    def group_settings(self) -> 'ValueWrapperGroupSettings':
        """
        Gets the group_settings of this UpdateActivityPlanRequest.
        Group settings for the activity plan

        :return: The group_settings of this UpdateActivityPlanRequest.
        :rtype: ValueWrapperGroupSettings
        """
        return self._group_settings

    @group_settings.setter
    def group_settings(self, group_settings: 'ValueWrapperGroupSettings') -> None:
        """
        Sets the group_settings of this UpdateActivityPlanRequest.
        Group settings for the activity plan

        :param group_settings: The group_settings of this UpdateActivityPlanRequest.
        :type: ValueWrapperGroupSettings
        """
        

        self._group_settings = group_settings

    @property
    def attendees_search_rule(self) -> 'ValueWrapperUserSearchRule':
        """
        Gets the attendees_search_rule of this UpdateActivityPlanRequest.
        Attendee search rule for this activity plan

        :return: The attendees_search_rule of this UpdateActivityPlanRequest.
        :rtype: ValueWrapperUserSearchRule
        """
        return self._attendees_search_rule

    @attendees_search_rule.setter
    def attendees_search_rule(self, attendees_search_rule: 'ValueWrapperUserSearchRule') -> None:
        """
        Sets the attendees_search_rule of this UpdateActivityPlanRequest.
        Attendee search rule for this activity plan

        :param attendees_search_rule: The attendees_search_rule of this UpdateActivityPlanRequest.
        :type: ValueWrapperUserSearchRule
        """
        

        self._attendees_search_rule = attendees_search_rule

    @property
    def facilitators_search_rule(self) -> 'ValueWrapperUserSearchRule':
        """
        Gets the facilitators_search_rule of this UpdateActivityPlanRequest.
        Facilitator search rule for this activity plan

        :return: The facilitators_search_rule of this UpdateActivityPlanRequest.
        :rtype: ValueWrapperUserSearchRule
        """
        return self._facilitators_search_rule

    @facilitators_search_rule.setter
    def facilitators_search_rule(self, facilitators_search_rule: 'ValueWrapperUserSearchRule') -> None:
        """
        Sets the facilitators_search_rule of this UpdateActivityPlanRequest.
        Facilitator search rule for this activity plan

        :param facilitators_search_rule: The facilitators_search_rule of this UpdateActivityPlanRequest.
        :type: ValueWrapperUserSearchRule
        """
        

        self._facilitators_search_rule = facilitators_search_rule

    @property
    def transition_time_minutes(self) -> int:
        """
        Gets the transition_time_minutes of this UpdateActivityPlanRequest.
        Transition time in minutes between facilitated sessions

        :return: The transition_time_minutes of this UpdateActivityPlanRequest.
        :rtype: int
        """
        return self._transition_time_minutes

    @transition_time_minutes.setter
    def transition_time_minutes(self, transition_time_minutes: int) -> None:
        """
        Sets the transition_time_minutes of this UpdateActivityPlanRequest.
        Transition time in minutes between facilitated sessions

        :param transition_time_minutes: The transition_time_minutes of this UpdateActivityPlanRequest.
        :type: int
        """
        

        self._transition_time_minutes = transition_time_minutes

    @property
    def service_goal_impact_overrides(self) -> 'ValueWrapperActivityPlanServiceGoalImpactOverrides':
        """
        Gets the service_goal_impact_overrides of this UpdateActivityPlanRequest.
        Allowable service goal impact override settings for this activity plan

        :return: The service_goal_impact_overrides of this UpdateActivityPlanRequest.
        :rtype: ValueWrapperActivityPlanServiceGoalImpactOverrides
        """
        return self._service_goal_impact_overrides

    @service_goal_impact_overrides.setter
    def service_goal_impact_overrides(self, service_goal_impact_overrides: 'ValueWrapperActivityPlanServiceGoalImpactOverrides') -> None:
        """
        Sets the service_goal_impact_overrides of this UpdateActivityPlanRequest.
        Allowable service goal impact override settings for this activity plan

        :param service_goal_impact_overrides: The service_goal_impact_overrides of this UpdateActivityPlanRequest.
        :type: ValueWrapperActivityPlanServiceGoalImpactOverrides
        """
        

        self._service_goal_impact_overrides = service_goal_impact_overrides

    @property
    def optimization_objective(self) -> str:
        """
        Gets the optimization_objective of this UpdateActivityPlanRequest.
        The optimization objective of this activity plan

        :return: The optimization_objective of this UpdateActivityPlanRequest.
        :rtype: str
        """
        return self._optimization_objective

    @optimization_objective.setter
    def optimization_objective(self, optimization_objective: str) -> None:
        """
        Sets the optimization_objective of this UpdateActivityPlanRequest.
        The optimization objective of this activity plan

        :param optimization_objective: The optimization_objective of this UpdateActivityPlanRequest.
        :type: str
        """
        if isinstance(optimization_objective, int):
            optimization_objective = str(optimization_objective)
        allowed_values = ["FavorServiceGoals", "FavorSchedulingAll"]
        if optimization_objective.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for optimization_objective -> " + optimization_objective)
            self._optimization_objective = "outdated_sdk_version"
        else:
            self._optimization_objective = optimization_objective

    @property
    def state(self) -> str:
        """
        Gets the state of this UpdateActivityPlanRequest.
        The state of this activity plan

        :return: The state of this UpdateActivityPlanRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this UpdateActivityPlanRequest.
        The state of this activity plan

        :param state: The state of this UpdateActivityPlanRequest.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Active", "Inactive"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def fixed_availability(self) -> 'ListWrapperFixedAvailability':
        """
        Gets the fixed_availability of this UpdateActivityPlanRequest.
        Fixed availability configuration for the activity plan

        :return: The fixed_availability of this UpdateActivityPlanRequest.
        :rtype: ListWrapperFixedAvailability
        """
        return self._fixed_availability

    @fixed_availability.setter
    def fixed_availability(self, fixed_availability: 'ListWrapperFixedAvailability') -> None:
        """
        Sets the fixed_availability of this UpdateActivityPlanRequest.
        Fixed availability configuration for the activity plan

        :param fixed_availability: The fixed_availability of this UpdateActivityPlanRequest.
        :type: ListWrapperFixedAvailability
        """
        

        self._fixed_availability = fixed_availability

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

