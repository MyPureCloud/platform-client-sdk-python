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

class JourneyWebActionEventsNotificationWebActionEventsNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JourneyWebActionEventsNotificationWebActionEventsNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'correlation_id': 'str',
            'external_contact': 'JourneyWebActionEventsNotificationExternalContact',
            'created_date': 'datetime',
            'customer_id': 'str',
            'customer_id_type': 'str',
            'event_type': 'str',
            'session': 'JourneyWebActionEventsNotificationSession',
            'web_action_event': 'JourneyWebActionEventsNotificationWebActionMessage',
            'blocked_web_action_offer_event': 'JourneyWebActionEventsNotificationBlockedWebActionOfferMessage'
        }

        self.attribute_map = {
            'id': 'id',
            'correlation_id': 'correlationId',
            'external_contact': 'externalContact',
            'created_date': 'createdDate',
            'customer_id': 'customerId',
            'customer_id_type': 'customerIdType',
            'event_type': 'eventType',
            'session': 'session',
            'web_action_event': 'webActionEvent',
            'blocked_web_action_offer_event': 'blockedWebActionOfferEvent'
        }

        self._id = None
        self._correlation_id = None
        self._external_contact = None
        self._created_date = None
        self._customer_id = None
        self._customer_id_type = None
        self._event_type = None
        self._session = None
        self._web_action_event = None
        self._blocked_web_action_offer_event = None

    @property
    def id(self):
        """
        Gets the id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param id: The id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: str
        """
        
        self._id = id

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The correlation_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param correlation_id: The correlation_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: str
        """
        
        self._correlation_id = correlation_id

    @property
    def external_contact(self):
        """
        Gets the external_contact of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The external_contact of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: JourneyWebActionEventsNotificationExternalContact
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact):
        """
        Sets the external_contact of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param external_contact: The external_contact of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: JourneyWebActionEventsNotificationExternalContact
        """
        
        self._external_contact = external_contact

    @property
    def created_date(self):
        """
        Gets the created_date of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The created_date of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param created_date: The created_date of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def customer_id(self):
        """
        Gets the customer_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The customer_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param customer_id: The customer_id of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: str
        """
        
        self._customer_id = customer_id

    @property
    def customer_id_type(self):
        """
        Gets the customer_id_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The customer_id_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: str
        """
        return self._customer_id_type

    @customer_id_type.setter
    def customer_id_type(self, customer_id_type):
        """
        Sets the customer_id_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param customer_id_type: The customer_id_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: str
        """
        
        self._customer_id_type = customer_id_type

    @property
    def event_type(self):
        """
        Gets the event_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The event_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param event_type: The event_type of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: str
        """
        allowed_values = ["WebEvent", "WebActionEvent", "OutcomeAchievedEvent", "BlockedWebActionOfferEvent", "OutcomeAttributionEvent"]
        if event_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for event_type -> " + event_type)
            self._event_type = "outdated_sdk_version"
        else:
            self._event_type = event_type

    @property
    def session(self):
        """
        Gets the session of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The session of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: JourneyWebActionEventsNotificationSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """
        Sets the session of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param session: The session of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: JourneyWebActionEventsNotificationSession
        """
        
        self._session = session

    @property
    def web_action_event(self):
        """
        Gets the web_action_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The web_action_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: JourneyWebActionEventsNotificationWebActionMessage
        """
        return self._web_action_event

    @web_action_event.setter
    def web_action_event(self, web_action_event):
        """
        Sets the web_action_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param web_action_event: The web_action_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: JourneyWebActionEventsNotificationWebActionMessage
        """
        
        self._web_action_event = web_action_event

    @property
    def blocked_web_action_offer_event(self):
        """
        Gets the blocked_web_action_offer_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :return: The blocked_web_action_offer_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :rtype: JourneyWebActionEventsNotificationBlockedWebActionOfferMessage
        """
        return self._blocked_web_action_offer_event

    @blocked_web_action_offer_event.setter
    def blocked_web_action_offer_event(self, blocked_web_action_offer_event):
        """
        Sets the blocked_web_action_offer_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.


        :param blocked_web_action_offer_event: The blocked_web_action_offer_event of this JourneyWebActionEventsNotificationWebActionEventsNotification.
        :type: JourneyWebActionEventsNotificationBlockedWebActionOfferMessage
        """
        
        self._blocked_web_action_offer_event = blocked_web_action_offer_event

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
