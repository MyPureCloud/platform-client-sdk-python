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
    from . import ExternalContactsOrganizationNoteChangedTopicDivision
    from . import ExternalContactsOrganizationNoteChangedTopicUser

class ExternalContactsOrganizationNoteChangedTopicNote(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalContactsOrganizationNoteChangedTopicNote - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'division': 'ExternalContactsOrganizationNoteChangedTopicDivision',
            'entity_id': 'str',
            'entity_type': 'str',
            'note_text': 'str',
            'created_by': 'ExternalContactsOrganizationNoteChangedTopicUser',
            'create_date': 'datetime',
            'modify_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'division': 'division',
            'entity_id': 'entityId',
            'entity_type': 'entityType',
            'note_text': 'noteText',
            'created_by': 'createdBy',
            'create_date': 'createDate',
            'modify_date': 'modifyDate'
        }

        self._id = None
        self._division = None
        self._entity_id = None
        self._entity_type = None
        self._note_text = None
        self._created_by = None
        self._create_date = None
        self._modify_date = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The id of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param id: The id of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: str
        """
        

        self._id = id

    @property
    def division(self) -> 'ExternalContactsOrganizationNoteChangedTopicDivision':
        """
        Gets the division of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The division of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: ExternalContactsOrganizationNoteChangedTopicDivision
        """
        return self._division

    @division.setter
    def division(self, division: 'ExternalContactsOrganizationNoteChangedTopicDivision') -> None:
        """
        Sets the division of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param division: The division of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: ExternalContactsOrganizationNoteChangedTopicDivision
        """
        

        self._division = division

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The entity_id of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param entity_id: The entity_id of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def entity_type(self) -> str:
        """
        Gets the entity_type of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The entity_type of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str) -> None:
        """
        Sets the entity_type of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param entity_type: The entity_type of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: str
        """
        if isinstance(entity_type, int):
            entity_type = str(entity_type)
        allowed_values = ["Contact", "Organization"]
        if entity_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for entity_type -> " + entity_type)
            self._entity_type = "outdated_sdk_version"
        else:
            self._entity_type = entity_type

    @property
    def note_text(self) -> str:
        """
        Gets the note_text of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The note_text of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: str
        """
        return self._note_text

    @note_text.setter
    def note_text(self, note_text: str) -> None:
        """
        Sets the note_text of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param note_text: The note_text of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: str
        """
        

        self._note_text = note_text

    @property
    def created_by(self) -> 'ExternalContactsOrganizationNoteChangedTopicUser':
        """
        Gets the created_by of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The created_by of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: ExternalContactsOrganizationNoteChangedTopicUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'ExternalContactsOrganizationNoteChangedTopicUser') -> None:
        """
        Sets the created_by of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param created_by: The created_by of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: ExternalContactsOrganizationNoteChangedTopicUser
        """
        

        self._created_by = created_by

    @property
    def create_date(self) -> datetime:
        """
        Gets the create_date of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The create_date of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime) -> None:
        """
        Sets the create_date of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param create_date: The create_date of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: datetime
        """
        

        self._create_date = create_date

    @property
    def modify_date(self) -> datetime:
        """
        Gets the modify_date of this ExternalContactsOrganizationNoteChangedTopicNote.


        :return: The modify_date of this ExternalContactsOrganizationNoteChangedTopicNote.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date: datetime) -> None:
        """
        Sets the modify_date of this ExternalContactsOrganizationNoteChangedTopicNote.


        :param modify_date: The modify_date of this ExternalContactsOrganizationNoteChangedTopicNote.
        :type: datetime
        """
        

        self._modify_date = modify_date

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
