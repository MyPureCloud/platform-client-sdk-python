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


class DashboardUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DashboardUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'dashboard_count': 'int',
            'public_dashboard_count': 'int',
            'state': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'dashboard_count': 'dashboardCount',
            'public_dashboard_count': 'publicDashboardCount',
            'state': 'state',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._dashboard_count = None
        self._public_dashboard_count = None
        self._state = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this DashboardUser.
        The globally unique identifier for the object.

        :return: The id of this DashboardUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DashboardUser.
        The globally unique identifier for the object.

        :param id: The id of this DashboardUser.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DashboardUser.


        :return: The name of this DashboardUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DashboardUser.


        :param name: The name of this DashboardUser.
        :type: str
        """
        

        self._name = name

    @property
    def dashboard_count(self) -> int:
        """
        Gets the dashboard_count of this DashboardUser.
        The count of dashboards for the user

        :return: The dashboard_count of this DashboardUser.
        :rtype: int
        """
        return self._dashboard_count

    @dashboard_count.setter
    def dashboard_count(self, dashboard_count: int) -> None:
        """
        Sets the dashboard_count of this DashboardUser.
        The count of dashboards for the user

        :param dashboard_count: The dashboard_count of this DashboardUser.
        :type: int
        """
        

        self._dashboard_count = dashboard_count

    @property
    def public_dashboard_count(self) -> int:
        """
        Gets the public_dashboard_count of this DashboardUser.
        The count of public dashboards for the user

        :return: The public_dashboard_count of this DashboardUser.
        :rtype: int
        """
        return self._public_dashboard_count

    @public_dashboard_count.setter
    def public_dashboard_count(self, public_dashboard_count: int) -> None:
        """
        Sets the public_dashboard_count of this DashboardUser.
        The count of public dashboards for the user

        :param public_dashboard_count: The public_dashboard_count of this DashboardUser.
        :type: int
        """
        

        self._public_dashboard_count = public_dashboard_count

    @property
    def state(self) -> str:
        """
        Gets the state of this DashboardUser.
        The state of the user

        :return: The state of this DashboardUser.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this DashboardUser.
        The state of the user

        :param state: The state of this DashboardUser.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["active", "inactive"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this DashboardUser.
        The URI for this object

        :return: The self_uri of this DashboardUser.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this DashboardUser.
        The URI for this object

        :param self_uri: The self_uri of this DashboardUser.
        :type: str
        """
        

        self._self_uri = self_uri

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

