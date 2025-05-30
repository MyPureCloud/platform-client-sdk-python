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
    from . import ScimEmail
    from . import ScimPhoneNumber
    from . import ScimUserExtensions
    from . import ScimUserRole
    from . import ScimV2EnterpriseUser
    from . import ScimV2GroupReference

class ScimV2CreateUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScimV2CreateUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'schemas': 'list[str]',
            'active': 'bool',
            'user_name': 'str',
            'display_name': 'str',
            'password': 'str',
            'title': 'str',
            'phone_numbers': 'list[ScimPhoneNumber]',
            'emails': 'list[ScimEmail]',
            'external_id': 'str',
            'groups': 'list[ScimV2GroupReference]',
            'roles': 'list[ScimUserRole]',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'ScimV2EnterpriseUser',
            'urnietfparamsscimschemasextensiongenesyspurecloud2_0_user': 'ScimUserExtensions'
        }

        self.attribute_map = {
            'schemas': 'schemas',
            'active': 'active',
            'user_name': 'userName',
            'display_name': 'displayName',
            'password': 'password',
            'title': 'title',
            'phone_numbers': 'phoneNumbers',
            'emails': 'emails',
            'external_id': 'externalId',
            'groups': 'groups',
            'roles': 'roles',
            'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User',
            'urnietfparamsscimschemasextensiongenesyspurecloud2_0_user': 'urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User'
        }

        self._schemas = None
        self._active = None
        self._user_name = None
        self._display_name = None
        self._password = None
        self._title = None
        self._phone_numbers = None
        self._emails = None
        self._external_id = None
        self._groups = None
        self._roles = None
        self._urnietfparamsscimschemasextensionenterprise2_0_user = None
        self._urnietfparamsscimschemasextensiongenesyspurecloud2_0_user = None

    @property
    def schemas(self) -> List[str]:
        """
        Gets the schemas of this ScimV2CreateUser.
        The list of supported schemas.

        :return: The schemas of this ScimV2CreateUser.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas: List[str]) -> None:
        """
        Sets the schemas of this ScimV2CreateUser.
        The list of supported schemas.

        :param schemas: The schemas of this ScimV2CreateUser.
        :type: list[str]
        """
        

        self._schemas = schemas

    @property
    def active(self) -> bool:
        """
        Gets the active of this ScimV2CreateUser.
        Indicates whether the user's administrative status is active.

        :return: The active of this ScimV2CreateUser.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool) -> None:
        """
        Sets the active of this ScimV2CreateUser.
        Indicates whether the user's administrative status is active.

        :param active: The active of this ScimV2CreateUser.
        :type: bool
        """
        

        self._active = active

    @property
    def user_name(self) -> str:
        """
        Gets the user_name of this ScimV2CreateUser.
        The user's Genesys Cloud email address. Must be unique.

        :return: The user_name of this ScimV2CreateUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str) -> None:
        """
        Sets the user_name of this ScimV2CreateUser.
        The user's Genesys Cloud email address. Must be unique.

        :param user_name: The user_name of this ScimV2CreateUser.
        :type: str
        """
        

        self._user_name = user_name

    @property
    def display_name(self) -> str:
        """
        Gets the display_name of this ScimV2CreateUser.
        The display name of the user.

        :return: The display_name of this ScimV2CreateUser.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str) -> None:
        """
        Sets the display_name of this ScimV2CreateUser.
        The display name of the user.

        :param display_name: The display_name of this ScimV2CreateUser.
        :type: str
        """
        

        self._display_name = display_name

    @property
    def password(self) -> str:
        """
        Gets the password of this ScimV2CreateUser.
        The new password for the Genesys Cloud user. Does not return an existing password. When creating a user, if a password is not supplied, then a password will be randomly generated that is 40 characters in length and contains five characters from each of the password policy groups.

        :return: The password of this ScimV2CreateUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        """
        Sets the password of this ScimV2CreateUser.
        The new password for the Genesys Cloud user. Does not return an existing password. When creating a user, if a password is not supplied, then a password will be randomly generated that is 40 characters in length and contains five characters from each of the password policy groups.

        :param password: The password of this ScimV2CreateUser.
        :type: str
        """
        

        self._password = password

    @property
    def title(self) -> str:
        """
        Gets the title of this ScimV2CreateUser.
        The user's title.

        :return: The title of this ScimV2CreateUser.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        """
        Sets the title of this ScimV2CreateUser.
        The user's title.

        :param title: The title of this ScimV2CreateUser.
        :type: str
        """
        

        self._title = title

    @property
    def phone_numbers(self) -> List['ScimPhoneNumber']:
        """
        Gets the phone_numbers of this ScimV2CreateUser.
        The list of the user's phone numbers.

        :return: The phone_numbers of this ScimV2CreateUser.
        :rtype: list[ScimPhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers: List['ScimPhoneNumber']) -> None:
        """
        Sets the phone_numbers of this ScimV2CreateUser.
        The list of the user's phone numbers.

        :param phone_numbers: The phone_numbers of this ScimV2CreateUser.
        :type: list[ScimPhoneNumber]
        """
        

        self._phone_numbers = phone_numbers

    @property
    def emails(self) -> List['ScimEmail']:
        """
        Gets the emails of this ScimV2CreateUser.
        The list of the user's email addresses.

        :return: The emails of this ScimV2CreateUser.
        :rtype: list[ScimEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails: List['ScimEmail']) -> None:
        """
        Sets the emails of this ScimV2CreateUser.
        The list of the user's email addresses.

        :param emails: The emails of this ScimV2CreateUser.
        :type: list[ScimEmail]
        """
        

        self._emails = emails

    @property
    def external_id(self) -> str:
        """
        Gets the external_id of this ScimV2CreateUser.
        The external ID of the user. Set by the provisioning client. \"caseExact\" is set to \"true\". \"mutability\" is set to \"readWrite\".

        :return: The external_id of this ScimV2CreateUser.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id: str) -> None:
        """
        Sets the external_id of this ScimV2CreateUser.
        The external ID of the user. Set by the provisioning client. \"caseExact\" is set to \"true\". \"mutability\" is set to \"readWrite\".

        :param external_id: The external_id of this ScimV2CreateUser.
        :type: str
        """
        

        self._external_id = external_id

    @property
    def groups(self) -> List['ScimV2GroupReference']:
        """
        Gets the groups of this ScimV2CreateUser.
        The list of groups that the user is a member of. This list is immutable per SCIM RFC and may only be updated using the GROUPS resource endpoint.

        :return: The groups of this ScimV2CreateUser.
        :rtype: list[ScimV2GroupReference]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: List['ScimV2GroupReference']) -> None:
        """
        Sets the groups of this ScimV2CreateUser.
        The list of groups that the user is a member of. This list is immutable per SCIM RFC and may only be updated using the GROUPS resource endpoint.

        :param groups: The groups of this ScimV2CreateUser.
        :type: list[ScimV2GroupReference]
        """
        

        self._groups = groups

    @property
    def roles(self) -> List['ScimUserRole']:
        """
        Gets the roles of this ScimV2CreateUser.
        The list of roles assigned to the user.

        :return: The roles of this ScimV2CreateUser.
        :rtype: list[ScimUserRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List['ScimUserRole']) -> None:
        """
        Sets the roles of this ScimV2CreateUser.
        The list of roles assigned to the user.

        :param roles: The roles of this ScimV2CreateUser.
        :type: list[ScimUserRole]
        """
        

        self._roles = roles

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self) -> 'ScimV2EnterpriseUser':
        """
        Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2CreateUser.
        The URI of the schema for the enterprise user.

        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2CreateUser.
        :rtype: ScimV2EnterpriseUser
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user: 'ScimV2EnterpriseUser') -> None:
        """
        Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2CreateUser.
        The URI of the schema for the enterprise user.

        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this ScimV2CreateUser.
        :type: ScimV2EnterpriseUser
        """
        

        self._urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def urnietfparamsscimschemasextensiongenesyspurecloud2_0_user(self) -> 'ScimUserExtensions':
        """
        Gets the urnietfparamsscimschemasextensiongenesyspurecloud2_0_user of this ScimV2CreateUser.
        The URI of the schema for the Genesys Cloud user.

        :return: The urnietfparamsscimschemasextensiongenesyspurecloud2_0_user of this ScimV2CreateUser.
        :rtype: ScimUserExtensions
        """
        return self._urnietfparamsscimschemasextensiongenesyspurecloud2_0_user

    @urnietfparamsscimschemasextensiongenesyspurecloud2_0_user.setter
    def urnietfparamsscimschemasextensiongenesyspurecloud2_0_user(self, urnietfparamsscimschemasextensiongenesyspurecloud2_0_user: 'ScimUserExtensions') -> None:
        """
        Sets the urnietfparamsscimschemasextensiongenesyspurecloud2_0_user of this ScimV2CreateUser.
        The URI of the schema for the Genesys Cloud user.

        :param urnietfparamsscimschemasextensiongenesyspurecloud2_0_user: The urnietfparamsscimschemasextensiongenesyspurecloud2_0_user of this ScimV2CreateUser.
        :type: ScimUserExtensions
        """
        

        self._urnietfparamsscimschemasextensiongenesyspurecloud2_0_user = urnietfparamsscimschemasextensiongenesyspurecloud2_0_user

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

