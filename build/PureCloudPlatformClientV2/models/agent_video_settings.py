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
    from . import BackgroundImageSettings

class AgentVideoSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentVideoSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_camera': 'bool',
            'allow_screen_share': 'bool',
            'background': 'str',
            'background_image': 'BackgroundImageSettings'
        }

        self.attribute_map = {
            'allow_camera': 'allowCamera',
            'allow_screen_share': 'allowScreenShare',
            'background': 'background',
            'background_image': 'backgroundImage'
        }

        self._allow_camera = None
        self._allow_screen_share = None
        self._background = None
        self._background_image = None

    @property
    def allow_camera(self) -> bool:
        """
        Gets the allow_camera of this AgentVideoSettings.
        whether or not agent camera is allowed

        :return: The allow_camera of this AgentVideoSettings.
        :rtype: bool
        """
        return self._allow_camera

    @allow_camera.setter
    def allow_camera(self, allow_camera: bool) -> None:
        """
        Sets the allow_camera of this AgentVideoSettings.
        whether or not agent camera is allowed

        :param allow_camera: The allow_camera of this AgentVideoSettings.
        :type: bool
        """
        

        self._allow_camera = allow_camera

    @property
    def allow_screen_share(self) -> bool:
        """
        Gets the allow_screen_share of this AgentVideoSettings.
        whether or not agent screen share is allowed

        :return: The allow_screen_share of this AgentVideoSettings.
        :rtype: bool
        """
        return self._allow_screen_share

    @allow_screen_share.setter
    def allow_screen_share(self, allow_screen_share: bool) -> None:
        """
        Sets the allow_screen_share of this AgentVideoSettings.
        whether or not agent screen share is allowed

        :param allow_screen_share: The allow_screen_share of this AgentVideoSettings.
        :type: bool
        """
        

        self._allow_screen_share = allow_screen_share

    @property
    def background(self) -> str:
        """
        Gets the background of this AgentVideoSettings.
        background for agent

        :return: The background of this AgentVideoSettings.
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background: str) -> None:
        """
        Sets the background of this AgentVideoSettings.
        background for agent

        :param background: The background of this AgentVideoSettings.
        :type: str
        """
        if isinstance(background, int):
            background = str(background)
        allowed_values = ["BLUR", "NONE", "IMAGE"]
        if background.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for background -> " + background)
            self._background = "outdated_sdk_version"
        else:
            self._background = background

    @property
    def background_image(self) -> 'BackgroundImageSettings':
        """
        Gets the background_image of this AgentVideoSettings.
        background image settings for agent

        :return: The background_image of this AgentVideoSettings.
        :rtype: BackgroundImageSettings
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image: 'BackgroundImageSettings') -> None:
        """
        Sets the background_image of this AgentVideoSettings.
        background image settings for agent

        :param background_image: The background_image of this AgentVideoSettings.
        :type: BackgroundImageSettings
        """
        

        self._background_image = background_image

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

