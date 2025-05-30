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
    from . import BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema
    from . import BuImportAgentScheduleUploadSchema
    from . import BuShortTermForecastReference

class ImportScheduleUploadSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ImportScheduleUploadSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'week_count': 'int',
            'published': 'bool',
            'short_term_forecast': 'BuShortTermForecastReference',
            'headcount_forecast': 'BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema',
            'agent_schedules': 'list[BuImportAgentScheduleUploadSchema]'
        }

        self.attribute_map = {
            'description': 'description',
            'week_count': 'weekCount',
            'published': 'published',
            'short_term_forecast': 'shortTermForecast',
            'headcount_forecast': 'headcountForecast',
            'agent_schedules': 'agentSchedules'
        }

        self._description = None
        self._week_count = None
        self._published = None
        self._short_term_forecast = None
        self._headcount_forecast = None
        self._agent_schedules = None

    @property
    def description(self) -> str:
        """
        Gets the description of this ImportScheduleUploadSchema.
        The description for the imported schedule

        :return: The description of this ImportScheduleUploadSchema.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this ImportScheduleUploadSchema.
        The description for the imported schedule

        :param description: The description of this ImportScheduleUploadSchema.
        :type: str
        """
        

        self._description = description

    @property
    def week_count(self) -> int:
        """
        Gets the week_count of this ImportScheduleUploadSchema.
        The number of weeks the imported schedule will cover

        :return: The week_count of this ImportScheduleUploadSchema.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count: int) -> None:
        """
        Sets the week_count of this ImportScheduleUploadSchema.
        The number of weeks the imported schedule will cover

        :param week_count: The week_count of this ImportScheduleUploadSchema.
        :type: int
        """
        

        self._week_count = week_count

    @property
    def published(self) -> bool:
        """
        Gets the published of this ImportScheduleUploadSchema.
        Whether the imported schedule should be immediately published

        :return: The published of this ImportScheduleUploadSchema.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published: bool) -> None:
        """
        Sets the published of this ImportScheduleUploadSchema.
        Whether the imported schedule should be immediately published

        :param published: The published of this ImportScheduleUploadSchema.
        :type: bool
        """
        

        self._published = published

    @property
    def short_term_forecast(self) -> 'BuShortTermForecastReference':
        """
        Gets the short_term_forecast of this ImportScheduleUploadSchema.
        The short term forecast to associate with the imported schedule

        :return: The short_term_forecast of this ImportScheduleUploadSchema.
        :rtype: BuShortTermForecastReference
        """
        return self._short_term_forecast

    @short_term_forecast.setter
    def short_term_forecast(self, short_term_forecast: 'BuShortTermForecastReference') -> None:
        """
        Sets the short_term_forecast of this ImportScheduleUploadSchema.
        The short term forecast to associate with the imported schedule

        :param short_term_forecast: The short_term_forecast of this ImportScheduleUploadSchema.
        :type: BuShortTermForecastReference
        """
        

        self._short_term_forecast = short_term_forecast

    @property
    def headcount_forecast(self) -> 'BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema':
        """
        Gets the headcount_forecast of this ImportScheduleUploadSchema.
        The headcount forecast to associate with the imported schedule

        :return: The headcount_forecast of this ImportScheduleUploadSchema.
        :rtype: BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema
        """
        return self._headcount_forecast

    @headcount_forecast.setter
    def headcount_forecast(self, headcount_forecast: 'BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema') -> None:
        """
        Sets the headcount_forecast of this ImportScheduleUploadSchema.
        The headcount forecast to associate with the imported schedule

        :param headcount_forecast: The headcount_forecast of this ImportScheduleUploadSchema.
        :type: BuHeadcountForecastBuPlanningGroupHeadcountForecastUploadSchema
        """
        

        self._headcount_forecast = headcount_forecast

    @property
    def agent_schedules(self) -> List['BuImportAgentScheduleUploadSchema']:
        """
        Gets the agent_schedules of this ImportScheduleUploadSchema.
        Individual agent schedules

        :return: The agent_schedules of this ImportScheduleUploadSchema.
        :rtype: list[BuImportAgentScheduleUploadSchema]
        """
        return self._agent_schedules

    @agent_schedules.setter
    def agent_schedules(self, agent_schedules: List['BuImportAgentScheduleUploadSchema']) -> None:
        """
        Sets the agent_schedules of this ImportScheduleUploadSchema.
        Individual agent schedules

        :param agent_schedules: The agent_schedules of this ImportScheduleUploadSchema.
        :type: list[BuImportAgentScheduleUploadSchema]
        """
        

        self._agent_schedules = agent_schedules

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

