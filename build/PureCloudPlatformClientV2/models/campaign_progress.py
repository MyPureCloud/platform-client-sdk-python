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
    from . import DomainEntityRef

class CampaignProgress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignProgress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'campaign': 'DomainEntityRef',
            'contact_list': 'DomainEntityRef',
            'number_of_contacts_called': 'int',
            'number_of_contacts_messaged': 'int',
            'total_number_of_contacts': 'int',
            'percentage': 'int',
            'number_of_contacts_skipped': 'dict(str, int)'
        }

        self.attribute_map = {
            'campaign': 'campaign',
            'contact_list': 'contactList',
            'number_of_contacts_called': 'numberOfContactsCalled',
            'number_of_contacts_messaged': 'numberOfContactsMessaged',
            'total_number_of_contacts': 'totalNumberOfContacts',
            'percentage': 'percentage',
            'number_of_contacts_skipped': 'numberOfContactsSkipped'
        }

        self._campaign = None
        self._contact_list = None
        self._number_of_contacts_called = None
        self._number_of_contacts_messaged = None
        self._total_number_of_contacts = None
        self._percentage = None
        self._number_of_contacts_skipped = None

    @property
    def campaign(self) -> 'DomainEntityRef':
        """
        Gets the campaign of this CampaignProgress.
        Identifier of the campaign

        :return: The campaign of this CampaignProgress.
        :rtype: DomainEntityRef
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign: 'DomainEntityRef') -> None:
        """
        Sets the campaign of this CampaignProgress.
        Identifier of the campaign

        :param campaign: The campaign of this CampaignProgress.
        :type: DomainEntityRef
        """
        

        self._campaign = campaign

    @property
    def contact_list(self) -> 'DomainEntityRef':
        """
        Gets the contact_list of this CampaignProgress.
        Identifier of the contact list

        :return: The contact_list of this CampaignProgress.
        :rtype: DomainEntityRef
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list: 'DomainEntityRef') -> None:
        """
        Sets the contact_list of this CampaignProgress.
        Identifier of the contact list

        :param contact_list: The contact_list of this CampaignProgress.
        :type: DomainEntityRef
        """
        

        self._contact_list = contact_list

    @property
    def number_of_contacts_called(self) -> int:
        """
        Gets the number_of_contacts_called of this CampaignProgress.
        Number of contacts called during the campaign

        :return: The number_of_contacts_called of this CampaignProgress.
        :rtype: int
        """
        return self._number_of_contacts_called

    @number_of_contacts_called.setter
    def number_of_contacts_called(self, number_of_contacts_called: int) -> None:
        """
        Sets the number_of_contacts_called of this CampaignProgress.
        Number of contacts called during the campaign

        :param number_of_contacts_called: The number_of_contacts_called of this CampaignProgress.
        :type: int
        """
        

        self._number_of_contacts_called = number_of_contacts_called

    @property
    def number_of_contacts_messaged(self) -> int:
        """
        Gets the number_of_contacts_messaged of this CampaignProgress.
        Number of contacts messaged during the campaign

        :return: The number_of_contacts_messaged of this CampaignProgress.
        :rtype: int
        """
        return self._number_of_contacts_messaged

    @number_of_contacts_messaged.setter
    def number_of_contacts_messaged(self, number_of_contacts_messaged: int) -> None:
        """
        Sets the number_of_contacts_messaged of this CampaignProgress.
        Number of contacts messaged during the campaign

        :param number_of_contacts_messaged: The number_of_contacts_messaged of this CampaignProgress.
        :type: int
        """
        

        self._number_of_contacts_messaged = number_of_contacts_messaged

    @property
    def total_number_of_contacts(self) -> int:
        """
        Gets the total_number_of_contacts of this CampaignProgress.
        Total number of contacts in the campaign

        :return: The total_number_of_contacts of this CampaignProgress.
        :rtype: int
        """
        return self._total_number_of_contacts

    @total_number_of_contacts.setter
    def total_number_of_contacts(self, total_number_of_contacts: int) -> None:
        """
        Sets the total_number_of_contacts of this CampaignProgress.
        Total number of contacts in the campaign

        :param total_number_of_contacts: The total_number_of_contacts of this CampaignProgress.
        :type: int
        """
        

        self._total_number_of_contacts = total_number_of_contacts

    @property
    def percentage(self) -> int:
        """
        Gets the percentage of this CampaignProgress.
        Percentage of contacts processed during the campaign

        :return: The percentage of this CampaignProgress.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage: int) -> None:
        """
        Sets the percentage of this CampaignProgress.
        Percentage of contacts processed during the campaign

        :param percentage: The percentage of this CampaignProgress.
        :type: int
        """
        

        self._percentage = percentage

    @property
    def number_of_contacts_skipped(self) -> Dict[str, int]:
        """
        Gets the number_of_contacts_skipped of this CampaignProgress.
        Number of contacts skipped during the campaign

        :return: The number_of_contacts_skipped of this CampaignProgress.
        :rtype: dict(str, int)
        """
        return self._number_of_contacts_skipped

    @number_of_contacts_skipped.setter
    def number_of_contacts_skipped(self, number_of_contacts_skipped: Dict[str, int]) -> None:
        """
        Sets the number_of_contacts_skipped of this CampaignProgress.
        Number of contacts skipped during the campaign

        :param number_of_contacts_skipped: The number_of_contacts_skipped of this CampaignProgress.
        :type: dict(str, int)
        """
        

        self._number_of_contacts_skipped = number_of_contacts_skipped

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

