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
    from . import AlternativeShiftBulkUpdateTradesResponseTemplate
    from . import AlternativeShiftOffersViewResponseTemplate
    from . import AlternativeShiftTradesViewResponseTemplate
    from . import ErrorBody

class BuAlternativeShiftJobResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuAlternativeShiftJobResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'type': 'str',
            'download_url': 'str',
            'error': 'ErrorBody',
            'view_offers_results': 'AlternativeShiftOffersViewResponseTemplate',
            'view_trades_results': 'AlternativeShiftTradesViewResponseTemplate',
            'bulk_update_trades_results': 'AlternativeShiftBulkUpdateTradesResponseTemplate',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'type': 'type',
            'download_url': 'downloadUrl',
            'error': 'error',
            'view_offers_results': 'viewOffersResults',
            'view_trades_results': 'viewTradesResults',
            'bulk_update_trades_results': 'bulkUpdateTradesResults',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._status = None
        self._type = None
        self._download_url = None
        self._error = None
        self._view_offers_results = None
        self._view_trades_results = None
        self._bulk_update_trades_results = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this BuAlternativeShiftJobResponse.
        The globally unique identifier for the object.

        :return: The id of this BuAlternativeShiftJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this BuAlternativeShiftJobResponse.
        The globally unique identifier for the object.

        :param id: The id of this BuAlternativeShiftJobResponse.
        :type: str
        """
        

        self._id = id

    @property
    def status(self) -> str:
        """
        Gets the status of this BuAlternativeShiftJobResponse.
        The status of the alternative shift job

        :return: The status of this BuAlternativeShiftJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this BuAlternativeShiftJobResponse.
        The status of the alternative shift job

        :param status: The status of this BuAlternativeShiftJobResponse.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Processing", "Complete", "Error"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def type(self) -> str:
        """
        Gets the type of this BuAlternativeShiftJobResponse.
        The type of job

        :return: The type of this BuAlternativeShiftJobResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this BuAlternativeShiftJobResponse.
        The type of job

        :param type: The type of this BuAlternativeShiftJobResponse.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["ListOffers", "SearchOffers", "ListUserTrades", "SearchTrades", "BulkUpdateTrades"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this BuAlternativeShiftJobResponse.
        The URL where completed results are available, only set if status == 'Complete'

        :return: The download_url of this BuAlternativeShiftJobResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this BuAlternativeShiftJobResponse.
        The URL where completed results are available, only set if status == 'Complete'

        :param download_url: The download_url of this BuAlternativeShiftJobResponse.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def error(self) -> 'ErrorBody':
        """
        Gets the error of this BuAlternativeShiftJobResponse.
        Any error information, only set if the status == 'Error'

        :return: The error of this BuAlternativeShiftJobResponse.
        :rtype: ErrorBody
        """
        return self._error

    @error.setter
    def error(self, error: 'ErrorBody') -> None:
        """
        Sets the error of this BuAlternativeShiftJobResponse.
        Any error information, only set if the status == 'Error'

        :param error: The error of this BuAlternativeShiftJobResponse.
        :type: ErrorBody
        """
        

        self._error = error

    @property
    def view_offers_results(self) -> 'AlternativeShiftOffersViewResponseTemplate':
        """
        Gets the view_offers_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'ListOffers' or 'SearchOffers'

        :return: The view_offers_results of this BuAlternativeShiftJobResponse.
        :rtype: AlternativeShiftOffersViewResponseTemplate
        """
        return self._view_offers_results

    @view_offers_results.setter
    def view_offers_results(self, view_offers_results: 'AlternativeShiftOffersViewResponseTemplate') -> None:
        """
        Sets the view_offers_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'ListOffers' or 'SearchOffers'

        :param view_offers_results: The view_offers_results of this BuAlternativeShiftJobResponse.
        :type: AlternativeShiftOffersViewResponseTemplate
        """
        

        self._view_offers_results = view_offers_results

    @property
    def view_trades_results(self) -> 'AlternativeShiftTradesViewResponseTemplate':
        """
        Gets the view_trades_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'ListUserTrades' or 'SearchTrades'

        :return: The view_trades_results of this BuAlternativeShiftJobResponse.
        :rtype: AlternativeShiftTradesViewResponseTemplate
        """
        return self._view_trades_results

    @view_trades_results.setter
    def view_trades_results(self, view_trades_results: 'AlternativeShiftTradesViewResponseTemplate') -> None:
        """
        Sets the view_trades_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'ListUserTrades' or 'SearchTrades'

        :param view_trades_results: The view_trades_results of this BuAlternativeShiftJobResponse.
        :type: AlternativeShiftTradesViewResponseTemplate
        """
        

        self._view_trades_results = view_trades_results

    @property
    def bulk_update_trades_results(self) -> 'AlternativeShiftBulkUpdateTradesResponseTemplate':
        """
        Gets the bulk_update_trades_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'BulkUpdateTrades'

        :return: The bulk_update_trades_results of this BuAlternativeShiftJobResponse.
        :rtype: AlternativeShiftBulkUpdateTradesResponseTemplate
        """
        return self._bulk_update_trades_results

    @bulk_update_trades_results.setter
    def bulk_update_trades_results(self, bulk_update_trades_results: 'AlternativeShiftBulkUpdateTradesResponseTemplate') -> None:
        """
        Sets the bulk_update_trades_results of this BuAlternativeShiftJobResponse.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'BulkUpdateTrades'

        :param bulk_update_trades_results: The bulk_update_trades_results of this BuAlternativeShiftJobResponse.
        :type: AlternativeShiftBulkUpdateTradesResponseTemplate
        """
        

        self._bulk_update_trades_results = bulk_update_trades_results

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this BuAlternativeShiftJobResponse.
        The URI for this object

        :return: The self_uri of this BuAlternativeShiftJobResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this BuAlternativeShiftJobResponse.
        The URI for this object

        :param self_uri: The self_uri of this BuAlternativeShiftJobResponse.
        :type: str
        """
        

        self._self_uri = self_uri

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
