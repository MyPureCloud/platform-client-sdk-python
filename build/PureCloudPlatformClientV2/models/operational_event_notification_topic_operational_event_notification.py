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
    from . import OperationalEventNotificationTopicEventEntity

class OperationalEventNotificationTopicOperationalEventNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OperationalEventNotificationTopicOperationalEventNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_entity': 'OperationalEventNotificationTopicEventEntity',
            'entity_id': 'str',
            'entity_name': 'str',
            'previous_value': 'str',
            'current_value': 'str',
            'error_code': 'str',
            'version': 'str',
            'parent_entity': 'str',
            'entity_type': 'str',
            'conversation_id': 'str',
            'entity_token': 'str',
            'timestamp': 'int'
        }

        self.attribute_map = {
            'event_entity': 'eventEntity',
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'previous_value': 'previousValue',
            'current_value': 'currentValue',
            'error_code': 'errorCode',
            'version': 'version',
            'parent_entity': 'parentEntity',
            'entity_type': 'entityType',
            'conversation_id': 'conversationId',
            'entity_token': 'entityToken',
            'timestamp': 'timestamp'
        }

        self._event_entity = None
        self._entity_id = None
        self._entity_name = None
        self._previous_value = None
        self._current_value = None
        self._error_code = None
        self._version = None
        self._parent_entity = None
        self._entity_type = None
        self._conversation_id = None
        self._entity_token = None
        self._timestamp = None

    @property
    def event_entity(self) -> 'OperationalEventNotificationTopicEventEntity':
        """
        Gets the event_entity of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The event_entity of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: OperationalEventNotificationTopicEventEntity
        """
        return self._event_entity

    @event_entity.setter
    def event_entity(self, event_entity: 'OperationalEventNotificationTopicEventEntity') -> None:
        """
        Sets the event_entity of this OperationalEventNotificationTopicOperationalEventNotification.


        :param event_entity: The event_entity of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: OperationalEventNotificationTopicEventEntity
        """
        

        self._event_entity = event_entity

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The entity_id of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this OperationalEventNotificationTopicOperationalEventNotification.


        :param entity_id: The entity_id of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def entity_name(self) -> str:
        """
        Gets the entity_name of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The entity_name of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name: str) -> None:
        """
        Sets the entity_name of this OperationalEventNotificationTopicOperationalEventNotification.


        :param entity_name: The entity_name of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._entity_name = entity_name

    @property
    def previous_value(self) -> str:
        """
        Gets the previous_value of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The previous_value of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value: str) -> None:
        """
        Sets the previous_value of this OperationalEventNotificationTopicOperationalEventNotification.


        :param previous_value: The previous_value of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._previous_value = previous_value

    @property
    def current_value(self) -> str:
        """
        Gets the current_value of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The current_value of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value: str) -> None:
        """
        Sets the current_value of this OperationalEventNotificationTopicOperationalEventNotification.


        :param current_value: The current_value of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._current_value = current_value

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The error_code of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this OperationalEventNotificationTopicOperationalEventNotification.


        :param error_code: The error_code of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def version(self) -> str:
        """
        Gets the version of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The version of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Sets the version of this OperationalEventNotificationTopicOperationalEventNotification.


        :param version: The version of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._version = version

    @property
    def parent_entity(self) -> str:
        """
        Gets the parent_entity of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The parent_entity of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._parent_entity

    @parent_entity.setter
    def parent_entity(self, parent_entity: str) -> None:
        """
        Sets the parent_entity of this OperationalEventNotificationTopicOperationalEventNotification.


        :param parent_entity: The parent_entity of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._parent_entity = parent_entity

    @property
    def entity_type(self) -> str:
        """
        Gets the entity_type of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The entity_type of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str) -> None:
        """
        Sets the entity_type of this OperationalEventNotificationTopicOperationalEventNotification.


        :param entity_type: The entity_type of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._entity_type = entity_type

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The conversation_id of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this OperationalEventNotificationTopicOperationalEventNotification.


        :param conversation_id: The conversation_id of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def entity_token(self) -> str:
        """
        Gets the entity_token of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The entity_token of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: str
        """
        return self._entity_token

    @entity_token.setter
    def entity_token(self, entity_token: str) -> None:
        """
        Sets the entity_token of this OperationalEventNotificationTopicOperationalEventNotification.


        :param entity_token: The entity_token of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: str
        """
        

        self._entity_token = entity_token

    @property
    def timestamp(self) -> int:
        """
        Gets the timestamp of this OperationalEventNotificationTopicOperationalEventNotification.


        :return: The timestamp of this OperationalEventNotificationTopicOperationalEventNotification.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int) -> None:
        """
        Sets the timestamp of this OperationalEventNotificationTopicOperationalEventNotification.


        :param timestamp: The timestamp of this OperationalEventNotificationTopicOperationalEventNotification.
        :type: int
        """
        

        self._timestamp = timestamp

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

