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
    from . import Browser
    from . import Device
    from . import JourneyCampaign
    from . import JourneyGeolocation
    from . import OutcomeAchievedEventOutcome
    from . import Referrer

class OutcomeAchievedEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OutcomeAchievedEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'outcome': 'OutcomeAchievedEventOutcome',
            'user_agent_string': 'str',
            'browser': 'Browser',
            'device': 'Device',
            'geolocation': 'JourneyGeolocation',
            'ip_address': 'str',
            'ip_organization': 'str',
            'mkt_campaign': 'JourneyCampaign',
            'visit_referrer': 'Referrer',
            'visit_created_date': 'datetime'
        }

        self.attribute_map = {
            'outcome': 'outcome',
            'user_agent_string': 'userAgentString',
            'browser': 'browser',
            'device': 'device',
            'geolocation': 'geolocation',
            'ip_address': 'ipAddress',
            'ip_organization': 'ipOrganization',
            'mkt_campaign': 'mktCampaign',
            'visit_referrer': 'visitReferrer',
            'visit_created_date': 'visitCreatedDate'
        }

        self._outcome = None
        self._user_agent_string = None
        self._browser = None
        self._device = None
        self._geolocation = None
        self._ip_address = None
        self._ip_organization = None
        self._mkt_campaign = None
        self._visit_referrer = None
        self._visit_created_date = None

    @property
    def outcome(self) -> 'OutcomeAchievedEventOutcome':
        """
        Gets the outcome of this OutcomeAchievedEvent.
        The outcome achieved.

        :return: The outcome of this OutcomeAchievedEvent.
        :rtype: OutcomeAchievedEventOutcome
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome: 'OutcomeAchievedEventOutcome') -> None:
        """
        Sets the outcome of this OutcomeAchievedEvent.
        The outcome achieved.

        :param outcome: The outcome of this OutcomeAchievedEvent.
        :type: OutcomeAchievedEventOutcome
        """
        

        self._outcome = outcome

    @property
    def user_agent_string(self) -> str:
        """
        Gets the user_agent_string of this OutcomeAchievedEvent.
        HTTP User-Agent string (see https://tools.ietf.org/html/rfc1945#section-10.15).

        :return: The user_agent_string of this OutcomeAchievedEvent.
        :rtype: str
        """
        return self._user_agent_string

    @user_agent_string.setter
    def user_agent_string(self, user_agent_string: str) -> None:
        """
        Sets the user_agent_string of this OutcomeAchievedEvent.
        HTTP User-Agent string (see https://tools.ietf.org/html/rfc1945#section-10.15).

        :param user_agent_string: The user_agent_string of this OutcomeAchievedEvent.
        :type: str
        """
        

        self._user_agent_string = user_agent_string

    @property
    def browser(self) -> 'Browser':
        """
        Gets the browser of this OutcomeAchievedEvent.
        Customer's browser.

        :return: The browser of this OutcomeAchievedEvent.
        :rtype: Browser
        """
        return self._browser

    @browser.setter
    def browser(self, browser: 'Browser') -> None:
        """
        Sets the browser of this OutcomeAchievedEvent.
        Customer's browser.

        :param browser: The browser of this OutcomeAchievedEvent.
        :type: Browser
        """
        

        self._browser = browser

    @property
    def device(self) -> 'Device':
        """
        Gets the device of this OutcomeAchievedEvent.
        Customer's device.

        :return: The device of this OutcomeAchievedEvent.
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device: 'Device') -> None:
        """
        Sets the device of this OutcomeAchievedEvent.
        Customer's device.

        :param device: The device of this OutcomeAchievedEvent.
        :type: Device
        """
        

        self._device = device

    @property
    def geolocation(self) -> 'JourneyGeolocation':
        """
        Gets the geolocation of this OutcomeAchievedEvent.
        Customer's geolocation.

        :return: The geolocation of this OutcomeAchievedEvent.
        :rtype: JourneyGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: 'JourneyGeolocation') -> None:
        """
        Sets the geolocation of this OutcomeAchievedEvent.
        Customer's geolocation.

        :param geolocation: The geolocation of this OutcomeAchievedEvent.
        :type: JourneyGeolocation
        """
        

        self._geolocation = geolocation

    @property
    def ip_address(self) -> str:
        """
        Gets the ip_address of this OutcomeAchievedEvent.
        Visitor's IP address.

        :return: The ip_address of this OutcomeAchievedEvent.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str) -> None:
        """
        Sets the ip_address of this OutcomeAchievedEvent.
        Visitor's IP address.

        :param ip_address: The ip_address of this OutcomeAchievedEvent.
        :type: str
        """
        

        self._ip_address = ip_address

    @property
    def ip_organization(self) -> str:
        """
        Gets the ip_organization of this OutcomeAchievedEvent.
        Visitor's IP-based organization or ISP name.

        :return: The ip_organization of this OutcomeAchievedEvent.
        :rtype: str
        """
        return self._ip_organization

    @ip_organization.setter
    def ip_organization(self, ip_organization: str) -> None:
        """
        Sets the ip_organization of this OutcomeAchievedEvent.
        Visitor's IP-based organization or ISP name.

        :param ip_organization: The ip_organization of this OutcomeAchievedEvent.
        :type: str
        """
        

        self._ip_organization = ip_organization

    @property
    def mkt_campaign(self) -> 'JourneyCampaign':
        """
        Gets the mkt_campaign of this OutcomeAchievedEvent.
        Marketing / traffic source information.

        :return: The mkt_campaign of this OutcomeAchievedEvent.
        :rtype: JourneyCampaign
        """
        return self._mkt_campaign

    @mkt_campaign.setter
    def mkt_campaign(self, mkt_campaign: 'JourneyCampaign') -> None:
        """
        Sets the mkt_campaign of this OutcomeAchievedEvent.
        Marketing / traffic source information.

        :param mkt_campaign: The mkt_campaign of this OutcomeAchievedEvent.
        :type: JourneyCampaign
        """
        

        self._mkt_campaign = mkt_campaign

    @property
    def visit_referrer(self) -> 'Referrer':
        """
        Gets the visit_referrer of this OutcomeAchievedEvent.
        Visit's referrer.

        :return: The visit_referrer of this OutcomeAchievedEvent.
        :rtype: Referrer
        """
        return self._visit_referrer

    @visit_referrer.setter
    def visit_referrer(self, visit_referrer: 'Referrer') -> None:
        """
        Sets the visit_referrer of this OutcomeAchievedEvent.
        Visit's referrer.

        :param visit_referrer: The visit_referrer of this OutcomeAchievedEvent.
        :type: Referrer
        """
        

        self._visit_referrer = visit_referrer

    @property
    def visit_created_date(self) -> datetime:
        """
        Gets the visit_created_date of this OutcomeAchievedEvent.
        When visit was created (e.g. timestamp of the first event in visit). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The visit_created_date of this OutcomeAchievedEvent.
        :rtype: datetime
        """
        return self._visit_created_date

    @visit_created_date.setter
    def visit_created_date(self, visit_created_date: datetime) -> None:
        """
        Sets the visit_created_date of this OutcomeAchievedEvent.
        When visit was created (e.g. timestamp of the first event in visit). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param visit_created_date: The visit_created_date of this OutcomeAchievedEvent.
        :type: datetime
        """
        

        self._visit_created_date = visit_created_date

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

