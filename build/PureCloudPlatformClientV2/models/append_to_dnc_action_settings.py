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

class AppendToDncActionSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AppendToDncActionSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expire': 'bool',
            'expiration_duration': 'str'
        }

        self.attribute_map = {
            'expire': 'expire',
            'expiration_duration': 'expirationDuration'
        }

        self._expire = None
        self._expiration_duration = None

    @property
    def expire(self):
        """
        Gets the expire of this AppendToDncActionSettings.
        Whether to expire the record appended to the DNC list.

        :return: The expire of this AppendToDncActionSettings.
        :rtype: bool
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """
        Sets the expire of this AppendToDncActionSettings.
        Whether to expire the record appended to the DNC list.

        :param expire: The expire of this AppendToDncActionSettings.
        :type: bool
        """
        

        self._expire = expire

    @property
    def expiration_duration(self):
        """
        Gets the expiration_duration of this AppendToDncActionSettings.
        If 'expire' is set to true, how long to keep the record.

        :return: The expiration_duration of this AppendToDncActionSettings.
        :rtype: str
        """
        return self._expiration_duration

    @expiration_duration.setter
    def expiration_duration(self, expiration_duration):
        """
        Sets the expiration_duration of this AppendToDncActionSettings.
        If 'expire' is set to true, how long to keep the record.

        :param expiration_duration: The expiration_duration of this AppendToDncActionSettings.
        :type: str
        """
        

        self._expiration_duration = expiration_duration

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
