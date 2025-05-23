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
    from . import QueueConversationVideoEventTopicScoredAgent
    from . import QueueConversationVideoEventTopicUriReference

class QueueConversationVideoEventTopicConversationRoutingData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationVideoEventTopicConversationRoutingData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue': 'QueueConversationVideoEventTopicUriReference',
            'language': 'QueueConversationVideoEventTopicUriReference',
            'priority': 'int',
            'skills': 'list[QueueConversationVideoEventTopicUriReference]',
            'scored_agents': 'list[QueueConversationVideoEventTopicScoredAgent]'
        }

        self.attribute_map = {
            'queue': 'queue',
            'language': 'language',
            'priority': 'priority',
            'skills': 'skills',
            'scored_agents': 'scoredAgents'
        }

        self._queue = None
        self._language = None
        self._priority = None
        self._skills = None
        self._scored_agents = None

    @property
    def queue(self) -> 'QueueConversationVideoEventTopicUriReference':
        """
        Gets the queue of this QueueConversationVideoEventTopicConversationRoutingData.


        :return: The queue of this QueueConversationVideoEventTopicConversationRoutingData.
        :rtype: QueueConversationVideoEventTopicUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'QueueConversationVideoEventTopicUriReference') -> None:
        """
        Sets the queue of this QueueConversationVideoEventTopicConversationRoutingData.


        :param queue: The queue of this QueueConversationVideoEventTopicConversationRoutingData.
        :type: QueueConversationVideoEventTopicUriReference
        """
        

        self._queue = queue

    @property
    def language(self) -> 'QueueConversationVideoEventTopicUriReference':
        """
        Gets the language of this QueueConversationVideoEventTopicConversationRoutingData.
        A UriReference for a resource

        :return: The language of this QueueConversationVideoEventTopicConversationRoutingData.
        :rtype: QueueConversationVideoEventTopicUriReference
        """
        return self._language

    @language.setter
    def language(self, language: 'QueueConversationVideoEventTopicUriReference') -> None:
        """
        Sets the language of this QueueConversationVideoEventTopicConversationRoutingData.
        A UriReference for a resource

        :param language: The language of this QueueConversationVideoEventTopicConversationRoutingData.
        :type: QueueConversationVideoEventTopicUriReference
        """
        

        self._language = language

    @property
    def priority(self) -> int:
        """
        Gets the priority of this QueueConversationVideoEventTopicConversationRoutingData.
        The priority of the conversation to use for routing decisions

        :return: The priority of this QueueConversationVideoEventTopicConversationRoutingData.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Sets the priority of this QueueConversationVideoEventTopicConversationRoutingData.
        The priority of the conversation to use for routing decisions

        :param priority: The priority of this QueueConversationVideoEventTopicConversationRoutingData.
        :type: int
        """
        

        self._priority = priority

    @property
    def skills(self) -> List['QueueConversationVideoEventTopicUriReference']:
        """
        Gets the skills of this QueueConversationVideoEventTopicConversationRoutingData.
        The skills to use for routing decisions

        :return: The skills of this QueueConversationVideoEventTopicConversationRoutingData.
        :rtype: list[QueueConversationVideoEventTopicUriReference]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List['QueueConversationVideoEventTopicUriReference']) -> None:
        """
        Sets the skills of this QueueConversationVideoEventTopicConversationRoutingData.
        The skills to use for routing decisions

        :param skills: The skills of this QueueConversationVideoEventTopicConversationRoutingData.
        :type: list[QueueConversationVideoEventTopicUriReference]
        """
        

        self._skills = skills

    @property
    def scored_agents(self) -> List['QueueConversationVideoEventTopicScoredAgent']:
        """
        Gets the scored_agents of this QueueConversationVideoEventTopicConversationRoutingData.
        A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents

        :return: The scored_agents of this QueueConversationVideoEventTopicConversationRoutingData.
        :rtype: list[QueueConversationVideoEventTopicScoredAgent]
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: List['QueueConversationVideoEventTopicScoredAgent']) -> None:
        """
        Sets the scored_agents of this QueueConversationVideoEventTopicConversationRoutingData.
        A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents

        :param scored_agents: The scored_agents of this QueueConversationVideoEventTopicConversationRoutingData.
        :type: list[QueueConversationVideoEventTopicScoredAgent]
        """
        

        self._scored_agents = scored_agents

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

