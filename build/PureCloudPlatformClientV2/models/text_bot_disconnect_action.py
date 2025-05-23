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
    from . import TextBotFlowLocation
    from . import TextBotFlowOutcome

class TextBotDisconnectAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TextBotDisconnectAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'reason': 'str',
            'reason_extended_info': 'str',
            'flow_location': 'TextBotFlowLocation',
            'flow_outcomes': 'list[TextBotFlowOutcome]'
        }

        self.attribute_map = {
            'reason': 'reason',
            'reason_extended_info': 'reasonExtendedInfo',
            'flow_location': 'flowLocation',
            'flow_outcomes': 'flowOutcomes'
        }

        self._reason = None
        self._reason_extended_info = None
        self._flow_location = None
        self._flow_outcomes = None

    @property
    def reason(self) -> str:
        """
        Gets the reason of this TextBotDisconnectAction.
        The reason for the disconnect.

        :return: The reason of this TextBotDisconnectAction.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str) -> None:
        """
        Sets the reason of this TextBotDisconnectAction.
        The reason for the disconnect.

        :param reason: The reason of this TextBotDisconnectAction.
        :type: str
        """
        if isinstance(reason, int):
            reason = str(reason)
        allowed_values = ["TriggeredByUser", "TriggeredByFlow", "SessionExpired", "Error", "RecognitionFailure"]
        if reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for reason -> " + reason)
            self._reason = "outdated_sdk_version"
        else:
            self._reason = reason

    @property
    def reason_extended_info(self) -> str:
        """
        Gets the reason_extended_info of this TextBotDisconnectAction.
        Extended information related to the reason, if available.

        :return: The reason_extended_info of this TextBotDisconnectAction.
        :rtype: str
        """
        return self._reason_extended_info

    @reason_extended_info.setter
    def reason_extended_info(self, reason_extended_info: str) -> None:
        """
        Sets the reason_extended_info of this TextBotDisconnectAction.
        Extended information related to the reason, if available.

        :param reason_extended_info: The reason_extended_info of this TextBotDisconnectAction.
        :type: str
        """
        

        self._reason_extended_info = reason_extended_info

    @property
    def flow_location(self) -> 'TextBotFlowLocation':
        """
        Gets the flow_location of this TextBotDisconnectAction.
        Describes where in the Bot Flow the user was when the disconnect occurred.

        :return: The flow_location of this TextBotDisconnectAction.
        :rtype: TextBotFlowLocation
        """
        return self._flow_location

    @flow_location.setter
    def flow_location(self, flow_location: 'TextBotFlowLocation') -> None:
        """
        Sets the flow_location of this TextBotDisconnectAction.
        Describes where in the Bot Flow the user was when the disconnect occurred.

        :param flow_location: The flow_location of this TextBotDisconnectAction.
        :type: TextBotFlowLocation
        """
        

        self._flow_location = flow_location

    @property
    def flow_outcomes(self) -> List['TextBotFlowOutcome']:
        """
        Gets the flow_outcomes of this TextBotDisconnectAction.
        The list of Flow Outcomes for the bot flow and their details.

        :return: The flow_outcomes of this TextBotDisconnectAction.
        :rtype: list[TextBotFlowOutcome]
        """
        return self._flow_outcomes

    @flow_outcomes.setter
    def flow_outcomes(self, flow_outcomes: List['TextBotFlowOutcome']) -> None:
        """
        Sets the flow_outcomes of this TextBotDisconnectAction.
        The list of Flow Outcomes for the bot flow and their details.

        :param flow_outcomes: The flow_outcomes of this TextBotDisconnectAction.
        :type: list[TextBotFlowOutcome]
        """
        

        self._flow_outcomes = flow_outcomes

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

