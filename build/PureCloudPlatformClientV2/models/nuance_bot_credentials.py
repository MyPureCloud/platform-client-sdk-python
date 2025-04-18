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


class NuanceBotCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        NuanceBotCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_id': 'str',
            'client_id': 'str',
            'client_secret': 'str',
            'client_secret_provided': 'bool'
        }

        self.attribute_map = {
            'app_id': 'appId',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'client_secret_provided': 'clientSecretProvided'
        }

        self._app_id = None
        self._client_id = None
        self._client_secret = None
        self._client_secret_provided = None

    @property
    def app_id(self) -> str:
        """
        Gets the app_id of this NuanceBotCredentials.
        The application ID

        :return: The app_id of this NuanceBotCredentials.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: str) -> None:
        """
        Sets the app_id of this NuanceBotCredentials.
        The application ID

        :param app_id: The app_id of this NuanceBotCredentials.
        :type: str
        """
        

        self._app_id = app_id

    @property
    def client_id(self) -> str:
        """
        Gets the client_id of this NuanceBotCredentials.
        The credentials client ID

        :return: The client_id of this NuanceBotCredentials.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str) -> None:
        """
        Sets the client_id of this NuanceBotCredentials.
        The credentials client ID

        :param client_id: The client_id of this NuanceBotCredentials.
        :type: str
        """
        

        self._client_id = client_id

    @property
    def client_secret(self) -> str:
        """
        Gets the client_secret of this NuanceBotCredentials.
        The credentials client secret

        :return: The client_secret of this NuanceBotCredentials.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret: str) -> None:
        """
        Sets the client_secret of this NuanceBotCredentials.
        The credentials client secret

        :param client_secret: The client_secret of this NuanceBotCredentials.
        :type: str
        """
        

        self._client_secret = client_secret

    @property
    def client_secret_provided(self) -> bool:
        """
        Gets the client_secret_provided of this NuanceBotCredentials.
        True if the credentials secret is set (but not returned due to security reasons)

        :return: The client_secret_provided of this NuanceBotCredentials.
        :rtype: bool
        """
        return self._client_secret_provided

    @client_secret_provided.setter
    def client_secret_provided(self, client_secret_provided: bool) -> None:
        """
        Sets the client_secret_provided of this NuanceBotCredentials.
        True if the credentials secret is set (but not returned due to security reasons)

        :param client_secret_provided: The client_secret_provided of this NuanceBotCredentials.
        :type: bool
        """
        

        self._client_secret_provided = client_secret_provided

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

