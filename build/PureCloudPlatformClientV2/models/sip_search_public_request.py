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


class SIPSearchPublicRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SIPSearchPublicRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'call_id': 'str',
            'to_user': 'str',
            'from_user': 'str',
            'conversation_id': 'str',
            'participant_id': 'str',
            'date_start': 'datetime',
            'date_end': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'call_id': 'callId',
            'to_user': 'toUser',
            'from_user': 'fromUser',
            'conversation_id': 'conversationId',
            'participant_id': 'participantId',
            'date_start': 'dateStart',
            'date_end': 'dateEnd',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._call_id = None
        self._to_user = None
        self._from_user = None
        self._conversation_id = None
        self._participant_id = None
        self._date_start = None
        self._date_end = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this SIPSearchPublicRequest.
        The globally unique identifier for the object.

        :return: The id of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this SIPSearchPublicRequest.
        The globally unique identifier for the object.

        :param id: The id of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this SIPSearchPublicRequest.


        :return: The name of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this SIPSearchPublicRequest.


        :param name: The name of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._name = name

    @property
    def call_id(self) -> str:
        """
        Gets the call_id of this SIPSearchPublicRequest.
        unique identification of the placed call

        :return: The call_id of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._call_id

    @call_id.setter
    def call_id(self, call_id: str) -> None:
        """
        Sets the call_id of this SIPSearchPublicRequest.
        unique identification of the placed call

        :param call_id: The call_id of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._call_id = call_id

    @property
    def to_user(self) -> str:
        """
        Gets the to_user of this SIPSearchPublicRequest.
        SIP user to who the call was placed

        :return: The to_user of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._to_user

    @to_user.setter
    def to_user(self, to_user: str) -> None:
        """
        Sets the to_user of this SIPSearchPublicRequest.
        SIP user to who the call was placed

        :param to_user: The to_user of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._to_user = to_user

    @property
    def from_user(self) -> str:
        """
        Gets the from_user of this SIPSearchPublicRequest.
        SIP user who placed the call

        :return: The from_user of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._from_user

    @from_user.setter
    def from_user(self, from_user: str) -> None:
        """
        Sets the from_user of this SIPSearchPublicRequest.
        SIP user who placed the call

        :param from_user: The from_user of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._from_user = from_user

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this SIPSearchPublicRequest.
        Unique identification of the conversation

        :return: The conversation_id of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this SIPSearchPublicRequest.
        Unique identification of the conversation

        :param conversation_id: The conversation_id of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def participant_id(self) -> str:
        """
        Gets the participant_id of this SIPSearchPublicRequest.
        Unique identification of the participant

        :return: The participant_id of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id: str) -> None:
        """
        Sets the participant_id of this SIPSearchPublicRequest.
        Unique identification of the participant

        :param participant_id: The participant_id of this SIPSearchPublicRequest.
        :type: str
        """
        

        self._participant_id = participant_id

    @property
    def date_start(self) -> datetime:
        """
        Gets the date_start of this SIPSearchPublicRequest.
        Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_start of this SIPSearchPublicRequest.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: datetime) -> None:
        """
        Sets the date_start of this SIPSearchPublicRequest.
        Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_start: The date_start of this SIPSearchPublicRequest.
        :type: datetime
        """
        

        self._date_start = date_start

    @property
    def date_end(self) -> datetime:
        """
        Gets the date_end of this SIPSearchPublicRequest.
        End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_end of this SIPSearchPublicRequest.
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end: datetime) -> None:
        """
        Sets the date_end of this SIPSearchPublicRequest.
        End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_end: The date_end of this SIPSearchPublicRequest.
        :type: datetime
        """
        

        self._date_end = date_end

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this SIPSearchPublicRequest.
        The URI for this object

        :return: The self_uri of this SIPSearchPublicRequest.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this SIPSearchPublicRequest.
        The URI for this object

        :param self_uri: The self_uri of this SIPSearchPublicRequest.
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

