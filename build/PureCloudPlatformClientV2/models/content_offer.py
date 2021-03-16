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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ContentOffer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContentOffer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'image_url': 'str',
            'display_mode': 'str',
            'layout_mode': 'str',
            'title': 'str',
            'headline': 'str',
            'body': 'str',
            'call_to_action': 'CallToAction',
            'style': 'ContentOfferStylingConfiguration'
        }

        self.attribute_map = {
            'image_url': 'imageUrl',
            'display_mode': 'displayMode',
            'layout_mode': 'layoutMode',
            'title': 'title',
            'headline': 'headline',
            'body': 'body',
            'call_to_action': 'callToAction',
            'style': 'style'
        }

        self._image_url = None
        self._display_mode = None
        self._layout_mode = None
        self._title = None
        self._headline = None
        self._body = None
        self._call_to_action = None
        self._style = None

    @property
    def image_url(self):
        """
        Gets the image_url of this ContentOffer.
        URL for image displayed to the customer when displaying content offer.

        :return: The image_url of this ContentOffer.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this ContentOffer.
        URL for image displayed to the customer when displaying content offer.

        :param image_url: The image_url of this ContentOffer.
        :type: str
        """
        
        self._image_url = image_url

    @property
    def display_mode(self):
        """
        Gets the display_mode of this ContentOffer.
        The display mode of Genesys Widgets when displaying content offer.

        :return: The display_mode of this ContentOffer.
        :rtype: str
        """
        return self._display_mode

    @display_mode.setter
    def display_mode(self, display_mode):
        """
        Sets the display_mode of this ContentOffer.
        The display mode of Genesys Widgets when displaying content offer.

        :param display_mode: The display_mode of this ContentOffer.
        :type: str
        """
        allowed_values = ["Modal", "Overlay", "Toast"]
        if display_mode.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for display_mode -> " + display_mode)
            self._display_mode = "outdated_sdk_version"
        else:
            self._display_mode = display_mode

    @property
    def layout_mode(self):
        """
        Gets the layout_mode of this ContentOffer.
        The layout mode of the text shown to the user when displaying content offer.

        :return: The layout_mode of this ContentOffer.
        :rtype: str
        """
        return self._layout_mode

    @layout_mode.setter
    def layout_mode(self, layout_mode):
        """
        Sets the layout_mode of this ContentOffer.
        The layout mode of the text shown to the user when displaying content offer.

        :param layout_mode: The layout_mode of this ContentOffer.
        :type: str
        """
        allowed_values = ["TextOnly", "ImageOnly", "LeftText", "RightText", "TopText", "BottomText"]
        if layout_mode.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for layout_mode -> " + layout_mode)
            self._layout_mode = "outdated_sdk_version"
        else:
            self._layout_mode = layout_mode

    @property
    def title(self):
        """
        Gets the title of this ContentOffer.
        Title used in the header of the content offer.

        :return: The title of this ContentOffer.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ContentOffer.
        Title used in the header of the content offer.

        :param title: The title of this ContentOffer.
        :type: str
        """
        
        self._title = title

    @property
    def headline(self):
        """
        Gets the headline of this ContentOffer.
        Headline displayed above the body text of the content offer.

        :return: The headline of this ContentOffer.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this ContentOffer.
        Headline displayed above the body text of the content offer.

        :param headline: The headline of this ContentOffer.
        :type: str
        """
        
        self._headline = headline

    @property
    def body(self):
        """
        Gets the body of this ContentOffer.
        Body text of the content offer.

        :return: The body of this ContentOffer.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this ContentOffer.
        Body text of the content offer.

        :param body: The body of this ContentOffer.
        :type: str
        """
        
        self._body = body

    @property
    def call_to_action(self):
        """
        Gets the call_to_action of this ContentOffer.
        Properties customizing the call to action button on the content offer.

        :return: The call_to_action of this ContentOffer.
        :rtype: CallToAction
        """
        return self._call_to_action

    @call_to_action.setter
    def call_to_action(self, call_to_action):
        """
        Sets the call_to_action of this ContentOffer.
        Properties customizing the call to action button on the content offer.

        :param call_to_action: The call_to_action of this ContentOffer.
        :type: CallToAction
        """
        
        self._call_to_action = call_to_action

    @property
    def style(self):
        """
        Gets the style of this ContentOffer.
        Properties customizing the styling of the content offer.

        :return: The style of this ContentOffer.
        :rtype: ContentOfferStylingConfiguration
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Sets the style of this ContentOffer.
        Properties customizing the styling of the content offer.

        :param style: The style of this ContentOffer.
        :type: ContentOfferStylingConfiguration
        """
        
        self._style = style

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
