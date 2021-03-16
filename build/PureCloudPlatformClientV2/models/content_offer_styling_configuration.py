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

class ContentOfferStylingConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContentOfferStylingConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'position': 'ContentPositionProperties',
            'offer': 'ContentOfferStyleProperties',
            'close_button': 'CloseButtonStyleProperties',
            'cta_button': 'CtaButtonStyleProperties',
            'title': 'TextStyleProperties',
            'headline': 'TextStyleProperties',
            'body': 'TextStyleProperties'
        }

        self.attribute_map = {
            'position': 'position',
            'offer': 'offer',
            'close_button': 'closeButton',
            'cta_button': 'ctaButton',
            'title': 'title',
            'headline': 'headline',
            'body': 'body'
        }

        self._position = None
        self._offer = None
        self._close_button = None
        self._cta_button = None
        self._title = None
        self._headline = None
        self._body = None

    @property
    def position(self):
        """
        Gets the position of this ContentOfferStylingConfiguration.
        Properties for customizing the positioning of the content offer.

        :return: The position of this ContentOfferStylingConfiguration.
        :rtype: ContentPositionProperties
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ContentOfferStylingConfiguration.
        Properties for customizing the positioning of the content offer.

        :param position: The position of this ContentOfferStylingConfiguration.
        :type: ContentPositionProperties
        """
        
        self._position = position

    @property
    def offer(self):
        """
        Gets the offer of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the content offer.

        :return: The offer of this ContentOfferStylingConfiguration.
        :rtype: ContentOfferStyleProperties
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """
        Sets the offer of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the content offer.

        :param offer: The offer of this ContentOfferStylingConfiguration.
        :type: ContentOfferStyleProperties
        """
        
        self._offer = offer

    @property
    def close_button(self):
        """
        Gets the close_button of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the close button.

        :return: The close_button of this ContentOfferStylingConfiguration.
        :rtype: CloseButtonStyleProperties
        """
        return self._close_button

    @close_button.setter
    def close_button(self, close_button):
        """
        Sets the close_button of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the close button.

        :param close_button: The close_button of this ContentOfferStylingConfiguration.
        :type: CloseButtonStyleProperties
        """
        
        self._close_button = close_button

    @property
    def cta_button(self):
        """
        Gets the cta_button of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the CTA button.

        :return: The cta_button of this ContentOfferStylingConfiguration.
        :rtype: CtaButtonStyleProperties
        """
        return self._cta_button

    @cta_button.setter
    def cta_button(self, cta_button):
        """
        Sets the cta_button of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the CTA button.

        :param cta_button: The cta_button of this ContentOfferStylingConfiguration.
        :type: CtaButtonStyleProperties
        """
        
        self._cta_button = cta_button

    @property
    def title(self):
        """
        Gets the title of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the title text.

        :return: The title of this ContentOfferStylingConfiguration.
        :rtype: TextStyleProperties
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the title text.

        :param title: The title of this ContentOfferStylingConfiguration.
        :type: TextStyleProperties
        """
        
        self._title = title

    @property
    def headline(self):
        """
        Gets the headline of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the headline text.

        :return: The headline of this ContentOfferStylingConfiguration.
        :rtype: TextStyleProperties
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the headline text.

        :param headline: The headline of this ContentOfferStylingConfiguration.
        :type: TextStyleProperties
        """
        
        self._headline = headline

    @property
    def body(self):
        """
        Gets the body of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the body text.

        :return: The body of this ContentOfferStylingConfiguration.
        :rtype: TextStyleProperties
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this ContentOfferStylingConfiguration.
        Properties for customizing the appearance of the body text.

        :param body: The body of this ContentOfferStylingConfiguration.
        :type: TextStyleProperties
        """
        
        self._body = body

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
