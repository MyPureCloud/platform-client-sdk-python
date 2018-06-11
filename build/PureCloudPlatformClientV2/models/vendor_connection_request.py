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


class VendorConnectionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VendorConnectionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'publisher': 'str',
            'type': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'publisher': 'publisher',
            'type': 'type',
            'name': 'name'
        }

        self._publisher = None
        self._type = None
        self._name = None

    @property
    def publisher(self):
        """
        Gets the publisher of this VendorConnectionRequest.
        Publisher of the integration or connector who registered the new connection. Typically, inin.

        :return: The publisher of this VendorConnectionRequest.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this VendorConnectionRequest.
        Publisher of the integration or connector who registered the new connection. Typically, inin.

        :param publisher: The publisher of this VendorConnectionRequest.
        :type: str
        """
        
        self._publisher = publisher

    @property
    def type(self):
        """
        Gets the type of this VendorConnectionRequest.
        Integration or connector type that registered the new connection. Example, wfm-rta-integration

        :return: The type of this VendorConnectionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VendorConnectionRequest.
        Integration or connector type that registered the new connection. Example, wfm-rta-integration

        :param type: The type of this VendorConnectionRequest.
        :type: str
        """
        
        self._type = type

    @property
    def name(self):
        """
        Gets the name of this VendorConnectionRequest.
        Name of the integration or connector instance that registered the new connection. Example, my-wfm

        :return: The name of this VendorConnectionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VendorConnectionRequest.
        Name of the integration or connector instance that registered the new connection. Example, my-wfm

        :param name: The name of this VendorConnectionRequest.
        :type: str
        """
        
        self._name = name

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
