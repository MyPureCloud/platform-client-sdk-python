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

class CampaignOutboundLinesAllocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignOutboundLinesAllocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'campaign': 'DomainEntityRef',
            'campaign_weight': 'int',
            'lines_assigned': 'int',
            'legacy_weight': 'bool'
        }

        self.attribute_map = {
            'campaign': 'campaign',
            'campaign_weight': 'campaignWeight',
            'lines_assigned': 'linesAssigned',
            'legacy_weight': 'legacyWeight'
        }

        self._campaign = None
        self._campaign_weight = None
        self._lines_assigned = None
        self._legacy_weight = None

    @property
    def campaign(self) -> 'DomainEntityRef':
        """
        Gets the campaign of this CampaignOutboundLinesAllocation.
        The Campaign

        :return: The campaign of this CampaignOutboundLinesAllocation.
        :rtype: DomainEntityRef
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign: 'DomainEntityRef') -> None:
        """
        Sets the campaign of this CampaignOutboundLinesAllocation.
        The Campaign

        :param campaign: The campaign of this CampaignOutboundLinesAllocation.
        :type: DomainEntityRef
        """
        

        self._campaign = campaign

    @property
    def campaign_weight(self) -> int:
        """
        Gets the campaign_weight of this CampaignOutboundLinesAllocation.
        The relative weight of the campaign

        :return: The campaign_weight of this CampaignOutboundLinesAllocation.
        :rtype: int
        """
        return self._campaign_weight

    @campaign_weight.setter
    def campaign_weight(self, campaign_weight: int) -> None:
        """
        Sets the campaign_weight of this CampaignOutboundLinesAllocation.
        The relative weight of the campaign

        :param campaign_weight: The campaign_weight of this CampaignOutboundLinesAllocation.
        :type: int
        """
        

        self._campaign_weight = campaign_weight

    @property
    def lines_assigned(self) -> int:
        """
        Gets the lines_assigned of this CampaignOutboundLinesAllocation.
        The number of lines dynamically assigned to the campaign

        :return: The lines_assigned of this CampaignOutboundLinesAllocation.
        :rtype: int
        """
        return self._lines_assigned

    @lines_assigned.setter
    def lines_assigned(self, lines_assigned: int) -> None:
        """
        Sets the lines_assigned of this CampaignOutboundLinesAllocation.
        The number of lines dynamically assigned to the campaign

        :param lines_assigned: The lines_assigned of this CampaignOutboundLinesAllocation.
        :type: int
        """
        

        self._lines_assigned = lines_assigned

    @property
    def legacy_weight(self) -> bool:
        """
        Gets the legacy_weight of this CampaignOutboundLinesAllocation.
        true if relative weight of the campaign is not explicitly specified, false otherwise

        :return: The legacy_weight of this CampaignOutboundLinesAllocation.
        :rtype: bool
        """
        return self._legacy_weight

    @legacy_weight.setter
    def legacy_weight(self, legacy_weight: bool) -> None:
        """
        Sets the legacy_weight of this CampaignOutboundLinesAllocation.
        true if relative weight of the campaign is not explicitly specified, false otherwise

        :param legacy_weight: The legacy_weight of this CampaignOutboundLinesAllocation.
        :type: bool
        """
        

        self._legacy_weight = legacy_weight

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

