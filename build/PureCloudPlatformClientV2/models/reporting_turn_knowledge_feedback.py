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
    from . import ReportingTurnKnowledgeDocument

class ReportingTurnKnowledgeFeedback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ReportingTurnKnowledgeFeedback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'search_id': 'str',
            'rating': 'int',
            'documents': 'list[ReportingTurnKnowledgeDocument]'
        }

        self.attribute_map = {
            'search_id': 'searchId',
            'rating': 'rating',
            'documents': 'documents'
        }

        self._search_id = None
        self._rating = None
        self._documents = None

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this ReportingTurnKnowledgeFeedback.
        The ID of the original knowledge search that this feedback relates to.

        :return: The search_id of this ReportingTurnKnowledgeFeedback.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this ReportingTurnKnowledgeFeedback.
        The ID of the original knowledge search that this feedback relates to.

        :param search_id: The search_id of this ReportingTurnKnowledgeFeedback.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def rating(self) -> int:
        """
        Gets the rating of this ReportingTurnKnowledgeFeedback.
        The feedback rating for the search (1.0 - 5.0). 1 = Negative, 5 = Positive.

        :return: The rating of this ReportingTurnKnowledgeFeedback.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating: int) -> None:
        """
        Sets the rating of this ReportingTurnKnowledgeFeedback.
        The feedback rating for the search (1.0 - 5.0). 1 = Negative, 5 = Positive.

        :param rating: The rating of this ReportingTurnKnowledgeFeedback.
        :type: int
        """
        

        self._rating = rating

    @property
    def documents(self) -> List['ReportingTurnKnowledgeDocument']:
        """
        Gets the documents of this ReportingTurnKnowledgeFeedback.
        The list of search documents that the feedback applies to.

        :return: The documents of this ReportingTurnKnowledgeFeedback.
        :rtype: list[ReportingTurnKnowledgeDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents: List['ReportingTurnKnowledgeDocument']) -> None:
        """
        Sets the documents of this ReportingTurnKnowledgeFeedback.
        The list of search documents that the feedback applies to.

        :param documents: The documents of this ReportingTurnKnowledgeFeedback.
        :type: list[ReportingTurnKnowledgeDocument]
        """
        

        self._documents = documents

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

