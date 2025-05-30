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
    from . import Attachment
    from . import EmailAddress

class EmailMessagePreview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EmailMessagePreview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'to': 'list[EmailAddress]',
            'cc': 'list[EmailAddress]',
            'bcc': 'list[EmailAddress]',
            'pcFrom': 'EmailAddress',
            'reply_to': 'EmailAddress',
            'subject': 'str',
            'attachments': 'list[Attachment]',
            'text_body_preview': 'str',
            'time': 'datetime',
            'history_included': 'bool',
            'state': 'str',
            'draft_type': 'str',
            'email_size_bytes': 'int',
            'max_email_size_bytes': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'to': 'to',
            'cc': 'cc',
            'bcc': 'bcc',
            'pcFrom': 'from',
            'reply_to': 'replyTo',
            'subject': 'subject',
            'attachments': 'attachments',
            'text_body_preview': 'textBodyPreview',
            'time': 'time',
            'history_included': 'historyIncluded',
            'state': 'state',
            'draft_type': 'draftType',
            'email_size_bytes': 'emailSizeBytes',
            'max_email_size_bytes': 'maxEmailSizeBytes',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._pcFrom = None
        self._reply_to = None
        self._subject = None
        self._attachments = None
        self._text_body_preview = None
        self._time = None
        self._history_included = None
        self._state = None
        self._draft_type = None
        self._email_size_bytes = None
        self._max_email_size_bytes = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this EmailMessagePreview.
        The globally unique identifier for the object.

        :return: The id of this EmailMessagePreview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this EmailMessagePreview.
        The globally unique identifier for the object.

        :param id: The id of this EmailMessagePreview.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EmailMessagePreview.


        :return: The name of this EmailMessagePreview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EmailMessagePreview.


        :param name: The name of this EmailMessagePreview.
        :type: str
        """
        

        self._name = name

    @property
    def to(self) -> List['EmailAddress']:
        """
        Gets the to of this EmailMessagePreview.
        The recipients of the email message.

        :return: The to of this EmailMessagePreview.
        :rtype: list[EmailAddress]
        """
        return self._to

    @to.setter
    def to(self, to: List['EmailAddress']) -> None:
        """
        Sets the to of this EmailMessagePreview.
        The recipients of the email message.

        :param to: The to of this EmailMessagePreview.
        :type: list[EmailAddress]
        """
        

        self._to = to

    @property
    def cc(self) -> List['EmailAddress']:
        """
        Gets the cc of this EmailMessagePreview.
        The recipients that were copied on the email message.

        :return: The cc of this EmailMessagePreview.
        :rtype: list[EmailAddress]
        """
        return self._cc

    @cc.setter
    def cc(self, cc: List['EmailAddress']) -> None:
        """
        Sets the cc of this EmailMessagePreview.
        The recipients that were copied on the email message.

        :param cc: The cc of this EmailMessagePreview.
        :type: list[EmailAddress]
        """
        

        self._cc = cc

    @property
    def bcc(self) -> List['EmailAddress']:
        """
        Gets the bcc of this EmailMessagePreview.
        The recipients that were blind copied on the email message.

        :return: The bcc of this EmailMessagePreview.
        :rtype: list[EmailAddress]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc: List['EmailAddress']) -> None:
        """
        Sets the bcc of this EmailMessagePreview.
        The recipients that were blind copied on the email message.

        :param bcc: The bcc of this EmailMessagePreview.
        :type: list[EmailAddress]
        """
        

        self._bcc = bcc

    @property
    def pcFrom(self) -> 'EmailAddress':
        """
        Gets the pcFrom of this EmailMessagePreview.
        The sender of the email message.

        :return: The pcFrom of this EmailMessagePreview.
        :rtype: EmailAddress
        """
        return self._pcFrom

    @pcFrom.setter
    def pcFrom(self, pcFrom: 'EmailAddress') -> None:
        """
        Sets the pcFrom of this EmailMessagePreview.
        The sender of the email message.

        :param pcFrom: The pcFrom of this EmailMessagePreview.
        :type: EmailAddress
        """
        

        self._pcFrom = pcFrom

    @property
    def reply_to(self) -> 'EmailAddress':
        """
        Gets the reply_to of this EmailMessagePreview.
        The receiver of the reply email message.

        :return: The reply_to of this EmailMessagePreview.
        :rtype: EmailAddress
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to: 'EmailAddress') -> None:
        """
        Sets the reply_to of this EmailMessagePreview.
        The receiver of the reply email message.

        :param reply_to: The reply_to of this EmailMessagePreview.
        :type: EmailAddress
        """
        

        self._reply_to = reply_to

    @property
    def subject(self) -> str:
        """
        Gets the subject of this EmailMessagePreview.
        The subject of the email message.

        :return: The subject of this EmailMessagePreview.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this EmailMessagePreview.
        The subject of the email message.

        :param subject: The subject of this EmailMessagePreview.
        :type: str
        """
        

        self._subject = subject

    @property
    def attachments(self) -> List['Attachment']:
        """
        Gets the attachments of this EmailMessagePreview.
        The attachments of the email message.

        :return: The attachments of this EmailMessagePreview.
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments: List['Attachment']) -> None:
        """
        Sets the attachments of this EmailMessagePreview.
        The attachments of the email message.

        :param attachments: The attachments of this EmailMessagePreview.
        :type: list[Attachment]
        """
        

        self._attachments = attachments

    @property
    def text_body_preview(self) -> str:
        """
        Gets the text_body_preview of this EmailMessagePreview.
        A truncated version of the textBody

        :return: The text_body_preview of this EmailMessagePreview.
        :rtype: str
        """
        return self._text_body_preview

    @text_body_preview.setter
    def text_body_preview(self, text_body_preview: str) -> None:
        """
        Sets the text_body_preview of this EmailMessagePreview.
        A truncated version of the textBody

        :param text_body_preview: The text_body_preview of this EmailMessagePreview.
        :type: str
        """
        

        self._text_body_preview = text_body_preview

    @property
    def time(self) -> datetime:
        """
        Gets the time of this EmailMessagePreview.
        The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The time of this EmailMessagePreview.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime) -> None:
        """
        Sets the time of this EmailMessagePreview.
        The time when the message was received or sent. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param time: The time of this EmailMessagePreview.
        :type: datetime
        """
        

        self._time = time

    @property
    def history_included(self) -> bool:
        """
        Gets the history_included of this EmailMessagePreview.
        Indicates whether the history of previous emails of the conversation is included within the email bodies of this message.

        :return: The history_included of this EmailMessagePreview.
        :rtype: bool
        """
        return self._history_included

    @history_included.setter
    def history_included(self, history_included: bool) -> None:
        """
        Sets the history_included of this EmailMessagePreview.
        Indicates whether the history of previous emails of the conversation is included within the email bodies of this message.

        :param history_included: The history_included of this EmailMessagePreview.
        :type: bool
        """
        

        self._history_included = history_included

    @property
    def state(self) -> str:
        """
        Gets the state of this EmailMessagePreview.
        The state of the current draft.

        :return: The state of this EmailMessagePreview.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this EmailMessagePreview.
        The state of the current draft.

        :param state: The state of this EmailMessagePreview.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Created", "Ready", "Edited"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def draft_type(self) -> str:
        """
        Gets the draft_type of this EmailMessagePreview.
        The type of draft that need to be treated.

        :return: The draft_type of this EmailMessagePreview.
        :rtype: str
        """
        return self._draft_type

    @draft_type.setter
    def draft_type(self, draft_type: str) -> None:
        """
        Sets the draft_type of this EmailMessagePreview.
        The type of draft that need to be treated.

        :param draft_type: The draft_type of this EmailMessagePreview.
        :type: str
        """
        if isinstance(draft_type, int):
            draft_type = str(draft_type)
        allowed_values = ["Reply", "ReplyAll", "Forward"]
        if draft_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for draft_type -> " + draft_type)
            self._draft_type = "outdated_sdk_version"
        else:
            self._draft_type = draft_type

    @property
    def email_size_bytes(self) -> int:
        """
        Gets the email_size_bytes of this EmailMessagePreview.
        Indicates an estimation of the size of the current email as a whole, in its final, ready to be sent form.

        :return: The email_size_bytes of this EmailMessagePreview.
        :rtype: int
        """
        return self._email_size_bytes

    @email_size_bytes.setter
    def email_size_bytes(self, email_size_bytes: int) -> None:
        """
        Sets the email_size_bytes of this EmailMessagePreview.
        Indicates an estimation of the size of the current email as a whole, in its final, ready to be sent form.

        :param email_size_bytes: The email_size_bytes of this EmailMessagePreview.
        :type: int
        """
        

        self._email_size_bytes = email_size_bytes

    @property
    def max_email_size_bytes(self) -> int:
        """
        Gets the max_email_size_bytes of this EmailMessagePreview.
        Indicates the maximum allowed size for an email to be send via SMTP server, based on the email domain configuration

        :return: The max_email_size_bytes of this EmailMessagePreview.
        :rtype: int
        """
        return self._max_email_size_bytes

    @max_email_size_bytes.setter
    def max_email_size_bytes(self, max_email_size_bytes: int) -> None:
        """
        Sets the max_email_size_bytes of this EmailMessagePreview.
        Indicates the maximum allowed size for an email to be send via SMTP server, based on the email domain configuration

        :param max_email_size_bytes: The max_email_size_bytes of this EmailMessagePreview.
        :type: int
        """
        

        self._max_email_size_bytes = max_email_size_bytes

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this EmailMessagePreview.
        The URI for this object

        :return: The self_uri of this EmailMessagePreview.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this EmailMessagePreview.
        The URI for this object

        :param self_uri: The self_uri of this EmailMessagePreview.
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

