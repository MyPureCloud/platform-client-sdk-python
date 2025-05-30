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


class OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email_subject': 'str',
            'configured_email_address': 'str',
            'contact_email_address': 'str',
            'reply_to_address': 'str',
            'contact_email_column_name': 'str'
        }

        self.attribute_map = {
            'email_subject': 'emailSubject',
            'configured_email_address': 'configuredEmailAddress',
            'contact_email_address': 'contactEmailAddress',
            'reply_to_address': 'replyToAddress',
            'contact_email_column_name': 'contactEmailColumnName'
        }

        self._email_subject = None
        self._configured_email_address = None
        self._contact_email_address = None
        self._reply_to_address = None
        self._contact_email_column_name = None

    @property
    def email_subject(self) -> str:
        """
        Gets the email_subject of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :return: The email_subject of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject: str) -> None:
        """
        Sets the email_subject of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :param email_subject: The email_subject of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :type: str
        """
        

        self._email_subject = email_subject

    @property
    def configured_email_address(self) -> str:
        """
        Gets the configured_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :return: The configured_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :rtype: str
        """
        return self._configured_email_address

    @configured_email_address.setter
    def configured_email_address(self, configured_email_address: str) -> None:
        """
        Sets the configured_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :param configured_email_address: The configured_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :type: str
        """
        

        self._configured_email_address = configured_email_address

    @property
    def contact_email_address(self) -> str:
        """
        Gets the contact_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :return: The contact_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :rtype: str
        """
        return self._contact_email_address

    @contact_email_address.setter
    def contact_email_address(self, contact_email_address: str) -> None:
        """
        Sets the contact_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :param contact_email_address: The contact_email_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :type: str
        """
        

        self._contact_email_address = contact_email_address

    @property
    def reply_to_address(self) -> str:
        """
        Gets the reply_to_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :return: The reply_to_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :rtype: str
        """
        return self._reply_to_address

    @reply_to_address.setter
    def reply_to_address(self, reply_to_address: str) -> None:
        """
        Sets the reply_to_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :param reply_to_address: The reply_to_address of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :type: str
        """
        

        self._reply_to_address = reply_to_address

    @property
    def contact_email_column_name(self) -> str:
        """
        Gets the contact_email_column_name of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :return: The contact_email_column_name of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :rtype: str
        """
        return self._contact_email_column_name

    @contact_email_column_name.setter
    def contact_email_column_name(self, contact_email_column_name: str) -> None:
        """
        Sets the contact_email_column_name of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.


        :param contact_email_column_name: The contact_email_column_name of this OutboundMessagingCampaignPostContactEmailEventTopicEmailAttributes.
        :type: str
        """
        

        self._contact_email_column_name = contact_email_column_name

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

