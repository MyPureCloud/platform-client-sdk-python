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
    from . import ShiftTradePreviewResponse

class ShiftTradeMatchReviewUserResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ShiftTradeMatchReviewUserResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'weekly_minimum_paid_minutes': 'int',
            'weekly_maximum_paid_minutes': 'int',
            'pre_trade_schedule_paid_minutes': 'int',
            'post_trade_schedule_paid_minutes': 'int',
            'post_trade_new_shift': 'ShiftTradePreviewResponse'
        }

        self.attribute_map = {
            'weekly_minimum_paid_minutes': 'weeklyMinimumPaidMinutes',
            'weekly_maximum_paid_minutes': 'weeklyMaximumPaidMinutes',
            'pre_trade_schedule_paid_minutes': 'preTradeSchedulePaidMinutes',
            'post_trade_schedule_paid_minutes': 'postTradeSchedulePaidMinutes',
            'post_trade_new_shift': 'postTradeNewShift'
        }

        self._weekly_minimum_paid_minutes = None
        self._weekly_maximum_paid_minutes = None
        self._pre_trade_schedule_paid_minutes = None
        self._post_trade_schedule_paid_minutes = None
        self._post_trade_new_shift = None

    @property
    def weekly_minimum_paid_minutes(self) -> int:
        """
        Gets the weekly_minimum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The minimum weekly paid minutes for this user per the work plan tied to the agent schedule

        :return: The weekly_minimum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :rtype: int
        """
        return self._weekly_minimum_paid_minutes

    @weekly_minimum_paid_minutes.setter
    def weekly_minimum_paid_minutes(self, weekly_minimum_paid_minutes: int) -> None:
        """
        Sets the weekly_minimum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The minimum weekly paid minutes for this user per the work plan tied to the agent schedule

        :param weekly_minimum_paid_minutes: The weekly_minimum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :type: int
        """
        

        self._weekly_minimum_paid_minutes = weekly_minimum_paid_minutes

    @property
    def weekly_maximum_paid_minutes(self) -> int:
        """
        Gets the weekly_maximum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The maximum weekly paid minutes for this user per the work plan tied to the agent schedule

        :return: The weekly_maximum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :rtype: int
        """
        return self._weekly_maximum_paid_minutes

    @weekly_maximum_paid_minutes.setter
    def weekly_maximum_paid_minutes(self, weekly_maximum_paid_minutes: int) -> None:
        """
        Sets the weekly_maximum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The maximum weekly paid minutes for this user per the work plan tied to the agent schedule

        :param weekly_maximum_paid_minutes: The weekly_maximum_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :type: int
        """
        

        self._weekly_maximum_paid_minutes = weekly_maximum_paid_minutes

    @property
    def pre_trade_schedule_paid_minutes(self) -> int:
        """
        Gets the pre_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The paid minutes on the week schedule for this user prior to the shift trade

        :return: The pre_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :rtype: int
        """
        return self._pre_trade_schedule_paid_minutes

    @pre_trade_schedule_paid_minutes.setter
    def pre_trade_schedule_paid_minutes(self, pre_trade_schedule_paid_minutes: int) -> None:
        """
        Sets the pre_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The paid minutes on the week schedule for this user prior to the shift trade

        :param pre_trade_schedule_paid_minutes: The pre_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :type: int
        """
        

        self._pre_trade_schedule_paid_minutes = pre_trade_schedule_paid_minutes

    @property
    def post_trade_schedule_paid_minutes(self) -> int:
        """
        Gets the post_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The paid minutes on the week schedule for this user if the shift trade is approved

        :return: The post_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :rtype: int
        """
        return self._post_trade_schedule_paid_minutes

    @post_trade_schedule_paid_minutes.setter
    def post_trade_schedule_paid_minutes(self, post_trade_schedule_paid_minutes: int) -> None:
        """
        Sets the post_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        The paid minutes on the week schedule for this user if the shift trade is approved

        :param post_trade_schedule_paid_minutes: The post_trade_schedule_paid_minutes of this ShiftTradeMatchReviewUserResponse.
        :type: int
        """
        

        self._post_trade_schedule_paid_minutes = post_trade_schedule_paid_minutes

    @property
    def post_trade_new_shift(self) -> 'ShiftTradePreviewResponse':
        """
        Gets the post_trade_new_shift of this ShiftTradeMatchReviewUserResponse.
        Preview of what the shift will look like for the opposite side of this trade after the match is approved

        :return: The post_trade_new_shift of this ShiftTradeMatchReviewUserResponse.
        :rtype: ShiftTradePreviewResponse
        """
        return self._post_trade_new_shift

    @post_trade_new_shift.setter
    def post_trade_new_shift(self, post_trade_new_shift: 'ShiftTradePreviewResponse') -> None:
        """
        Sets the post_trade_new_shift of this ShiftTradeMatchReviewUserResponse.
        Preview of what the shift will look like for the opposite side of this trade after the match is approved

        :param post_trade_new_shift: The post_trade_new_shift of this ShiftTradeMatchReviewUserResponse.
        :type: ShiftTradePreviewResponse
        """
        

        self._post_trade_new_shift = post_trade_new_shift

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

