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


class ApiUsageSimpleSearch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ApiUsageSimpleSearch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval': 'str',
            'metrics': 'list[str]',
            'oauth_client_names': 'list[str]',
            'http_methods': 'list[str]',
            'template_uris': 'list[str]'
        }

        self.attribute_map = {
            'interval': 'interval',
            'metrics': 'metrics',
            'oauth_client_names': 'oauthClientNames',
            'http_methods': 'httpMethods',
            'template_uris': 'templateUris'
        }

        self._interval = None
        self._metrics = None
        self._oauth_client_names = None
        self._http_methods = None
        self._template_uris = None

    @property
    def interval(self) -> str:
        """
        Gets the interval of this ApiUsageSimpleSearch.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this ApiUsageSimpleSearch.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval: str) -> None:
        """
        Sets the interval of this ApiUsageSimpleSearch.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this ApiUsageSimpleSearch.
        :type: str
        """
        

        self._interval = interval

    @property
    def metrics(self) -> List[str]:
        """
        Gets the metrics of this ApiUsageSimpleSearch.
        Behaves like a SQL SELECT clause. Enables retrieving only named metrics. If omitted, all metrics that are available will be returned (like SELECT *).

        :return: The metrics of this ApiUsageSimpleSearch.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List[str]) -> None:
        """
        Sets the metrics of this ApiUsageSimpleSearch.
        Behaves like a SQL SELECT clause. Enables retrieving only named metrics. If omitted, all metrics that are available will be returned (like SELECT *).

        :param metrics: The metrics of this ApiUsageSimpleSearch.
        :type: list[str]
        """
        

        self._metrics = metrics

    @property
    def oauth_client_names(self) -> List[str]:
        """
        Gets the oauth_client_names of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of OAuth client names to be queried.

        :return: The oauth_client_names of this ApiUsageSimpleSearch.
        :rtype: list[str]
        """
        return self._oauth_client_names

    @oauth_client_names.setter
    def oauth_client_names(self, oauth_client_names: List[str]) -> None:
        """
        Sets the oauth_client_names of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of OAuth client names to be queried.

        :param oauth_client_names: The oauth_client_names of this ApiUsageSimpleSearch.
        :type: list[str]
        """
        

        self._oauth_client_names = oauth_client_names

    @property
    def http_methods(self) -> List[str]:
        """
        Gets the http_methods of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of HTTP methods to be queried.

        :return: The http_methods of this ApiUsageSimpleSearch.
        :rtype: list[str]
        """
        return self._http_methods

    @http_methods.setter
    def http_methods(self, http_methods: List[str]) -> None:
        """
        Sets the http_methods of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of HTTP methods to be queried.

        :param http_methods: The http_methods of this ApiUsageSimpleSearch.
        :type: list[str]
        """
        

        self._http_methods = http_methods

    @property
    def template_uris(self) -> List[str]:
        """
        Gets the template_uris of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of Template Uris to be queried.

        :return: The template_uris of this ApiUsageSimpleSearch.
        :rtype: list[str]
        """
        return self._template_uris

    @template_uris.setter
    def template_uris(self, template_uris: List[str]) -> None:
        """
        Sets the template_uris of this ApiUsageSimpleSearch.
        Behaves like a SQL WHERE with multiple IN operators. Specifies a list of Template Uris to be queried.

        :param template_uris: The template_uris of this ApiUsageSimpleSearch.
        :type: list[str]
        """
        

        self._template_uris = template_uris

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
