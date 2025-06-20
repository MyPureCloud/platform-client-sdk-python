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
    from . import ConversationContentIntroduction
    from . import ConversationContentReceivedReplyMessage
    from . import ConversationFormPage
    from . import ConversationFormResponseComponent

class ConversationContentForm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationContentForm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'introduction': 'ConversationContentIntroduction',
            'form_pages': 'list[ConversationFormPage]',
            'received_message': 'ConversationContentReceivedReplyMessage',
            'reply_message': 'ConversationContentReceivedReplyMessage',
            'show_summary': 'bool',
            'response': 'list[ConversationFormResponseComponent]',
            'originating_message_id': 'str',
            'canned_response_id': 'str'
        }

        self.attribute_map = {
            'introduction': 'introduction',
            'form_pages': 'formPages',
            'received_message': 'receivedMessage',
            'reply_message': 'replyMessage',
            'show_summary': 'showSummary',
            'response': 'response',
            'originating_message_id': 'originatingMessageId',
            'canned_response_id': 'cannedResponseId'
        }

        self._introduction = None
        self._form_pages = None
        self._received_message = None
        self._reply_message = None
        self._show_summary = None
        self._response = None
        self._originating_message_id = None
        self._canned_response_id = None

    @property
    def introduction(self) -> 'ConversationContentIntroduction':
        """
        Gets the introduction of this ConversationContentForm.
        The intro component, used to give an intro into what the form entails

        :return: The introduction of this ConversationContentForm.
        :rtype: ConversationContentIntroduction
        """
        return self._introduction

    @introduction.setter
    def introduction(self, introduction: 'ConversationContentIntroduction') -> None:
        """
        Sets the introduction of this ConversationContentForm.
        The intro component, used to give an intro into what the form entails

        :param introduction: The introduction of this ConversationContentForm.
        :type: ConversationContentIntroduction
        """
        

        self._introduction = introduction

    @property
    def form_pages(self) -> List['ConversationFormPage']:
        """
        Gets the form_pages of this ConversationContentForm.
        Form pages

        :return: The form_pages of this ConversationContentForm.
        :rtype: list[ConversationFormPage]
        """
        return self._form_pages

    @form_pages.setter
    def form_pages(self, form_pages: List['ConversationFormPage']) -> None:
        """
        Sets the form_pages of this ConversationContentForm.
        Form pages

        :param form_pages: The form_pages of this ConversationContentForm.
        :type: list[ConversationFormPage]
        """
        

        self._form_pages = form_pages

    @property
    def received_message(self) -> 'ConversationContentReceivedReplyMessage':
        """
        Gets the received_message of this ConversationContentForm.
        The message prompt to fill out the form received.

        :return: The received_message of this ConversationContentForm.
        :rtype: ConversationContentReceivedReplyMessage
        """
        return self._received_message

    @received_message.setter
    def received_message(self, received_message: 'ConversationContentReceivedReplyMessage') -> None:
        """
        Sets the received_message of this ConversationContentForm.
        The message prompt to fill out the form received.

        :param received_message: The received_message of this ConversationContentForm.
        :type: ConversationContentReceivedReplyMessage
        """
        

        self._received_message = received_message

    @property
    def reply_message(self) -> 'ConversationContentReceivedReplyMessage':
        """
        Gets the reply_message of this ConversationContentForm.
        The reply message after the user has filled out the form received.

        :return: The reply_message of this ConversationContentForm.
        :rtype: ConversationContentReceivedReplyMessage
        """
        return self._reply_message

    @reply_message.setter
    def reply_message(self, reply_message: 'ConversationContentReceivedReplyMessage') -> None:
        """
        Sets the reply_message of this ConversationContentForm.
        The reply message after the user has filled out the form received.

        :param reply_message: The reply_message of this ConversationContentForm.
        :type: ConversationContentReceivedReplyMessage
        """
        

        self._reply_message = reply_message

    @property
    def show_summary(self) -> bool:
        """
        Gets the show_summary of this ConversationContentForm.
        Show summary at end of form submission.

        :return: The show_summary of this ConversationContentForm.
        :rtype: bool
        """
        return self._show_summary

    @show_summary.setter
    def show_summary(self, show_summary: bool) -> None:
        """
        Sets the show_summary of this ConversationContentForm.
        Show summary at end of form submission.

        :param show_summary: The show_summary of this ConversationContentForm.
        :type: bool
        """
        

        self._show_summary = show_summary

    @property
    def response(self) -> List['ConversationFormResponseComponent']:
        """
        Gets the response of this ConversationContentForm.
        Content of the payload included in the Form response.

        :return: The response of this ConversationContentForm.
        :rtype: list[ConversationFormResponseComponent]
        """
        return self._response

    @response.setter
    def response(self, response: List['ConversationFormResponseComponent']) -> None:
        """
        Sets the response of this ConversationContentForm.
        Content of the payload included in the Form response.

        :param response: The response of this ConversationContentForm.
        :type: list[ConversationFormResponseComponent]
        """
        

        self._response = response

    @property
    def originating_message_id(self) -> str:
        """
        Gets the originating_message_id of this ConversationContentForm.
        Reference to the ID of the original message.

        :return: The originating_message_id of this ConversationContentForm.
        :rtype: str
        """
        return self._originating_message_id

    @originating_message_id.setter
    def originating_message_id(self, originating_message_id: str) -> None:
        """
        Sets the originating_message_id of this ConversationContentForm.
        Reference to the ID of the original message.

        :param originating_message_id: The originating_message_id of this ConversationContentForm.
        :type: str
        """
        

        self._originating_message_id = originating_message_id

    @property
    def canned_response_id(self) -> str:
        """
        Gets the canned_response_id of this ConversationContentForm.
        The id of the canned response which was used to create the form.

        :return: The canned_response_id of this ConversationContentForm.
        :rtype: str
        """
        return self._canned_response_id

    @canned_response_id.setter
    def canned_response_id(self, canned_response_id: str) -> None:
        """
        Sets the canned_response_id of this ConversationContentForm.
        The id of the canned response which was used to create the form.

        :param canned_response_id: The canned_response_id of this ConversationContentForm.
        :type: str
        """
        

        self._canned_response_id = canned_response_id

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

