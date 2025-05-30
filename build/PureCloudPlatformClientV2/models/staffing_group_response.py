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
    from . import ManagementUnitReference
    from . import UserReference
    from . import WfmVersionedEntityMetadata

class StaffingGroupResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        StaffingGroupResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'users': 'list[UserReference]',
            'management_unit': 'ManagementUnitReference',
            'metadata': 'WfmVersionedEntityMetadata',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'users': 'users',
            'management_unit': 'managementUnit',
            'metadata': 'metadata',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._users = None
        self._management_unit = None
        self._metadata = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this StaffingGroupResponse.
        The globally unique identifier for the object.

        :return: The id of this StaffingGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this StaffingGroupResponse.
        The globally unique identifier for the object.

        :param id: The id of this StaffingGroupResponse.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this StaffingGroupResponse.
        The name of the staffing group

        :return: The name of this StaffingGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this StaffingGroupResponse.
        The name of the staffing group

        :param name: The name of this StaffingGroupResponse.
        :type: str
        """
        

        self._name = name

    @property
    def users(self) -> List['UserReference']:
        """
        Gets the users of this StaffingGroupResponse.
        The list of users that belong to the staffing group

        :return: The users of this StaffingGroupResponse.
        :rtype: list[UserReference]
        """
        return self._users

    @users.setter
    def users(self, users: List['UserReference']) -> None:
        """
        Sets the users of this StaffingGroupResponse.
        The list of users that belong to the staffing group

        :param users: The users of this StaffingGroupResponse.
        :type: list[UserReference]
        """
        

        self._users = users

    @property
    def management_unit(self) -> 'ManagementUnitReference':
        """
        Gets the management_unit of this StaffingGroupResponse.
        The ID of the management unit to which the staffing group users belong. If undefined the staffing group can include users from the entire business unit

        :return: The management_unit of this StaffingGroupResponse.
        :rtype: ManagementUnitReference
        """
        return self._management_unit

    @management_unit.setter
    def management_unit(self, management_unit: 'ManagementUnitReference') -> None:
        """
        Sets the management_unit of this StaffingGroupResponse.
        The ID of the management unit to which the staffing group users belong. If undefined the staffing group can include users from the entire business unit

        :param management_unit: The management_unit of this StaffingGroupResponse.
        :type: ManagementUnitReference
        """
        

        self._management_unit = management_unit

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this StaffingGroupResponse.
        Version metadata for the staffing group

        :return: The metadata of this StaffingGroupResponse.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this StaffingGroupResponse.
        Version metadata for the staffing group

        :param metadata: The metadata of this StaffingGroupResponse.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this StaffingGroupResponse.
        The URI for this object

        :return: The self_uri of this StaffingGroupResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this StaffingGroupResponse.
        The URI for this object

        :param self_uri: The self_uri of this StaffingGroupResponse.
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

