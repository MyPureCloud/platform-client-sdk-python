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
    from . import DialerRulesetConfigChangeRule
    from . import DialerRulesetConfigChangeUriReference

class DialerRulesetConfigChangeRuleSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerRulesetConfigChangeRuleSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_list': 'DialerRulesetConfigChangeUriReference',
            'queue': 'DialerRulesetConfigChangeUriReference',
            'rules': 'list[DialerRulesetConfigChangeRule]',
            'additional_properties': 'dict(str, object)',
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int'
        }

        self.attribute_map = {
            'contact_list': 'contactList',
            'queue': 'queue',
            'rules': 'rules',
            'additional_properties': 'additionalProperties',
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version'
        }

        self._contact_list = None
        self._queue = None
        self._rules = None
        self._additional_properties = None
        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None

    @property
    def contact_list(self) -> 'DialerRulesetConfigChangeUriReference':
        """
        Gets the contact_list of this DialerRulesetConfigChangeRuleSet.


        :return: The contact_list of this DialerRulesetConfigChangeRuleSet.
        :rtype: DialerRulesetConfigChangeUriReference
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list: 'DialerRulesetConfigChangeUriReference') -> None:
        """
        Sets the contact_list of this DialerRulesetConfigChangeRuleSet.


        :param contact_list: The contact_list of this DialerRulesetConfigChangeRuleSet.
        :type: DialerRulesetConfigChangeUriReference
        """
        

        self._contact_list = contact_list

    @property
    def queue(self) -> 'DialerRulesetConfigChangeUriReference':
        """
        Gets the queue of this DialerRulesetConfigChangeRuleSet.
        A UriReference for a resource

        :return: The queue of this DialerRulesetConfigChangeRuleSet.
        :rtype: DialerRulesetConfigChangeUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'DialerRulesetConfigChangeUriReference') -> None:
        """
        Sets the queue of this DialerRulesetConfigChangeRuleSet.
        A UriReference for a resource

        :param queue: The queue of this DialerRulesetConfigChangeRuleSet.
        :type: DialerRulesetConfigChangeUriReference
        """
        

        self._queue = queue

    @property
    def rules(self) -> List['DialerRulesetConfigChangeRule']:
        """
        Gets the rules of this DialerRulesetConfigChangeRuleSet.


        :return: The rules of this DialerRulesetConfigChangeRuleSet.
        :rtype: list[DialerRulesetConfigChangeRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules: List['DialerRulesetConfigChangeRule']) -> None:
        """
        Sets the rules of this DialerRulesetConfigChangeRuleSet.


        :param rules: The rules of this DialerRulesetConfigChangeRuleSet.
        :type: list[DialerRulesetConfigChangeRule]
        """
        

        self._rules = rules

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerRulesetConfigChangeRuleSet.


        :return: The additional_properties of this DialerRulesetConfigChangeRuleSet.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerRulesetConfigChangeRuleSet.


        :param additional_properties: The additional_properties of this DialerRulesetConfigChangeRuleSet.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def id(self) -> str:
        """
        Gets the id of this DialerRulesetConfigChangeRuleSet.
        The globally unique identifier for the object.

        :return: The id of this DialerRulesetConfigChangeRuleSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DialerRulesetConfigChangeRuleSet.
        The globally unique identifier for the object.

        :param id: The id of this DialerRulesetConfigChangeRuleSet.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DialerRulesetConfigChangeRuleSet.
        The UI-visible name of the object

        :return: The name of this DialerRulesetConfigChangeRuleSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DialerRulesetConfigChangeRuleSet.
        The UI-visible name of the object

        :param name: The name of this DialerRulesetConfigChangeRuleSet.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this DialerRulesetConfigChangeRuleSet.
        Creation time of the entity

        :return: The date_created of this DialerRulesetConfigChangeRuleSet.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this DialerRulesetConfigChangeRuleSet.
        Creation time of the entity

        :param date_created: The date_created of this DialerRulesetConfigChangeRuleSet.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this DialerRulesetConfigChangeRuleSet.
        Last modified time of the entity

        :return: The date_modified of this DialerRulesetConfigChangeRuleSet.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this DialerRulesetConfigChangeRuleSet.
        Last modified time of the entity

        :param date_modified: The date_modified of this DialerRulesetConfigChangeRuleSet.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this DialerRulesetConfigChangeRuleSet.
        Required for updates, must match the version number of the most recent update

        :return: The version of this DialerRulesetConfigChangeRuleSet.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this DialerRulesetConfigChangeRuleSet.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this DialerRulesetConfigChangeRuleSet.
        :type: int
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

