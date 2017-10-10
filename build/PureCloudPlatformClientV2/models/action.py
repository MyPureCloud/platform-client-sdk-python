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


class Action(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Action - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'integration_id': 'str',
            'category': 'str',
            'contract': 'ActionContract',
            'version': 'int',
            'secure': 'bool',
            'config': 'ActionConfig',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'integration_id': 'integrationId',
            'category': 'category',
            'contract': 'contract',
            'version': 'version',
            'secure': 'secure',
            'config': 'config',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._integration_id = None
        self._category = None
        self._contract = None
        self._version = None
        self._secure = None
        self._config = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Action.
        The globally unique identifier for the object.

        :return: The id of this Action.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Action.
        The globally unique identifier for the object.

        :param id: The id of this Action.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Action.


        :return: The name of this Action.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Action.


        :param name: The name of this Action.
        :type: str
        """
        
        self._name = name

    @property
    def integration_id(self):
        """
        Gets the integration_id of this Action.
        The ID of the integration for which this action is associated

        :return: The integration_id of this Action.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this Action.
        The ID of the integration for which this action is associated

        :param integration_id: The integration_id of this Action.
        :type: str
        """
        
        self._integration_id = integration_id

    @property
    def category(self):
        """
        Gets the category of this Action.
        Category of Action

        :return: The category of this Action.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Action.
        Category of Action

        :param category: The category of this Action.
        :type: str
        """
        
        self._category = category

    @property
    def contract(self):
        """
        Gets the contract of this Action.
        Action contract

        :return: The contract of this Action.
        :rtype: ActionContract
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """
        Sets the contract of this Action.
        Action contract

        :param contract: The contract of this Action.
        :type: ActionContract
        """
        
        self._contract = contract

    @property
    def version(self):
        """
        Gets the version of this Action.
        Version of this action

        :return: The version of this Action.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Action.
        Version of this action

        :param version: The version of this Action.
        :type: int
        """
        
        self._version = version

    @property
    def secure(self):
        """
        Gets the secure of this Action.
        Indication of whether or not the action is designed to accept sensitive data

        :return: The secure of this Action.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """
        Sets the secure of this Action.
        Indication of whether or not the action is designed to accept sensitive data

        :param secure: The secure of this Action.
        :type: bool
        """
        
        self._secure = secure

    @property
    def config(self):
        """
        Gets the config of this Action.
        Configuration to support request and response processing

        :return: The config of this Action.
        :rtype: ActionConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this Action.
        Configuration to support request and response processing

        :param config: The config of this Action.
        :type: ActionConfig
        """
        
        self._config = config

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Action.
        The URI for this object

        :return: The self_uri of this Action.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Action.
        The URI for this object

        :param self_uri: The self_uri of this Action.
        :type: str
        """
        
        self._self_uri = self_uri

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
