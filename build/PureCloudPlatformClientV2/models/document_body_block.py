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

class DocumentBodyBlock(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentBodyBlock - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'paragraph': 'DocumentBodyParagraph',
            'image': 'DocumentBodyImage',
            'video': 'DocumentBodyVideo',
            'list': 'DocumentBodyList'
        }

        self.attribute_map = {
            'type': 'type',
            'paragraph': 'paragraph',
            'image': 'image',
            'video': 'video',
            'list': 'list'
        }

        self._type = None
        self._paragraph = None
        self._image = None
        self._video = None
        self._list = None

    @property
    def type(self):
        """
        Gets the type of this DocumentBodyBlock.
        The type of the block for the body. This determines which body block object (paragraph, list, video or image) would have a value.

        :return: The type of this DocumentBodyBlock.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DocumentBodyBlock.
        The type of the block for the body. This determines which body block object (paragraph, list, video or image) would have a value.

        :param type: The type of this DocumentBodyBlock.
        :type: str
        """
        allowed_values = ["Paragraph", "Image", "Video", "OrderedList", "UnorderedList"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def paragraph(self):
        """
        Gets the paragraph of this DocumentBodyBlock.
        Paragraph. It must contain a value if the type of the block is Paragraph.

        :return: The paragraph of this DocumentBodyBlock.
        :rtype: DocumentBodyParagraph
        """
        return self._paragraph

    @paragraph.setter
    def paragraph(self, paragraph):
        """
        Sets the paragraph of this DocumentBodyBlock.
        Paragraph. It must contain a value if the type of the block is Paragraph.

        :param paragraph: The paragraph of this DocumentBodyBlock.
        :type: DocumentBodyParagraph
        """
        

        self._paragraph = paragraph

    @property
    def image(self):
        """
        Gets the image of this DocumentBodyBlock.
        Image. It must contain a value if the type of the block is Image.

        :return: The image of this DocumentBodyBlock.
        :rtype: DocumentBodyImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this DocumentBodyBlock.
        Image. It must contain a value if the type of the block is Image.

        :param image: The image of this DocumentBodyBlock.
        :type: DocumentBodyImage
        """
        

        self._image = image

    @property
    def video(self):
        """
        Gets the video of this DocumentBodyBlock.
        Video. It must contain a value if the type of the block is Video.

        :return: The video of this DocumentBodyBlock.
        :rtype: DocumentBodyVideo
        """
        return self._video

    @video.setter
    def video(self, video):
        """
        Sets the video of this DocumentBodyBlock.
        Video. It must contain a value if the type of the block is Video.

        :param video: The video of this DocumentBodyBlock.
        :type: DocumentBodyVideo
        """
        

        self._video = video

    @property
    def list(self):
        """
        Gets the list of this DocumentBodyBlock.
        List. It must contain a value if the type of the block is UnorderedList or OrderedList.

        :return: The list of this DocumentBodyBlock.
        :rtype: DocumentBodyList
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this DocumentBodyBlock.
        List. It must contain a value if the type of the block is UnorderedList or OrderedList.

        :param list: The list of this DocumentBodyBlock.
        :type: DocumentBodyList
        """
        

        self._list = list

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
