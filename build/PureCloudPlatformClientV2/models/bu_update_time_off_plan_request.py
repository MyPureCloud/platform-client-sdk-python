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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import SetWrapperString
    from . import UpdateTimeOffPlanBusinessUnitAssociation
    from . import UpdateTimeOffPlanManagementUnitAssociation
    from . import ValueWrapperHrisTimeOffType
    from . import WfmVersionedEntityMetadata

class BuUpdateTimeOffPlanRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuUpdateTimeOffPlanRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'activity_code_ids': 'SetWrapperString',
            'auto_approval_rule': 'str',
            'days_before_start_to_expire_from_waitlist': 'int',
            'hris_time_off_type': 'ValueWrapperHrisTimeOffType',
            'enabled': 'bool',
            'count_against_time_off_limits': 'bool',
            'business_unit_association': 'UpdateTimeOffPlanBusinessUnitAssociation',
            'management_unit_association': 'UpdateTimeOffPlanManagementUnitAssociation',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'name': 'name',
            'activity_code_ids': 'activityCodeIds',
            'auto_approval_rule': 'autoApprovalRule',
            'days_before_start_to_expire_from_waitlist': 'daysBeforeStartToExpireFromWaitlist',
            'hris_time_off_type': 'hrisTimeOffType',
            'enabled': 'enabled',
            'count_against_time_off_limits': 'countAgainstTimeOffLimits',
            'business_unit_association': 'businessUnitAssociation',
            'management_unit_association': 'managementUnitAssociation',
            'metadata': 'metadata'
        }

        self._name = None
        self._activity_code_ids = None
        self._auto_approval_rule = None
        self._days_before_start_to_expire_from_waitlist = None
        self._hris_time_off_type = None
        self._enabled = None
        self._count_against_time_off_limits = None
        self._business_unit_association = None
        self._management_unit_association = None
        self._metadata = None

    @property
    def name(self) -> str:
        """
        Gets the name of this BuUpdateTimeOffPlanRequest.
        The name of this time-off plan

        :return: The name of this BuUpdateTimeOffPlanRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this BuUpdateTimeOffPlanRequest.
        The name of this time-off plan

        :param name: The name of this BuUpdateTimeOffPlanRequest.
        :type: str
        """
        

        self._name = name

    @property
    def activity_code_ids(self) -> 'SetWrapperString':
        """
        Gets the activity_code_ids of this BuUpdateTimeOffPlanRequest.
        The IDs of activity codes to associate with this time-off plan

        :return: The activity_code_ids of this BuUpdateTimeOffPlanRequest.
        :rtype: SetWrapperString
        """
        return self._activity_code_ids

    @activity_code_ids.setter
    def activity_code_ids(self, activity_code_ids: 'SetWrapperString') -> None:
        """
        Sets the activity_code_ids of this BuUpdateTimeOffPlanRequest.
        The IDs of activity codes to associate with this time-off plan

        :param activity_code_ids: The activity_code_ids of this BuUpdateTimeOffPlanRequest.
        :type: SetWrapperString
        """
        

        self._activity_code_ids = activity_code_ids

    @property
    def auto_approval_rule(self) -> str:
        """
        Gets the auto_approval_rule of this BuUpdateTimeOffPlanRequest.
        Auto approval rule for this time-off plan

        :return: The auto_approval_rule of this BuUpdateTimeOffPlanRequest.
        :rtype: str
        """
        return self._auto_approval_rule

    @auto_approval_rule.setter
    def auto_approval_rule(self, auto_approval_rule: str) -> None:
        """
        Sets the auto_approval_rule of this BuUpdateTimeOffPlanRequest.
        Auto approval rule for this time-off plan

        :param auto_approval_rule: The auto_approval_rule of this BuUpdateTimeOffPlanRequest.
        :type: str
        """
        if isinstance(auto_approval_rule, int):
            auto_approval_rule = str(auto_approval_rule)
        allowed_values = ["Never", "Always", "CheckLimits"]
        if auto_approval_rule.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for auto_approval_rule -> " + auto_approval_rule)
            self._auto_approval_rule = "outdated_sdk_version"
        else:
            self._auto_approval_rule = auto_approval_rule

    @property
    def days_before_start_to_expire_from_waitlist(self) -> int:
        """
        Gets the days_before_start_to_expire_from_waitlist of this BuUpdateTimeOffPlanRequest.
        The number of days before the time-off request start date for when the request will be expired from the waitlist

        :return: The days_before_start_to_expire_from_waitlist of this BuUpdateTimeOffPlanRequest.
        :rtype: int
        """
        return self._days_before_start_to_expire_from_waitlist

    @days_before_start_to_expire_from_waitlist.setter
    def days_before_start_to_expire_from_waitlist(self, days_before_start_to_expire_from_waitlist: int) -> None:
        """
        Sets the days_before_start_to_expire_from_waitlist of this BuUpdateTimeOffPlanRequest.
        The number of days before the time-off request start date for when the request will be expired from the waitlist

        :param days_before_start_to_expire_from_waitlist: The days_before_start_to_expire_from_waitlist of this BuUpdateTimeOffPlanRequest.
        :type: int
        """
        

        self._days_before_start_to_expire_from_waitlist = days_before_start_to_expire_from_waitlist

    @property
    def hris_time_off_type(self) -> 'ValueWrapperHrisTimeOffType':
        """
        Gets the hris_time_off_type of this BuUpdateTimeOffPlanRequest.
        Time-off type, if this time-off plan is associated with the integration

        :return: The hris_time_off_type of this BuUpdateTimeOffPlanRequest.
        :rtype: ValueWrapperHrisTimeOffType
        """
        return self._hris_time_off_type

    @hris_time_off_type.setter
    def hris_time_off_type(self, hris_time_off_type: 'ValueWrapperHrisTimeOffType') -> None:
        """
        Sets the hris_time_off_type of this BuUpdateTimeOffPlanRequest.
        Time-off type, if this time-off plan is associated with the integration

        :param hris_time_off_type: The hris_time_off_type of this BuUpdateTimeOffPlanRequest.
        :type: ValueWrapperHrisTimeOffType
        """
        

        self._hris_time_off_type = hris_time_off_type

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this BuUpdateTimeOffPlanRequest.
        Whether this time-off plan should be used by agents

        :return: The enabled of this BuUpdateTimeOffPlanRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this BuUpdateTimeOffPlanRequest.
        Whether this time-off plan should be used by agents

        :param enabled: The enabled of this BuUpdateTimeOffPlanRequest.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def count_against_time_off_limits(self) -> bool:
        """
        Gets the count_against_time_off_limits of this BuUpdateTimeOffPlanRequest.
        Whether this time-off plan should count against time-off limits

        :return: The count_against_time_off_limits of this BuUpdateTimeOffPlanRequest.
        :rtype: bool
        """
        return self._count_against_time_off_limits

    @count_against_time_off_limits.setter
    def count_against_time_off_limits(self, count_against_time_off_limits: bool) -> None:
        """
        Sets the count_against_time_off_limits of this BuUpdateTimeOffPlanRequest.
        Whether this time-off plan should count against time-off limits

        :param count_against_time_off_limits: The count_against_time_off_limits of this BuUpdateTimeOffPlanRequest.
        :type: bool
        """
        

        self._count_against_time_off_limits = count_against_time_off_limits

    @property
    def business_unit_association(self) -> 'UpdateTimeOffPlanBusinessUnitAssociation':
        """
        Gets the business_unit_association of this BuUpdateTimeOffPlanRequest.
        Business unit association, if the time-off plan belongs to a business unit. managementUnitAssociation must not be set if this is populated

        :return: The business_unit_association of this BuUpdateTimeOffPlanRequest.
        :rtype: UpdateTimeOffPlanBusinessUnitAssociation
        """
        return self._business_unit_association

    @business_unit_association.setter
    def business_unit_association(self, business_unit_association: 'UpdateTimeOffPlanBusinessUnitAssociation') -> None:
        """
        Sets the business_unit_association of this BuUpdateTimeOffPlanRequest.
        Business unit association, if the time-off plan belongs to a business unit. managementUnitAssociation must not be set if this is populated

        :param business_unit_association: The business_unit_association of this BuUpdateTimeOffPlanRequest.
        :type: UpdateTimeOffPlanBusinessUnitAssociation
        """
        

        self._business_unit_association = business_unit_association

    @property
    def management_unit_association(self) -> 'UpdateTimeOffPlanManagementUnitAssociation':
        """
        Gets the management_unit_association of this BuUpdateTimeOffPlanRequest.
        Management unit association, if the time-off plan belongs to a management unit. businessUnitAssociation must not be set if this is populated

        :return: The management_unit_association of this BuUpdateTimeOffPlanRequest.
        :rtype: UpdateTimeOffPlanManagementUnitAssociation
        """
        return self._management_unit_association

    @management_unit_association.setter
    def management_unit_association(self, management_unit_association: 'UpdateTimeOffPlanManagementUnitAssociation') -> None:
        """
        Sets the management_unit_association of this BuUpdateTimeOffPlanRequest.
        Management unit association, if the time-off plan belongs to a management unit. businessUnitAssociation must not be set if this is populated

        :param management_unit_association: The management_unit_association of this BuUpdateTimeOffPlanRequest.
        :type: UpdateTimeOffPlanManagementUnitAssociation
        """
        

        self._management_unit_association = management_unit_association

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this BuUpdateTimeOffPlanRequest.
        Version metadata for this time-off plan

        :return: The metadata of this BuUpdateTimeOffPlanRequest.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this BuUpdateTimeOffPlanRequest.
        Version metadata for this time-off plan

        :param metadata: The metadata of this BuUpdateTimeOffPlanRequest.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

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
