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
    from . import DomainEntityRef
    from . import RoleDivision

class OAuthClientListing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OAuthClientListing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'access_token_validity_seconds': 'int',
            'description': 'str',
            'registered_redirect_uri': 'list[str]',
            'secret': 'str',
            'role_ids': 'list[str]',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'DomainEntityRef',
            'modified_by': 'DomainEntityRef',
            'scope': 'list[str]',
            'role_divisions': 'list[RoleDivision]',
            'state': 'str',
            'date_to_delete': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'access_token_validity_seconds': 'accessTokenValiditySeconds',
            'description': 'description',
            'registered_redirect_uri': 'registeredRedirectUri',
            'secret': 'secret',
            'role_ids': 'roleIds',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'scope': 'scope',
            'role_divisions': 'roleDivisions',
            'state': 'state',
            'date_to_delete': 'dateToDelete',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._access_token_validity_seconds = None
        self._description = None
        self._registered_redirect_uri = None
        self._secret = None
        self._role_ids = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._scope = None
        self._role_divisions = None
        self._state = None
        self._date_to_delete = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this OAuthClientListing.
        The globally unique identifier for the object.

        :return: The id of this OAuthClientListing.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this OAuthClientListing.
        The globally unique identifier for the object.

        :param id: The id of this OAuthClientListing.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this OAuthClientListing.
        The name of the OAuth client.

        :return: The name of this OAuthClientListing.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this OAuthClientListing.
        The name of the OAuth client.

        :param name: The name of this OAuthClientListing.
        :type: str
        """
        

        self._name = name

    @property
    def access_token_validity_seconds(self) -> int:
        """
        Gets the access_token_validity_seconds of this OAuthClientListing.
        The number of seconds, between 5mins and 48hrs, until tokens created with this client expire. If this field is omitted, a default of 24 hours will be applied.

        :return: The access_token_validity_seconds of this OAuthClientListing.
        :rtype: int
        """
        return self._access_token_validity_seconds

    @access_token_validity_seconds.setter
    def access_token_validity_seconds(self, access_token_validity_seconds: int) -> None:
        """
        Sets the access_token_validity_seconds of this OAuthClientListing.
        The number of seconds, between 5mins and 48hrs, until tokens created with this client expire. If this field is omitted, a default of 24 hours will be applied.

        :param access_token_validity_seconds: The access_token_validity_seconds of this OAuthClientListing.
        :type: int
        """
        

        self._access_token_validity_seconds = access_token_validity_seconds

    @property
    def description(self) -> str:
        """
        Gets the description of this OAuthClientListing.


        :return: The description of this OAuthClientListing.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this OAuthClientListing.


        :param description: The description of this OAuthClientListing.
        :type: str
        """
        

        self._description = description

    @property
    def registered_redirect_uri(self) -> List[str]:
        """
        Gets the registered_redirect_uri of this OAuthClientListing.
        List of allowed callbacks for this client. For example: https://myap.example.com/auth/callback

        :return: The registered_redirect_uri of this OAuthClientListing.
        :rtype: list[str]
        """
        return self._registered_redirect_uri

    @registered_redirect_uri.setter
    def registered_redirect_uri(self, registered_redirect_uri: List[str]) -> None:
        """
        Sets the registered_redirect_uri of this OAuthClientListing.
        List of allowed callbacks for this client. For example: https://myap.example.com/auth/callback

        :param registered_redirect_uri: The registered_redirect_uri of this OAuthClientListing.
        :type: list[str]
        """
        

        self._registered_redirect_uri = registered_redirect_uri

    @property
    def secret(self) -> str:
        """
        Gets the secret of this OAuthClientListing.
        System created secret assigned to this client. Secrets are required for code authorization and client credential grants.

        :return: The secret of this OAuthClientListing.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret: str) -> None:
        """
        Sets the secret of this OAuthClientListing.
        System created secret assigned to this client. Secrets are required for code authorization and client credential grants.

        :param secret: The secret of this OAuthClientListing.
        :type: str
        """
        

        self._secret = secret

    @property
    def role_ids(self) -> List[str]:
        """
        Gets the role_ids of this OAuthClientListing.
        Deprecated. Use roleDivisions instead.

        :return: The role_ids of this OAuthClientListing.
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids: List[str]) -> None:
        """
        Sets the role_ids of this OAuthClientListing.
        Deprecated. Use roleDivisions instead.

        :param role_ids: The role_ids of this OAuthClientListing.
        :type: list[str]
        """
        

        self._role_ids = role_ids

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this OAuthClientListing.
        Date this client was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this OAuthClientListing.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this OAuthClientListing.
        Date this client was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this OAuthClientListing.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this OAuthClientListing.
        Date this client was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this OAuthClientListing.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this OAuthClientListing.
        Date this client was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this OAuthClientListing.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def created_by(self) -> 'DomainEntityRef':
        """
        Gets the created_by of this OAuthClientListing.
        User that created this client

        :return: The created_by of this OAuthClientListing.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'DomainEntityRef') -> None:
        """
        Sets the created_by of this OAuthClientListing.
        User that created this client

        :param created_by: The created_by of this OAuthClientListing.
        :type: DomainEntityRef
        """
        

        self._created_by = created_by

    @property
    def modified_by(self) -> 'DomainEntityRef':
        """
        Gets the modified_by of this OAuthClientListing.
        User that last modified this client

        :return: The modified_by of this OAuthClientListing.
        :rtype: DomainEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'DomainEntityRef') -> None:
        """
        Sets the modified_by of this OAuthClientListing.
        User that last modified this client

        :param modified_by: The modified_by of this OAuthClientListing.
        :type: DomainEntityRef
        """
        

        self._modified_by = modified_by

    @property
    def scope(self) -> List[str]:
        """
        Gets the scope of this OAuthClientListing.
        The scope requested by this client. Scopes only apply to clients not using the client_credential grant

        :return: The scope of this OAuthClientListing.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope: List[str]) -> None:
        """
        Sets the scope of this OAuthClientListing.
        The scope requested by this client. Scopes only apply to clients not using the client_credential grant

        :param scope: The scope of this OAuthClientListing.
        :type: list[str]
        """
        

        self._scope = scope

    @property
    def role_divisions(self) -> List['RoleDivision']:
        """
        Gets the role_divisions of this OAuthClientListing.
        Set of roles and their corresponding divisions associated with this client. Roles and divisions only apply to clients using the client_credential grant

        :return: The role_divisions of this OAuthClientListing.
        :rtype: list[RoleDivision]
        """
        return self._role_divisions

    @role_divisions.setter
    def role_divisions(self, role_divisions: List['RoleDivision']) -> None:
        """
        Sets the role_divisions of this OAuthClientListing.
        Set of roles and their corresponding divisions associated with this client. Roles and divisions only apply to clients using the client_credential grant

        :param role_divisions: The role_divisions of this OAuthClientListing.
        :type: list[RoleDivision]
        """
        

        self._role_divisions = role_divisions

    @property
    def state(self) -> str:
        """
        Gets the state of this OAuthClientListing.
        The state of the OAuth client. Active: The OAuth client can be used to create access tokens. This is the default state. Disabled: Access tokens created by the client are invalid and new ones cannot be created. Inactive: Access tokens cannot be created with this OAuth client and it will be deleted.

        :return: The state of this OAuthClientListing.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this OAuthClientListing.
        The state of the OAuth client. Active: The OAuth client can be used to create access tokens. This is the default state. Disabled: Access tokens created by the client are invalid and new ones cannot be created. Inactive: Access tokens cannot be created with this OAuth client and it will be deleted.

        :param state: The state of this OAuthClientListing.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["active", "disabled", "inactive"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def date_to_delete(self) -> datetime:
        """
        Gets the date_to_delete of this OAuthClientListing.
        The time at which this client will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_to_delete of this OAuthClientListing.
        :rtype: datetime
        """
        return self._date_to_delete

    @date_to_delete.setter
    def date_to_delete(self, date_to_delete: datetime) -> None:
        """
        Sets the date_to_delete of this OAuthClientListing.
        The time at which this client will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_to_delete: The date_to_delete of this OAuthClientListing.
        :type: datetime
        """
        

        self._date_to_delete = date_to_delete

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this OAuthClientListing.
        The URI for this object

        :return: The self_uri of this OAuthClientListing.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this OAuthClientListing.
        The URI for this object

        :param self_uri: The self_uri of this OAuthClientListing.
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

