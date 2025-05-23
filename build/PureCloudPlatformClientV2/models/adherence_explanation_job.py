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
    from . import AdherenceExplanationListingAgentQueryResponse
    from . import AdherenceExplanationListingBuQueryResponse
    from . import AdherenceExplanationResponse
    from . import ErrorBody

class AdherenceExplanationJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AdherenceExplanationJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'status': 'str',
            'adherence_explanation': 'AdherenceExplanationResponse',
            'download_url': 'str',
            'error': 'ErrorBody',
            'agent_query_response_template': 'AdherenceExplanationListingAgentQueryResponse',
            'bu_query_response_template': 'AdherenceExplanationListingBuQueryResponse',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'status': 'status',
            'adherence_explanation': 'adherenceExplanation',
            'download_url': 'downloadUrl',
            'error': 'error',
            'agent_query_response_template': 'agentQueryResponseTemplate',
            'bu_query_response_template': 'buQueryResponseTemplate',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._type = None
        self._status = None
        self._adherence_explanation = None
        self._download_url = None
        self._error = None
        self._agent_query_response_template = None
        self._bu_query_response_template = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AdherenceExplanationJob.
        The globally unique identifier for the object.

        :return: The id of this AdherenceExplanationJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AdherenceExplanationJob.
        The globally unique identifier for the object.

        :param id: The id of this AdherenceExplanationJob.
        :type: str
        """
        

        self._id = id

    @property
    def type(self) -> str:
        """
        Gets the type of this AdherenceExplanationJob.
        The type of the adherence explanation job

        :return: The type of this AdherenceExplanationJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this AdherenceExplanationJob.
        The type of the adherence explanation job

        :param type: The type of this AdherenceExplanationJob.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["AddExplanation", "UpdateExplanation", "QueryAgentExplanations", "QueryBuExplanations"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def status(self) -> str:
        """
        Gets the status of this AdherenceExplanationJob.
        The status of the adherence explanation job

        :return: The status of this AdherenceExplanationJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this AdherenceExplanationJob.
        The status of the adherence explanation job

        :param status: The status of this AdherenceExplanationJob.
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
    def adherence_explanation(self) -> 'AdherenceExplanationResponse':
        """
        Gets the adherence_explanation of this AdherenceExplanationJob.
        The adherence explanation added or modified by the job once complete; may be null if status == 'Error'. Used if type is in [ 'AddExplanation', 'UpdateExplanation' ]

        :return: The adherence_explanation of this AdherenceExplanationJob.
        :rtype: AdherenceExplanationResponse
        """
        return self._adherence_explanation

    @adherence_explanation.setter
    def adherence_explanation(self, adherence_explanation: 'AdherenceExplanationResponse') -> None:
        """
        Sets the adherence_explanation of this AdherenceExplanationJob.
        The adherence explanation added or modified by the job once complete; may be null if status == 'Error'. Used if type is in [ 'AddExplanation', 'UpdateExplanation' ]

        :param adherence_explanation: The adherence_explanation of this AdherenceExplanationJob.
        :type: AdherenceExplanationResponse
        """
        

        self._adherence_explanation = adherence_explanation

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this AdherenceExplanationJob.
        A URL to fetch results of the job. Only set if status == 'Complete' and type is in [ 'QueryAgentExplanations', 'QueryBuExplanations' ]

        :return: The download_url of this AdherenceExplanationJob.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this AdherenceExplanationJob.
        A URL to fetch results of the job. Only set if status == 'Complete' and type is in [ 'QueryAgentExplanations', 'QueryBuExplanations' ]

        :param download_url: The download_url of this AdherenceExplanationJob.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def error(self) -> 'ErrorBody':
        """
        Gets the error of this AdherenceExplanationJob.
        Error details if status == 'Error'

        :return: The error of this AdherenceExplanationJob.
        :rtype: ErrorBody
        """
        return self._error

    @error.setter
    def error(self, error: 'ErrorBody') -> None:
        """
        Sets the error of this AdherenceExplanationJob.
        Error details if status == 'Error'

        :param error: The error of this AdherenceExplanationJob.
        :type: ErrorBody
        """
        

        self._error = error

    @property
    def agent_query_response_template(self) -> 'AdherenceExplanationListingAgentQueryResponse':
        """
        Gets the agent_query_response_template of this AdherenceExplanationJob.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'QueryAgentExplanations'

        :return: The agent_query_response_template of this AdherenceExplanationJob.
        :rtype: AdherenceExplanationListingAgentQueryResponse
        """
        return self._agent_query_response_template

    @agent_query_response_template.setter
    def agent_query_response_template(self, agent_query_response_template: 'AdherenceExplanationListingAgentQueryResponse') -> None:
        """
        Sets the agent_query_response_template of this AdherenceExplanationJob.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'QueryAgentExplanations'

        :param agent_query_response_template: The agent_query_response_template of this AdherenceExplanationJob.
        :type: AdherenceExplanationListingAgentQueryResponse
        """
        

        self._agent_query_response_template = agent_query_response_template

    @property
    def bu_query_response_template(self) -> 'AdherenceExplanationListingBuQueryResponse':
        """
        Gets the bu_query_response_template of this AdherenceExplanationJob.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'QueryBuExplanations'

        :return: The bu_query_response_template of this AdherenceExplanationJob.
        :rtype: AdherenceExplanationListingBuQueryResponse
        """
        return self._bu_query_response_template

    @bu_query_response_template.setter
    def bu_query_response_template(self, bu_query_response_template: 'AdherenceExplanationListingBuQueryResponse') -> None:
        """
        Sets the bu_query_response_template of this AdherenceExplanationJob.
        Schema template for deserializing data returned from the downloadUrl. Use if type == 'QueryBuExplanations'

        :param bu_query_response_template: The bu_query_response_template of this AdherenceExplanationJob.
        :type: AdherenceExplanationListingBuQueryResponse
        """
        

        self._bu_query_response_template = bu_query_response_template

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this AdherenceExplanationJob.
        The URI for this object

        :return: The self_uri of this AdherenceExplanationJob.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this AdherenceExplanationJob.
        The URI for this object

        :param self_uri: The self_uri of this AdherenceExplanationJob.
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

