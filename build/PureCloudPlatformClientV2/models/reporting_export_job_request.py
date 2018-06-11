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


class ReportingExportJobRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportingExportJobRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'time_zone': 'TimeZone',
            'export_format': 'str',
            'interval': 'str',
            'period': 'str',
            'view_type': 'str',
            'filter': 'ViewFilter',
            'read': 'bool',
            'locale': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'time_zone': 'timeZone',
            'export_format': 'exportFormat',
            'interval': 'interval',
            'period': 'period',
            'view_type': 'viewType',
            'filter': 'filter',
            'read': 'read',
            'locale': 'locale'
        }

        self._name = None
        self._time_zone = None
        self._export_format = None
        self._interval = None
        self._period = None
        self._view_type = None
        self._filter = None
        self._read = None
        self._locale = None

    @property
    def name(self):
        """
        Gets the name of this ReportingExportJobRequest.
        The user supplied name of the export request

        :return: The name of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportingExportJobRequest.
        The user supplied name of the export request

        :param name: The name of this ReportingExportJobRequest.
        :type: str
        """
        
        self._name = name

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ReportingExportJobRequest.
        The requested timezone of the exported data

        :return: The time_zone of this ReportingExportJobRequest.
        :rtype: TimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ReportingExportJobRequest.
        The requested timezone of the exported data

        :param time_zone: The time_zone of this ReportingExportJobRequest.
        :type: TimeZone
        """
        
        self._time_zone = time_zone

    @property
    def export_format(self):
        """
        Gets the export_format of this ReportingExportJobRequest.
        The requested format of the exported data

        :return: The export_format of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        """
        Sets the export_format of this ReportingExportJobRequest.
        The requested format of the exported data

        :param export_format: The export_format of this ReportingExportJobRequest.
        :type: str
        """
        allowed_values = ["CSV"]
        if export_format.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for export_format -> " + export_format
            self._export_format = "outdated_sdk_version"
        else:
            self._export_format = export_format

    @property
    def interval(self):
        """
        Gets the interval of this ReportingExportJobRequest.
        The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ReportingExportJobRequest.
        The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this ReportingExportJobRequest.
        :type: str
        """
        
        self._interval = interval

    @property
    def period(self):
        """
        Gets the period of this ReportingExportJobRequest.
        The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The period of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this ReportingExportJobRequest.
        The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param period: The period of this ReportingExportJobRequest.
        :type: str
        """
        
        self._period = period

    @property
    def view_type(self):
        """
        Gets the view_type of this ReportingExportJobRequest.
        The type of view export job to be created

        :return: The view_type of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """
        Sets the view_type of this ReportingExportJobRequest.
        The type of view export job to be created

        :param view_type: The view_type of this ReportingExportJobRequest.
        :type: str
        """
        allowed_values = ["QUEUE_PERFORMANCE_SUMMARY_VIEW", "QUEUE_PERFORMANCE_DETAIL_VIEW", "INTERACTION_SEARCH_VIEW", "AGENT_PERFORMANCE_SUMMARY_VIEW", "AGENT_PERFORMANCE_DETAIL_VIEW", "AGENT_STATUS_SUMMARY_VIEW", "AGENT_STATUS_DETAIL_VIEW", "AGENT_EVALUATION_SUMMARY_VIEW", "AGENT_EVALUATION_DETAIL_VIEW", "AGENT_QUEUE_DETAIL_VIEW", "AGENT_INTERACTION_DETAIL_VIEW", "ABANDON_INSIGHTS_VIEW", "SKILLS_PERFORMANCE_VIEW"]
        if view_type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for view_type -> " + view_type
            self._view_type = "outdated_sdk_version"
        else:
            self._view_type = view_type

    @property
    def filter(self):
        """
        Gets the filter of this ReportingExportJobRequest.
        Filters to apply to create the view

        :return: The filter of this ReportingExportJobRequest.
        :rtype: ViewFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this ReportingExportJobRequest.
        Filters to apply to create the view

        :param filter: The filter of this ReportingExportJobRequest.
        :type: ViewFilter
        """
        
        self._filter = filter

    @property
    def read(self):
        """
        Gets the read of this ReportingExportJobRequest.
        Indicates if the request has been marked as read

        :return: The read of this ReportingExportJobRequest.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this ReportingExportJobRequest.
        Indicates if the request has been marked as read

        :param read: The read of this ReportingExportJobRequest.
        :type: bool
        """
        
        self._read = read

    @property
    def locale(self):
        """
        Gets the locale of this ReportingExportJobRequest.
        The locale use for localization of the exported data, i.e. en-us, es-mx  

        :return: The locale of this ReportingExportJobRequest.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this ReportingExportJobRequest.
        The locale use for localization of the exported data, i.e. en-us, es-mx  

        :param locale: The locale of this ReportingExportJobRequest.
        :type: str
        """
        
        self._locale = locale

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
