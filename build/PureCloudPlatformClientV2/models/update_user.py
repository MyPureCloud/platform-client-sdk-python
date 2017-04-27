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


class UpdateUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UpdateUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'chat': 'Chat',
            'department': 'str',
            'email': 'str',
            'primary_contact_info': 'list[Contact]',
            'addresses': 'list[Contact]',
            'title': 'str',
            'username': 'str',
            'manager': 'str',
            'images': 'list[UserImage]',
            'version': 'int',
            'profile_skills': 'list[str]',
            'locations': 'list[Location]',
            'groups': 'list[Group]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'chat': 'chat',
            'department': 'department',
            'email': 'email',
            'primary_contact_info': 'primaryContactInfo',
            'addresses': 'addresses',
            'title': 'title',
            'username': 'username',
            'manager': 'manager',
            'images': 'images',
            'version': 'version',
            'profile_skills': 'profileSkills',
            'locations': 'locations',
            'groups': 'groups',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._chat = None
        self._department = None
        self._email = None
        self._primary_contact_info = None
        self._addresses = None
        self._title = None
        self._username = None
        self._manager = None
        self._images = None
        self._version = None
        self._profile_skills = None
        self._locations = None
        self._groups = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this UpdateUser.
        The globally unique identifier for the object.

        :return: The id of this UpdateUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateUser.
        The globally unique identifier for the object.

        :param id: The id of this UpdateUser.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this UpdateUser.


        :return: The name of this UpdateUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateUser.


        :param name: The name of this UpdateUser.
        :type: str
        """
        
        self._name = name

    @property
    def chat(self):
        """
        Gets the chat of this UpdateUser.


        :return: The chat of this UpdateUser.
        :rtype: Chat
        """
        return self._chat

    @chat.setter
    def chat(self, chat):
        """
        Sets the chat of this UpdateUser.


        :param chat: The chat of this UpdateUser.
        :type: Chat
        """
        
        self._chat = chat

    @property
    def department(self):
        """
        Gets the department of this UpdateUser.


        :return: The department of this UpdateUser.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this UpdateUser.


        :param department: The department of this UpdateUser.
        :type: str
        """
        
        self._department = department

    @property
    def email(self):
        """
        Gets the email of this UpdateUser.


        :return: The email of this UpdateUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateUser.


        :param email: The email of this UpdateUser.
        :type: str
        """
        
        self._email = email

    @property
    def primary_contact_info(self):
        """
        Gets the primary_contact_info of this UpdateUser.


        :return: The primary_contact_info of this UpdateUser.
        :rtype: list[Contact]
        """
        return self._primary_contact_info

    @primary_contact_info.setter
    def primary_contact_info(self, primary_contact_info):
        """
        Sets the primary_contact_info of this UpdateUser.


        :param primary_contact_info: The primary_contact_info of this UpdateUser.
        :type: list[Contact]
        """
        
        self._primary_contact_info = primary_contact_info

    @property
    def addresses(self):
        """
        Gets the addresses of this UpdateUser.
        Email addresses and phone numbers for this user

        :return: The addresses of this UpdateUser.
        :rtype: list[Contact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this UpdateUser.
        Email addresses and phone numbers for this user

        :param addresses: The addresses of this UpdateUser.
        :type: list[Contact]
        """
        
        self._addresses = addresses

    @property
    def title(self):
        """
        Gets the title of this UpdateUser.


        :return: The title of this UpdateUser.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UpdateUser.


        :param title: The title of this UpdateUser.
        :type: str
        """
        
        self._title = title

    @property
    def username(self):
        """
        Gets the username of this UpdateUser.


        :return: The username of this UpdateUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateUser.


        :param username: The username of this UpdateUser.
        :type: str
        """
        
        self._username = username

    @property
    def manager(self):
        """
        Gets the manager of this UpdateUser.


        :return: The manager of this UpdateUser.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this UpdateUser.


        :param manager: The manager of this UpdateUser.
        :type: str
        """
        
        self._manager = manager

    @property
    def images(self):
        """
        Gets the images of this UpdateUser.


        :return: The images of this UpdateUser.
        :rtype: list[UserImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this UpdateUser.


        :param images: The images of this UpdateUser.
        :type: list[UserImage]
        """
        
        self._images = images

    @property
    def version(self):
        """
        Gets the version of this UpdateUser.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :return: The version of this UpdateUser.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateUser.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :param version: The version of this UpdateUser.
        :type: int
        """
        
        self._version = version

    @property
    def profile_skills(self):
        """
        Gets the profile_skills of this UpdateUser.
        Skills possessed by the user

        :return: The profile_skills of this UpdateUser.
        :rtype: list[str]
        """
        return self._profile_skills

    @profile_skills.setter
    def profile_skills(self, profile_skills):
        """
        Sets the profile_skills of this UpdateUser.
        Skills possessed by the user

        :param profile_skills: The profile_skills of this UpdateUser.
        :type: list[str]
        """
        
        self._profile_skills = profile_skills

    @property
    def locations(self):
        """
        Gets the locations of this UpdateUser.
        The user placement at each site location.

        :return: The locations of this UpdateUser.
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this UpdateUser.
        The user placement at each site location.

        :param locations: The locations of this UpdateUser.
        :type: list[Location]
        """
        
        self._locations = locations

    @property
    def groups(self):
        """
        Gets the groups of this UpdateUser.
        The groups the user is a member of

        :return: The groups of this UpdateUser.
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UpdateUser.
        The groups the user is a member of

        :param groups: The groups of this UpdateUser.
        :type: list[Group]
        """
        
        self._groups = groups

    @property
    def self_uri(self):
        """
        Gets the self_uri of this UpdateUser.
        The URI for this object

        :return: The self_uri of this UpdateUser.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this UpdateUser.
        The URI for this object

        :param self_uri: The self_uri of this UpdateUser.
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
