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

if TYPE_CHECKING:
    from . import AuditEntity
    from . import AuditUser
    from . import Change
    from . import ServiceContext

class AuditMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AuditMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user': 'AuditUser',
            'correlation_id': 'str',
            'transaction_id': 'str',
            'transaction_initiator': 'bool',
            'application': 'str',
            'service_name': 'str',
            'level': 'str',
            'timestamp': 'str',
            'received_timestamp': 'str',
            'status': 'str',
            'action_context': 'str',
            'action': 'str',
            'changes': 'list[Change]',
            'entity': 'AuditEntity',
            'service_context': 'ServiceContext'
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'correlation_id': 'correlationId',
            'transaction_id': 'transactionId',
            'transaction_initiator': 'transactionInitiator',
            'application': 'application',
            'service_name': 'serviceName',
            'level': 'level',
            'timestamp': 'timestamp',
            'received_timestamp': 'receivedTimestamp',
            'status': 'status',
            'action_context': 'actionContext',
            'action': 'action',
            'changes': 'changes',
            'entity': 'entity',
            'service_context': 'serviceContext'
        }

        self._id = None
        self._user = None
        self._correlation_id = None
        self._transaction_id = None
        self._transaction_initiator = None
        self._application = None
        self._service_name = None
        self._level = None
        self._timestamp = None
        self._received_timestamp = None
        self._status = None
        self._action_context = None
        self._action = None
        self._changes = None
        self._entity = None
        self._service_context = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AuditMessage.
        AuditMessage ID.

        :return: The id of this AuditMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AuditMessage.
        AuditMessage ID.

        :param id: The id of this AuditMessage.
        :type: str
        """
        

        self._id = id

    @property
    def user(self) -> 'AuditUser':
        """
        Gets the user of this AuditMessage.


        :return: The user of this AuditMessage.
        :rtype: AuditUser
        """
        return self._user

    @user.setter
    def user(self, user: 'AuditUser') -> None:
        """
        Sets the user of this AuditMessage.


        :param user: The user of this AuditMessage.
        :type: AuditUser
        """
        

        self._user = user

    @property
    def correlation_id(self) -> str:
        """
        Gets the correlation_id of this AuditMessage.
        Correlation ID.

        :return: The correlation_id of this AuditMessage.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id: str) -> None:
        """
        Sets the correlation_id of this AuditMessage.
        Correlation ID.

        :param correlation_id: The correlation_id of this AuditMessage.
        :type: str
        """
        

        self._correlation_id = correlation_id

    @property
    def transaction_id(self) -> str:
        """
        Gets the transaction_id of this AuditMessage.
        Transaction ID.

        :return: The transaction_id of this AuditMessage.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str) -> None:
        """
        Sets the transaction_id of this AuditMessage.
        Transaction ID.

        :param transaction_id: The transaction_id of this AuditMessage.
        :type: str
        """
        

        self._transaction_id = transaction_id

    @property
    def transaction_initiator(self) -> bool:
        """
        Gets the transaction_initiator of this AuditMessage.
        Whether or not this audit can be considered the initiator of the transaction it is a part of.

        :return: The transaction_initiator of this AuditMessage.
        :rtype: bool
        """
        return self._transaction_initiator

    @transaction_initiator.setter
    def transaction_initiator(self, transaction_initiator: bool) -> None:
        """
        Sets the transaction_initiator of this AuditMessage.
        Whether or not this audit can be considered the initiator of the transaction it is a part of.

        :param transaction_initiator: The transaction_initiator of this AuditMessage.
        :type: bool
        """
        

        self._transaction_initiator = transaction_initiator

    @property
    def application(self) -> str:
        """
        Gets the application of this AuditMessage.
        The application through which the action of this AuditMessage was initiated.

        :return: The application of this AuditMessage.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application: str) -> None:
        """
        Sets the application of this AuditMessage.
        The application through which the action of this AuditMessage was initiated.

        :param application: The application of this AuditMessage.
        :type: str
        """
        

        self._application = application

    @property
    def service_name(self) -> str:
        """
        Gets the service_name of this AuditMessage.
        The name of the service which sent this AuditMessage.

        :return: The service_name of this AuditMessage.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str) -> None:
        """
        Sets the service_name of this AuditMessage.
        The name of the service which sent this AuditMessage.

        :param service_name: The service_name of this AuditMessage.
        :type: str
        """
        

        self._service_name = service_name

    @property
    def level(self) -> str:
        """
        Gets the level of this AuditMessage.
        The level of this audit. USER or SYSTEM.

        :return: The level of this AuditMessage.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str) -> None:
        """
        Sets the level of this AuditMessage.
        The level of this audit. USER or SYSTEM.

        :param level: The level of this AuditMessage.
        :type: str
        """
        

        self._level = level

    @property
    def timestamp(self) -> str:
        """
        Gets the timestamp of this AuditMessage.
        The time at which the action of this AuditMessage was initiated.

        :return: The timestamp of this AuditMessage.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str) -> None:
        """
        Sets the timestamp of this AuditMessage.
        The time at which the action of this AuditMessage was initiated.

        :param timestamp: The timestamp of this AuditMessage.
        :type: str
        """
        

        self._timestamp = timestamp

    @property
    def received_timestamp(self) -> str:
        """
        Gets the received_timestamp of this AuditMessage.
        The time at which this AuditMessage was received.

        :return: The received_timestamp of this AuditMessage.
        :rtype: str
        """
        return self._received_timestamp

    @received_timestamp.setter
    def received_timestamp(self, received_timestamp: str) -> None:
        """
        Sets the received_timestamp of this AuditMessage.
        The time at which this AuditMessage was received.

        :param received_timestamp: The received_timestamp of this AuditMessage.
        :type: str
        """
        

        self._received_timestamp = received_timestamp

    @property
    def status(self) -> str:
        """
        Gets the status of this AuditMessage.
        The status of the action of this AuditMessage

        :return: The status of this AuditMessage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this AuditMessage.
        The status of the action of this AuditMessage

        :param status: The status of this AuditMessage.
        :type: str
        """
        

        self._status = status

    @property
    def action_context(self) -> str:
        """
        Gets the action_context of this AuditMessage.
        The context of a system-level action

        :return: The action_context of this AuditMessage.
        :rtype: str
        """
        return self._action_context

    @action_context.setter
    def action_context(self, action_context: str) -> None:
        """
        Sets the action_context of this AuditMessage.
        The context of a system-level action

        :param action_context: The action_context of this AuditMessage.
        :type: str
        """
        

        self._action_context = action_context

    @property
    def action(self) -> str:
        """
        Gets the action of this AuditMessage.
        A string representing the action that took place

        :return: The action of this AuditMessage.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        """
        Sets the action of this AuditMessage.
        A string representing the action that took place

        :param action: The action of this AuditMessage.
        :type: str
        """
        

        self._action = action

    @property
    def changes(self) -> List['Change']:
        """
        Gets the changes of this AuditMessage.
        Details about any changes that occurred in this audit

        :return: The changes of this AuditMessage.
        :rtype: list[Change]
        """
        return self._changes

    @changes.setter
    def changes(self, changes: List['Change']) -> None:
        """
        Sets the changes of this AuditMessage.
        Details about any changes that occurred in this audit

        :param changes: The changes of this AuditMessage.
        :type: list[Change]
        """
        

        self._changes = changes

    @property
    def entity(self) -> 'AuditEntity':
        """
        Gets the entity of this AuditMessage.


        :return: The entity of this AuditMessage.
        :rtype: AuditEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity: 'AuditEntity') -> None:
        """
        Sets the entity of this AuditMessage.


        :param entity: The entity of this AuditMessage.
        :type: AuditEntity
        """
        

        self._entity = entity

    @property
    def service_context(self) -> 'ServiceContext':
        """
        Gets the service_context of this AuditMessage.
        The service-specific context associated with this AuditMessage.

        :return: The service_context of this AuditMessage.
        :rtype: ServiceContext
        """
        return self._service_context

    @service_context.setter
    def service_context(self, service_context: 'ServiceContext') -> None:
        """
        Sets the service_context of this AuditMessage.
        The service-specific context associated with this AuditMessage.

        :param service_context: The service_context of this AuditMessage.
        :type: ServiceContext
        """
        

        self._service_context = service_context

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

