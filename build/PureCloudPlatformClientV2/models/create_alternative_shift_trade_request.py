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


class CreateAlternativeShiftTradeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateAlternativeShiftTradeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job_id': 'str',
            'drop_shift_reference_keys': 'list[str]',
            'pickup_shift_reference_keys': 'list[str]',
            'alternative_shift_trade_granularity': 'str',
            'expiration_date': 'datetime'
        }

        self.attribute_map = {
            'job_id': 'jobId',
            'drop_shift_reference_keys': 'dropShiftReferenceKeys',
            'pickup_shift_reference_keys': 'pickupShiftReferenceKeys',
            'alternative_shift_trade_granularity': 'alternativeShiftTradeGranularity',
            'expiration_date': 'expirationDate'
        }

        self._job_id = None
        self._drop_shift_reference_keys = None
        self._pickup_shift_reference_keys = None
        self._alternative_shift_trade_granularity = None
        self._expiration_date = None

    @property
    def job_id(self) -> str:
        """
        Gets the job_id of this CreateAlternativeShiftTradeRequest.
        The ID of this alternative shift job

        :return: The job_id of this CreateAlternativeShiftTradeRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: str) -> None:
        """
        Sets the job_id of this CreateAlternativeShiftTradeRequest.
        The ID of this alternative shift job

        :param job_id: The job_id of this CreateAlternativeShiftTradeRequest.
        :type: str
        """
        

        self._job_id = job_id

    @property
    def drop_shift_reference_keys(self) -> List[str]:
        """
        Gets the drop_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        A list of offered shift reference keys an agent wants to drop

        :return: The drop_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        :rtype: list[str]
        """
        return self._drop_shift_reference_keys

    @drop_shift_reference_keys.setter
    def drop_shift_reference_keys(self, drop_shift_reference_keys: List[str]) -> None:
        """
        Sets the drop_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        A list of offered shift reference keys an agent wants to drop

        :param drop_shift_reference_keys: The drop_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        :type: list[str]
        """
        

        self._drop_shift_reference_keys = drop_shift_reference_keys

    @property
    def pickup_shift_reference_keys(self) -> List[str]:
        """
        Gets the pickup_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        A list of offered shift reference keys an agent wants to pick up

        :return: The pickup_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        :rtype: list[str]
        """
        return self._pickup_shift_reference_keys

    @pickup_shift_reference_keys.setter
    def pickup_shift_reference_keys(self, pickup_shift_reference_keys: List[str]) -> None:
        """
        Sets the pickup_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        A list of offered shift reference keys an agent wants to pick up

        :param pickup_shift_reference_keys: The pickup_shift_reference_keys of this CreateAlternativeShiftTradeRequest.
        :type: list[str]
        """
        

        self._pickup_shift_reference_keys = pickup_shift_reference_keys

    @property
    def alternative_shift_trade_granularity(self) -> str:
        """
        Gets the alternative_shift_trade_granularity of this CreateAlternativeShiftTradeRequest.
        The granularity of alternative shifts to be traded

        :return: The alternative_shift_trade_granularity of this CreateAlternativeShiftTradeRequest.
        :rtype: str
        """
        return self._alternative_shift_trade_granularity

    @alternative_shift_trade_granularity.setter
    def alternative_shift_trade_granularity(self, alternative_shift_trade_granularity: str) -> None:
        """
        Sets the alternative_shift_trade_granularity of this CreateAlternativeShiftTradeRequest.
        The granularity of alternative shifts to be traded

        :param alternative_shift_trade_granularity: The alternative_shift_trade_granularity of this CreateAlternativeShiftTradeRequest.
        :type: str
        """
        if isinstance(alternative_shift_trade_granularity, int):
            alternative_shift_trade_granularity = str(alternative_shift_trade_granularity)
        allowed_values = ["Daily"]
        if alternative_shift_trade_granularity.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for alternative_shift_trade_granularity -> " + alternative_shift_trade_granularity)
            self._alternative_shift_trade_granularity = "outdated_sdk_version"
        else:
            self._alternative_shift_trade_granularity = alternative_shift_trade_granularity

    @property
    def expiration_date(self) -> datetime:
        """
        Gets the expiration_date of this CreateAlternativeShiftTradeRequest.
        The date when the trade will expire in ISO-8601 format. The trade cannot be approved after expiration

        :return: The expiration_date of this CreateAlternativeShiftTradeRequest.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime) -> None:
        """
        Sets the expiration_date of this CreateAlternativeShiftTradeRequest.
        The date when the trade will expire in ISO-8601 format. The trade cannot be approved after expiration

        :param expiration_date: The expiration_date of this CreateAlternativeShiftTradeRequest.
        :type: datetime
        """
        

        self._expiration_date = expiration_date

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
