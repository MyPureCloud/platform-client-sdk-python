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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ExternalContactsContactChangedTopicContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ExternalContactsContactChangedTopicContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'salutation': 'str',
            'title': 'str',
            'work_phone': 'ExternalContactsContactChangedTopicPhoneNumber',
            'cell_phone': 'ExternalContactsContactChangedTopicPhoneNumber',
            'home_phone': 'ExternalContactsContactChangedTopicPhoneNumber',
            'other_phone': 'ExternalContactsContactChangedTopicPhoneNumber',
            'work_email': 'str',
            'personal_email': 'str',
            'other_email': 'str',
            'address': 'ExternalContactsContactChangedTopicContactAddress',
            'survey_opt_out': 'bool',
            'external_system_url': 'str',
            'twitter_id': 'ExternalContactsContactChangedTopicTwitterId',
            'line_id': 'ExternalContactsContactChangedTopicLineId',
            'whats_app_id': 'ExternalContactsContactChangedTopicWhatsAppId',
            'facebook_id': 'ExternalContactsContactChangedTopicFacebookId'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
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
            'survey_opt_out': 'surveyOptOut',
            'external_system_url': 'externalSystemUrl',
            'twitter_id': 'twitterId',
            'line_id': 'lineId',
            'whats_app_id': 'whatsAppId',
            'facebook_id': 'facebookId'
        }

        self._id = None
        self._type = None
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
        self._survey_opt_out = None
        self._external_system_url = None
        self._twitter_id = None
        self._line_id = None
        self._whats_app_id = None
        self._facebook_id = None

    @property
    def id(self):
        """
        Gets the id of this ExternalContactsContactChangedTopicContact.


        :return: The id of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalContactsContactChangedTopicContact.


        :param id: The id of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this ExternalContactsContactChangedTopicContact.


        :return: The type of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExternalContactsContactChangedTopicContact.


        :param type: The type of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        allowed_values = ["Ephemeral", "Identified", "Curated"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def first_name(self):
        """
        Gets the first_name of this ExternalContactsContactChangedTopicContact.


        :return: The first_name of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this ExternalContactsContactChangedTopicContact.


        :param first_name: The first_name of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this ExternalContactsContactChangedTopicContact.


        :return: The middle_name of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this ExternalContactsContactChangedTopicContact.


        :param middle_name: The middle_name of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this ExternalContactsContactChangedTopicContact.


        :return: The last_name of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this ExternalContactsContactChangedTopicContact.


        :param last_name: The last_name of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._last_name = last_name

    @property
    def salutation(self):
        """
        Gets the salutation of this ExternalContactsContactChangedTopicContact.


        :return: The salutation of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """
        Sets the salutation of this ExternalContactsContactChangedTopicContact.


        :param salutation: The salutation of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._salutation = salutation

    @property
    def title(self):
        """
        Gets the title of this ExternalContactsContactChangedTopicContact.


        :return: The title of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ExternalContactsContactChangedTopicContact.


        :param title: The title of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._title = title

    @property
    def work_phone(self):
        """
        Gets the work_phone of this ExternalContactsContactChangedTopicContact.


        :return: The work_phone of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicPhoneNumber
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """
        Sets the work_phone of this ExternalContactsContactChangedTopicContact.


        :param work_phone: The work_phone of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicPhoneNumber
        """
        

        self._work_phone = work_phone

    @property
    def cell_phone(self):
        """
        Gets the cell_phone of this ExternalContactsContactChangedTopicContact.


        :return: The cell_phone of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicPhoneNumber
        """
        return self._cell_phone

    @cell_phone.setter
    def cell_phone(self, cell_phone):
        """
        Sets the cell_phone of this ExternalContactsContactChangedTopicContact.


        :param cell_phone: The cell_phone of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicPhoneNumber
        """
        

        self._cell_phone = cell_phone

    @property
    def home_phone(self):
        """
        Gets the home_phone of this ExternalContactsContactChangedTopicContact.


        :return: The home_phone of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicPhoneNumber
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """
        Sets the home_phone of this ExternalContactsContactChangedTopicContact.


        :param home_phone: The home_phone of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicPhoneNumber
        """
        

        self._home_phone = home_phone

    @property
    def other_phone(self):
        """
        Gets the other_phone of this ExternalContactsContactChangedTopicContact.


        :return: The other_phone of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicPhoneNumber
        """
        return self._other_phone

    @other_phone.setter
    def other_phone(self, other_phone):
        """
        Sets the other_phone of this ExternalContactsContactChangedTopicContact.


        :param other_phone: The other_phone of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicPhoneNumber
        """
        

        self._other_phone = other_phone

    @property
    def work_email(self):
        """
        Gets the work_email of this ExternalContactsContactChangedTopicContact.


        :return: The work_email of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email):
        """
        Sets the work_email of this ExternalContactsContactChangedTopicContact.


        :param work_email: The work_email of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._work_email = work_email

    @property
    def personal_email(self):
        """
        Gets the personal_email of this ExternalContactsContactChangedTopicContact.


        :return: The personal_email of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """
        Sets the personal_email of this ExternalContactsContactChangedTopicContact.


        :param personal_email: The personal_email of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._personal_email = personal_email

    @property
    def other_email(self):
        """
        Gets the other_email of this ExternalContactsContactChangedTopicContact.


        :return: The other_email of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._other_email

    @other_email.setter
    def other_email(self, other_email):
        """
        Sets the other_email of this ExternalContactsContactChangedTopicContact.


        :param other_email: The other_email of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._other_email = other_email

    @property
    def address(self):
        """
        Gets the address of this ExternalContactsContactChangedTopicContact.


        :return: The address of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicContactAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ExternalContactsContactChangedTopicContact.


        :param address: The address of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicContactAddress
        """
        

        self._address = address

    @property
    def survey_opt_out(self):
        """
        Gets the survey_opt_out of this ExternalContactsContactChangedTopicContact.


        :return: The survey_opt_out of this ExternalContactsContactChangedTopicContact.
        :rtype: bool
        """
        return self._survey_opt_out

    @survey_opt_out.setter
    def survey_opt_out(self, survey_opt_out):
        """
        Sets the survey_opt_out of this ExternalContactsContactChangedTopicContact.


        :param survey_opt_out: The survey_opt_out of this ExternalContactsContactChangedTopicContact.
        :type: bool
        """
        

        self._survey_opt_out = survey_opt_out

    @property
    def external_system_url(self):
        """
        Gets the external_system_url of this ExternalContactsContactChangedTopicContact.


        :return: The external_system_url of this ExternalContactsContactChangedTopicContact.
        :rtype: str
        """
        return self._external_system_url

    @external_system_url.setter
    def external_system_url(self, external_system_url):
        """
        Sets the external_system_url of this ExternalContactsContactChangedTopicContact.


        :param external_system_url: The external_system_url of this ExternalContactsContactChangedTopicContact.
        :type: str
        """
        

        self._external_system_url = external_system_url

    @property
    def twitter_id(self):
        """
        Gets the twitter_id of this ExternalContactsContactChangedTopicContact.


        :return: The twitter_id of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicTwitterId
        """
        return self._twitter_id

    @twitter_id.setter
    def twitter_id(self, twitter_id):
        """
        Sets the twitter_id of this ExternalContactsContactChangedTopicContact.


        :param twitter_id: The twitter_id of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicTwitterId
        """
        

        self._twitter_id = twitter_id

    @property
    def line_id(self):
        """
        Gets the line_id of this ExternalContactsContactChangedTopicContact.


        :return: The line_id of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicLineId
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """
        Sets the line_id of this ExternalContactsContactChangedTopicContact.


        :param line_id: The line_id of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicLineId
        """
        

        self._line_id = line_id

    @property
    def whats_app_id(self):
        """
        Gets the whats_app_id of this ExternalContactsContactChangedTopicContact.


        :return: The whats_app_id of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicWhatsAppId
        """
        return self._whats_app_id

    @whats_app_id.setter
    def whats_app_id(self, whats_app_id):
        """
        Sets the whats_app_id of this ExternalContactsContactChangedTopicContact.


        :param whats_app_id: The whats_app_id of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicWhatsAppId
        """
        

        self._whats_app_id = whats_app_id

    @property
    def facebook_id(self):
        """
        Gets the facebook_id of this ExternalContactsContactChangedTopicContact.


        :return: The facebook_id of this ExternalContactsContactChangedTopicContact.
        :rtype: ExternalContactsContactChangedTopicFacebookId
        """
        return self._facebook_id

    @facebook_id.setter
    def facebook_id(self, facebook_id):
        """
        Sets the facebook_id of this ExternalContactsContactChangedTopicContact.


        :param facebook_id: The facebook_id of this ExternalContactsContactChangedTopicContact.
        :type: ExternalContactsContactChangedTopicFacebookId
        """
        

        self._facebook_id = facebook_id

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
