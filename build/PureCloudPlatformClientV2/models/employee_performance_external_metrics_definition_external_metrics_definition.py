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


class EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'unit': 'str',
            'unit_definition': 'str',
            'precision': 'int',
            'default_objective_type': 'str',
            'retention_months': 'int',
            'enabled': 'bool',
            'in_use': 'bool',
            'date_last_refreshed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'unit': 'unit',
            'unit_definition': 'unitDefinition',
            'precision': 'precision',
            'default_objective_type': 'defaultObjectiveType',
            'retention_months': 'retentionMonths',
            'enabled': 'enabled',
            'in_use': 'inUse',
            'date_last_refreshed': 'dateLastRefreshed'
        }

        self._id = None
        self._name = None
        self._unit = None
        self._unit_definition = None
        self._precision = None
        self._default_objective_type = None
        self._retention_months = None
        self._enabled = None
        self._in_use = None
        self._date_last_refreshed = None

    @property
    def id(self) -> str:
        """
        Gets the id of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The id of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param id: The id of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The name of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param name: The name of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: str
        """
        

        self._name = name

    @property
    def unit(self) -> str:
        """
        Gets the unit of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The unit of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str) -> None:
        """
        Sets the unit of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param unit: The unit of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: str
        """
        if isinstance(unit, int):
            unit = str(unit)
        allowed_values = ["Seconds", "Percent", "Number", "Currency", "Unknown"]
        if unit.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for unit -> " + unit)
            self._unit = "outdated_sdk_version"
        else:
            self._unit = unit

    @property
    def unit_definition(self) -> str:
        """
        Gets the unit_definition of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The unit_definition of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: str
        """
        return self._unit_definition

    @unit_definition.setter
    def unit_definition(self, unit_definition: str) -> None:
        """
        Sets the unit_definition of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param unit_definition: The unit_definition of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: str
        """
        

        self._unit_definition = unit_definition

    @property
    def precision(self) -> int:
        """
        Gets the precision of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The precision of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision: int) -> None:
        """
        Sets the precision of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param precision: The precision of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: int
        """
        

        self._precision = precision

    @property
    def default_objective_type(self) -> str:
        """
        Gets the default_objective_type of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The default_objective_type of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: str
        """
        return self._default_objective_type

    @default_objective_type.setter
    def default_objective_type(self, default_objective_type: str) -> None:
        """
        Sets the default_objective_type of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param default_objective_type: The default_objective_type of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: str
        """
        if isinstance(default_objective_type, int):
            default_objective_type = str(default_objective_type)
        allowed_values = ["HigherIsBetter", "LowerIsBetter", "TargetArea", "Unknown"]
        if default_objective_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for default_objective_type -> " + default_objective_type)
            self._default_objective_type = "outdated_sdk_version"
        else:
            self._default_objective_type = default_objective_type

    @property
    def retention_months(self) -> int:
        """
        Gets the retention_months of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The retention_months of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: int
        """
        return self._retention_months

    @retention_months.setter
    def retention_months(self, retention_months: int) -> None:
        """
        Sets the retention_months of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param retention_months: The retention_months of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: int
        """
        

        self._retention_months = retention_months

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The enabled of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param enabled: The enabled of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def in_use(self) -> bool:
        """
        Gets the in_use of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The in_use of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: bool
        """
        return self._in_use

    @in_use.setter
    def in_use(self, in_use: bool) -> None:
        """
        Sets the in_use of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param in_use: The in_use of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: bool
        """
        

        self._in_use = in_use

    @property
    def date_last_refreshed(self) -> datetime:
        """
        Gets the date_last_refreshed of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :return: The date_last_refreshed of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :rtype: datetime
        """
        return self._date_last_refreshed

    @date_last_refreshed.setter
    def date_last_refreshed(self, date_last_refreshed: datetime) -> None:
        """
        Sets the date_last_refreshed of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.


        :param date_last_refreshed: The date_last_refreshed of this EmployeePerformanceExternalMetricsDefinitionExternalMetricsDefinition.
        :type: datetime
        """
        

        self._date_last_refreshed = date_last_refreshed

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

