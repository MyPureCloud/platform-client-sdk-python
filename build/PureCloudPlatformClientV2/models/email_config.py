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
    from . import DomainEntityRef
    from . import FromEmailAddress
    from . import ReplyToEmailAddress

class EmailConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EmailConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email_columns': 'list[str]',
            'content_template': 'DomainEntityRef',
            'from_address': 'FromEmailAddress',
            'reply_to_address': 'ReplyToEmailAddress'
        }

        self.attribute_map = {
            'email_columns': 'emailColumns',
            'content_template': 'contentTemplate',
            'from_address': 'fromAddress',
            'reply_to_address': 'replyToAddress'
        }

        self._email_columns = None
        self._content_template = None
        self._from_address = None
        self._reply_to_address = None

    @property
    def email_columns(self) -> List[str]:
        """
        Gets the email_columns of this EmailConfig.
        The contact list columns specifying the email address(es) of the contact.

        :return: The email_columns of this EmailConfig.
        :rtype: list[str]
        """
        return self._email_columns

    @email_columns.setter
    def email_columns(self, email_columns: List[str]) -> None:
        """
        Sets the email_columns of this EmailConfig.
        The contact list columns specifying the email address(es) of the contact.

        :param email_columns: The email_columns of this EmailConfig.
        :type: list[str]
        """
        

        self._email_columns = email_columns

    @property
    def content_template(self) -> 'DomainEntityRef':
        """
        Gets the content_template of this EmailConfig.
        The content template used to formulate the email to send to the contact.

        :return: The content_template of this EmailConfig.
        :rtype: DomainEntityRef
        """
        return self._content_template

    @content_template.setter
    def content_template(self, content_template: 'DomainEntityRef') -> None:
        """
        Sets the content_template of this EmailConfig.
        The content template used to formulate the email to send to the contact.

        :param content_template: The content_template of this EmailConfig.
        :type: DomainEntityRef
        """
        

        self._content_template = content_template

    @property
    def from_address(self) -> 'FromEmailAddress':
        """
        Gets the from_address of this EmailConfig.
        The email address that will be used as the sender of the email.

        :return: The from_address of this EmailConfig.
        :rtype: FromEmailAddress
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address: 'FromEmailAddress') -> None:
        """
        Sets the from_address of this EmailConfig.
        The email address that will be used as the sender of the email.

        :param from_address: The from_address of this EmailConfig.
        :type: FromEmailAddress
        """
        

        self._from_address = from_address

    @property
    def reply_to_address(self) -> 'ReplyToEmailAddress':
        """
        Gets the reply_to_address of this EmailConfig.
        The email address from which any reply will be sent.

        :return: The reply_to_address of this EmailConfig.
        :rtype: ReplyToEmailAddress
        """
        return self._reply_to_address

    @reply_to_address.setter
    def reply_to_address(self, reply_to_address: 'ReplyToEmailAddress') -> None:
        """
        Sets the reply_to_address of this EmailConfig.
        The email address from which any reply will be sent.

        :param reply_to_address: The reply_to_address of this EmailConfig.
        :type: ReplyToEmailAddress
        """
        

        self._reply_to_address = reply_to_address

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

