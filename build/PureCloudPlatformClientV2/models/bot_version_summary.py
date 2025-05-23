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


class BotVersionSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BotVersionSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'description': 'str',
            'bot_composite_tag': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'description': 'description',
            'bot_composite_tag': 'botCompositeTag',
            'version': 'version'
        }

        self._name = None
        self._id = None
        self._description = None
        self._bot_composite_tag = None
        self._version = None

    @property
    def name(self) -> str:
        """
        Gets the name of this BotVersionSummary.
        The name of the bot.

        :return: The name of this BotVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this BotVersionSummary.
        The name of the bot.

        :param name: The name of this BotVersionSummary.
        :type: str
        """
        

        self._name = name

    @property
    def id(self) -> str:
        """
        Gets the id of this BotVersionSummary.
        The id of the bot.

        :return: The id of this BotVersionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BotVersionSummary.
        The id of the bot.

        :param id: The id of this BotVersionSummary.
        :type: str
        """
        

        self._id = id

    @property
    def description(self) -> str:
        """
        Gets the description of this BotVersionSummary.
        An optional description of the bot.

        :return: The description of this BotVersionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this BotVersionSummary.
        An optional description of the bot.

        :param description: The description of this BotVersionSummary.
        :type: str
        """
        

        self._description = description

    @property
    def bot_composite_tag(self) -> str:
        """
        Gets the bot_composite_tag of this BotVersionSummary.
        A system-generated string that contains metadata about this bot.

        :return: The bot_composite_tag of this BotVersionSummary.
        :rtype: str
        """
        return self._bot_composite_tag

    @bot_composite_tag.setter
    def bot_composite_tag(self, bot_composite_tag: str) -> None:
        """
        Sets the bot_composite_tag of this BotVersionSummary.
        A system-generated string that contains metadata about this bot.

        :param bot_composite_tag: The bot_composite_tag of this BotVersionSummary.
        :type: str
        """
        

        self._bot_composite_tag = bot_composite_tag

    @property
    def version(self) -> str:
        """
        Gets the version of this BotVersionSummary.
        The name of the version.

        :return: The version of this BotVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Sets the version of this BotVersionSummary.
        The name of the version.

        :param version: The version of this BotVersionSummary.
        :type: str
        """
        

        self._version = version

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

