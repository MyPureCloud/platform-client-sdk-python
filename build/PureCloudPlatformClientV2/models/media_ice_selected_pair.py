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
    from . import MediaIceSelectedCandidate

class MediaIceSelectedPair(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MediaIceSelectedPair - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client': 'MediaIceSelectedCandidate',
            'server': 'MediaIceSelectedCandidate',
            'candidate_pair_selected_milliseconds': 'int'
        }

        self.attribute_map = {
            'client': 'client',
            'server': 'server',
            'candidate_pair_selected_milliseconds': 'candidatePairSelectedMilliseconds'
        }

        self._client = None
        self._server = None
        self._candidate_pair_selected_milliseconds = None

    @property
    def client(self) -> 'MediaIceSelectedCandidate':
        """
        Gets the client of this MediaIceSelectedPair.
        The remote candidate that was chosen

        :return: The client of this MediaIceSelectedPair.
        :rtype: MediaIceSelectedCandidate
        """
        return self._client

    @client.setter
    def client(self, client: 'MediaIceSelectedCandidate') -> None:
        """
        Sets the client of this MediaIceSelectedPair.
        The remote candidate that was chosen

        :param client: The client of this MediaIceSelectedPair.
        :type: MediaIceSelectedCandidate
        """
        

        self._client = client

    @property
    def server(self) -> 'MediaIceSelectedCandidate':
        """
        Gets the server of this MediaIceSelectedPair.
        The local candidate that was chosen

        :return: The server of this MediaIceSelectedPair.
        :rtype: MediaIceSelectedCandidate
        """
        return self._server

    @server.setter
    def server(self, server: 'MediaIceSelectedCandidate') -> None:
        """
        Sets the server of this MediaIceSelectedPair.
        The local candidate that was chosen

        :param server: The server of this MediaIceSelectedPair.
        :type: MediaIceSelectedCandidate
        """
        

        self._server = server

    @property
    def candidate_pair_selected_milliseconds(self) -> int:
        """
        Gets the candidate_pair_selected_milliseconds of this MediaIceSelectedPair.
        Relative milliseconds since creation of endpoint when this ICE candidate pair has been selected

        :return: The candidate_pair_selected_milliseconds of this MediaIceSelectedPair.
        :rtype: int
        """
        return self._candidate_pair_selected_milliseconds

    @candidate_pair_selected_milliseconds.setter
    def candidate_pair_selected_milliseconds(self, candidate_pair_selected_milliseconds: int) -> None:
        """
        Sets the candidate_pair_selected_milliseconds of this MediaIceSelectedPair.
        Relative milliseconds since creation of endpoint when this ICE candidate pair has been selected

        :param candidate_pair_selected_milliseconds: The candidate_pair_selected_milliseconds of this MediaIceSelectedPair.
        :type: int
        """
        

        self._candidate_pair_selected_milliseconds = candidate_pair_selected_milliseconds

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
