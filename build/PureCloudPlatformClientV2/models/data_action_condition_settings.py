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
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import DataActionContactColumnFieldMapping
    from . import DigitalDataActionConditionPredicate

class DataActionConditionSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DataActionConditionSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_action_id': 'str',
            'contact_id_field': 'str',
            'data_not_found_resolution': 'bool',
            'predicates': 'list[DigitalDataActionConditionPredicate]',
            'contact_column_to_data_action_field_mappings': 'list[DataActionContactColumnFieldMapping]'
        }

        self.attribute_map = {
            'data_action_id': 'dataActionId',
            'contact_id_field': 'contactIdField',
            'data_not_found_resolution': 'dataNotFoundResolution',
            'predicates': 'predicates',
            'contact_column_to_data_action_field_mappings': 'contactColumnToDataActionFieldMappings'
        }

        self._data_action_id = None
        self._contact_id_field = None
        self._data_not_found_resolution = None
        self._predicates = None
        self._contact_column_to_data_action_field_mappings = None

    @property
    def data_action_id(self) -> str:
        """
        Gets the data_action_id of this DataActionConditionSettings.
        The Data Action Id to use for this condition.

        :return: The data_action_id of this DataActionConditionSettings.
        :rtype: str
        """
        return self._data_action_id

    @data_action_id.setter
    def data_action_id(self, data_action_id: str) -> None:
        """
        Sets the data_action_id of this DataActionConditionSettings.
        The Data Action Id to use for this condition.

        :param data_action_id: The data_action_id of this DataActionConditionSettings.
        :type: str
        """
        

        self._data_action_id = data_action_id

    @property
    def contact_id_field(self) -> str:
        """
        Gets the contact_id_field of this DataActionConditionSettings.
        The input field from the data action that the contactId will be passed into.

        :return: The contact_id_field of this DataActionConditionSettings.
        :rtype: str
        """
        return self._contact_id_field

    @contact_id_field.setter
    def contact_id_field(self, contact_id_field: str) -> None:
        """
        Sets the contact_id_field of this DataActionConditionSettings.
        The input field from the data action that the contactId will be passed into.

        :param contact_id_field: The contact_id_field of this DataActionConditionSettings.
        :type: str
        """
        

        self._contact_id_field = contact_id_field

    @property
    def data_not_found_resolution(self) -> bool:
        """
        Gets the data_not_found_resolution of this DataActionConditionSettings.
        The result of this condition if the data action returns a result indicating there was no data.

        :return: The data_not_found_resolution of this DataActionConditionSettings.
        :rtype: bool
        """
        return self._data_not_found_resolution

    @data_not_found_resolution.setter
    def data_not_found_resolution(self, data_not_found_resolution: bool) -> None:
        """
        Sets the data_not_found_resolution of this DataActionConditionSettings.
        The result of this condition if the data action returns a result indicating there was no data.

        :param data_not_found_resolution: The data_not_found_resolution of this DataActionConditionSettings.
        :type: bool
        """
        

        self._data_not_found_resolution = data_not_found_resolution

    @property
    def predicates(self) -> List['DigitalDataActionConditionPredicate']:
        """
        Gets the predicates of this DataActionConditionSettings.
        A list of predicates defining the comparisons to use for this condition.

        :return: The predicates of this DataActionConditionSettings.
        :rtype: list[DigitalDataActionConditionPredicate]
        """
        return self._predicates

    @predicates.setter
    def predicates(self, predicates: List['DigitalDataActionConditionPredicate']) -> None:
        """
        Sets the predicates of this DataActionConditionSettings.
        A list of predicates defining the comparisons to use for this condition.

        :param predicates: The predicates of this DataActionConditionSettings.
        :type: list[DigitalDataActionConditionPredicate]
        """
        

        self._predicates = predicates

    @property
    def contact_column_to_data_action_field_mappings(self) -> List['DataActionContactColumnFieldMapping']:
        """
        Gets the contact_column_to_data_action_field_mappings of this DataActionConditionSettings.
        A list of mappings defining which contact data fields will be passed to which data action input fields.

        :return: The contact_column_to_data_action_field_mappings of this DataActionConditionSettings.
        :rtype: list[DataActionContactColumnFieldMapping]
        """
        return self._contact_column_to_data_action_field_mappings

    @contact_column_to_data_action_field_mappings.setter
    def contact_column_to_data_action_field_mappings(self, contact_column_to_data_action_field_mappings: List['DataActionContactColumnFieldMapping']) -> None:
        """
        Sets the contact_column_to_data_action_field_mappings of this DataActionConditionSettings.
        A list of mappings defining which contact data fields will be passed to which data action input fields.

        :param contact_column_to_data_action_field_mappings: The contact_column_to_data_action_field_mappings of this DataActionConditionSettings.
        :type: list[DataActionContactColumnFieldMapping]
        """
        

        self._contact_column_to_data_action_field_mappings = contact_column_to_data_action_field_mappings

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
