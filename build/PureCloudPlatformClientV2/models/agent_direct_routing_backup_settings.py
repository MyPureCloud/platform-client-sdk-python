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


class AgentDirectRoutingBackupSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentDirectRoutingBackupSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue_id': 'str',
            'user_id': 'str',
            'wait_for_agent': 'bool',
            'agent_wait_seconds': 'int',
            'backed_up_users': 'list[str]'
        }

        self.attribute_map = {
            'queue_id': 'queueId',
            'user_id': 'userId',
            'wait_for_agent': 'waitForAgent',
            'agent_wait_seconds': 'agentWaitSeconds',
            'backed_up_users': 'backedUpUsers'
        }

        self._queue_id = None
        self._user_id = None
        self._wait_for_agent = None
        self._agent_wait_seconds = None
        self._backed_up_users = None

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this AgentDirectRoutingBackupSettings.
        ID of queue to be used as backup. If queueId and userId are both specified, queue behaves as secondary backup.

        :return: The queue_id of this AgentDirectRoutingBackupSettings.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this AgentDirectRoutingBackupSettings.
        ID of queue to be used as backup. If queueId and userId are both specified, queue behaves as secondary backup.

        :param queue_id: The queue_id of this AgentDirectRoutingBackupSettings.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this AgentDirectRoutingBackupSettings.
        ID of user to be used as backup. If queueId and userId are both specified, user behaves as primary backup.

        :return: The user_id of this AgentDirectRoutingBackupSettings.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this AgentDirectRoutingBackupSettings.
        ID of user to be used as backup. If queueId and userId are both specified, user behaves as primary backup.

        :param user_id: The user_id of this AgentDirectRoutingBackupSettings.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def wait_for_agent(self) -> bool:
        """
        Gets the wait_for_agent of this AgentDirectRoutingBackupSettings.
        Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup.

        :return: The wait_for_agent of this AgentDirectRoutingBackupSettings.
        :rtype: bool
        """
        return self._wait_for_agent

    @wait_for_agent.setter
    def wait_for_agent(self, wait_for_agent: bool) -> None:
        """
        Sets the wait_for_agent of this AgentDirectRoutingBackupSettings.
        Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup.

        :param wait_for_agent: The wait_for_agent of this AgentDirectRoutingBackupSettings.
        :type: bool
        """
        

        self._wait_for_agent = wait_for_agent

    @property
    def agent_wait_seconds(self) -> int:
        """
        Gets the agent_wait_seconds of this AgentDirectRoutingBackupSettings.
        Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000].

        :return: The agent_wait_seconds of this AgentDirectRoutingBackupSettings.
        :rtype: int
        """
        return self._agent_wait_seconds

    @agent_wait_seconds.setter
    def agent_wait_seconds(self, agent_wait_seconds: int) -> None:
        """
        Sets the agent_wait_seconds of this AgentDirectRoutingBackupSettings.
        Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000].

        :param agent_wait_seconds: The agent_wait_seconds of this AgentDirectRoutingBackupSettings.
        :type: int
        """
        

        self._agent_wait_seconds = agent_wait_seconds

    @property
    def backed_up_users(self) -> List[str]:
        """
        Gets the backed_up_users of this AgentDirectRoutingBackupSettings.
        Set of users that this user is a backup for.

        :return: The backed_up_users of this AgentDirectRoutingBackupSettings.
        :rtype: list[str]
        """
        return self._backed_up_users

    @backed_up_users.setter
    def backed_up_users(self, backed_up_users: List[str]) -> None:
        """
        Sets the backed_up_users of this AgentDirectRoutingBackupSettings.
        Set of users that this user is a backup for.

        :param backed_up_users: The backed_up_users of this AgentDirectRoutingBackupSettings.
        :type: list[str]
        """
        

        self._backed_up_users = backed_up_users

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
