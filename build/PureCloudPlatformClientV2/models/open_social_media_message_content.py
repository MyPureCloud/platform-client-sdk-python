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
    from . import ConversationContentAttachment
    from . import ConversationContentReaction
    from . import ConversationContentText

class OpenSocialMediaMessageContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OpenSocialMediaMessageContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_type': 'str',
            'attachment': 'ConversationContentAttachment',
            'text': 'ConversationContentText',
            'reaction': 'ConversationContentReaction'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'attachment': 'attachment',
            'text': 'text',
            'reaction': 'reaction'
        }

        self._content_type = None
        self._attachment = None
        self._text = None
        self._reaction = None

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this OpenSocialMediaMessageContent.
        Type of this content element.

        :return: The content_type of this OpenSocialMediaMessageContent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this OpenSocialMediaMessageContent.
        Type of this content element.

        :param content_type: The content_type of this OpenSocialMediaMessageContent.
        :type: str
        """
        if isinstance(content_type, int):
            content_type = str(content_type)
        allowed_values = ["Attachment", "Reactions", "Text"]
        if content_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for content_type -> " + content_type)
            self._content_type = "outdated_sdk_version"
        else:
            self._content_type = content_type

    @property
    def attachment(self) -> 'ConversationContentAttachment':
        """
        Gets the attachment of this OpenSocialMediaMessageContent.
        Attachment content.

        :return: The attachment of this OpenSocialMediaMessageContent.
        :rtype: ConversationContentAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment: 'ConversationContentAttachment') -> None:
        """
        Sets the attachment of this OpenSocialMediaMessageContent.
        Attachment content.

        :param attachment: The attachment of this OpenSocialMediaMessageContent.
        :type: ConversationContentAttachment
        """
        

        self._attachment = attachment

    @property
    def text(self) -> 'ConversationContentText':
        """
        Gets the text of this OpenSocialMediaMessageContent.
        A content type containing text.

        :return: The text of this OpenSocialMediaMessageContent.
        :rtype: ConversationContentText
        """
        return self._text

    @text.setter
    def text(self, text: 'ConversationContentText') -> None:
        """
        Sets the text of this OpenSocialMediaMessageContent.
        A content type containing text.

        :param text: The text of this OpenSocialMediaMessageContent.
        :type: ConversationContentText
        """
        

        self._text = text

    @property
    def reaction(self) -> 'ConversationContentReaction':
        """
        Gets the reaction of this OpenSocialMediaMessageContent.
        A set of reactions to a message.

        :return: The reaction of this OpenSocialMediaMessageContent.
        :rtype: ConversationContentReaction
        """
        return self._reaction

    @reaction.setter
    def reaction(self, reaction: 'ConversationContentReaction') -> None:
        """
        Sets the reaction of this OpenSocialMediaMessageContent.
        A set of reactions to a message.

        :param reaction: The reaction of this OpenSocialMediaMessageContent.
        :type: ConversationContentReaction
        """
        

        self._reaction = reaction

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

