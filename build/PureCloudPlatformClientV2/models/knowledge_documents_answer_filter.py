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


class KnowledgeDocumentsAnswerFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeDocumentsAnswerFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'str',
            'language': 'str',
            'app_type': 'str',
            'query_type': 'str',
            'search_id': 'str',
            'insert_highlight_into_variation_content': 'bool',
            'answer_mode': 'list[str]',
            'variation_ids': 'list[str]'
        }

        self.attribute_map = {
            'query': 'query',
            'language': 'language',
            'app_type': 'appType',
            'query_type': 'queryType',
            'search_id': 'searchId',
            'insert_highlight_into_variation_content': 'insertHighlightIntoVariationContent',
            'answer_mode': 'answerMode',
            'variation_ids': 'variationIds'
        }

        self._query = None
        self._language = None
        self._app_type = None
        self._query_type = None
        self._search_id = None
        self._insert_highlight_into_variation_content = None
        self._answer_mode = None
        self._variation_ids = None

    @property
    def query(self) -> str:
        """
        Gets the query of this KnowledgeDocumentsAnswerFilter.
        The search query.

        :return: The query of this KnowledgeDocumentsAnswerFilter.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str) -> None:
        """
        Sets the query of this KnowledgeDocumentsAnswerFilter.
        The search query.

        :param query: The query of this KnowledgeDocumentsAnswerFilter.
        :type: str
        """
        

        self._query = query

    @property
    def language(self) -> str:
        """
        Gets the language of this KnowledgeDocumentsAnswerFilter.
        The language of the documents.

        :return: The language of this KnowledgeDocumentsAnswerFilter.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this KnowledgeDocumentsAnswerFilter.
        The language of the documents.

        :param language: The language of this KnowledgeDocumentsAnswerFilter.
        :type: str
        """
        if isinstance(language, int):
            language = str(language)
        allowed_values = ["en-US", "en-UK", "en-AU", "en-CA", "en-HK", "en-IN", "en-IE", "en-NZ", "en-PH", "en-SG", "en-ZA", "de-DE", "de-AT", "de-CH", "es-AR", "es-CO", "es-MX", "es-US", "es-ES", "fr-FR", "fr-BE", "fr-CA", "fr-CH", "pt-BR", "pt-PT", "nl-NL", "nl-BE", "it-IT", "ca-ES", "tr-TR", "sv-SE", "fi-FI", "nb-NO", "da-DK", "ja-JP", "ar-AE", "zh-CN", "zh-TW", "zh-HK", "ko-KR", "pl-PL", "hi-IN", "th-TH", "hu-HU", "vi-VN", "uk-UA"]
        if language.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language -> " + language)
            self._language = "outdated_sdk_version"
        else:
            self._language = language

    @property
    def app_type(self) -> str:
        """
        Gets the app_type of this KnowledgeDocumentsAnswerFilter.
        The appType

        :return: The app_type of this KnowledgeDocumentsAnswerFilter.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type: str) -> None:
        """
        Sets the app_type of this KnowledgeDocumentsAnswerFilter.
        The appType

        :param app_type: The app_type of this KnowledgeDocumentsAnswerFilter.
        :type: str
        """
        if isinstance(app_type, int):
            app_type = str(app_type)
        allowed_values = ["Assistant", "BotFlow", "MessengerKnowledgeApp", "SmartAdvisor", "SupportCenter"]
        if app_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for app_type -> " + app_type)
            self._app_type = "outdated_sdk_version"
        else:
            self._app_type = app_type

    @property
    def query_type(self) -> str:
        """
        Gets the query_type of this KnowledgeDocumentsAnswerFilter.
        The query type

        :return: The query_type of this KnowledgeDocumentsAnswerFilter.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this KnowledgeDocumentsAnswerFilter.
        The query type

        :param query_type: The query_type of this KnowledgeDocumentsAnswerFilter.
        :type: str
        """
        if isinstance(query_type, int):
            query_type = str(query_type)
        allowed_values = ["Unknown", "Article", "AutoSearch", "Category", "ManualSearch", "Recommendation", "Suggestion"]
        if query_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_type -> " + query_type)
            self._query_type = "outdated_sdk_version"
        else:
            self._query_type = query_type

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this KnowledgeDocumentsAnswerFilter.
        The search id.

        :return: The search_id of this KnowledgeDocumentsAnswerFilter.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this KnowledgeDocumentsAnswerFilter.
        The search id.

        :param search_id: The search_id of this KnowledgeDocumentsAnswerFilter.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def insert_highlight_into_variation_content(self) -> bool:
        """
        Gets the insert_highlight_into_variation_content of this KnowledgeDocumentsAnswerFilter.
        If specified - insert highlight data into the variation content.

        :return: The insert_highlight_into_variation_content of this KnowledgeDocumentsAnswerFilter.
        :rtype: bool
        """
        return self._insert_highlight_into_variation_content

    @insert_highlight_into_variation_content.setter
    def insert_highlight_into_variation_content(self, insert_highlight_into_variation_content: bool) -> None:
        """
        Sets the insert_highlight_into_variation_content of this KnowledgeDocumentsAnswerFilter.
        If specified - insert highlight data into the variation content.

        :param insert_highlight_into_variation_content: The insert_highlight_into_variation_content of this KnowledgeDocumentsAnswerFilter.
        :type: bool
        """
        

        self._insert_highlight_into_variation_content = insert_highlight_into_variation_content

    @property
    def answer_mode(self) -> List[str]:
        """
        Gets the answer_mode of this KnowledgeDocumentsAnswerFilter.
        Allows extracted answers from an article (AnswerHighlight) and/or AI-generated answers (AnswerGeneration). Default mode: AnswerHighlight

        :return: The answer_mode of this KnowledgeDocumentsAnswerFilter.
        :rtype: list[str]
        """
        return self._answer_mode

    @answer_mode.setter
    def answer_mode(self, answer_mode: List[str]) -> None:
        """
        Sets the answer_mode of this KnowledgeDocumentsAnswerFilter.
        Allows extracted answers from an article (AnswerHighlight) and/or AI-generated answers (AnswerGeneration). Default mode: AnswerHighlight

        :param answer_mode: The answer_mode of this KnowledgeDocumentsAnswerFilter.
        :type: list[str]
        """
        

        self._answer_mode = answer_mode

    @property
    def variation_ids(self) -> List[str]:
        """
        Gets the variation_ids of this KnowledgeDocumentsAnswerFilter.
        The variation Ids to answer.

        :return: The variation_ids of this KnowledgeDocumentsAnswerFilter.
        :rtype: list[str]
        """
        return self._variation_ids

    @variation_ids.setter
    def variation_ids(self, variation_ids: List[str]) -> None:
        """
        Sets the variation_ids of this KnowledgeDocumentsAnswerFilter.
        The variation Ids to answer.

        :param variation_ids: The variation_ids of this KnowledgeDocumentsAnswerFilter.
        :type: list[str]
        """
        

        self._variation_ids = variation_ids

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
