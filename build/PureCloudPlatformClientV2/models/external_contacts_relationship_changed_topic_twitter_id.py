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


class ExternalContactsRelationshipChangedTopicTwitterId(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalContactsRelationshipChangedTopicTwitterId - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'screen_name': 'str',
            'verified': 'bool',
            'profile_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'screen_name': 'screenName',
            'verified': 'verified',
            'profile_url': 'profileUrl'
        }

        self._id = None
        self._name = None
        self._screen_name = None
        self._verified = None
        self._profile_url = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ExternalContactsRelationshipChangedTopicTwitterId.


        :return: The id of this ExternalContactsRelationshipChangedTopicTwitterId.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ExternalContactsRelationshipChangedTopicTwitterId.


        :param id: The id of this ExternalContactsRelationshipChangedTopicTwitterId.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ExternalContactsRelationshipChangedTopicTwitterId.


        :return: The name of this ExternalContactsRelationshipChangedTopicTwitterId.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ExternalContactsRelationshipChangedTopicTwitterId.


        :param name: The name of this ExternalContactsRelationshipChangedTopicTwitterId.
        :type: str
        """
        

        self._name = name

    @property
    def screen_name(self) -> str:
        """
        Gets the screen_name of this ExternalContactsRelationshipChangedTopicTwitterId.


        :return: The screen_name of this ExternalContactsRelationshipChangedTopicTwitterId.
        :rtype: str
        """
        return self._screen_name

    @screen_name.setter
    def screen_name(self, screen_name: str) -> None:
        """
        Sets the screen_name of this ExternalContactsRelationshipChangedTopicTwitterId.


        :param screen_name: The screen_name of this ExternalContactsRelationshipChangedTopicTwitterId.
        :type: str
        """
        

        self._screen_name = screen_name

    @property
    def verified(self) -> bool:
        """
        Gets the verified of this ExternalContactsRelationshipChangedTopicTwitterId.


        :return: The verified of this ExternalContactsRelationshipChangedTopicTwitterId.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified: bool) -> None:
        """
        Sets the verified of this ExternalContactsRelationshipChangedTopicTwitterId.


        :param verified: The verified of this ExternalContactsRelationshipChangedTopicTwitterId.
        :type: bool
        """
        

        self._verified = verified

    @property
    def profile_url(self) -> str:
        """
        Gets the profile_url of this ExternalContactsRelationshipChangedTopicTwitterId.


        :return: The profile_url of this ExternalContactsRelationshipChangedTopicTwitterId.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url: str) -> None:
        """
        Sets the profile_url of this ExternalContactsRelationshipChangedTopicTwitterId.


        :param profile_url: The profile_url of this ExternalContactsRelationshipChangedTopicTwitterId.
        :type: str
        """
        

        self._profile_url = profile_url

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

