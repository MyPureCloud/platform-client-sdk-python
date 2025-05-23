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
    from . import NamedEntity
    from . import SubscriptionOverviewUsage

class TrusteeBillingOverview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrusteeBillingOverview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'organization': 'NamedEntity',
            'currency': 'str',
            'enabled_products': 'list[str]',
            'subscription_type': 'str',
            'ramp_period_start_date': 'datetime',
            'ramp_period_end_date': 'datetime',
            'billing_period_start_date': 'datetime',
            'billing_period_end_date': 'datetime',
            'usages': 'list[SubscriptionOverviewUsage]',
            'contract_amendment_date': 'datetime',
            'contract_effective_date': 'datetime',
            'contract_end_date': 'datetime',
            'minimum_monthly_amount': 'str',
            'in_ramp_period': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'organization': 'organization',
            'currency': 'currency',
            'enabled_products': 'enabledProducts',
            'subscription_type': 'subscriptionType',
            'ramp_period_start_date': 'rampPeriodStartDate',
            'ramp_period_end_date': 'rampPeriodEndDate',
            'billing_period_start_date': 'billingPeriodStartDate',
            'billing_period_end_date': 'billingPeriodEndDate',
            'usages': 'usages',
            'contract_amendment_date': 'contractAmendmentDate',
            'contract_effective_date': 'contractEffectiveDate',
            'contract_end_date': 'contractEndDate',
            'minimum_monthly_amount': 'minimumMonthlyAmount',
            'in_ramp_period': 'inRampPeriod',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._organization = None
        self._currency = None
        self._enabled_products = None
        self._subscription_type = None
        self._ramp_period_start_date = None
        self._ramp_period_end_date = None
        self._billing_period_start_date = None
        self._billing_period_end_date = None
        self._usages = None
        self._contract_amendment_date = None
        self._contract_effective_date = None
        self._contract_end_date = None
        self._minimum_monthly_amount = None
        self._in_ramp_period = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TrusteeBillingOverview.
        The globally unique identifier for the object.

        :return: The id of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TrusteeBillingOverview.
        The globally unique identifier for the object.

        :param id: The id of this TrusteeBillingOverview.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this TrusteeBillingOverview.


        :return: The name of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this TrusteeBillingOverview.


        :param name: The name of this TrusteeBillingOverview.
        :type: str
        """
        

        self._name = name

    @property
    def organization(self) -> 'NamedEntity':
        """
        Gets the organization of this TrusteeBillingOverview.
        Organization

        :return: The organization of this TrusteeBillingOverview.
        :rtype: NamedEntity
        """
        return self._organization

    @organization.setter
    def organization(self, organization: 'NamedEntity') -> None:
        """
        Sets the organization of this TrusteeBillingOverview.
        Organization

        :param organization: The organization of this TrusteeBillingOverview.
        :type: NamedEntity
        """
        

        self._organization = organization

    @property
    def currency(self) -> str:
        """
        Gets the currency of this TrusteeBillingOverview.
        The currency type.

        :return: The currency of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str) -> None:
        """
        Sets the currency of this TrusteeBillingOverview.
        The currency type.

        :param currency: The currency of this TrusteeBillingOverview.
        :type: str
        """
        

        self._currency = currency

    @property
    def enabled_products(self) -> List[str]:
        """
        Gets the enabled_products of this TrusteeBillingOverview.
        The charge short names for products enabled during the specified period.

        :return: The enabled_products of this TrusteeBillingOverview.
        :rtype: list[str]
        """
        return self._enabled_products

    @enabled_products.setter
    def enabled_products(self, enabled_products: List[str]) -> None:
        """
        Sets the enabled_products of this TrusteeBillingOverview.
        The charge short names for products enabled during the specified period.

        :param enabled_products: The enabled_products of this TrusteeBillingOverview.
        :type: list[str]
        """
        

        self._enabled_products = enabled_products

    @property
    def subscription_type(self) -> str:
        """
        Gets the subscription_type of this TrusteeBillingOverview.
        The subscription type.

        :return: The subscription_type of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str) -> None:
        """
        Sets the subscription_type of this TrusteeBillingOverview.
        The subscription type.

        :param subscription_type: The subscription_type of this TrusteeBillingOverview.
        :type: str
        """
        if isinstance(subscription_type, int):
            subscription_type = str(subscription_type)
        allowed_values = ["ININ", "MONTH_TO_MONTH", "FREE_TRIAL_MONTH_TO_MONTH", "PREPAY_MONTHLY_COMMITMENT", "PREPAY", "DEV_ORG_MONTH_TO_MONTH", "DEV_ORG_PREPAY_MONTHLY_COMMITMENT", "DEV_ORG_PREPAY"]
        if subscription_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for subscription_type -> " + subscription_type)
            self._subscription_type = "outdated_sdk_version"
        else:
            self._subscription_type = subscription_type

    @property
    def ramp_period_start_date(self) -> datetime:
        """
        Gets the ramp_period_start_date of this TrusteeBillingOverview.
        Date-time the ramp period starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The ramp_period_start_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._ramp_period_start_date

    @ramp_period_start_date.setter
    def ramp_period_start_date(self, ramp_period_start_date: datetime) -> None:
        """
        Sets the ramp_period_start_date of this TrusteeBillingOverview.
        Date-time the ramp period starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param ramp_period_start_date: The ramp_period_start_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._ramp_period_start_date = ramp_period_start_date

    @property
    def ramp_period_end_date(self) -> datetime:
        """
        Gets the ramp_period_end_date of this TrusteeBillingOverview.
        Date-time the ramp period ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The ramp_period_end_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._ramp_period_end_date

    @ramp_period_end_date.setter
    def ramp_period_end_date(self, ramp_period_end_date: datetime) -> None:
        """
        Sets the ramp_period_end_date of this TrusteeBillingOverview.
        Date-time the ramp period ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param ramp_period_end_date: The ramp_period_end_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._ramp_period_end_date = ramp_period_end_date

    @property
    def billing_period_start_date(self) -> datetime:
        """
        Gets the billing_period_start_date of this TrusteeBillingOverview.
        Date-time the billing period started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The billing_period_start_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._billing_period_start_date

    @billing_period_start_date.setter
    def billing_period_start_date(self, billing_period_start_date: datetime) -> None:
        """
        Sets the billing_period_start_date of this TrusteeBillingOverview.
        Date-time the billing period started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param billing_period_start_date: The billing_period_start_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._billing_period_start_date = billing_period_start_date

    @property
    def billing_period_end_date(self) -> datetime:
        """
        Gets the billing_period_end_date of this TrusteeBillingOverview.
        Date-time the billing period ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The billing_period_end_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._billing_period_end_date

    @billing_period_end_date.setter
    def billing_period_end_date(self, billing_period_end_date: datetime) -> None:
        """
        Sets the billing_period_end_date of this TrusteeBillingOverview.
        Date-time the billing period ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param billing_period_end_date: The billing_period_end_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._billing_period_end_date = billing_period_end_date

    @property
    def usages(self) -> List['SubscriptionOverviewUsage']:
        """
        Gets the usages of this TrusteeBillingOverview.
        Usages for the specified period.

        :return: The usages of this TrusteeBillingOverview.
        :rtype: list[SubscriptionOverviewUsage]
        """
        return self._usages

    @usages.setter
    def usages(self, usages: List['SubscriptionOverviewUsage']) -> None:
        """
        Sets the usages of this TrusteeBillingOverview.
        Usages for the specified period.

        :param usages: The usages of this TrusteeBillingOverview.
        :type: list[SubscriptionOverviewUsage]
        """
        

        self._usages = usages

    @property
    def contract_amendment_date(self) -> datetime:
        """
        Gets the contract_amendment_date of this TrusteeBillingOverview.
        Date-time the contract was last amended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The contract_amendment_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._contract_amendment_date

    @contract_amendment_date.setter
    def contract_amendment_date(self, contract_amendment_date: datetime) -> None:
        """
        Sets the contract_amendment_date of this TrusteeBillingOverview.
        Date-time the contract was last amended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param contract_amendment_date: The contract_amendment_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._contract_amendment_date = contract_amendment_date

    @property
    def contract_effective_date(self) -> datetime:
        """
        Gets the contract_effective_date of this TrusteeBillingOverview.
        Date-time the contract became effective. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The contract_effective_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date: datetime) -> None:
        """
        Sets the contract_effective_date of this TrusteeBillingOverview.
        Date-time the contract became effective. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param contract_effective_date: The contract_effective_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._contract_effective_date = contract_effective_date

    @property
    def contract_end_date(self) -> datetime:
        """
        Gets the contract_end_date of this TrusteeBillingOverview.
        Date-time the contract ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The contract_end_date of this TrusteeBillingOverview.
        :rtype: datetime
        """
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, contract_end_date: datetime) -> None:
        """
        Sets the contract_end_date of this TrusteeBillingOverview.
        Date-time the contract ends. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param contract_end_date: The contract_end_date of this TrusteeBillingOverview.
        :type: datetime
        """
        

        self._contract_end_date = contract_end_date

    @property
    def minimum_monthly_amount(self) -> str:
        """
        Gets the minimum_monthly_amount of this TrusteeBillingOverview.
        Minimum amount that will be charged for the month

        :return: The minimum_monthly_amount of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._minimum_monthly_amount

    @minimum_monthly_amount.setter
    def minimum_monthly_amount(self, minimum_monthly_amount: str) -> None:
        """
        Sets the minimum_monthly_amount of this TrusteeBillingOverview.
        Minimum amount that will be charged for the month

        :param minimum_monthly_amount: The minimum_monthly_amount of this TrusteeBillingOverview.
        :type: str
        """
        

        self._minimum_monthly_amount = minimum_monthly_amount

    @property
    def in_ramp_period(self) -> bool:
        """
        Gets the in_ramp_period of this TrusteeBillingOverview.


        :return: The in_ramp_period of this TrusteeBillingOverview.
        :rtype: bool
        """
        return self._in_ramp_period

    @in_ramp_period.setter
    def in_ramp_period(self, in_ramp_period: bool) -> None:
        """
        Sets the in_ramp_period of this TrusteeBillingOverview.


        :param in_ramp_period: The in_ramp_period of this TrusteeBillingOverview.
        :type: bool
        """
        

        self._in_ramp_period = in_ramp_period

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this TrusteeBillingOverview.
        The URI for this object

        :return: The self_uri of this TrusteeBillingOverview.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this TrusteeBillingOverview.
        The URI for this object

        :param self_uri: The self_uri of this TrusteeBillingOverview.
        :type: str
        """
        

        self._self_uri = self_uri

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

