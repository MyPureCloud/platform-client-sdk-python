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

class Session(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Session - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'customer_id': 'str',
            'customer_id_type': 'str',
            'type': 'str',
            'external_id': 'str',
            'external_url': 'str',
            'short_id': 'str',
            'outcome_achievements': 'list[OutcomeAchievement]',
            'segment_assignments': 'list[SessionSegmentAssignment]',
            'attributes': 'dict(str, CustomEventAttribute)',
            'attribute_lists': 'dict(str, CustomEventAttributeList)',
            'browser': 'Browser',
            'device': 'Device',
            'geolocation': 'JourneyGeolocation',
            'ip_address': 'str',
            'ip_organization': 'str',
            'last_page': 'JourneyPage',
            'mkt_campaign': 'JourneyCampaign',
            'referrer': 'Referrer',
            'search_terms': 'list[str]',
            'user_agent_string': 'str',
            'duration_in_seconds': 'int',
            'event_count': 'int',
            'pageview_count': 'int',
            'screenview_count': 'int',
            'last_event': 'SessionLastEvent',
            'last_connected_queue': 'ConnectedQueue',
            'last_connected_user': 'ConnectedUser',
            'last_user_disposition': 'ConversationUserDisposition',
            'conversation_channels': 'list[ConversationChannel]',
            'originating_direction': 'str',
            'conversation_subject': 'str',
            'authenticated': 'bool',
            'self_uri': 'str',
            'created_date': 'datetime',
            'ended_date': 'datetime',
            'external_contact': 'AddressableEntityRef',
            'away_date': 'datetime',
            'idle_date': 'datetime',
            'conversation': 'AddressableEntityRef'
        }

        self.attribute_map = {
            'id': 'id',
            'customer_id': 'customerId',
            'customer_id_type': 'customerIdType',
            'type': 'type',
            'external_id': 'externalId',
            'external_url': 'externalUrl',
            'short_id': 'shortId',
            'outcome_achievements': 'outcomeAchievements',
            'segment_assignments': 'segmentAssignments',
            'attributes': 'attributes',
            'attribute_lists': 'attributeLists',
            'browser': 'browser',
            'device': 'device',
            'geolocation': 'geolocation',
            'ip_address': 'ipAddress',
            'ip_organization': 'ipOrganization',
            'last_page': 'lastPage',
            'mkt_campaign': 'mktCampaign',
            'referrer': 'referrer',
            'search_terms': 'searchTerms',
            'user_agent_string': 'userAgentString',
            'duration_in_seconds': 'durationInSeconds',
            'event_count': 'eventCount',
            'pageview_count': 'pageviewCount',
            'screenview_count': 'screenviewCount',
            'last_event': 'lastEvent',
            'last_connected_queue': 'lastConnectedQueue',
            'last_connected_user': 'lastConnectedUser',
            'last_user_disposition': 'lastUserDisposition',
            'conversation_channels': 'conversationChannels',
            'originating_direction': 'originatingDirection',
            'conversation_subject': 'conversationSubject',
            'authenticated': 'authenticated',
            'self_uri': 'selfUri',
            'created_date': 'createdDate',
            'ended_date': 'endedDate',
            'external_contact': 'externalContact',
            'away_date': 'awayDate',
            'idle_date': 'idleDate',
            'conversation': 'conversation'
        }

        self._id = None
        self._customer_id = None
        self._customer_id_type = None
        self._type = None
        self._external_id = None
        self._external_url = None
        self._short_id = None
        self._outcome_achievements = None
        self._segment_assignments = None
        self._attributes = None
        self._attribute_lists = None
        self._browser = None
        self._device = None
        self._geolocation = None
        self._ip_address = None
        self._ip_organization = None
        self._last_page = None
        self._mkt_campaign = None
        self._referrer = None
        self._search_terms = None
        self._user_agent_string = None
        self._duration_in_seconds = None
        self._event_count = None
        self._pageview_count = None
        self._screenview_count = None
        self._last_event = None
        self._last_connected_queue = None
        self._last_connected_user = None
        self._last_user_disposition = None
        self._conversation_channels = None
        self._originating_direction = None
        self._conversation_subject = None
        self._authenticated = None
        self._self_uri = None
        self._created_date = None
        self._ended_date = None
        self._external_contact = None
        self._away_date = None
        self._idle_date = None
        self._conversation = None

    @property
    def id(self):
        """
        Gets the id of this Session.
        The globally unique identifier for the object.

        :return: The id of this Session.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Session.
        The globally unique identifier for the object.

        :param id: The id of this Session.
        :type: str
        """
        
        self._id = id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Session.
        Primary identifier of the customer in the source where the events for the session originate from.

        :return: The customer_id of this Session.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Session.
        Primary identifier of the customer in the source where the events for the session originate from.

        :param customer_id: The customer_id of this Session.
        :type: str
        """
        
        self._customer_id = customer_id

    @property
    def customer_id_type(self):
        """
        Gets the customer_id_type of this Session.
        Type of source customer identifier (e.g. cookie, email, phone).

        :return: The customer_id_type of this Session.
        :rtype: str
        """
        return self._customer_id_type

    @customer_id_type.setter
    def customer_id_type(self, customer_id_type):
        """
        Sets the customer_id_type of this Session.
        Type of source customer identifier (e.g. cookie, email, phone).

        :param customer_id_type: The customer_id_type of this Session.
        :type: str
        """
        
        self._customer_id_type = customer_id_type

    @property
    def type(self):
        """
        Gets the type of this Session.
        Session types indicate the type or category of sessions (e.g. web, ticket, delivery, atm).

        :return: The type of this Session.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Session.
        Session types indicate the type or category of sessions (e.g. web, ticket, delivery, atm).

        :param type: The type of this Session.
        :type: str
        """
        
        self._type = type

    @property
    def external_id(self):
        """
        Gets the external_id of this Session.
        Unique identifier in the external system where the events for the session originate from.

        :return: The external_id of this Session.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this Session.
        Unique identifier in the external system where the events for the session originate from.

        :param external_id: The external_id of this Session.
        :type: str
        """
        
        self._external_id = external_id

    @property
    def external_url(self):
        """
        Gets the external_url of this Session.
        A URL that identifies an external system-of-record resource that may have more detailed information on the session.

        :return: The external_url of this Session.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """
        Sets the external_url of this Session.
        A URL that identifies an external system-of-record resource that may have more detailed information on the session.

        :param external_url: The external_url of this Session.
        :type: str
        """
        
        self._external_url = external_url

    @property
    def short_id(self):
        """
        Gets the short_id of this Session.
        Shortened numeric identifier of 4-6 digits.

        :return: The short_id of this Session.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """
        Sets the short_id of this Session.
        Shortened numeric identifier of 4-6 digits.

        :param short_id: The short_id of this Session.
        :type: str
        """
        
        self._short_id = short_id

    @property
    def outcome_achievements(self):
        """
        Gets the outcome_achievements of this Session.
        List of the outcome achievements by the customer in this session.

        :return: The outcome_achievements of this Session.
        :rtype: list[OutcomeAchievement]
        """
        return self._outcome_achievements

    @outcome_achievements.setter
    def outcome_achievements(self, outcome_achievements):
        """
        Sets the outcome_achievements of this Session.
        List of the outcome achievements by the customer in this session.

        :param outcome_achievements: The outcome_achievements of this Session.
        :type: list[OutcomeAchievement]
        """
        
        self._outcome_achievements = outcome_achievements

    @property
    def segment_assignments(self):
        """
        Gets the segment_assignments of this Session.
        List of the segment assignments to the customer in this session.

        :return: The segment_assignments of this Session.
        :rtype: list[SessionSegmentAssignment]
        """
        return self._segment_assignments

    @segment_assignments.setter
    def segment_assignments(self, segment_assignments):
        """
        Sets the segment_assignments of this Session.
        List of the segment assignments to the customer in this session.

        :param segment_assignments: The segment_assignments of this Session.
        :type: list[SessionSegmentAssignment]
        """
        
        self._segment_assignments = segment_assignments

    @property
    def attributes(self):
        """
        Gets the attributes of this Session.
        Attributes projected from the session's event stream.

        :return: The attributes of this Session.
        :rtype: dict(str, CustomEventAttribute)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this Session.
        Attributes projected from the session's event stream.

        :param attributes: The attributes of this Session.
        :type: dict(str, CustomEventAttribute)
        """
        
        self._attributes = attributes

    @property
    def attribute_lists(self):
        """
        Gets the attribute_lists of this Session.
        List-type attributes projected from the session's event stream.

        :return: The attribute_lists of this Session.
        :rtype: dict(str, CustomEventAttributeList)
        """
        return self._attribute_lists

    @attribute_lists.setter
    def attribute_lists(self, attribute_lists):
        """
        Sets the attribute_lists of this Session.
        List-type attributes projected from the session's event stream.

        :param attribute_lists: The attribute_lists of this Session.
        :type: dict(str, CustomEventAttributeList)
        """
        
        self._attribute_lists = attribute_lists

    @property
    def browser(self):
        """
        Gets the browser of this Session.
        Customer's browser.

        :return: The browser of this Session.
        :rtype: Browser
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """
        Sets the browser of this Session.
        Customer's browser.

        :param browser: The browser of this Session.
        :type: Browser
        """
        
        self._browser = browser

    @property
    def device(self):
        """
        Gets the device of this Session.
        Customer's device.

        :return: The device of this Session.
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Session.
        Customer's device.

        :param device: The device of this Session.
        :type: Device
        """
        
        self._device = device

    @property
    def geolocation(self):
        """
        Gets the geolocation of this Session.
        Customer's geolocation.

        :return: The geolocation of this Session.
        :rtype: JourneyGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """
        Sets the geolocation of this Session.
        Customer's geolocation.

        :param geolocation: The geolocation of this Session.
        :type: JourneyGeolocation
        """
        
        self._geolocation = geolocation

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Session.
        Customer's IP address.

        :return: The ip_address of this Session.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Session.
        Customer's IP address.

        :param ip_address: The ip_address of this Session.
        :type: str
        """
        
        self._ip_address = ip_address

    @property
    def ip_organization(self):
        """
        Gets the ip_organization of this Session.
        Customer's IP-based organization or ISP name.

        :return: The ip_organization of this Session.
        :rtype: str
        """
        return self._ip_organization

    @ip_organization.setter
    def ip_organization(self, ip_organization):
        """
        Sets the ip_organization of this Session.
        Customer's IP-based organization or ISP name.

        :param ip_organization: The ip_organization of this Session.
        :type: str
        """
        
        self._ip_organization = ip_organization

    @property
    def last_page(self):
        """
        Gets the last_page of this Session.
        The webpage where the customer's last web interaction occurred.

        :return: The last_page of this Session.
        :rtype: JourneyPage
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """
        Sets the last_page of this Session.
        The webpage where the customer's last web interaction occurred.

        :param last_page: The last_page of this Session.
        :type: JourneyPage
        """
        
        self._last_page = last_page

    @property
    def mkt_campaign(self):
        """
        Gets the mkt_campaign of this Session.
        Marketing / traffic source information.

        :return: The mkt_campaign of this Session.
        :rtype: JourneyCampaign
        """
        return self._mkt_campaign

    @mkt_campaign.setter
    def mkt_campaign(self, mkt_campaign):
        """
        Sets the mkt_campaign of this Session.
        Marketing / traffic source information.

        :param mkt_campaign: The mkt_campaign of this Session.
        :type: JourneyCampaign
        """
        
        self._mkt_campaign = mkt_campaign

    @property
    def referrer(self):
        """
        Gets the referrer of this Session.
        Identifies the page URL that originally generated the request for the current page being viewed.

        :return: The referrer of this Session.
        :rtype: Referrer
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """
        Sets the referrer of this Session.
        Identifies the page URL that originally generated the request for the current page being viewed.

        :param referrer: The referrer of this Session.
        :type: Referrer
        """
        
        self._referrer = referrer

    @property
    def search_terms(self):
        """
        Gets the search_terms of this Session.
        Search terms associated with the session.

        :return: The search_terms of this Session.
        :rtype: list[str]
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """
        Sets the search_terms of this Session.
        Search terms associated with the session.

        :param search_terms: The search_terms of this Session.
        :type: list[str]
        """
        
        self._search_terms = search_terms

    @property
    def user_agent_string(self):
        """
        Gets the user_agent_string of this Session.
        String identifying the user agent.

        :return: The user_agent_string of this Session.
        :rtype: str
        """
        return self._user_agent_string

    @user_agent_string.setter
    def user_agent_string(self, user_agent_string):
        """
        Sets the user_agent_string of this Session.
        String identifying the user agent.

        :param user_agent_string: The user_agent_string of this Session.
        :type: str
        """
        
        self._user_agent_string = user_agent_string

    @property
    def duration_in_seconds(self):
        """
        Gets the duration_in_seconds of this Session.
        Indicates how long the session has been active (valid for an individual device).

        :return: The duration_in_seconds of this Session.
        :rtype: int
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        """
        Sets the duration_in_seconds of this Session.
        Indicates how long the session has been active (valid for an individual device).

        :param duration_in_seconds: The duration_in_seconds of this Session.
        :type: int
        """
        
        self._duration_in_seconds = duration_in_seconds

    @property
    def event_count(self):
        """
        Gets the event_count of this Session.
        The count of all events performed during the session.

        :return: The event_count of this Session.
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """
        Sets the event_count of this Session.
        The count of all events performed during the session.

        :param event_count: The event_count of this Session.
        :type: int
        """
        
        self._event_count = event_count

    @property
    def pageview_count(self):
        """
        Gets the pageview_count of this Session.
        The count of all pageviews performed during the session.

        :return: The pageview_count of this Session.
        :rtype: int
        """
        return self._pageview_count

    @pageview_count.setter
    def pageview_count(self, pageview_count):
        """
        Sets the pageview_count of this Session.
        The count of all pageviews performed during the session.

        :param pageview_count: The pageview_count of this Session.
        :type: int
        """
        
        self._pageview_count = pageview_count

    @property
    def screenview_count(self):
        """
        Gets the screenview_count of this Session.
        The count of all screenviews performed during the session.

        :return: The screenview_count of this Session.
        :rtype: int
        """
        return self._screenview_count

    @screenview_count.setter
    def screenview_count(self, screenview_count):
        """
        Sets the screenview_count of this Session.
        The count of all screenviews performed during the session.

        :param screenview_count: The screenview_count of this Session.
        :type: int
        """
        
        self._screenview_count = screenview_count

    @property
    def last_event(self):
        """
        Gets the last_event of this Session.
        Information about the most recent event in this session.

        :return: The last_event of this Session.
        :rtype: SessionLastEvent
        """
        return self._last_event

    @last_event.setter
    def last_event(self, last_event):
        """
        Sets the last_event of this Session.
        Information about the most recent event in this session.

        :param last_event: The last_event of this Session.
        :type: SessionLastEvent
        """
        
        self._last_event = last_event

    @property
    def last_connected_queue(self):
        """
        Gets the last_connected_queue of this Session.
        The last queue connected to this session.

        :return: The last_connected_queue of this Session.
        :rtype: ConnectedQueue
        """
        return self._last_connected_queue

    @last_connected_queue.setter
    def last_connected_queue(self, last_connected_queue):
        """
        Sets the last_connected_queue of this Session.
        The last queue connected to this session.

        :param last_connected_queue: The last_connected_queue of this Session.
        :type: ConnectedQueue
        """
        
        self._last_connected_queue = last_connected_queue

    @property
    def last_connected_user(self):
        """
        Gets the last_connected_user of this Session.
        The last user connected to this session.

        :return: The last_connected_user of this Session.
        :rtype: ConnectedUser
        """
        return self._last_connected_user

    @last_connected_user.setter
    def last_connected_user(self, last_connected_user):
        """
        Sets the last_connected_user of this Session.
        The last user connected to this session.

        :param last_connected_user: The last_connected_user of this Session.
        :type: ConnectedUser
        """
        
        self._last_connected_user = last_connected_user

    @property
    def last_user_disposition(self):
        """
        Gets the last_user_disposition of this Session.
        The last user disposition connected to this session.

        :return: The last_user_disposition of this Session.
        :rtype: ConversationUserDisposition
        """
        return self._last_user_disposition

    @last_user_disposition.setter
    def last_user_disposition(self, last_user_disposition):
        """
        Sets the last_user_disposition of this Session.
        The last user disposition connected to this session.

        :param last_user_disposition: The last_user_disposition of this Session.
        :type: ConversationUserDisposition
        """
        
        self._last_user_disposition = last_user_disposition

    @property
    def conversation_channels(self):
        """
        Gets the conversation_channels of this Session.
        Represents the channels used for this conversation.

        :return: The conversation_channels of this Session.
        :rtype: list[ConversationChannel]
        """
        return self._conversation_channels

    @conversation_channels.setter
    def conversation_channels(self, conversation_channels):
        """
        Sets the conversation_channels of this Session.
        Represents the channels used for this conversation.

        :param conversation_channels: The conversation_channels of this Session.
        :type: list[ConversationChannel]
        """
        
        self._conversation_channels = conversation_channels

    @property
    def originating_direction(self):
        """
        Gets the originating_direction of this Session.
        The original direction of the conversation.

        :return: The originating_direction of this Session.
        :rtype: str
        """
        return self._originating_direction

    @originating_direction.setter
    def originating_direction(self, originating_direction):
        """
        Sets the originating_direction of this Session.
        The original direction of the conversation.

        :param originating_direction: The originating_direction of this Session.
        :type: str
        """
        allowed_values = ["Inbound", "Outbound"]
        if originating_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for originating_direction -> " + originating_direction)
            self._originating_direction = "outdated_sdk_version"
        else:
            self._originating_direction = originating_direction

    @property
    def conversation_subject(self):
        """
        Gets the conversation_subject of this Session.
        The subject for the conversation, for example an email subject.

        :return: The conversation_subject of this Session.
        :rtype: str
        """
        return self._conversation_subject

    @conversation_subject.setter
    def conversation_subject(self, conversation_subject):
        """
        Sets the conversation_subject of this Session.
        The subject for the conversation, for example an email subject.

        :param conversation_subject: The conversation_subject of this Session.
        :type: str
        """
        
        self._conversation_subject = conversation_subject

    @property
    def authenticated(self):
        """
        Gets the authenticated of this Session.
        Indicates whether or not the session is authenticated.

        :return: The authenticated of this Session.
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """
        Sets the authenticated of this Session.
        Indicates whether or not the session is authenticated.

        :param authenticated: The authenticated of this Session.
        :type: bool
        """
        
        self._authenticated = authenticated

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Session.
        The URI for this object

        :return: The self_uri of this Session.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Session.
        The URI for this object

        :param self_uri: The self_uri of this Session.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def created_date(self):
        """
        Gets the created_date of this Session.
        Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this Session.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Session.
        Timestamp indicating when the session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this Session.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def ended_date(self):
        """
        Gets the ended_date of this Session.
        Timestamp indicating when the session was ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The ended_date of this Session.
        :rtype: datetime
        """
        return self._ended_date

    @ended_date.setter
    def ended_date(self, ended_date):
        """
        Sets the ended_date of this Session.
        Timestamp indicating when the session was ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param ended_date: The ended_date of this Session.
        :type: datetime
        """
        
        self._ended_date = ended_date

    @property
    def external_contact(self):
        """
        Gets the external_contact of this Session.
        The external contact associated with this session.

        :return: The external_contact of this Session.
        :rtype: AddressableEntityRef
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact):
        """
        Sets the external_contact of this Session.
        The external contact associated with this session.

        :param external_contact: The external_contact of this Session.
        :type: AddressableEntityRef
        """
        
        self._external_contact = external_contact

    @property
    def away_date(self):
        """
        Gets the away_date of this Session.
        Timestamp indicating when the visitor should be considered as away. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The away_date of this Session.
        :rtype: datetime
        """
        return self._away_date

    @away_date.setter
    def away_date(self, away_date):
        """
        Sets the away_date of this Session.
        Timestamp indicating when the visitor should be considered as away. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param away_date: The away_date of this Session.
        :type: datetime
        """
        
        self._away_date = away_date

    @property
    def idle_date(self):
        """
        Gets the idle_date of this Session.
        Timestamp indicating when the visitor should be considered as idle. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The idle_date of this Session.
        :rtype: datetime
        """
        return self._idle_date

    @idle_date.setter
    def idle_date(self, idle_date):
        """
        Sets the idle_date of this Session.
        Timestamp indicating when the visitor should be considered as idle. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param idle_date: The idle_date of this Session.
        :type: datetime
        """
        
        self._idle_date = idle_date

    @property
    def conversation(self):
        """
        Gets the conversation of this Session.
        The conversation for this session.

        :return: The conversation of this Session.
        :rtype: AddressableEntityRef
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this Session.
        The conversation for this session.

        :param conversation: The conversation of this Session.
        :type: AddressableEntityRef
        """
        
        self._conversation = conversation

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
