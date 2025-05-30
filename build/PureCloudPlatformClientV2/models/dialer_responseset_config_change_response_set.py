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
    from . import DialerResponsesetConfigChangeReaction

class DialerResponsesetConfigChangeResponseSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerResponsesetConfigChangeResponseSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'responses': 'dict(str, DialerResponsesetConfigChangeReaction)',
            'beep_detection_enabled': 'bool',
            'additional_properties': 'dict(str, object)',
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int'
        }

        self.attribute_map = {
            'responses': 'responses',
            'beep_detection_enabled': 'beepDetectionEnabled',
            'additional_properties': 'additionalProperties',
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version'
        }

        self._responses = None
        self._beep_detection_enabled = None
        self._additional_properties = None
        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None

    @property
    def responses(self) -> Dict[str, 'DialerResponsesetConfigChangeReaction']:
        """
        Gets the responses of this DialerResponsesetConfigChangeResponseSet.
        Map of disposition identifiers to reactions. For example: {\"disposition.classification.callable.person\": {\"reactionType\": \"transfer\"}}

        :return: The responses of this DialerResponsesetConfigChangeResponseSet.
        :rtype: dict(str, DialerResponsesetConfigChangeReaction)
        """
        return self._responses

    @responses.setter
    def responses(self, responses: Dict[str, 'DialerResponsesetConfigChangeReaction']) -> None:
        """
        Sets the responses of this DialerResponsesetConfigChangeResponseSet.
        Map of disposition identifiers to reactions. For example: {\"disposition.classification.callable.person\": {\"reactionType\": \"transfer\"}}

        :param responses: The responses of this DialerResponsesetConfigChangeResponseSet.
        :type: dict(str, DialerResponsesetConfigChangeReaction)
        """
        

        self._responses = responses

    @property
    def beep_detection_enabled(self) -> bool:
        """
        Gets the beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        When beep detection is enabled, answering machine detection will wait for the beep before transferring the call

        :return: The beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        :rtype: bool
        """
        return self._beep_detection_enabled

    @beep_detection_enabled.setter
    def beep_detection_enabled(self, beep_detection_enabled: bool) -> None:
        """
        Sets the beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        When beep detection is enabled, answering machine detection will wait for the beep before transferring the call

        :param beep_detection_enabled: The beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        :type: bool
        """
        

        self._beep_detection_enabled = beep_detection_enabled

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerResponsesetConfigChangeResponseSet.


        :return: The additional_properties of this DialerResponsesetConfigChangeResponseSet.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerResponsesetConfigChangeResponseSet.


        :param additional_properties: The additional_properties of this DialerResponsesetConfigChangeResponseSet.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def id(self) -> str:
        """
        Gets the id of this DialerResponsesetConfigChangeResponseSet.
        The globally unique identifier for the object.

        :return: The id of this DialerResponsesetConfigChangeResponseSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DialerResponsesetConfigChangeResponseSet.
        The globally unique identifier for the object.

        :param id: The id of this DialerResponsesetConfigChangeResponseSet.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DialerResponsesetConfigChangeResponseSet.
        The UI-visible name of the object

        :return: The name of this DialerResponsesetConfigChangeResponseSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DialerResponsesetConfigChangeResponseSet.
        The UI-visible name of the object

        :param name: The name of this DialerResponsesetConfigChangeResponseSet.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this DialerResponsesetConfigChangeResponseSet.
        Creation time of the entity

        :return: The date_created of this DialerResponsesetConfigChangeResponseSet.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this DialerResponsesetConfigChangeResponseSet.
        Creation time of the entity

        :param date_created: The date_created of this DialerResponsesetConfigChangeResponseSet.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this DialerResponsesetConfigChangeResponseSet.
        Last modified time of the entity

        :return: The date_modified of this DialerResponsesetConfigChangeResponseSet.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this DialerResponsesetConfigChangeResponseSet.
        Last modified time of the entity

        :param date_modified: The date_modified of this DialerResponsesetConfigChangeResponseSet.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this DialerResponsesetConfigChangeResponseSet.
        Required for updates, must match the version number of the most recent update

        :return: The version of this DialerResponsesetConfigChangeResponseSet.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this DialerResponsesetConfigChangeResponseSet.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this DialerResponsesetConfigChangeResponseSet.
        :type: int
        """
        

        self._version = version

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

