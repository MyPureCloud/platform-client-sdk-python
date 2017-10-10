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


class OrgUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrgUser - a model defined in Swagger

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
            'state': 'str',
            'title': 'str',
            'username': 'str',
            'manager': 'User',
            'images': 'list[UserImage]',
            'version': 'int',
            'routing_status': 'RoutingStatus',
            'presence': 'UserPresence',
            'conversation_summary': 'UserConversationSummary',
            'out_of_office': 'OutOfOffice',
            'geolocation': 'Geolocation',
            'station': 'UserStations',
            'authorization': 'UserAuthorization',
            'profile_skills': 'list[str]',
            'locations': 'list[Location]',
            'groups': 'list[Group]',
            'organization': 'Organization'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'chat': 'chat',
            'department': 'department',
            'email': 'email',
            'primary_contact_info': 'primaryContactInfo',
            'addresses': 'addresses',
            'state': 'state',
            'title': 'title',
            'username': 'username',
            'manager': 'manager',
            'images': 'images',
            'version': 'version',
            'routing_status': 'routingStatus',
            'presence': 'presence',
            'conversation_summary': 'conversationSummary',
            'out_of_office': 'outOfOffice',
            'geolocation': 'geolocation',
            'station': 'station',
            'authorization': 'authorization',
            'profile_skills': 'profileSkills',
            'locations': 'locations',
            'groups': 'groups',
            'organization': 'organization'
        }

        self._id = None
        self._name = None
        self._chat = None
        self._department = None
        self._email = None
        self._primary_contact_info = None
        self._addresses = None
        self._state = None
        self._title = None
        self._username = None
        self._manager = None
        self._images = None
        self._version = None
        self._routing_status = None
        self._presence = None
        self._conversation_summary = None
        self._out_of_office = None
        self._geolocation = None
        self._station = None
        self._authorization = None
        self._profile_skills = None
        self._locations = None
        self._groups = None
        self._organization = None

    @property
    def id(self):
        """
        Gets the id of this OrgUser.
        The globally unique identifier for the object.

        :return: The id of this OrgUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrgUser.
        The globally unique identifier for the object.

        :param id: The id of this OrgUser.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OrgUser.


        :return: The name of this OrgUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrgUser.


        :param name: The name of this OrgUser.
        :type: str
        """
        
        self._name = name

    @property
    def chat(self):
        """
        Gets the chat of this OrgUser.


        :return: The chat of this OrgUser.
        :rtype: Chat
        """
        return self._chat

    @chat.setter
    def chat(self, chat):
        """
        Sets the chat of this OrgUser.


        :param chat: The chat of this OrgUser.
        :type: Chat
        """
        
        self._chat = chat

    @property
    def department(self):
        """
        Gets the department of this OrgUser.


        :return: The department of this OrgUser.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this OrgUser.


        :param department: The department of this OrgUser.
        :type: str
        """
        
        self._department = department

    @property
    def email(self):
        """
        Gets the email of this OrgUser.


        :return: The email of this OrgUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this OrgUser.


        :param email: The email of this OrgUser.
        :type: str
        """
        
        self._email = email

    @property
    def primary_contact_info(self):
        """
        Gets the primary_contact_info of this OrgUser.
        Auto populated from addresses.

        :return: The primary_contact_info of this OrgUser.
        :rtype: list[Contact]
        """
        return self._primary_contact_info

    @primary_contact_info.setter
    def primary_contact_info(self, primary_contact_info):
        """
        Sets the primary_contact_info of this OrgUser.
        Auto populated from addresses.

        :param primary_contact_info: The primary_contact_info of this OrgUser.
        :type: list[Contact]
        """
        
        self._primary_contact_info = primary_contact_info

    @property
    def addresses(self):
        """
        Gets the addresses of this OrgUser.
        Email addresses and phone numbers for this user

        :return: The addresses of this OrgUser.
        :rtype: list[Contact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this OrgUser.
        Email addresses and phone numbers for this user

        :param addresses: The addresses of this OrgUser.
        :type: list[Contact]
        """
        
        self._addresses = addresses

    @property
    def state(self):
        """
        Gets the state of this OrgUser.
        The current state for this user.

        :return: The state of this OrgUser.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this OrgUser.
        The current state for this user.

        :param state: The state of this OrgUser.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def title(self):
        """
        Gets the title of this OrgUser.


        :return: The title of this OrgUser.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OrgUser.


        :param title: The title of this OrgUser.
        :type: str
        """
        
        self._title = title

    @property
    def username(self):
        """
        Gets the username of this OrgUser.


        :return: The username of this OrgUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this OrgUser.


        :param username: The username of this OrgUser.
        :type: str
        """
        
        self._username = username

    @property
    def manager(self):
        """
        Gets the manager of this OrgUser.


        :return: The manager of this OrgUser.
        :rtype: User
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this OrgUser.


        :param manager: The manager of this OrgUser.
        :type: User
        """
        
        self._manager = manager

    @property
    def images(self):
        """
        Gets the images of this OrgUser.


        :return: The images of this OrgUser.
        :rtype: list[UserImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this OrgUser.


        :param images: The images of this OrgUser.
        :type: list[UserImage]
        """
        
        self._images = images

    @property
    def version(self):
        """
        Gets the version of this OrgUser.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :return: The version of this OrgUser.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OrgUser.
        Required when updating a user, this value should be the current version of the user.  The current version can be obtained with a GET on the user before doing a PATCH.

        :param version: The version of this OrgUser.
        :type: int
        """
        
        self._version = version

    @property
    def routing_status(self):
        """
        Gets the routing_status of this OrgUser.
        ACD routing status

        :return: The routing_status of this OrgUser.
        :rtype: RoutingStatus
        """
        return self._routing_status

    @routing_status.setter
    def routing_status(self, routing_status):
        """
        Sets the routing_status of this OrgUser.
        ACD routing status

        :param routing_status: The routing_status of this OrgUser.
        :type: RoutingStatus
        """
        
        self._routing_status = routing_status

    @property
    def presence(self):
        """
        Gets the presence of this OrgUser.
        Active presence

        :return: The presence of this OrgUser.
        :rtype: UserPresence
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this OrgUser.
        Active presence

        :param presence: The presence of this OrgUser.
        :type: UserPresence
        """
        
        self._presence = presence

    @property
    def conversation_summary(self):
        """
        Gets the conversation_summary of this OrgUser.
        Summary of conversion statistics for conversation types.

        :return: The conversation_summary of this OrgUser.
        :rtype: UserConversationSummary
        """
        return self._conversation_summary

    @conversation_summary.setter
    def conversation_summary(self, conversation_summary):
        """
        Sets the conversation_summary of this OrgUser.
        Summary of conversion statistics for conversation types.

        :param conversation_summary: The conversation_summary of this OrgUser.
        :type: UserConversationSummary
        """
        
        self._conversation_summary = conversation_summary

    @property
    def out_of_office(self):
        """
        Gets the out_of_office of this OrgUser.
        Determine if out of office is enabled

        :return: The out_of_office of this OrgUser.
        :rtype: OutOfOffice
        """
        return self._out_of_office

    @out_of_office.setter
    def out_of_office(self, out_of_office):
        """
        Sets the out_of_office of this OrgUser.
        Determine if out of office is enabled

        :param out_of_office: The out_of_office of this OrgUser.
        :type: OutOfOffice
        """
        
        self._out_of_office = out_of_office

    @property
    def geolocation(self):
        """
        Gets the geolocation of this OrgUser.
        Current geolocation position

        :return: The geolocation of this OrgUser.
        :rtype: Geolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """
        Sets the geolocation of this OrgUser.
        Current geolocation position

        :param geolocation: The geolocation of this OrgUser.
        :type: Geolocation
        """
        
        self._geolocation = geolocation

    @property
    def station(self):
        """
        Gets the station of this OrgUser.
        Effective, default, and last station information

        :return: The station of this OrgUser.
        :rtype: UserStations
        """
        return self._station

    @station.setter
    def station(self, station):
        """
        Sets the station of this OrgUser.
        Effective, default, and last station information

        :param station: The station of this OrgUser.
        :type: UserStations
        """
        
        self._station = station

    @property
    def authorization(self):
        """
        Gets the authorization of this OrgUser.
        Roles and permissions assigned to the user

        :return: The authorization of this OrgUser.
        :rtype: UserAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this OrgUser.
        Roles and permissions assigned to the user

        :param authorization: The authorization of this OrgUser.
        :type: UserAuthorization
        """
        
        self._authorization = authorization

    @property
    def profile_skills(self):
        """
        Gets the profile_skills of this OrgUser.
        Skills possessed by the user

        :return: The profile_skills of this OrgUser.
        :rtype: list[str]
        """
        return self._profile_skills

    @profile_skills.setter
    def profile_skills(self, profile_skills):
        """
        Sets the profile_skills of this OrgUser.
        Skills possessed by the user

        :param profile_skills: The profile_skills of this OrgUser.
        :type: list[str]
        """
        
        self._profile_skills = profile_skills

    @property
    def locations(self):
        """
        Gets the locations of this OrgUser.
        The user placement at each site location.

        :return: The locations of this OrgUser.
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this OrgUser.
        The user placement at each site location.

        :param locations: The locations of this OrgUser.
        :type: list[Location]
        """
        
        self._locations = locations

    @property
    def groups(self):
        """
        Gets the groups of this OrgUser.
        The groups the user is a member of

        :return: The groups of this OrgUser.
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this OrgUser.
        The groups the user is a member of

        :param groups: The groups of this OrgUser.
        :type: list[Group]
        """
        
        self._groups = groups

    @property
    def organization(self):
        """
        Gets the organization of this OrgUser.


        :return: The organization of this OrgUser.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this OrgUser.


        :param organization: The organization of this OrgUser.
        :type: Organization
        """
        
        self._organization = organization

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
