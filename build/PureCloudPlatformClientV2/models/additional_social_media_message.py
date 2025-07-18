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


class AdditionalSocialMediaMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AdditionalSocialMediaMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'text_body': 'str',
            'media_ids': 'list[str]',
            'in_reply_to_message_id': 'str'
        }

        self.attribute_map = {
            'text_body': 'textBody',
            'media_ids': 'mediaIds',
            'in_reply_to_message_id': 'inReplyToMessageId'
        }

        self._text_body = None
        self._media_ids = None
        self._in_reply_to_message_id = None

    @property
    def text_body(self) -> str:
        """
        Gets the text_body of this AdditionalSocialMediaMessage.
        The body of the text message.  Maximum character count is 2000 characters.

        :return: The text_body of this AdditionalSocialMediaMessage.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body: str) -> None:
        """
        Sets the text_body of this AdditionalSocialMediaMessage.
        The body of the text message.  Maximum character count is 2000 characters.

        :param text_body: The text_body of this AdditionalSocialMediaMessage.
        :type: str
        """
        

        self._text_body = text_body

    @property
    def media_ids(self) -> List[str]:
        """
        Gets the media_ids of this AdditionalSocialMediaMessage.
        The media ids associated with the text message. See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

        :return: The media_ids of this AdditionalSocialMediaMessage.
        :rtype: list[str]
        """
        return self._media_ids

    @media_ids.setter
    def media_ids(self, media_ids: List[str]) -> None:
        """
        Sets the media_ids of this AdditionalSocialMediaMessage.
        The media ids associated with the text message. See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

        :param media_ids: The media_ids of this AdditionalSocialMediaMessage.
        :type: list[str]
        """
        

        self._media_ids = media_ids

    @property
    def in_reply_to_message_id(self) -> str:
        """
        Gets the in_reply_to_message_id of this AdditionalSocialMediaMessage.
        The ID of the message to which this request is replying.

        :return: The in_reply_to_message_id of this AdditionalSocialMediaMessage.
        :rtype: str
        """
        return self._in_reply_to_message_id

    @in_reply_to_message_id.setter
    def in_reply_to_message_id(self, in_reply_to_message_id: str) -> None:
        """
        Sets the in_reply_to_message_id of this AdditionalSocialMediaMessage.
        The ID of the message to which this request is replying.

        :param in_reply_to_message_id: The in_reply_to_message_id of this AdditionalSocialMediaMessage.
        :type: str
        """
        

        self._in_reply_to_message_id = in_reply_to_message_id

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

