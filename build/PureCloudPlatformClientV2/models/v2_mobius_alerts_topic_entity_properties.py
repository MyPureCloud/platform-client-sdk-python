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


class V2MobiusAlertsTopicEntityProperties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        V2MobiusAlertsTopicEntityProperties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entity_type': 'str',
            'user_display_name': 'str',
            'group_display_name': 'str',
            'queue_display_name': 'str'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'user_display_name': 'userDisplayName',
            'group_display_name': 'groupDisplayName',
            'queue_display_name': 'queueDisplayName'
        }

        self._entity_type = None
        self._user_display_name = None
        self._group_display_name = None
        self._queue_display_name = None

    @property
    def entity_type(self) -> str:
        """
        Gets the entity_type of this V2MobiusAlertsTopicEntityProperties.


        :return: The entity_type of this V2MobiusAlertsTopicEntityProperties.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str) -> None:
        """
        Sets the entity_type of this V2MobiusAlertsTopicEntityProperties.


        :param entity_type: The entity_type of this V2MobiusAlertsTopicEntityProperties.
        :type: str
        """
        if isinstance(entity_type, int):
            entity_type = str(entity_type)
        allowed_values = ["Organization", "User", "Queue", "Group", "Edge"]
        if entity_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for entity_type -> " + entity_type)
            self._entity_type = "outdated_sdk_version"
        else:
            self._entity_type = entity_type

    @property
    def user_display_name(self) -> str:
        """
        Gets the user_display_name of this V2MobiusAlertsTopicEntityProperties.


        :return: The user_display_name of this V2MobiusAlertsTopicEntityProperties.
        :rtype: str
        """
        return self._user_display_name

    @user_display_name.setter
    def user_display_name(self, user_display_name: str) -> None:
        """
        Sets the user_display_name of this V2MobiusAlertsTopicEntityProperties.


        :param user_display_name: The user_display_name of this V2MobiusAlertsTopicEntityProperties.
        :type: str
        """
        

        self._user_display_name = user_display_name

    @property
    def group_display_name(self) -> str:
        """
        Gets the group_display_name of this V2MobiusAlertsTopicEntityProperties.


        :return: The group_display_name of this V2MobiusAlertsTopicEntityProperties.
        :rtype: str
        """
        return self._group_display_name

    @group_display_name.setter
    def group_display_name(self, group_display_name: str) -> None:
        """
        Sets the group_display_name of this V2MobiusAlertsTopicEntityProperties.


        :param group_display_name: The group_display_name of this V2MobiusAlertsTopicEntityProperties.
        :type: str
        """
        

        self._group_display_name = group_display_name

    @property
    def queue_display_name(self) -> str:
        """
        Gets the queue_display_name of this V2MobiusAlertsTopicEntityProperties.


        :return: The queue_display_name of this V2MobiusAlertsTopicEntityProperties.
        :rtype: str
        """
        return self._queue_display_name

    @queue_display_name.setter
    def queue_display_name(self, queue_display_name: str) -> None:
        """
        Sets the queue_display_name of this V2MobiusAlertsTopicEntityProperties.


        :param queue_display_name: The queue_display_name of this V2MobiusAlertsTopicEntityProperties.
        :type: str
        """
        

        self._queue_display_name = queue_display_name

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
