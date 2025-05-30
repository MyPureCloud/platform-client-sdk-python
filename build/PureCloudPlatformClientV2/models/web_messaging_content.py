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
    from . import ContentCard
    from . import ContentCarousel
    from . import ContentDatePicker
    from . import WebMessagingAttachment
    from . import WebMessagingButtonResponse
    from . import WebMessagingGeneric
    from . import WebMessagingQuickReply

class WebMessagingContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WebMessagingContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_type': 'str',
            'attachment': 'WebMessagingAttachment',
            'quick_reply': 'WebMessagingQuickReply',
            'button_response': 'WebMessagingButtonResponse',
            'generic': 'WebMessagingGeneric',
            'card': 'ContentCard',
            'carousel': 'ContentCarousel',
            'date_picker': 'ContentDatePicker'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'attachment': 'attachment',
            'quick_reply': 'quickReply',
            'button_response': 'buttonResponse',
            'generic': 'generic',
            'card': 'card',
            'carousel': 'carousel',
            'date_picker': 'datePicker'
        }

        self._content_type = None
        self._attachment = None
        self._quick_reply = None
        self._button_response = None
        self._generic = None
        self._card = None
        self._carousel = None
        self._date_picker = None

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this WebMessagingContent.
        Type of this content element. If contentType = \"Attachment\" only one item is allowed.

        :return: The content_type of this WebMessagingContent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this WebMessagingContent.
        Type of this content element. If contentType = \"Attachment\" only one item is allowed.

        :param content_type: The content_type of this WebMessagingContent.
        :type: str
        """
        if isinstance(content_type, int):
            content_type = str(content_type)
        allowed_values = ["Attachment", "QuickReply", "ButtonResponse", "GenericTemplate", "Card", "Carousel", "DatePicker"]
        if content_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for content_type -> " + content_type)
            self._content_type = "outdated_sdk_version"
        else:
            self._content_type = content_type

    @property
    def attachment(self) -> 'WebMessagingAttachment':
        """
        Gets the attachment of this WebMessagingContent.
        Attachment content.

        :return: The attachment of this WebMessagingContent.
        :rtype: WebMessagingAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment: 'WebMessagingAttachment') -> None:
        """
        Sets the attachment of this WebMessagingContent.
        Attachment content.

        :param attachment: The attachment of this WebMessagingContent.
        :type: WebMessagingAttachment
        """
        

        self._attachment = attachment

    @property
    def quick_reply(self) -> 'WebMessagingQuickReply':
        """
        Gets the quick_reply of this WebMessagingContent.
        Quick reply content.

        :return: The quick_reply of this WebMessagingContent.
        :rtype: WebMessagingQuickReply
        """
        return self._quick_reply

    @quick_reply.setter
    def quick_reply(self, quick_reply: 'WebMessagingQuickReply') -> None:
        """
        Sets the quick_reply of this WebMessagingContent.
        Quick reply content.

        :param quick_reply: The quick_reply of this WebMessagingContent.
        :type: WebMessagingQuickReply
        """
        

        self._quick_reply = quick_reply

    @property
    def button_response(self) -> 'WebMessagingButtonResponse':
        """
        Gets the button_response of this WebMessagingContent.
        Button response content.

        :return: The button_response of this WebMessagingContent.
        :rtype: WebMessagingButtonResponse
        """
        return self._button_response

    @button_response.setter
    def button_response(self, button_response: 'WebMessagingButtonResponse') -> None:
        """
        Sets the button_response of this WebMessagingContent.
        Button response content.

        :param button_response: The button_response of this WebMessagingContent.
        :type: WebMessagingButtonResponse
        """
        

        self._button_response = button_response

    @property
    def generic(self) -> 'WebMessagingGeneric':
        """
        Gets the generic of this WebMessagingContent.
        Generic content (Deprecated).

        :return: The generic of this WebMessagingContent.
        :rtype: WebMessagingGeneric
        """
        return self._generic

    @generic.setter
    def generic(self, generic: 'WebMessagingGeneric') -> None:
        """
        Sets the generic of this WebMessagingContent.
        Generic content (Deprecated).

        :param generic: The generic of this WebMessagingContent.
        :type: WebMessagingGeneric
        """
        

        self._generic = generic

    @property
    def card(self) -> 'ContentCard':
        """
        Gets the card of this WebMessagingContent.
        Card content

        :return: The card of this WebMessagingContent.
        :rtype: ContentCard
        """
        return self._card

    @card.setter
    def card(self, card: 'ContentCard') -> None:
        """
        Sets the card of this WebMessagingContent.
        Card content

        :param card: The card of this WebMessagingContent.
        :type: ContentCard
        """
        

        self._card = card

    @property
    def carousel(self) -> 'ContentCarousel':
        """
        Gets the carousel of this WebMessagingContent.
        Carousel content

        :return: The carousel of this WebMessagingContent.
        :rtype: ContentCarousel
        """
        return self._carousel

    @carousel.setter
    def carousel(self, carousel: 'ContentCarousel') -> None:
        """
        Sets the carousel of this WebMessagingContent.
        Carousel content

        :param carousel: The carousel of this WebMessagingContent.
        :type: ContentCarousel
        """
        

        self._carousel = carousel

    @property
    def date_picker(self) -> 'ContentDatePicker':
        """
        Gets the date_picker of this WebMessagingContent.
        DatePicker content

        :return: The date_picker of this WebMessagingContent.
        :rtype: ContentDatePicker
        """
        return self._date_picker

    @date_picker.setter
    def date_picker(self, date_picker: 'ContentDatePicker') -> None:
        """
        Sets the date_picker of this WebMessagingContent.
        DatePicker content

        :param date_picker: The date_picker of this WebMessagingContent.
        :type: ContentDatePicker
        """
        

        self._date_picker = date_picker

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

