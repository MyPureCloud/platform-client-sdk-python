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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ShiftTradeActivityRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ShiftTradeActivityRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_category': 'str',
            'action': 'str',
            'activity_code_id_replacement': 'str'
        }

        self.attribute_map = {
            'activity_category': 'activityCategory',
            'action': 'action',
            'activity_code_id_replacement': 'activityCodeIdReplacement'
        }

        self._activity_category = None
        self._action = None
        self._activity_code_id_replacement = None

    @property
    def activity_category(self):
        """
        Gets the activity_category of this ShiftTradeActivityRule.
        The activity category to which to apply this rule

        :return: The activity_category of this ShiftTradeActivityRule.
        :rtype: str
        """
        return self._activity_category

    @activity_category.setter
    def activity_category(self, activity_category):
        """
        Sets the activity_category of this ShiftTradeActivityRule.
        The activity category to which to apply this rule

        :param activity_category: The activity_category of this ShiftTradeActivityRule.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if activity_category.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for activity_category -> " + activity_category
            self._activity_category = "outdated_sdk_version"
        else:
            self._activity_category = activity_category

    @property
    def action(self):
        """
        Gets the action of this ShiftTradeActivityRule.
        The action this rule invokes

        :return: The action of this ShiftTradeActivityRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ShiftTradeActivityRule.
        The action this rule invokes

        :param action: The action of this ShiftTradeActivityRule.
        :type: str
        """
        allowed_values = ["Replace", "DoNotAllowTrade", "KeepWithSchedule"]
        if action.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for action -> " + action
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def activity_code_id_replacement(self):
        """
        Gets the activity_code_id_replacement of this ShiftTradeActivityRule.
        The activity code ID with which to replace activities belonging to the original category if applicable (required if action == Replace, must be a default activity code ID)

        :return: The activity_code_id_replacement of this ShiftTradeActivityRule.
        :rtype: str
        """
        return self._activity_code_id_replacement

    @activity_code_id_replacement.setter
    def activity_code_id_replacement(self, activity_code_id_replacement):
        """
        Sets the activity_code_id_replacement of this ShiftTradeActivityRule.
        The activity code ID with which to replace activities belonging to the original category if applicable (required if action == Replace, must be a default activity code ID)

        :param activity_code_id_replacement: The activity_code_id_replacement of this ShiftTradeActivityRule.
        :type: str
        """
        
        self._activity_code_id_replacement = activity_code_id_replacement

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
