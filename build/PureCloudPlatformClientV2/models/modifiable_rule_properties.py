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
    from . import AlertNotification
    from . import CommonRuleConditions

class ModifiableRuleProperties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ModifiableRuleProperties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'enabled': 'bool',
            'notifications': 'list[AlertNotification]',
            'send_exiting_alarm_notifications': 'bool',
            'wait_between_notification_ms': 'int',
            'conditions': 'CommonRuleConditions',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'enabled': 'enabled',
            'notifications': 'notifications',
            'send_exiting_alarm_notifications': 'sendExitingAlarmNotifications',
            'wait_between_notification_ms': 'waitBetweenNotificationMs',
            'conditions': 'conditions',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._enabled = None
        self._notifications = None
        self._send_exiting_alarm_notifications = None
        self._wait_between_notification_ms = None
        self._conditions = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ModifiableRuleProperties.
        The globally unique identifier for the object.

        :return: The id of this ModifiableRuleProperties.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ModifiableRuleProperties.
        The globally unique identifier for the object.

        :param id: The id of this ModifiableRuleProperties.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ModifiableRuleProperties.
        Name of the rule

        :return: The name of this ModifiableRuleProperties.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ModifiableRuleProperties.
        Name of the rule

        :param name: The name of this ModifiableRuleProperties.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this ModifiableRuleProperties.
        The description of the rule.

        :return: The description of this ModifiableRuleProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this ModifiableRuleProperties.
        The description of the rule.

        :param description: The description of this ModifiableRuleProperties.
        :type: str
        """
        

        self._description = description

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this ModifiableRuleProperties.
        Indicates if the rule is enabled.

        :return: The enabled of this ModifiableRuleProperties.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this ModifiableRuleProperties.
        Indicates if the rule is enabled.

        :param enabled: The enabled of this ModifiableRuleProperties.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def notifications(self) -> List['AlertNotification']:
        """
        Gets the notifications of this ModifiableRuleProperties.
        The alert notification types to trigger when alarm state changes as well as the users they will be sent to.

        :return: The notifications of this ModifiableRuleProperties.
        :rtype: list[AlertNotification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications: List['AlertNotification']) -> None:
        """
        Sets the notifications of this ModifiableRuleProperties.
        The alert notification types to trigger when alarm state changes as well as the users they will be sent to.

        :param notifications: The notifications of this ModifiableRuleProperties.
        :type: list[AlertNotification]
        """
        

        self._notifications = notifications

    @property
    def send_exiting_alarm_notifications(self) -> bool:
        """
        Gets the send_exiting_alarm_notifications of this ModifiableRuleProperties.
        Indicates if the alert will send a notification when it is closed.

        :return: The send_exiting_alarm_notifications of this ModifiableRuleProperties.
        :rtype: bool
        """
        return self._send_exiting_alarm_notifications

    @send_exiting_alarm_notifications.setter
    def send_exiting_alarm_notifications(self, send_exiting_alarm_notifications: bool) -> None:
        """
        Sets the send_exiting_alarm_notifications of this ModifiableRuleProperties.
        Indicates if the alert will send a notification when it is closed.

        :param send_exiting_alarm_notifications: The send_exiting_alarm_notifications of this ModifiableRuleProperties.
        :type: bool
        """
        

        self._send_exiting_alarm_notifications = send_exiting_alarm_notifications

    @property
    def wait_between_notification_ms(self) -> int:
        """
        Gets the wait_between_notification_ms of this ModifiableRuleProperties.
        The amount of time in milliseconds to wait between notification.

        :return: The wait_between_notification_ms of this ModifiableRuleProperties.
        :rtype: int
        """
        return self._wait_between_notification_ms

    @wait_between_notification_ms.setter
    def wait_between_notification_ms(self, wait_between_notification_ms: int) -> None:
        """
        Sets the wait_between_notification_ms of this ModifiableRuleProperties.
        The amount of time in milliseconds to wait between notification.

        :param wait_between_notification_ms: The wait_between_notification_ms of this ModifiableRuleProperties.
        :type: int
        """
        

        self._wait_between_notification_ms = wait_between_notification_ms

    @property
    def conditions(self) -> 'CommonRuleConditions':
        """
        Gets the conditions of this ModifiableRuleProperties.
        The set of metric conditions that would trigger an alert.

        :return: The conditions of this ModifiableRuleProperties.
        :rtype: CommonRuleConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: 'CommonRuleConditions') -> None:
        """
        Sets the conditions of this ModifiableRuleProperties.
        The set of metric conditions that would trigger an alert.

        :param conditions: The conditions of this ModifiableRuleProperties.
        :type: CommonRuleConditions
        """
        

        self._conditions = conditions

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ModifiableRuleProperties.
        The URI for this object

        :return: The self_uri of this ModifiableRuleProperties.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ModifiableRuleProperties.
        The URI for this object

        :param self_uri: The self_uri of this ModifiableRuleProperties.
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

