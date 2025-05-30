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
    from . import ImportStatus

class DncList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DncList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'import_status': 'ImportStatus',
            'size': 'int',
            'dnc_source_type': 'str',
            'contact_method': 'str',
            'login_id': 'str',
            'campaign_id': 'str',
            'dnc_codes': 'list[str]',
            'license_id': 'str',
            'division': 'DomainEntityRef',
            'custom_exclusion_column': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'import_status': 'importStatus',
            'size': 'size',
            'dnc_source_type': 'dncSourceType',
            'contact_method': 'contactMethod',
            'login_id': 'loginId',
            'campaign_id': 'campaignId',
            'dnc_codes': 'dncCodes',
            'license_id': 'licenseId',
            'division': 'division',
            'custom_exclusion_column': 'customExclusionColumn',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._import_status = None
        self._size = None
        self._dnc_source_type = None
        self._contact_method = None
        self._login_id = None
        self._campaign_id = None
        self._dnc_codes = None
        self._license_id = None
        self._division = None
        self._custom_exclusion_column = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this DncList.
        The globally unique identifier for the object.

        :return: The id of this DncList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DncList.
        The globally unique identifier for the object.

        :param id: The id of this DncList.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DncList.
        The name of the DncList.

        :return: The name of this DncList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DncList.
        The name of the DncList.

        :param name: The name of this DncList.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this DncList.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this DncList.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this DncList.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this DncList.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this DncList.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this DncList.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this DncList.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this DncList.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this DncList.
        Required for updates, must match the version number of the most recent update

        :return: The version of this DncList.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this DncList.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this DncList.
        :type: int
        """
        

        self._version = version

    @property
    def import_status(self) -> 'ImportStatus':
        """
        Gets the import_status of this DncList.
        The status of the import process

        :return: The import_status of this DncList.
        :rtype: ImportStatus
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status: 'ImportStatus') -> None:
        """
        Sets the import_status of this DncList.
        The status of the import process

        :param import_status: The import_status of this DncList.
        :type: ImportStatus
        """
        

        self._import_status = import_status

    @property
    def size(self) -> int:
        """
        Gets the size of this DncList.
        The total number of phone numbers in the DncList.

        :return: The size of this DncList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        """
        Sets the size of this DncList.
        The total number of phone numbers in the DncList.

        :param size: The size of this DncList.
        :type: int
        """
        

        self._size = size

    @property
    def dnc_source_type(self) -> str:
        """
        Gets the dnc_source_type of this DncList.
        The type of the DncList.

        :return: The dnc_source_type of this DncList.
        :rtype: str
        """
        return self._dnc_source_type

    @dnc_source_type.setter
    def dnc_source_type(self, dnc_source_type: str) -> None:
        """
        Sets the dnc_source_type of this DncList.
        The type of the DncList.

        :param dnc_source_type: The dnc_source_type of this DncList.
        :type: str
        """
        if isinstance(dnc_source_type, int):
            dnc_source_type = str(dnc_source_type)
        allowed_values = ["rds", "rds_custom", "dnc.com", "gryphon"]
        if dnc_source_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for dnc_source_type -> " + dnc_source_type)
            self._dnc_source_type = "outdated_sdk_version"
        else:
            self._dnc_source_type = dnc_source_type

    @property
    def contact_method(self) -> str:
        """
        Gets the contact_method of this DncList.
        The contact method. Required if dncSourceType is rds.

        :return: The contact_method of this DncList.
        :rtype: str
        """
        return self._contact_method

    @contact_method.setter
    def contact_method(self, contact_method: str) -> None:
        """
        Sets the contact_method of this DncList.
        The contact method. Required if dncSourceType is rds.

        :param contact_method: The contact_method of this DncList.
        :type: str
        """
        if isinstance(contact_method, int):
            contact_method = str(contact_method)
        allowed_values = ["Email", "Phone", "Any", "WhatsApp"]
        if contact_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for contact_method -> " + contact_method)
            self._contact_method = "outdated_sdk_version"
        else:
            self._contact_method = contact_method

    @property
    def login_id(self) -> str:
        """
        Gets the login_id of this DncList.
        A dnc.com loginId. Required if the dncSourceType is dnc.com.

        :return: The login_id of this DncList.
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id: str) -> None:
        """
        Sets the login_id of this DncList.
        A dnc.com loginId. Required if the dncSourceType is dnc.com.

        :param login_id: The login_id of this DncList.
        :type: str
        """
        

        self._login_id = login_id

    @property
    def campaign_id(self) -> str:
        """
        Gets the campaign_id of this DncList.
        A dnc.com campaignId. Optional if the dncSourceType is dnc.com.

        :return: The campaign_id of this DncList.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id: str) -> None:
        """
        Sets the campaign_id of this DncList.
        A dnc.com campaignId. Optional if the dncSourceType is dnc.com.

        :param campaign_id: The campaign_id of this DncList.
        :type: str
        """
        

        self._campaign_id = campaign_id

    @property
    def dnc_codes(self) -> List[str]:
        """
        Gets the dnc_codes of this DncList.
        The list of dnc.com codes to be treated as DNC. Required if the dncSourceType is dnc.com.

        :return: The dnc_codes of this DncList.
        :rtype: list[str]
        """
        return self._dnc_codes

    @dnc_codes.setter
    def dnc_codes(self, dnc_codes: List[str]) -> None:
        """
        Sets the dnc_codes of this DncList.
        The list of dnc.com codes to be treated as DNC. Required if the dncSourceType is dnc.com.

        :param dnc_codes: The dnc_codes of this DncList.
        :type: list[str]
        """
        

        self._dnc_codes = dnc_codes

    @property
    def license_id(self) -> str:
        """
        Gets the license_id of this DncList.
        A gryphon license number. Required if the dncSourceType is gryphon.

        :return: The license_id of this DncList.
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id: str) -> None:
        """
        Sets the license_id of this DncList.
        A gryphon license number. Required if the dncSourceType is gryphon.

        :param license_id: The license_id of this DncList.
        :type: str
        """
        

        self._license_id = license_id

    @property
    def division(self) -> 'DomainEntityRef':
        """
        Gets the division of this DncList.
        The division this DncList belongs to.

        :return: The division of this DncList.
        :rtype: DomainEntityRef
        """
        return self._division

    @division.setter
    def division(self, division: 'DomainEntityRef') -> None:
        """
        Sets the division of this DncList.
        The division this DncList belongs to.

        :param division: The division of this DncList.
        :type: DomainEntityRef
        """
        

        self._division = division

    @property
    def custom_exclusion_column(self) -> str:
        """
        Gets the custom_exclusion_column of this DncList.
        The column to evaluate exclusion against. Required if the dncSourceType is rds_custom.

        :return: The custom_exclusion_column of this DncList.
        :rtype: str
        """
        return self._custom_exclusion_column

    @custom_exclusion_column.setter
    def custom_exclusion_column(self, custom_exclusion_column: str) -> None:
        """
        Sets the custom_exclusion_column of this DncList.
        The column to evaluate exclusion against. Required if the dncSourceType is rds_custom.

        :param custom_exclusion_column: The custom_exclusion_column of this DncList.
        :type: str
        """
        

        self._custom_exclusion_column = custom_exclusion_column

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this DncList.
        The URI for this object

        :return: The self_uri of this DncList.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this DncList.
        The URI for this object

        :param self_uri: The self_uri of this DncList.
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

