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
    from . import CampaignRuleCondition

class CampaignRuleConditionGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignRuleConditionGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'match_any_conditions': 'bool',
            'conditions': 'list[CampaignRuleCondition]'
        }

        self.attribute_map = {
            'match_any_conditions': 'matchAnyConditions',
            'conditions': 'conditions'
        }

        self._match_any_conditions = None
        self._conditions = None

    @property
    def match_any_conditions(self) -> bool:
        """
        Gets the match_any_conditions of this CampaignRuleConditionGroup.
        Whether or not this condition group should be evaluated as true if any of sub conditions is matched

        :return: The match_any_conditions of this CampaignRuleConditionGroup.
        :rtype: bool
        """
        return self._match_any_conditions

    @match_any_conditions.setter
    def match_any_conditions(self, match_any_conditions: bool) -> None:
        """
        Sets the match_any_conditions of this CampaignRuleConditionGroup.
        Whether or not this condition group should be evaluated as true if any of sub conditions is matched

        :param match_any_conditions: The match_any_conditions of this CampaignRuleConditionGroup.
        :type: bool
        """
        

        self._match_any_conditions = match_any_conditions

    @property
    def conditions(self) -> List['CampaignRuleCondition']:
        """
        Gets the conditions of this CampaignRuleConditionGroup.
        The parameters for the CampaignRuleCondition.

        :return: The conditions of this CampaignRuleConditionGroup.
        :rtype: list[CampaignRuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: List['CampaignRuleCondition']) -> None:
        """
        Sets the conditions of this CampaignRuleConditionGroup.
        The parameters for the CampaignRuleCondition.

        :param conditions: The conditions of this CampaignRuleConditionGroup.
        :type: list[CampaignRuleCondition]
        """
        

        self._conditions = conditions

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

