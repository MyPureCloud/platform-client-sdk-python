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

class QueueConversationSocialExpressionEventTopicErrorDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationSocialExpressionEventTopicErrorDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'int',
            'code': 'str',
            'message': 'str',
            'message_with_params': 'str',
            'message_params': 'dict(str, str)',
            'context_id': 'str',
            'uri': 'str',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'status': 'status',
            'code': 'code',
            'message': 'message',
            'message_with_params': 'messageWithParams',
            'message_params': 'messageParams',
            'context_id': 'contextId',
            'uri': 'uri',
            'additional_properties': 'additionalProperties'
        }

        self._status = None
        self._code = None
        self._message = None
        self._message_with_params = None
        self._message_params = None
        self._context_id = None
        self._uri = None
        self._additional_properties = None

    @property
    def status(self):
        """
        Gets the status of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The status of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param status: The status of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: int
        """
        
        self._status = status

    @property
    def code(self):
        """
        Gets the code of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The code of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param code: The code of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: str
        """
        
        self._code = code

    @property
    def message(self):
        """
        Gets the message of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The message of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param message: The message of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: str
        """
        
        self._message = message

    @property
    def message_with_params(self):
        """
        Gets the message_with_params of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The message_with_params of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: str
        """
        return self._message_with_params

    @message_with_params.setter
    def message_with_params(self, message_with_params):
        """
        Sets the message_with_params of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param message_with_params: The message_with_params of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: str
        """
        
        self._message_with_params = message_with_params

    @property
    def message_params(self):
        """
        Gets the message_params of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The message_params of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: dict(str, str)
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params):
        """
        Sets the message_params of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param message_params: The message_params of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: dict(str, str)
        """
        
        self._message_params = message_params

    @property
    def context_id(self):
        """
        Gets the context_id of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The context_id of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param context_id: The context_id of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: str
        """
        
        self._context_id = context_id

    @property
    def uri(self):
        """
        Gets the uri of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The uri of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param uri: The uri of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: str
        """
        
        self._uri = uri

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :return: The additional_properties of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationSocialExpressionEventTopicErrorDetails.


        :param additional_properties: The additional_properties of this QueueConversationSocialExpressionEventTopicErrorDetails.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

