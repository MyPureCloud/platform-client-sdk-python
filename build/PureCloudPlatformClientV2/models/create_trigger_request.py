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

class CreateTriggerRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateTriggerRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'target': 'TriggerTarget',
            'enabled': 'bool',
            'match_criteria': 'list[MatchCriteria]',
            'name': 'str',
            'topic_name': 'str',
            'event_ttl_seconds': 'int',
            'description': 'str'
        }

        self.attribute_map = {
            'target': 'target',
            'enabled': 'enabled',
            'match_criteria': 'matchCriteria',
            'name': 'name',
            'topic_name': 'topicName',
            'event_ttl_seconds': 'eventTTLSeconds',
            'description': 'description'
        }

        self._target = None
        self._enabled = None
        self._match_criteria = None
        self._name = None
        self._topic_name = None
        self._event_ttl_seconds = None
        self._description = None

    @property
    def target(self):
        """
        Gets the target of this CreateTriggerRequest.
        The target to invoke when a matching event is received

        :return: The target of this CreateTriggerRequest.
        :rtype: TriggerTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateTriggerRequest.
        The target to invoke when a matching event is received

        :param target: The target of this CreateTriggerRequest.
        :type: TriggerTarget
        """
        

        self._target = target

    @property
    def enabled(self):
        """
        Gets the enabled of this CreateTriggerRequest.
        Boolean indicating if Trigger is enabled

        :return: The enabled of this CreateTriggerRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CreateTriggerRequest.
        Boolean indicating if Trigger is enabled

        :param enabled: The enabled of this CreateTriggerRequest.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def match_criteria(self):
        """
        Gets the match_criteria of this CreateTriggerRequest.
        The configuration for when a trigger is considered to be a match for an event. When not provided, all events will fire the trigger

        :return: The match_criteria of this CreateTriggerRequest.
        :rtype: list[MatchCriteria]
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, match_criteria):
        """
        Sets the match_criteria of this CreateTriggerRequest.
        The configuration for when a trigger is considered to be a match for an event. When not provided, all events will fire the trigger

        :param match_criteria: The match_criteria of this CreateTriggerRequest.
        :type: list[MatchCriteria]
        """
        

        self._match_criteria = match_criteria

    @property
    def name(self):
        """
        Gets the name of this CreateTriggerRequest.
        The name of the trigger

        :return: The name of this CreateTriggerRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTriggerRequest.
        The name of the trigger

        :param name: The name of this CreateTriggerRequest.
        :type: str
        """
        

        self._name = name

    @property
    def topic_name(self):
        """
        Gets the topic_name of this CreateTriggerRequest.
        The topic that will cause the trigger to be invoked. Cannot be updated after creation. Valid topics can be found at /processautomation/triggers/topics 

        :return: The topic_name of this CreateTriggerRequest.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """
        Sets the topic_name of this CreateTriggerRequest.
        The topic that will cause the trigger to be invoked. Cannot be updated after creation. Valid topics can be found at /processautomation/triggers/topics 

        :param topic_name: The topic_name of this CreateTriggerRequest.
        :type: str
        """
        

        self._topic_name = topic_name

    @property
    def event_ttl_seconds(self):
        """
        Gets the event_ttl_seconds of this CreateTriggerRequest.
        How long each event is meaningful after origination, in seconds. Events older than this threshold may be dropped if the platform is delayed in processing events. Unset means events are valid indefinitely.

        :return: The event_ttl_seconds of this CreateTriggerRequest.
        :rtype: int
        """
        return self._event_ttl_seconds

    @event_ttl_seconds.setter
    def event_ttl_seconds(self, event_ttl_seconds):
        """
        Sets the event_ttl_seconds of this CreateTriggerRequest.
        How long each event is meaningful after origination, in seconds. Events older than this threshold may be dropped if the platform is delayed in processing events. Unset means events are valid indefinitely.

        :param event_ttl_seconds: The event_ttl_seconds of this CreateTriggerRequest.
        :type: int
        """
        

        self._event_ttl_seconds = event_ttl_seconds

    @property
    def description(self):
        """
        Gets the description of this CreateTriggerRequest.
        Description of the trigger. Can be up to 512 characters in length.

        :return: The description of this CreateTriggerRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTriggerRequest.
        Description of the trigger. Can be up to 512 characters in length.

        :param description: The description of this CreateTriggerRequest.
        :type: str
        """
        

        self._description = description

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
