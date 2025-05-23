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
    from . import KnowledgeGroupStatistics
    from . import UnansweredGroupSuggestedDocument
    from . import UnansweredPhraseGroup

class UnansweredGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UnansweredGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'label': 'str',
            'phrase_groups': 'list[UnansweredPhraseGroup]',
            'suggested_documents': 'list[UnansweredGroupSuggestedDocument]',
            'statistics': 'KnowledgeGroupStatistics',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'phrase_groups': 'phraseGroups',
            'suggested_documents': 'suggestedDocuments',
            'statistics': 'statistics',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._label = None
        self._phrase_groups = None
        self._suggested_documents = None
        self._statistics = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this UnansweredGroup.
        The globally unique identifier for the object.

        :return: The id of this UnansweredGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this UnansweredGroup.
        The globally unique identifier for the object.

        :param id: The id of this UnansweredGroup.
        :type: str
        """
        

        self._id = id

    @property
    def label(self) -> str:
        """
        Gets the label of this UnansweredGroup.
        Knowledge base unanswered group label

        :return: The label of this UnansweredGroup.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        """
        Sets the label of this UnansweredGroup.
        Knowledge base unanswered group label

        :param label: The label of this UnansweredGroup.
        :type: str
        """
        

        self._label = label

    @property
    def phrase_groups(self) -> List['UnansweredPhraseGroup']:
        """
        Gets the phrase_groups of this UnansweredGroup.
        Represents a list of phrase groups inside an unanswered group

        :return: The phrase_groups of this UnansweredGroup.
        :rtype: list[UnansweredPhraseGroup]
        """
        return self._phrase_groups

    @phrase_groups.setter
    def phrase_groups(self, phrase_groups: List['UnansweredPhraseGroup']) -> None:
        """
        Sets the phrase_groups of this UnansweredGroup.
        Represents a list of phrase groups inside an unanswered group

        :param phrase_groups: The phrase_groups of this UnansweredGroup.
        :type: list[UnansweredPhraseGroup]
        """
        

        self._phrase_groups = phrase_groups

    @property
    def suggested_documents(self) -> List['UnansweredGroupSuggestedDocument']:
        """
        Gets the suggested_documents of this UnansweredGroup.
        Represents a list of documents that may be linked to an unanswered group

        :return: The suggested_documents of this UnansweredGroup.
        :rtype: list[UnansweredGroupSuggestedDocument]
        """
        return self._suggested_documents

    @suggested_documents.setter
    def suggested_documents(self, suggested_documents: List['UnansweredGroupSuggestedDocument']) -> None:
        """
        Sets the suggested_documents of this UnansweredGroup.
        Represents a list of documents that may be linked to an unanswered group

        :param suggested_documents: The suggested_documents of this UnansweredGroup.
        :type: list[UnansweredGroupSuggestedDocument]
        """
        

        self._suggested_documents = suggested_documents

    @property
    def statistics(self) -> 'KnowledgeGroupStatistics':
        """
        Gets the statistics of this UnansweredGroup.
        Statistics object containing the various hit counts for an unanswered group

        :return: The statistics of this UnansweredGroup.
        :rtype: KnowledgeGroupStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics: 'KnowledgeGroupStatistics') -> None:
        """
        Sets the statistics of this UnansweredGroup.
        Statistics object containing the various hit counts for an unanswered group

        :param statistics: The statistics of this UnansweredGroup.
        :type: KnowledgeGroupStatistics
        """
        

        self._statistics = statistics

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this UnansweredGroup.
        The URI for this object

        :return: The self_uri of this UnansweredGroup.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this UnansweredGroup.
        The URI for this object

        :param self_uri: The self_uri of this UnansweredGroup.
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

