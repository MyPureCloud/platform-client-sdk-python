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
    from . import SkillGroupCondition
    from . import WritableDivision

class SkillGroupWithMemberDivisions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SkillGroupWithMemberDivisions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'WritableDivision',
            'description': 'str',
            'member_count': 'int',
            'date_modified': 'datetime',
            'date_created': 'datetime',
            'status': 'str',
            'skill_conditions': 'list[SkillGroupCondition]',
            'member_divisions': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'member_count': 'memberCount',
            'date_modified': 'dateModified',
            'date_created': 'dateCreated',
            'status': 'status',
            'skill_conditions': 'skillConditions',
            'member_divisions': 'memberDivisions',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._member_count = None
        self._date_modified = None
        self._date_created = None
        self._status = None
        self._skill_conditions = None
        self._member_divisions = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this SkillGroupWithMemberDivisions.
        The globally unique identifier for the object.

        :return: The id of this SkillGroupWithMemberDivisions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this SkillGroupWithMemberDivisions.
        The globally unique identifier for the object.

        :param id: The id of this SkillGroupWithMemberDivisions.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this SkillGroupWithMemberDivisions.
        The group name.

        :return: The name of this SkillGroupWithMemberDivisions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this SkillGroupWithMemberDivisions.
        The group name.

        :param name: The name of this SkillGroupWithMemberDivisions.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'WritableDivision':
        """
        Gets the division of this SkillGroupWithMemberDivisions.
        The division to which this entity belongs.

        :return: The division of this SkillGroupWithMemberDivisions.
        :rtype: WritableDivision
        """
        return self._division

    @division.setter
    def division(self, division: 'WritableDivision') -> None:
        """
        Sets the division of this SkillGroupWithMemberDivisions.
        The division to which this entity belongs.

        :param division: The division of this SkillGroupWithMemberDivisions.
        :type: WritableDivision
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this SkillGroupWithMemberDivisions.
        Group description

        :return: The description of this SkillGroupWithMemberDivisions.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this SkillGroupWithMemberDivisions.
        Group description

        :param description: The description of this SkillGroupWithMemberDivisions.
        :type: str
        """
        

        self._description = description

    @property
    def member_count(self) -> int:
        """
        Gets the member_count of this SkillGroupWithMemberDivisions.
        Estimated number of members in this group. It can take some time for the count to be updated after expressions are changed.

        :return: The member_count of this SkillGroupWithMemberDivisions.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count: int) -> None:
        """
        Sets the member_count of this SkillGroupWithMemberDivisions.
        Estimated number of members in this group. It can take some time for the count to be updated after expressions are changed.

        :param member_count: The member_count of this SkillGroupWithMemberDivisions.
        :type: int
        """
        

        self._member_count = member_count

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this SkillGroupWithMemberDivisions.
        Last modified date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this SkillGroupWithMemberDivisions.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this SkillGroupWithMemberDivisions.
        Last modified date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this SkillGroupWithMemberDivisions.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this SkillGroupWithMemberDivisions.
        Created date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this SkillGroupWithMemberDivisions.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this SkillGroupWithMemberDivisions.
        Created date/time of the skill group. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this SkillGroupWithMemberDivisions.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def status(self) -> str:
        """
        Gets the status of this SkillGroupWithMemberDivisions.
        Group's filling status

        :return: The status of this SkillGroupWithMemberDivisions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this SkillGroupWithMemberDivisions.
        Group's filling status

        :param status: The status of this SkillGroupWithMemberDivisions.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["InProgress", "Complete"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def skill_conditions(self) -> List['SkillGroupCondition']:
        """
        Gets the skill_conditions of this SkillGroupWithMemberDivisions.
        Conditions for this group

        :return: The skill_conditions of this SkillGroupWithMemberDivisions.
        :rtype: list[SkillGroupCondition]
        """
        return self._skill_conditions

    @skill_conditions.setter
    def skill_conditions(self, skill_conditions: List['SkillGroupCondition']) -> None:
        """
        Sets the skill_conditions of this SkillGroupWithMemberDivisions.
        Conditions for this group

        :param skill_conditions: The skill_conditions of this SkillGroupWithMemberDivisions.
        :type: list[SkillGroupCondition]
        """
        

        self._skill_conditions = skill_conditions

    @property
    def member_divisions(self) -> List[str]:
        """
        Gets the member_divisions of this SkillGroupWithMemberDivisions.
        Member divisions for this skill group

        :return: The member_divisions of this SkillGroupWithMemberDivisions.
        :rtype: list[str]
        """
        return self._member_divisions

    @member_divisions.setter
    def member_divisions(self, member_divisions: List[str]) -> None:
        """
        Sets the member_divisions of this SkillGroupWithMemberDivisions.
        Member divisions for this skill group

        :param member_divisions: The member_divisions of this SkillGroupWithMemberDivisions.
        :type: list[str]
        """
        

        self._member_divisions = member_divisions

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this SkillGroupWithMemberDivisions.
        The URI for this object

        :return: The self_uri of this SkillGroupWithMemberDivisions.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this SkillGroupWithMemberDivisions.
        The URI for this object

        :param self_uri: The self_uri of this SkillGroupWithMemberDivisions.
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

