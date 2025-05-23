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
    from . import BuIntradayDataGroup
    from . import BuScheduleReference
    from . import BuShortTermForecastReference

class BuIntradayResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuIntradayResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'interval_length_minutes': 'int',
            'no_data_reason': 'str',
            'categories': 'list[str]',
            'short_term_forecast': 'BuShortTermForecastReference',
            'schedule': 'BuScheduleReference',
            'intraday_data_groupings': 'list[BuIntradayDataGroup]'
        }

        self.attribute_map = {
            'start_date': 'startDate',
            'end_date': 'endDate',
            'interval_length_minutes': 'intervalLengthMinutes',
            'no_data_reason': 'noDataReason',
            'categories': 'categories',
            'short_term_forecast': 'shortTermForecast',
            'schedule': 'schedule',
            'intraday_data_groupings': 'intradayDataGroupings'
        }

        self._start_date = None
        self._end_date = None
        self._interval_length_minutes = None
        self._no_data_reason = None
        self._categories = None
        self._short_term_forecast = None
        self._schedule = None
        self._intraday_data_groupings = None

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this BuIntradayResponse.
        The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_date of this BuIntradayResponse.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this BuIntradayResponse.
        The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_date: The start_date of this BuIntradayResponse.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def end_date(self) -> datetime:
        """
        Gets the end_date of this BuIntradayResponse.
        The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The end_date of this BuIntradayResponse.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime) -> None:
        """
        Sets the end_date of this BuIntradayResponse.
        The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param end_date: The end_date of this BuIntradayResponse.
        :type: datetime
        """
        

        self._end_date = end_date

    @property
    def interval_length_minutes(self) -> int:
        """
        Gets the interval_length_minutes of this BuIntradayResponse.
        The aggregation period in minutes, which determines the interval duration of the returned data

        :return: The interval_length_minutes of this BuIntradayResponse.
        :rtype: int
        """
        return self._interval_length_minutes

    @interval_length_minutes.setter
    def interval_length_minutes(self, interval_length_minutes: int) -> None:
        """
        Sets the interval_length_minutes of this BuIntradayResponse.
        The aggregation period in minutes, which determines the interval duration of the returned data

        :param interval_length_minutes: The interval_length_minutes of this BuIntradayResponse.
        :type: int
        """
        

        self._interval_length_minutes = interval_length_minutes

    @property
    def no_data_reason(self) -> str:
        """
        Gets the no_data_reason of this BuIntradayResponse.
        If not null, the reason there was no data for the request

        :return: The no_data_reason of this BuIntradayResponse.
        :rtype: str
        """
        return self._no_data_reason

    @no_data_reason.setter
    def no_data_reason(self, no_data_reason: str) -> None:
        """
        Sets the no_data_reason of this BuIntradayResponse.
        If not null, the reason there was no data for the request

        :param no_data_reason: The no_data_reason of this BuIntradayResponse.
        :type: str
        """
        if isinstance(no_data_reason, int):
            no_data_reason = str(no_data_reason)
        allowed_values = ["NoPublishedSchedule", "NoSourceForecast"]
        if no_data_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for no_data_reason -> " + no_data_reason)
            self._no_data_reason = "outdated_sdk_version"
        else:
            self._no_data_reason = no_data_reason

    @property
    def categories(self) -> List[str]:
        """
        Gets the categories of this BuIntradayResponse.
        The categories to which this data corresponds

        :return: The categories of this BuIntradayResponse.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]) -> None:
        """
        Sets the categories of this BuIntradayResponse.
        The categories to which this data corresponds

        :param categories: The categories of this BuIntradayResponse.
        :type: list[str]
        """
        

        self._categories = categories

    @property
    def short_term_forecast(self) -> 'BuShortTermForecastReference':
        """
        Gets the short_term_forecast of this BuIntradayResponse.
        Short term forecast reference

        :return: The short_term_forecast of this BuIntradayResponse.
        :rtype: BuShortTermForecastReference
        """
        return self._short_term_forecast

    @short_term_forecast.setter
    def short_term_forecast(self, short_term_forecast: 'BuShortTermForecastReference') -> None:
        """
        Sets the short_term_forecast of this BuIntradayResponse.
        Short term forecast reference

        :param short_term_forecast: The short_term_forecast of this BuIntradayResponse.
        :type: BuShortTermForecastReference
        """
        

        self._short_term_forecast = short_term_forecast

    @property
    def schedule(self) -> 'BuScheduleReference':
        """
        Gets the schedule of this BuIntradayResponse.
        Schedule reference

        :return: The schedule of this BuIntradayResponse.
        :rtype: BuScheduleReference
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: 'BuScheduleReference') -> None:
        """
        Sets the schedule of this BuIntradayResponse.
        Schedule reference

        :param schedule: The schedule of this BuIntradayResponse.
        :type: BuScheduleReference
        """
        

        self._schedule = schedule

    @property
    def intraday_data_groupings(self) -> List['BuIntradayDataGroup']:
        """
        Gets the intraday_data_groupings of this BuIntradayResponse.
        Intraday data grouped by a single media type and set of planning group IDs

        :return: The intraday_data_groupings of this BuIntradayResponse.
        :rtype: list[BuIntradayDataGroup]
        """
        return self._intraday_data_groupings

    @intraday_data_groupings.setter
    def intraday_data_groupings(self, intraday_data_groupings: List['BuIntradayDataGroup']) -> None:
        """
        Sets the intraday_data_groupings of this BuIntradayResponse.
        Intraday data grouped by a single media type and set of planning group IDs

        :param intraday_data_groupings: The intraday_data_groupings of this BuIntradayResponse.
        :type: list[BuIntradayDataGroup]
        """
        

        self._intraday_data_groupings = intraday_data_groupings

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

