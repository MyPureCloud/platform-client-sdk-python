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
    from . import PermissionDetails

class AvailableTopic(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AvailableTopic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'id': 'str',
            'permission_details': 'list[PermissionDetails]',
            'requires_permissions': 'list[str]',
            'requires_division_permissions': 'bool',
            'requires_any_validator': 'bool',
            'enforced': 'bool',
            'visibility': 'str',
            'schema': 'dict(str, object)',
            'requires_current_user': 'bool',
            'requires_current_user_or_permission': 'bool',
            'transports': 'list[str]',
            'public_api_template_uri_paths': 'list[str]',
            'topic_parameters': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'permission_details': 'permissionDetails',
            'requires_permissions': 'requiresPermissions',
            'requires_division_permissions': 'requiresDivisionPermissions',
            'requires_any_validator': 'requiresAnyValidator',
            'enforced': 'enforced',
            'visibility': 'visibility',
            'schema': 'schema',
            'requires_current_user': 'requiresCurrentUser',
            'requires_current_user_or_permission': 'requiresCurrentUserOrPermission',
            'transports': 'transports',
            'public_api_template_uri_paths': 'publicApiTemplateUriPaths',
            'topic_parameters': 'topicParameters'
        }

        self._description = None
        self._id = None
        self._permission_details = None
        self._requires_permissions = None
        self._requires_division_permissions = None
        self._requires_any_validator = None
        self._enforced = None
        self._visibility = None
        self._schema = None
        self._requires_current_user = None
        self._requires_current_user_or_permission = None
        self._transports = None
        self._public_api_template_uri_paths = None
        self._topic_parameters = None

    @property
    def description(self) -> str:
        """
        Gets the description of this AvailableTopic.


        :return: The description of this AvailableTopic.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this AvailableTopic.


        :param description: The description of this AvailableTopic.
        :type: str
        """
        

        self._description = description

    @property
    def id(self) -> str:
        """
        Gets the id of this AvailableTopic.


        :return: The id of this AvailableTopic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AvailableTopic.


        :param id: The id of this AvailableTopic.
        :type: str
        """
        

        self._id = id

    @property
    def permission_details(self) -> List['PermissionDetails']:
        """
        Gets the permission_details of this AvailableTopic.
        Full detailed permissions required to subscribe to the topic

        :return: The permission_details of this AvailableTopic.
        :rtype: list[PermissionDetails]
        """
        return self._permission_details

    @permission_details.setter
    def permission_details(self, permission_details: List['PermissionDetails']) -> None:
        """
        Sets the permission_details of this AvailableTopic.
        Full detailed permissions required to subscribe to the topic

        :param permission_details: The permission_details of this AvailableTopic.
        :type: list[PermissionDetails]
        """
        

        self._permission_details = permission_details

    @property
    def requires_permissions(self) -> List[str]:
        """
        Gets the requires_permissions of this AvailableTopic.
        Permissions required to subscribe to the topic

        :return: The requires_permissions of this AvailableTopic.
        :rtype: list[str]
        """
        return self._requires_permissions

    @requires_permissions.setter
    def requires_permissions(self, requires_permissions: List[str]) -> None:
        """
        Sets the requires_permissions of this AvailableTopic.
        Permissions required to subscribe to the topic

        :param requires_permissions: The requires_permissions of this AvailableTopic.
        :type: list[str]
        """
        

        self._requires_permissions = requires_permissions

    @property
    def requires_division_permissions(self) -> bool:
        """
        Gets the requires_division_permissions of this AvailableTopic.
        True if the subscribing user must belong to the same division as the topic object ID

        :return: The requires_division_permissions of this AvailableTopic.
        :rtype: bool
        """
        return self._requires_division_permissions

    @requires_division_permissions.setter
    def requires_division_permissions(self, requires_division_permissions: bool) -> None:
        """
        Sets the requires_division_permissions of this AvailableTopic.
        True if the subscribing user must belong to the same division as the topic object ID

        :param requires_division_permissions: The requires_division_permissions of this AvailableTopic.
        :type: bool
        """
        

        self._requires_division_permissions = requires_division_permissions

    @property
    def requires_any_validator(self) -> bool:
        """
        Gets the requires_any_validator of this AvailableTopic.
        If multiple permissions are required for this topic, such as both requiresCurrentUser and requiresDivisionPermissions, then true here indicates that meeting any one condition will satisfy the requirements; false indicates all conditions must be met.

        :return: The requires_any_validator of this AvailableTopic.
        :rtype: bool
        """
        return self._requires_any_validator

    @requires_any_validator.setter
    def requires_any_validator(self, requires_any_validator: bool) -> None:
        """
        Sets the requires_any_validator of this AvailableTopic.
        If multiple permissions are required for this topic, such as both requiresCurrentUser and requiresDivisionPermissions, then true here indicates that meeting any one condition will satisfy the requirements; false indicates all conditions must be met.

        :param requires_any_validator: The requires_any_validator of this AvailableTopic.
        :type: bool
        """
        

        self._requires_any_validator = requires_any_validator

    @property
    def enforced(self) -> bool:
        """
        Gets the enforced of this AvailableTopic.
        Whether or not the permissions on this topic are enforced

        :return: The enforced of this AvailableTopic.
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced: bool) -> None:
        """
        Sets the enforced of this AvailableTopic.
        Whether or not the permissions on this topic are enforced

        :param enforced: The enforced of this AvailableTopic.
        :type: bool
        """
        

        self._enforced = enforced

    @property
    def visibility(self) -> str:
        """
        Gets the visibility of this AvailableTopic.
        Visibility of this topic (Public or Preview)

        :return: The visibility of this AvailableTopic.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility: str) -> None:
        """
        Sets the visibility of this AvailableTopic.
        Visibility of this topic (Public or Preview)

        :param visibility: The visibility of this AvailableTopic.
        :type: str
        """
        if isinstance(visibility, int):
            visibility = str(visibility)
        allowed_values = ["Public", "Preview"]
        if visibility.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for visibility -> " + visibility)
            self._visibility = "outdated_sdk_version"
        else:
            self._visibility = visibility

    @property
    def schema(self) -> Dict[str, object]:
        """
        Gets the schema of this AvailableTopic.


        :return: The schema of this AvailableTopic.
        :rtype: dict(str, object)
        """
        return self._schema

    @schema.setter
    def schema(self, schema: Dict[str, object]) -> None:
        """
        Sets the schema of this AvailableTopic.


        :param schema: The schema of this AvailableTopic.
        :type: dict(str, object)
        """
        

        self._schema = schema

    @property
    def requires_current_user(self) -> bool:
        """
        Gets the requires_current_user of this AvailableTopic.
        True if the topic user ID is required to match the subscribing user ID

        :return: The requires_current_user of this AvailableTopic.
        :rtype: bool
        """
        return self._requires_current_user

    @requires_current_user.setter
    def requires_current_user(self, requires_current_user: bool) -> None:
        """
        Sets the requires_current_user of this AvailableTopic.
        True if the topic user ID is required to match the subscribing user ID

        :param requires_current_user: The requires_current_user of this AvailableTopic.
        :type: bool
        """
        

        self._requires_current_user = requires_current_user

    @property
    def requires_current_user_or_permission(self) -> bool:
        """
        Gets the requires_current_user_or_permission of this AvailableTopic.
        True if permissions are only required when the topic user ID does not match the subscribing user ID

        :return: The requires_current_user_or_permission of this AvailableTopic.
        :rtype: bool
        """
        return self._requires_current_user_or_permission

    @requires_current_user_or_permission.setter
    def requires_current_user_or_permission(self, requires_current_user_or_permission: bool) -> None:
        """
        Sets the requires_current_user_or_permission of this AvailableTopic.
        True if permissions are only required when the topic user ID does not match the subscribing user ID

        :param requires_current_user_or_permission: The requires_current_user_or_permission of this AvailableTopic.
        :type: bool
        """
        

        self._requires_current_user_or_permission = requires_current_user_or_permission

    @property
    def transports(self) -> List[str]:
        """
        Gets the transports of this AvailableTopic.
        Transports that support events for the topic

        :return: The transports of this AvailableTopic.
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports: List[str]) -> None:
        """
        Sets the transports of this AvailableTopic.
        Transports that support events for the topic

        :param transports: The transports of this AvailableTopic.
        :type: list[str]
        """
        

        self._transports = transports

    @property
    def public_api_template_uri_paths(self) -> List[str]:
        """
        Gets the public_api_template_uri_paths of this AvailableTopic.


        :return: The public_api_template_uri_paths of this AvailableTopic.
        :rtype: list[str]
        """
        return self._public_api_template_uri_paths

    @public_api_template_uri_paths.setter
    def public_api_template_uri_paths(self, public_api_template_uri_paths: List[str]) -> None:
        """
        Sets the public_api_template_uri_paths of this AvailableTopic.


        :param public_api_template_uri_paths: The public_api_template_uri_paths of this AvailableTopic.
        :type: list[str]
        """
        

        self._public_api_template_uri_paths = public_api_template_uri_paths

    @property
    def topic_parameters(self) -> List[str]:
        """
        Gets the topic_parameters of this AvailableTopic.
        Parameters in the topic name that can be substituted, in the order they appear in the topic name

        :return: The topic_parameters of this AvailableTopic.
        :rtype: list[str]
        """
        return self._topic_parameters

    @topic_parameters.setter
    def topic_parameters(self, topic_parameters: List[str]) -> None:
        """
        Sets the topic_parameters of this AvailableTopic.
        Parameters in the topic name that can be substituted, in the order they appear in the topic name

        :param topic_parameters: The topic_parameters of this AvailableTopic.
        :type: list[str]
        """
        

        self._topic_parameters = topic_parameters

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

