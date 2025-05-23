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
    from . import ConversationChatEventTopicDetail
    from . import ConversationChatEventTopicLimit

class ConversationChatEventTopicErrorBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationChatEventTopicErrorBody - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'code': 'str',
            'status': 'int',
            'entity_id': 'str',
            'entity_name': 'str',
            'message_with_params': 'str',
            'message_params': 'dict(str, str)',
            'context_id': 'str',
            'details': 'list[ConversationChatEventTopicDetail]',
            'errors': 'list[ConversationChatEventTopicErrorBody]',
            'limit': 'ConversationChatEventTopicLimit'
        }

        self.attribute_map = {
            'message': 'message',
            'code': 'code',
            'status': 'status',
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'message_with_params': 'messageWithParams',
            'message_params': 'messageParams',
            'context_id': 'contextId',
            'details': 'details',
            'errors': 'errors',
            'limit': 'limit'
        }

        self._message = None
        self._code = None
        self._status = None
        self._entity_id = None
        self._entity_name = None
        self._message_with_params = None
        self._message_params = None
        self._context_id = None
        self._details = None
        self._errors = None
        self._limit = None

    @property
    def message(self) -> str:
        """
        Gets the message of this ConversationChatEventTopicErrorBody.


        :return: The message of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the message of this ConversationChatEventTopicErrorBody.


        :param message: The message of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._message = message

    @property
    def code(self) -> str:
        """
        Gets the code of this ConversationChatEventTopicErrorBody.


        :return: The code of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str) -> None:
        """
        Sets the code of this ConversationChatEventTopicErrorBody.


        :param code: The code of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._code = code

    @property
    def status(self) -> int:
        """
        Gets the status of this ConversationChatEventTopicErrorBody.


        :return: The status of this ConversationChatEventTopicErrorBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int) -> None:
        """
        Sets the status of this ConversationChatEventTopicErrorBody.


        :param status: The status of this ConversationChatEventTopicErrorBody.
        :type: int
        """
        

        self._status = status

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this ConversationChatEventTopicErrorBody.


        :return: The entity_id of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this ConversationChatEventTopicErrorBody.


        :param entity_id: The entity_id of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def entity_name(self) -> str:
        """
        Gets the entity_name of this ConversationChatEventTopicErrorBody.


        :return: The entity_name of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name: str) -> None:
        """
        Sets the entity_name of this ConversationChatEventTopicErrorBody.


        :param entity_name: The entity_name of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._entity_name = entity_name

    @property
    def message_with_params(self) -> str:
        """
        Gets the message_with_params of this ConversationChatEventTopicErrorBody.


        :return: The message_with_params of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._message_with_params

    @message_with_params.setter
    def message_with_params(self, message_with_params: str) -> None:
        """
        Sets the message_with_params of this ConversationChatEventTopicErrorBody.


        :param message_with_params: The message_with_params of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._message_with_params = message_with_params

    @property
    def message_params(self) -> Dict[str, str]:
        """
        Gets the message_params of this ConversationChatEventTopicErrorBody.


        :return: The message_params of this ConversationChatEventTopicErrorBody.
        :rtype: dict(str, str)
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params: Dict[str, str]) -> None:
        """
        Sets the message_params of this ConversationChatEventTopicErrorBody.


        :param message_params: The message_params of this ConversationChatEventTopicErrorBody.
        :type: dict(str, str)
        """
        

        self._message_params = message_params

    @property
    def context_id(self) -> str:
        """
        Gets the context_id of this ConversationChatEventTopicErrorBody.


        :return: The context_id of this ConversationChatEventTopicErrorBody.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id: str) -> None:
        """
        Sets the context_id of this ConversationChatEventTopicErrorBody.


        :param context_id: The context_id of this ConversationChatEventTopicErrorBody.
        :type: str
        """
        

        self._context_id = context_id

    @property
    def details(self) -> List['ConversationChatEventTopicDetail']:
        """
        Gets the details of this ConversationChatEventTopicErrorBody.


        :return: The details of this ConversationChatEventTopicErrorBody.
        :rtype: list[ConversationChatEventTopicDetail]
        """
        return self._details

    @details.setter
    def details(self, details: List['ConversationChatEventTopicDetail']) -> None:
        """
        Sets the details of this ConversationChatEventTopicErrorBody.


        :param details: The details of this ConversationChatEventTopicErrorBody.
        :type: list[ConversationChatEventTopicDetail]
        """
        

        self._details = details

    @property
    def errors(self) -> List['ConversationChatEventTopicErrorBody']:
        """
        Gets the errors of this ConversationChatEventTopicErrorBody.


        :return: The errors of this ConversationChatEventTopicErrorBody.
        :rtype: list[ConversationChatEventTopicErrorBody]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List['ConversationChatEventTopicErrorBody']) -> None:
        """
        Sets the errors of this ConversationChatEventTopicErrorBody.


        :param errors: The errors of this ConversationChatEventTopicErrorBody.
        :type: list[ConversationChatEventTopicErrorBody]
        """
        

        self._errors = errors

    @property
    def limit(self) -> 'ConversationChatEventTopicLimit':
        """
        Gets the limit of this ConversationChatEventTopicErrorBody.


        :return: The limit of this ConversationChatEventTopicErrorBody.
        :rtype: ConversationChatEventTopicLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit: 'ConversationChatEventTopicLimit') -> None:
        """
        Sets the limit of this ConversationChatEventTopicErrorBody.


        :param limit: The limit of this ConversationChatEventTopicErrorBody.
        :type: ConversationChatEventTopicLimit
        """
        

        self._limit = limit

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

