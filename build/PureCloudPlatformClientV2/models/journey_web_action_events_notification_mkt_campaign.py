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

class JourneyWebActionEventsNotificationMktCampaign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JourneyWebActionEventsNotificationMktCampaign - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'str',
            'medium': 'str',
            'name': 'str',
            'source': 'str',
            'term': 'str',
            'click_id': 'str',
            'network': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'medium': 'medium',
            'name': 'name',
            'source': 'source',
            'term': 'term',
            'click_id': 'clickId',
            'network': 'network'
        }

        self._content = None
        self._medium = None
        self._name = None
        self._source = None
        self._term = None
        self._click_id = None
        self._network = None

    @property
    def content(self):
        """
        Gets the content of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The content of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this JourneyWebActionEventsNotificationMktCampaign.


        :param content: The content of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._content = content

    @property
    def medium(self):
        """
        Gets the medium of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The medium of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """
        Sets the medium of this JourneyWebActionEventsNotificationMktCampaign.


        :param medium: The medium of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._medium = medium

    @property
    def name(self):
        """
        Gets the name of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The name of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JourneyWebActionEventsNotificationMktCampaign.


        :param name: The name of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._name = name

    @property
    def source(self):
        """
        Gets the source of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The source of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this JourneyWebActionEventsNotificationMktCampaign.


        :param source: The source of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._source = source

    @property
    def term(self):
        """
        Gets the term of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The term of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """
        Sets the term of this JourneyWebActionEventsNotificationMktCampaign.


        :param term: The term of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._term = term

    @property
    def click_id(self):
        """
        Gets the click_id of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The click_id of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._click_id

    @click_id.setter
    def click_id(self, click_id):
        """
        Sets the click_id of this JourneyWebActionEventsNotificationMktCampaign.


        :param click_id: The click_id of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._click_id = click_id

    @property
    def network(self):
        """
        Gets the network of this JourneyWebActionEventsNotificationMktCampaign.


        :return: The network of this JourneyWebActionEventsNotificationMktCampaign.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this JourneyWebActionEventsNotificationMktCampaign.


        :param network: The network of this JourneyWebActionEventsNotificationMktCampaign.
        :type: str
        """
        
        self._network = network

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
