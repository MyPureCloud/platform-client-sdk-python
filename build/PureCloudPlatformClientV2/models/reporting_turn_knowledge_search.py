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

class ReportingTurnKnowledgeSearch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ReportingTurnKnowledgeSearch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'search_id': 'str',
            'documents': 'list[ReportingTurnKnowledgeDocument]',
            'query': 'str'
        }

        self.attribute_map = {
            'search_id': 'searchId',
            'documents': 'documents',
            'query': 'query'
        }

        self._search_id = None
        self._documents = None
        self._query = None

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this ReportingTurnKnowledgeSearch.
        The ID of this knowledge search.

        :return: The search_id of this ReportingTurnKnowledgeSearch.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this ReportingTurnKnowledgeSearch.
        The ID of this knowledge search.

        :param search_id: The search_id of this ReportingTurnKnowledgeSearch.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def documents(self) -> List['ReportingTurnKnowledgeDocument']:
        """
        Gets the documents of this ReportingTurnKnowledgeSearch.
        The list of search documents captured during this reporting turn.

        :return: The documents of this ReportingTurnKnowledgeSearch.
        :rtype: list[ReportingTurnKnowledgeDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents: List['ReportingTurnKnowledgeDocument']) -> None:
        """
        Sets the documents of this ReportingTurnKnowledgeSearch.
        The list of search documents captured during this reporting turn.

        :param documents: The documents of this ReportingTurnKnowledgeSearch.
        :type: list[ReportingTurnKnowledgeDocument]
        """
        

        self._documents = documents

    @property
    def query(self) -> str:
        """
        Gets the query of this ReportingTurnKnowledgeSearch.
        The search query that was used to search the Knowledge Base documents for a matching question.

        :return: The query of this ReportingTurnKnowledgeSearch.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str) -> None:
        """
        Sets the query of this ReportingTurnKnowledgeSearch.
        The search query that was used to search the Knowledge Base documents for a matching question.

        :param query: The query of this ReportingTurnKnowledgeSearch.
        :type: str
        """
        

        self._query = query

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

