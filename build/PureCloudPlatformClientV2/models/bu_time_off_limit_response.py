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

if TYPE_CHECKING:
    from . import ManagementUnitReference
    from . import StaffingGroupReference
    from . import WfmVersionedEntityMetadata

class BuTimeOffLimitResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuTimeOffLimitResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'staffing_group': 'StaffingGroupReference',
            'management_unit': 'ManagementUnitReference',
            'metadata': 'WfmVersionedEntityMetadata',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'staffing_group': 'staffingGroup',
            'management_unit': 'managementUnit',
            'metadata': 'metadata',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._staffing_group = None
        self._management_unit = None
        self._metadata = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BuTimeOffLimitResponse.
        The globally unique identifier for the object.

        :return: The id of this BuTimeOffLimitResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BuTimeOffLimitResponse.
        The globally unique identifier for the object.

        :param id: The id of this BuTimeOffLimitResponse.
        :type: str
        """
        

        self._id = id

    @property
    def staffing_group(self) -> 'StaffingGroupReference':
        """
        Gets the staffing_group of this BuTimeOffLimitResponse.
        The staffing group to which this time-off limit is associated. If managementUnit is set, then the staffing group belongs to that management unit.Otherwise, if managementUnit is not set, it is a business unit level staffing group.At least one of managementUnit and staffingGroup must be set

        :return: The staffing_group of this BuTimeOffLimitResponse.
        :rtype: StaffingGroupReference
        """
        return self._staffing_group

    @staffing_group.setter
    def staffing_group(self, staffing_group: 'StaffingGroupReference') -> None:
        """
        Sets the staffing_group of this BuTimeOffLimitResponse.
        The staffing group to which this time-off limit is associated. If managementUnit is set, then the staffing group belongs to that management unit.Otherwise, if managementUnit is not set, it is a business unit level staffing group.At least one of managementUnit and staffingGroup must be set

        :param staffing_group: The staffing_group of this BuTimeOffLimitResponse.
        :type: StaffingGroupReference
        """
        

        self._staffing_group = staffing_group

    @property
    def management_unit(self) -> 'ManagementUnitReference':
        """
        Gets the management_unit of this BuTimeOffLimitResponse.
        The management unit to which this time-off limit is associated. If staffingGroup is set, then the limit is associated with that staffing group, which belongs to this management unit.At least one of managementUnit and staffingGroup must be set

        :return: The management_unit of this BuTimeOffLimitResponse.
        :rtype: ManagementUnitReference
        """
        return self._management_unit

    @management_unit.setter
    def management_unit(self, management_unit: 'ManagementUnitReference') -> None:
        """
        Sets the management_unit of this BuTimeOffLimitResponse.
        The management unit to which this time-off limit is associated. If staffingGroup is set, then the limit is associated with that staffing group, which belongs to this management unit.At least one of managementUnit and staffingGroup must be set

        :param management_unit: The management_unit of this BuTimeOffLimitResponse.
        :type: ManagementUnitReference
        """
        

        self._management_unit = management_unit

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this BuTimeOffLimitResponse.
        Version metadata for the time-off limit

        :return: The metadata of this BuTimeOffLimitResponse.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this BuTimeOffLimitResponse.
        Version metadata for the time-off limit

        :param metadata: The metadata of this BuTimeOffLimitResponse.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this BuTimeOffLimitResponse.
        The URI for this object

        :return: The self_uri of this BuTimeOffLimitResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this BuTimeOffLimitResponse.
        The URI for this object

        :param self_uri: The self_uri of this BuTimeOffLimitResponse.
        :type: str
        """
        

        self._self_uri = self_uri

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
