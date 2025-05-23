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
    from . import GroupContact
    from . import Image

class GroupUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GroupUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'state': 'str',
            'version': 'int',
            'images': 'list[Image]',
            'addresses': 'list[GroupContact]',
            'rules_visible': 'bool',
            'visibility': 'str',
            'roles_enabled': 'bool',
            'include_owners': 'bool',
            'calls_enabled': 'bool',
            'owner_ids': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'state': 'state',
            'version': 'version',
            'images': 'images',
            'addresses': 'addresses',
            'rules_visible': 'rulesVisible',
            'visibility': 'visibility',
            'roles_enabled': 'rolesEnabled',
            'include_owners': 'includeOwners',
            'calls_enabled': 'callsEnabled',
            'owner_ids': 'ownerIds',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._state = None
        self._version = None
        self._images = None
        self._addresses = None
        self._rules_visible = None
        self._visibility = None
        self._roles_enabled = None
        self._include_owners = None
        self._calls_enabled = None
        self._owner_ids = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this GroupUpdate.
        The globally unique identifier for the object.

        :return: The id of this GroupUpdate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this GroupUpdate.
        The globally unique identifier for the object.

        :param id: The id of this GroupUpdate.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this GroupUpdate.
        The group name.

        :return: The name of this GroupUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this GroupUpdate.
        The group name.

        :param name: The name of this GroupUpdate.
        :type: str
        """
        

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this GroupUpdate.


        :return: The description of this GroupUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this GroupUpdate.


        :param description: The description of this GroupUpdate.
        :type: str
        """
        

        self._description = description

    @property
    def state(self) -> str:
        """
        Gets the state of this GroupUpdate.
        State of the group.

        :return: The state of this GroupUpdate.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this GroupUpdate.
        State of the group.

        :param state: The state of this GroupUpdate.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def version(self) -> int:
        """
        Gets the version of this GroupUpdate.
        Current version for this resource.

        :return: The version of this GroupUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this GroupUpdate.
        Current version for this resource.

        :param version: The version of this GroupUpdate.
        :type: int
        """
        

        self._version = version

    @property
    def images(self) -> List['Image']:
        """
        Gets the images of this GroupUpdate.


        :return: The images of this GroupUpdate.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images: List['Image']) -> None:
        """
        Sets the images of this GroupUpdate.


        :param images: The images of this GroupUpdate.
        :type: list[Image]
        """
        

        self._images = images

    @property
    def addresses(self) -> List['GroupContact']:
        """
        Gets the addresses of this GroupUpdate.


        :return: The addresses of this GroupUpdate.
        :rtype: list[GroupContact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List['GroupContact']) -> None:
        """
        Sets the addresses of this GroupUpdate.


        :param addresses: The addresses of this GroupUpdate.
        :type: list[GroupContact]
        """
        

        self._addresses = addresses

    @property
    def rules_visible(self) -> bool:
        """
        Gets the rules_visible of this GroupUpdate.
        Are membership rules visible to the person requesting to view the group

        :return: The rules_visible of this GroupUpdate.
        :rtype: bool
        """
        return self._rules_visible

    @rules_visible.setter
    def rules_visible(self, rules_visible: bool) -> None:
        """
        Sets the rules_visible of this GroupUpdate.
        Are membership rules visible to the person requesting to view the group

        :param rules_visible: The rules_visible of this GroupUpdate.
        :type: bool
        """
        

        self._rules_visible = rules_visible

    @property
    def visibility(self) -> str:
        """
        Gets the visibility of this GroupUpdate.
        Who can view this group

        :return: The visibility of this GroupUpdate.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility: str) -> None:
        """
        Sets the visibility of this GroupUpdate.
        Who can view this group

        :param visibility: The visibility of this GroupUpdate.
        :type: str
        """
        if isinstance(visibility, int):
            visibility = str(visibility)
        allowed_values = ["public", "ownerIds", "members"]
        if visibility.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for visibility -> " + visibility)
            self._visibility = "outdated_sdk_version"
        else:
            self._visibility = visibility

    @property
    def roles_enabled(self) -> bool:
        """
        Gets the roles_enabled of this GroupUpdate.
        Allow roles to be assigned to this group

        :return: The roles_enabled of this GroupUpdate.
        :rtype: bool
        """
        return self._roles_enabled

    @roles_enabled.setter
    def roles_enabled(self, roles_enabled: bool) -> None:
        """
        Sets the roles_enabled of this GroupUpdate.
        Allow roles to be assigned to this group

        :param roles_enabled: The roles_enabled of this GroupUpdate.
        :type: bool
        """
        

        self._roles_enabled = roles_enabled

    @property
    def include_owners(self) -> bool:
        """
        Gets the include_owners of this GroupUpdate.
        Allow owners to be included as members of the group

        :return: The include_owners of this GroupUpdate.
        :rtype: bool
        """
        return self._include_owners

    @include_owners.setter
    def include_owners(self, include_owners: bool) -> None:
        """
        Sets the include_owners of this GroupUpdate.
        Allow owners to be included as members of the group

        :param include_owners: The include_owners of this GroupUpdate.
        :type: bool
        """
        

        self._include_owners = include_owners

    @property
    def calls_enabled(self) -> bool:
        """
        Gets the calls_enabled of this GroupUpdate.
        Allow calls to be placed to this group.

        :return: The calls_enabled of this GroupUpdate.
        :rtype: bool
        """
        return self._calls_enabled

    @calls_enabled.setter
    def calls_enabled(self, calls_enabled: bool) -> None:
        """
        Sets the calls_enabled of this GroupUpdate.
        Allow calls to be placed to this group.

        :param calls_enabled: The calls_enabled of this GroupUpdate.
        :type: bool
        """
        

        self._calls_enabled = calls_enabled

    @property
    def owner_ids(self) -> List[str]:
        """
        Gets the owner_ids of this GroupUpdate.
        Owners of the group

        :return: The owner_ids of this GroupUpdate.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids: List[str]) -> None:
        """
        Sets the owner_ids of this GroupUpdate.
        Owners of the group

        :param owner_ids: The owner_ids of this GroupUpdate.
        :type: list[str]
        """
        

        self._owner_ids = owner_ids

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this GroupUpdate.
        The URI for this object

        :return: The self_uri of this GroupUpdate.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this GroupUpdate.
        The URI for this object

        :param self_uri: The self_uri of this GroupUpdate.
        :type: str
        """
        

        self._self_uri = self_uri

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

