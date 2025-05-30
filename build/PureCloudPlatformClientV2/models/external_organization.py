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
    from . import ContactAddress
    from . import DataSchema
    from . import ExternalDataSource
    from . import ExternalId
    from . import ExternalOrganizationIdentifier
    from . import PhoneNumber
    from . import Ticker
    from . import Trustor
    from . import TwitterId
    from . import WritableStarrableDivision

class ExternalOrganization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalOrganization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'WritableStarrableDivision',
            'company_type': 'str',
            'industry': 'str',
            'address': 'ContactAddress',
            'phone_number': 'PhoneNumber',
            'fax_number': 'PhoneNumber',
            'employee_count': 'int',
            'revenue': 'int',
            'tags': 'list[str]',
            'websites': 'list[str]',
            'tickers': 'list[Ticker]',
            'twitter_id': 'TwitterId',
            'external_system_url': 'str',
            'modify_date': 'datetime',
            'create_date': 'datetime',
            'trustor': 'Trustor',
            'schema': 'DataSchema',
            'custom_fields': 'dict(str, object)',
            'identifiers': 'list[ExternalOrganizationIdentifier]',
            'external_ids': 'list[ExternalId]',
            'external_data_sources': 'list[ExternalDataSource]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'company_type': 'companyType',
            'industry': 'industry',
            'address': 'address',
            'phone_number': 'phoneNumber',
            'fax_number': 'faxNumber',
            'employee_count': 'employeeCount',
            'revenue': 'revenue',
            'tags': 'tags',
            'websites': 'websites',
            'tickers': 'tickers',
            'twitter_id': 'twitterId',
            'external_system_url': 'externalSystemUrl',
            'modify_date': 'modifyDate',
            'create_date': 'createDate',
            'trustor': 'trustor',
            'schema': 'schema',
            'custom_fields': 'customFields',
            'identifiers': 'identifiers',
            'external_ids': 'externalIds',
            'external_data_sources': 'externalDataSources',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._company_type = None
        self._industry = None
        self._address = None
        self._phone_number = None
        self._fax_number = None
        self._employee_count = None
        self._revenue = None
        self._tags = None
        self._websites = None
        self._tickers = None
        self._twitter_id = None
        self._external_system_url = None
        self._modify_date = None
        self._create_date = None
        self._trustor = None
        self._schema = None
        self._custom_fields = None
        self._identifiers = None
        self._external_ids = None
        self._external_data_sources = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ExternalOrganization.
        The globally unique identifier for the object.

        :return: The id of this ExternalOrganization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ExternalOrganization.
        The globally unique identifier for the object.

        :param id: The id of this ExternalOrganization.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ExternalOrganization.
        The name of the company.

        :return: The name of this ExternalOrganization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ExternalOrganization.
        The name of the company.

        :param name: The name of this ExternalOrganization.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'WritableStarrableDivision':
        """
        Gets the division of this ExternalOrganization.
        The division to which this entity belongs.

        :return: The division of this ExternalOrganization.
        :rtype: WritableStarrableDivision
        """
        return self._division

    @division.setter
    def division(self, division: 'WritableStarrableDivision') -> None:
        """
        Sets the division of this ExternalOrganization.
        The division to which this entity belongs.

        :param division: The division of this ExternalOrganization.
        :type: WritableStarrableDivision
        """
        

        self._division = division

    @property
    def company_type(self) -> str:
        """
        Gets the company_type of this ExternalOrganization.


        :return: The company_type of this ExternalOrganization.
        :rtype: str
        """
        return self._company_type

    @company_type.setter
    def company_type(self, company_type: str) -> None:
        """
        Sets the company_type of this ExternalOrganization.


        :param company_type: The company_type of this ExternalOrganization.
        :type: str
        """
        

        self._company_type = company_type

    @property
    def industry(self) -> str:
        """
        Gets the industry of this ExternalOrganization.


        :return: The industry of this ExternalOrganization.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry: str) -> None:
        """
        Sets the industry of this ExternalOrganization.


        :param industry: The industry of this ExternalOrganization.
        :type: str
        """
        

        self._industry = industry

    @property
    def address(self) -> 'ContactAddress':
        """
        Gets the address of this ExternalOrganization.


        :return: The address of this ExternalOrganization.
        :rtype: ContactAddress
        """
        return self._address

    @address.setter
    def address(self, address: 'ContactAddress') -> None:
        """
        Sets the address of this ExternalOrganization.


        :param address: The address of this ExternalOrganization.
        :type: ContactAddress
        """
        

        self._address = address

    @property
    def phone_number(self) -> 'PhoneNumber':
        """
        Gets the phone_number of this ExternalOrganization.


        :return: The phone_number of this ExternalOrganization.
        :rtype: PhoneNumber
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: 'PhoneNumber') -> None:
        """
        Sets the phone_number of this ExternalOrganization.


        :param phone_number: The phone_number of this ExternalOrganization.
        :type: PhoneNumber
        """
        

        self._phone_number = phone_number

    @property
    def fax_number(self) -> 'PhoneNumber':
        """
        Gets the fax_number of this ExternalOrganization.


        :return: The fax_number of this ExternalOrganization.
        :rtype: PhoneNumber
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number: 'PhoneNumber') -> None:
        """
        Sets the fax_number of this ExternalOrganization.


        :param fax_number: The fax_number of this ExternalOrganization.
        :type: PhoneNumber
        """
        

        self._fax_number = fax_number

    @property
    def employee_count(self) -> int:
        """
        Gets the employee_count of this ExternalOrganization.


        :return: The employee_count of this ExternalOrganization.
        :rtype: int
        """
        return self._employee_count

    @employee_count.setter
    def employee_count(self, employee_count: int) -> None:
        """
        Sets the employee_count of this ExternalOrganization.


        :param employee_count: The employee_count of this ExternalOrganization.
        :type: int
        """
        

        self._employee_count = employee_count

    @property
    def revenue(self) -> int:
        """
        Gets the revenue of this ExternalOrganization.


        :return: The revenue of this ExternalOrganization.
        :rtype: int
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue: int) -> None:
        """
        Sets the revenue of this ExternalOrganization.


        :param revenue: The revenue of this ExternalOrganization.
        :type: int
        """
        

        self._revenue = revenue

    @property
    def tags(self) -> List[str]:
        """
        Gets the tags of this ExternalOrganization.


        :return: The tags of this ExternalOrganization.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]) -> None:
        """
        Sets the tags of this ExternalOrganization.


        :param tags: The tags of this ExternalOrganization.
        :type: list[str]
        """
        

        self._tags = tags

    @property
    def websites(self) -> List[str]:
        """
        Gets the websites of this ExternalOrganization.


        :return: The websites of this ExternalOrganization.
        :rtype: list[str]
        """
        return self._websites

    @websites.setter
    def websites(self, websites: List[str]) -> None:
        """
        Sets the websites of this ExternalOrganization.


        :param websites: The websites of this ExternalOrganization.
        :type: list[str]
        """
        

        self._websites = websites

    @property
    def tickers(self) -> List['Ticker']:
        """
        Gets the tickers of this ExternalOrganization.


        :return: The tickers of this ExternalOrganization.
        :rtype: list[Ticker]
        """
        return self._tickers

    @tickers.setter
    def tickers(self, tickers: List['Ticker']) -> None:
        """
        Sets the tickers of this ExternalOrganization.


        :param tickers: The tickers of this ExternalOrganization.
        :type: list[Ticker]
        """
        

        self._tickers = tickers

    @property
    def twitter_id(self) -> 'TwitterId':
        """
        Gets the twitter_id of this ExternalOrganization.


        :return: The twitter_id of this ExternalOrganization.
        :rtype: TwitterId
        """
        return self._twitter_id

    @twitter_id.setter
    def twitter_id(self, twitter_id: 'TwitterId') -> None:
        """
        Sets the twitter_id of this ExternalOrganization.


        :param twitter_id: The twitter_id of this ExternalOrganization.
        :type: TwitterId
        """
        

        self._twitter_id = twitter_id

    @property
    def external_system_url(self) -> str:
        """
        Gets the external_system_url of this ExternalOrganization.
        A string that identifies an external system-of-record resource that may have more detailed information on the organization. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :return: The external_system_url of this ExternalOrganization.
        :rtype: str
        """
        return self._external_system_url

    @external_system_url.setter
    def external_system_url(self, external_system_url: str) -> None:
        """
        Sets the external_system_url of this ExternalOrganization.
        A string that identifies an external system-of-record resource that may have more detailed information on the organization. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :param external_system_url: The external_system_url of this ExternalOrganization.
        :type: str
        """
        

        self._external_system_url = external_system_url

    @property
    def modify_date(self) -> datetime:
        """
        Gets the modify_date of this ExternalOrganization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modify_date of this ExternalOrganization.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date: datetime) -> None:
        """
        Sets the modify_date of this ExternalOrganization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modify_date: The modify_date of this ExternalOrganization.
        :type: datetime
        """
        

        self._modify_date = modify_date

    @property
    def create_date(self) -> datetime:
        """
        Gets the create_date of this ExternalOrganization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The create_date of this ExternalOrganization.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime) -> None:
        """
        Sets the create_date of this ExternalOrganization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param create_date: The create_date of this ExternalOrganization.
        :type: datetime
        """
        

        self._create_date = create_date

    @property
    def trustor(self) -> 'Trustor':
        """
        Gets the trustor of this ExternalOrganization.


        :return: The trustor of this ExternalOrganization.
        :rtype: Trustor
        """
        return self._trustor

    @trustor.setter
    def trustor(self, trustor: 'Trustor') -> None:
        """
        Sets the trustor of this ExternalOrganization.


        :param trustor: The trustor of this ExternalOrganization.
        :type: Trustor
        """
        

        self._trustor = trustor

    @property
    def schema(self) -> 'DataSchema':
        """
        Gets the schema of this ExternalOrganization.
        The schema defining custom fields for this contact

        :return: The schema of this ExternalOrganization.
        :rtype: DataSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema: 'DataSchema') -> None:
        """
        Sets the schema of this ExternalOrganization.
        The schema defining custom fields for this contact

        :param schema: The schema of this ExternalOrganization.
        :type: DataSchema
        """
        

        self._schema = schema

    @property
    def custom_fields(self) -> Dict[str, object]:
        """
        Gets the custom_fields of this ExternalOrganization.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :return: The custom_fields of this ExternalOrganization.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields: Dict[str, object]) -> None:
        """
        Sets the custom_fields of this ExternalOrganization.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :param custom_fields: The custom_fields of this ExternalOrganization.
        :type: dict(str, object)
        """
        

        self._custom_fields = custom_fields

    @property
    def identifiers(self) -> List['ExternalOrganizationIdentifier']:
        """
        Gets the identifiers of this ExternalOrganization.
        Identifiers claimed by this external org

        :return: The identifiers of this ExternalOrganization.
        :rtype: list[ExternalOrganizationIdentifier]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers: List['ExternalOrganizationIdentifier']) -> None:
        """
        Sets the identifiers of this ExternalOrganization.
        Identifiers claimed by this external org

        :param identifiers: The identifiers of this ExternalOrganization.
        :type: list[ExternalOrganizationIdentifier]
        """
        

        self._identifiers = identifiers

    @property
    def external_ids(self) -> List['ExternalId']:
        """
        Gets the external_ids of this ExternalOrganization.
        A list of external identifiers that identify this External Organization in an external system

        :return: The external_ids of this ExternalOrganization.
        :rtype: list[ExternalId]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids: List['ExternalId']) -> None:
        """
        Sets the external_ids of this ExternalOrganization.
        A list of external identifiers that identify this External Organization in an external system

        :param external_ids: The external_ids of this ExternalOrganization.
        :type: list[ExternalId]
        """
        

        self._external_ids = external_ids

    @property
    def external_data_sources(self) -> List['ExternalDataSource']:
        """
        Gets the external_data_sources of this ExternalOrganization.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :return: The external_data_sources of this ExternalOrganization.
        :rtype: list[ExternalDataSource]
        """
        return self._external_data_sources

    @external_data_sources.setter
    def external_data_sources(self, external_data_sources: List['ExternalDataSource']) -> None:
        """
        Sets the external_data_sources of this ExternalOrganization.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :param external_data_sources: The external_data_sources of this ExternalOrganization.
        :type: list[ExternalDataSource]
        """
        

        self._external_data_sources = external_data_sources

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ExternalOrganization.
        The URI for this object

        :return: The self_uri of this ExternalOrganization.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ExternalOrganization.
        The URI for this object

        :param self_uri: The self_uri of this ExternalOrganization.
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

