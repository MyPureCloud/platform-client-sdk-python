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
    from . import ContactAddressableEntityRef
    from . import ContactIdentifier
    from . import DataSchema
    from . import ExternalDataSource
    from . import ExternalId
    from . import ExternalOrganization
    from . import FacebookId
    from . import InstagramId
    from . import LineId
    from . import MergeOperation
    from . import PhoneNumber
    from . import TwitterId
    from . import WhatsAppId
    from . import WritableStarrableDivision

class ExternalContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'division': 'WritableStarrableDivision',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'salutation': 'str',
            'title': 'str',
            'work_phone': 'PhoneNumber',
            'cell_phone': 'PhoneNumber',
            'home_phone': 'PhoneNumber',
            'other_phone': 'PhoneNumber',
            'work_email': 'str',
            'personal_email': 'str',
            'other_email': 'str',
            'address': 'ContactAddress',
            'twitter_id': 'TwitterId',
            'line_id': 'LineId',
            'whats_app_id': 'WhatsAppId',
            'facebook_id': 'FacebookId',
            'instagram_id': 'InstagramId',
            'external_ids': 'list[ExternalId]',
            'identifiers': 'list[ContactIdentifier]',
            'modify_date': 'datetime',
            'create_date': 'datetime',
            'external_organization': 'ExternalOrganization',
            'survey_opt_out': 'bool',
            'external_system_url': 'str',
            'schema': 'DataSchema',
            'custom_fields': 'dict(str, object)',
            'external_data_sources': 'list[ExternalDataSource]',
            'type': 'str',
            'canonical_contact': 'ContactAddressableEntityRef',
            'merge_set': 'list[ContactAddressableEntityRef]',
            'merged_from': 'list[ContactAddressableEntityRef]',
            'merged_to': 'ContactAddressableEntityRef',
            'merge_operation': 'MergeOperation',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'division': 'division',
            'first_name': 'firstName',
            'middle_name': 'middleName',
            'last_name': 'lastName',
            'salutation': 'salutation',
            'title': 'title',
            'work_phone': 'workPhone',
            'cell_phone': 'cellPhone',
            'home_phone': 'homePhone',
            'other_phone': 'otherPhone',
            'work_email': 'workEmail',
            'personal_email': 'personalEmail',
            'other_email': 'otherEmail',
            'address': 'address',
            'twitter_id': 'twitterId',
            'line_id': 'lineId',
            'whats_app_id': 'whatsAppId',
            'facebook_id': 'facebookId',
            'instagram_id': 'instagramId',
            'external_ids': 'externalIds',
            'identifiers': 'identifiers',
            'modify_date': 'modifyDate',
            'create_date': 'createDate',
            'external_organization': 'externalOrganization',
            'survey_opt_out': 'surveyOptOut',
            'external_system_url': 'externalSystemUrl',
            'schema': 'schema',
            'custom_fields': 'customFields',
            'external_data_sources': 'externalDataSources',
            'type': 'type',
            'canonical_contact': 'canonicalContact',
            'merge_set': 'mergeSet',
            'merged_from': 'mergedFrom',
            'merged_to': 'mergedTo',
            'merge_operation': 'mergeOperation',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._division = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._salutation = None
        self._title = None
        self._work_phone = None
        self._cell_phone = None
        self._home_phone = None
        self._other_phone = None
        self._work_email = None
        self._personal_email = None
        self._other_email = None
        self._address = None
        self._twitter_id = None
        self._line_id = None
        self._whats_app_id = None
        self._facebook_id = None
        self._instagram_id = None
        self._external_ids = None
        self._identifiers = None
        self._modify_date = None
        self._create_date = None
        self._external_organization = None
        self._survey_opt_out = None
        self._external_system_url = None
        self._schema = None
        self._custom_fields = None
        self._external_data_sources = None
        self._type = None
        self._canonical_contact = None
        self._merge_set = None
        self._merged_from = None
        self._merged_to = None
        self._merge_operation = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ExternalContact.
        The globally unique identifier for the object.

        :return: The id of this ExternalContact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ExternalContact.
        The globally unique identifier for the object.

        :param id: The id of this ExternalContact.
        :type: str
        """
        

        self._id = id

    @property
    def division(self) -> 'WritableStarrableDivision':
        """
        Gets the division of this ExternalContact.
        The division to which this entity belongs.

        :return: The division of this ExternalContact.
        :rtype: WritableStarrableDivision
        """
        return self._division

    @division.setter
    def division(self, division: 'WritableStarrableDivision') -> None:
        """
        Sets the division of this ExternalContact.
        The division to which this entity belongs.

        :param division: The division of this ExternalContact.
        :type: WritableStarrableDivision
        """
        

        self._division = division

    @property
    def first_name(self) -> str:
        """
        Gets the first_name of this ExternalContact.
        The first name of the contact.

        :return: The first_name of this ExternalContact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """
        Sets the first_name of this ExternalContact.
        The first name of the contact.

        :param first_name: The first_name of this ExternalContact.
        :type: str
        """
        

        self._first_name = first_name

    @property
    def middle_name(self) -> str:
        """
        Gets the middle_name of this ExternalContact.


        :return: The middle_name of this ExternalContact.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name: str) -> None:
        """
        Sets the middle_name of this ExternalContact.


        :param middle_name: The middle_name of this ExternalContact.
        :type: str
        """
        

        self._middle_name = middle_name

    @property
    def last_name(self) -> str:
        """
        Gets the last_name of this ExternalContact.
        The last name of the contact.

        :return: The last_name of this ExternalContact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Sets the last_name of this ExternalContact.
        The last name of the contact.

        :param last_name: The last_name of this ExternalContact.
        :type: str
        """
        

        self._last_name = last_name

    @property
    def salutation(self) -> str:
        """
        Gets the salutation of this ExternalContact.


        :return: The salutation of this ExternalContact.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation: str) -> None:
        """
        Sets the salutation of this ExternalContact.


        :param salutation: The salutation of this ExternalContact.
        :type: str
        """
        

        self._salutation = salutation

    @property
    def title(self) -> str:
        """
        Gets the title of this ExternalContact.


        :return: The title of this ExternalContact.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        """
        Sets the title of this ExternalContact.


        :param title: The title of this ExternalContact.
        :type: str
        """
        

        self._title = title

    @property
    def work_phone(self) -> 'PhoneNumber':
        """
        Gets the work_phone of this ExternalContact.


        :return: The work_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone: 'PhoneNumber') -> None:
        """
        Sets the work_phone of this ExternalContact.


        :param work_phone: The work_phone of this ExternalContact.
        :type: PhoneNumber
        """
        

        self._work_phone = work_phone

    @property
    def cell_phone(self) -> 'PhoneNumber':
        """
        Gets the cell_phone of this ExternalContact.


        :return: The cell_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._cell_phone

    @cell_phone.setter
    def cell_phone(self, cell_phone: 'PhoneNumber') -> None:
        """
        Sets the cell_phone of this ExternalContact.


        :param cell_phone: The cell_phone of this ExternalContact.
        :type: PhoneNumber
        """
        

        self._cell_phone = cell_phone

    @property
    def home_phone(self) -> 'PhoneNumber':
        """
        Gets the home_phone of this ExternalContact.


        :return: The home_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone: 'PhoneNumber') -> None:
        """
        Sets the home_phone of this ExternalContact.


        :param home_phone: The home_phone of this ExternalContact.
        :type: PhoneNumber
        """
        

        self._home_phone = home_phone

    @property
    def other_phone(self) -> 'PhoneNumber':
        """
        Gets the other_phone of this ExternalContact.


        :return: The other_phone of this ExternalContact.
        :rtype: PhoneNumber
        """
        return self._other_phone

    @other_phone.setter
    def other_phone(self, other_phone: 'PhoneNumber') -> None:
        """
        Sets the other_phone of this ExternalContact.


        :param other_phone: The other_phone of this ExternalContact.
        :type: PhoneNumber
        """
        

        self._other_phone = other_phone

    @property
    def work_email(self) -> str:
        """
        Gets the work_email of this ExternalContact.


        :return: The work_email of this ExternalContact.
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email: str) -> None:
        """
        Sets the work_email of this ExternalContact.


        :param work_email: The work_email of this ExternalContact.
        :type: str
        """
        

        self._work_email = work_email

    @property
    def personal_email(self) -> str:
        """
        Gets the personal_email of this ExternalContact.


        :return: The personal_email of this ExternalContact.
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email: str) -> None:
        """
        Sets the personal_email of this ExternalContact.


        :param personal_email: The personal_email of this ExternalContact.
        :type: str
        """
        

        self._personal_email = personal_email

    @property
    def other_email(self) -> str:
        """
        Gets the other_email of this ExternalContact.


        :return: The other_email of this ExternalContact.
        :rtype: str
        """
        return self._other_email

    @other_email.setter
    def other_email(self, other_email: str) -> None:
        """
        Sets the other_email of this ExternalContact.


        :param other_email: The other_email of this ExternalContact.
        :type: str
        """
        

        self._other_email = other_email

    @property
    def address(self) -> 'ContactAddress':
        """
        Gets the address of this ExternalContact.


        :return: The address of this ExternalContact.
        :rtype: ContactAddress
        """
        return self._address

    @address.setter
    def address(self, address: 'ContactAddress') -> None:
        """
        Sets the address of this ExternalContact.


        :param address: The address of this ExternalContact.
        :type: ContactAddress
        """
        

        self._address = address

    @property
    def twitter_id(self) -> 'TwitterId':
        """
        Gets the twitter_id of this ExternalContact.


        :return: The twitter_id of this ExternalContact.
        :rtype: TwitterId
        """
        return self._twitter_id

    @twitter_id.setter
    def twitter_id(self, twitter_id: 'TwitterId') -> None:
        """
        Sets the twitter_id of this ExternalContact.


        :param twitter_id: The twitter_id of this ExternalContact.
        :type: TwitterId
        """
        

        self._twitter_id = twitter_id

    @property
    def line_id(self) -> 'LineId':
        """
        Gets the line_id of this ExternalContact.


        :return: The line_id of this ExternalContact.
        :rtype: LineId
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id: 'LineId') -> None:
        """
        Sets the line_id of this ExternalContact.


        :param line_id: The line_id of this ExternalContact.
        :type: LineId
        """
        

        self._line_id = line_id

    @property
    def whats_app_id(self) -> 'WhatsAppId':
        """
        Gets the whats_app_id of this ExternalContact.


        :return: The whats_app_id of this ExternalContact.
        :rtype: WhatsAppId
        """
        return self._whats_app_id

    @whats_app_id.setter
    def whats_app_id(self, whats_app_id: 'WhatsAppId') -> None:
        """
        Sets the whats_app_id of this ExternalContact.


        :param whats_app_id: The whats_app_id of this ExternalContact.
        :type: WhatsAppId
        """
        

        self._whats_app_id = whats_app_id

    @property
    def facebook_id(self) -> 'FacebookId':
        """
        Gets the facebook_id of this ExternalContact.


        :return: The facebook_id of this ExternalContact.
        :rtype: FacebookId
        """
        return self._facebook_id

    @facebook_id.setter
    def facebook_id(self, facebook_id: 'FacebookId') -> None:
        """
        Sets the facebook_id of this ExternalContact.


        :param facebook_id: The facebook_id of this ExternalContact.
        :type: FacebookId
        """
        

        self._facebook_id = facebook_id

    @property
    def instagram_id(self) -> 'InstagramId':
        """
        Gets the instagram_id of this ExternalContact.
        User information for an Instagram account

        :return: The instagram_id of this ExternalContact.
        :rtype: InstagramId
        """
        return self._instagram_id

    @instagram_id.setter
    def instagram_id(self, instagram_id: 'InstagramId') -> None:
        """
        Sets the instagram_id of this ExternalContact.
        User information for an Instagram account

        :param instagram_id: The instagram_id of this ExternalContact.
        :type: InstagramId
        """
        

        self._instagram_id = instagram_id

    @property
    def external_ids(self) -> List['ExternalId']:
        """
        Gets the external_ids of this ExternalContact.
        A list of external identifiers that identify this contact in an external system

        :return: The external_ids of this ExternalContact.
        :rtype: list[ExternalId]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids: List['ExternalId']) -> None:
        """
        Sets the external_ids of this ExternalContact.
        A list of external identifiers that identify this contact in an external system

        :param external_ids: The external_ids of this ExternalContact.
        :type: list[ExternalId]
        """
        

        self._external_ids = external_ids

    @property
    def identifiers(self) -> List['ContactIdentifier']:
        """
        Gets the identifiers of this ExternalContact.
        Identifiers claimed by this contact

        :return: The identifiers of this ExternalContact.
        :rtype: list[ContactIdentifier]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers: List['ContactIdentifier']) -> None:
        """
        Sets the identifiers of this ExternalContact.
        Identifiers claimed by this contact

        :param identifiers: The identifiers of this ExternalContact.
        :type: list[ContactIdentifier]
        """
        

        self._identifiers = identifiers

    @property
    def modify_date(self) -> datetime:
        """
        Gets the modify_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modify_date of this ExternalContact.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date: datetime) -> None:
        """
        Sets the modify_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modify_date: The modify_date of this ExternalContact.
        :type: datetime
        """
        

        self._modify_date = modify_date

    @property
    def create_date(self) -> datetime:
        """
        Gets the create_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The create_date of this ExternalContact.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime) -> None:
        """
        Sets the create_date of this ExternalContact.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param create_date: The create_date of this ExternalContact.
        :type: datetime
        """
        

        self._create_date = create_date

    @property
    def external_organization(self) -> 'ExternalOrganization':
        """
        Gets the external_organization of this ExternalContact.


        :return: The external_organization of this ExternalContact.
        :rtype: ExternalOrganization
        """
        return self._external_organization

    @external_organization.setter
    def external_organization(self, external_organization: 'ExternalOrganization') -> None:
        """
        Sets the external_organization of this ExternalContact.


        :param external_organization: The external_organization of this ExternalContact.
        :type: ExternalOrganization
        """
        

        self._external_organization = external_organization

    @property
    def survey_opt_out(self) -> bool:
        """
        Gets the survey_opt_out of this ExternalContact.


        :return: The survey_opt_out of this ExternalContact.
        :rtype: bool
        """
        return self._survey_opt_out

    @survey_opt_out.setter
    def survey_opt_out(self, survey_opt_out: bool) -> None:
        """
        Sets the survey_opt_out of this ExternalContact.


        :param survey_opt_out: The survey_opt_out of this ExternalContact.
        :type: bool
        """
        

        self._survey_opt_out = survey_opt_out

    @property
    def external_system_url(self) -> str:
        """
        Gets the external_system_url of this ExternalContact.
        A string that identifies an external system-of-record resource that may have more detailed information on the contact. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :return: The external_system_url of this ExternalContact.
        :rtype: str
        """
        return self._external_system_url

    @external_system_url.setter
    def external_system_url(self, external_system_url: str) -> None:
        """
        Sets the external_system_url of this ExternalContact.
        A string that identifies an external system-of-record resource that may have more detailed information on the contact. It should be a valid URL (including the http/https protocol, port, and path [if any]). The value is automatically trimmed of any leading and trailing whitespace.

        :param external_system_url: The external_system_url of this ExternalContact.
        :type: str
        """
        

        self._external_system_url = external_system_url

    @property
    def schema(self) -> 'DataSchema':
        """
        Gets the schema of this ExternalContact.
        The schema defining custom fields for this contact

        :return: The schema of this ExternalContact.
        :rtype: DataSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema: 'DataSchema') -> None:
        """
        Sets the schema of this ExternalContact.
        The schema defining custom fields for this contact

        :param schema: The schema of this ExternalContact.
        :type: DataSchema
        """
        

        self._schema = schema

    @property
    def custom_fields(self) -> Dict[str, object]:
        """
        Gets the custom_fields of this ExternalContact.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :return: The custom_fields of this ExternalContact.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields: Dict[str, object]) -> None:
        """
        Sets the custom_fields of this ExternalContact.
        Custom fields defined in the schema referenced by schemaId and schemaVersion.

        :param custom_fields: The custom_fields of this ExternalContact.
        :type: dict(str, object)
        """
        

        self._custom_fields = custom_fields

    @property
    def external_data_sources(self) -> List['ExternalDataSource']:
        """
        Gets the external_data_sources of this ExternalContact.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :return: The external_data_sources of this ExternalContact.
        :rtype: list[ExternalDataSource]
        """
        return self._external_data_sources

    @external_data_sources.setter
    def external_data_sources(self, external_data_sources: List['ExternalDataSource']) -> None:
        """
        Sets the external_data_sources of this ExternalContact.
        Links to the sources of data (e.g. one source might be a CRM) that contributed data to this record.  Read-only, and only populated when requested via expand param.

        :param external_data_sources: The external_data_sources of this ExternalContact.
        :type: list[ExternalDataSource]
        """
        

        self._external_data_sources = external_data_sources

    @property
    def type(self) -> str:
        """
        Gets the type of this ExternalContact.
        The type of contact

        :return: The type of this ExternalContact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this ExternalContact.
        The type of contact

        :param type: The type of this ExternalContact.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Ephemeral", "Identified", "Curated"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def canonical_contact(self) -> 'ContactAddressableEntityRef':
        """
        Gets the canonical_contact of this ExternalContact.
        The contact at the head of the merge tree. If null, this contact is not a part of any merge.

        :return: The canonical_contact of this ExternalContact.
        :rtype: ContactAddressableEntityRef
        """
        return self._canonical_contact

    @canonical_contact.setter
    def canonical_contact(self, canonical_contact: 'ContactAddressableEntityRef') -> None:
        """
        Sets the canonical_contact of this ExternalContact.
        The contact at the head of the merge tree. If null, this contact is not a part of any merge.

        :param canonical_contact: The canonical_contact of this ExternalContact.
        :type: ContactAddressableEntityRef
        """
        

        self._canonical_contact = canonical_contact

    @property
    def merge_set(self) -> List['ContactAddressableEntityRef']:
        """
        Gets the merge_set of this ExternalContact.
        The set of all contacts that are a part of the merge tree. If null, this contact is not a part of any merge.

        :return: The merge_set of this ExternalContact.
        :rtype: list[ContactAddressableEntityRef]
        """
        return self._merge_set

    @merge_set.setter
    def merge_set(self, merge_set: List['ContactAddressableEntityRef']) -> None:
        """
        Sets the merge_set of this ExternalContact.
        The set of all contacts that are a part of the merge tree. If null, this contact is not a part of any merge.

        :param merge_set: The merge_set of this ExternalContact.
        :type: list[ContactAddressableEntityRef]
        """
        

        self._merge_set = merge_set

    @property
    def merged_from(self) -> List['ContactAddressableEntityRef']:
        """
        Gets the merged_from of this ExternalContact.
        The input contacts from the merge operation.

        :return: The merged_from of this ExternalContact.
        :rtype: list[ContactAddressableEntityRef]
        """
        return self._merged_from

    @merged_from.setter
    def merged_from(self, merged_from: List['ContactAddressableEntityRef']) -> None:
        """
        Sets the merged_from of this ExternalContact.
        The input contacts from the merge operation.

        :param merged_from: The merged_from of this ExternalContact.
        :type: list[ContactAddressableEntityRef]
        """
        

        self._merged_from = merged_from

    @property
    def merged_to(self) -> 'ContactAddressableEntityRef':
        """
        Gets the merged_to of this ExternalContact.
        The output contact from the merge operation.

        :return: The merged_to of this ExternalContact.
        :rtype: ContactAddressableEntityRef
        """
        return self._merged_to

    @merged_to.setter
    def merged_to(self, merged_to: 'ContactAddressableEntityRef') -> None:
        """
        Sets the merged_to of this ExternalContact.
        The output contact from the merge operation.

        :param merged_to: The merged_to of this ExternalContact.
        :type: ContactAddressableEntityRef
        """
        

        self._merged_to = merged_to

    @property
    def merge_operation(self) -> 'MergeOperation':
        """
        Gets the merge_operation of this ExternalContact.
        Information about the merge history of this contact. If null, this contact is not a part of any merge.

        :return: The merge_operation of this ExternalContact.
        :rtype: MergeOperation
        """
        return self._merge_operation

    @merge_operation.setter
    def merge_operation(self, merge_operation: 'MergeOperation') -> None:
        """
        Sets the merge_operation of this ExternalContact.
        Information about the merge history of this contact. If null, this contact is not a part of any merge.

        :param merge_operation: The merge_operation of this ExternalContact.
        :type: MergeOperation
        """
        

        self._merge_operation = merge_operation

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ExternalContact.
        The URI for this object

        :return: The self_uri of this ExternalContact.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ExternalContact.
        The URI for this object

        :param self_uri: The self_uri of this ExternalContact.
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

