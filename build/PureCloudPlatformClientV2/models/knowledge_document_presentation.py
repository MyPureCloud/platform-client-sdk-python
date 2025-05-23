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
    from . import KnowledgeConversationContext
    from . import KnowledgeSearchClientApplication
    from . import PresentedKnowledgeDocument

class KnowledgeDocumentPresentation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeDocumentPresentation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'documents': 'list[PresentedKnowledgeDocument]',
            'search_id': 'str',
            'query_type': 'str',
            'surfacing_method': 'str',
            'session_id': 'str',
            'conversation_context': 'KnowledgeConversationContext',
            'application': 'KnowledgeSearchClientApplication'
        }

        self.attribute_map = {
            'documents': 'documents',
            'search_id': 'searchId',
            'query_type': 'queryType',
            'surfacing_method': 'surfacingMethod',
            'session_id': 'sessionId',
            'conversation_context': 'conversationContext',
            'application': 'application'
        }

        self._documents = None
        self._search_id = None
        self._query_type = None
        self._surfacing_method = None
        self._session_id = None
        self._conversation_context = None
        self._application = None

    @property
    def documents(self) -> List['PresentedKnowledgeDocument']:
        """
        Gets the documents of this KnowledgeDocumentPresentation.
        The presented documents

        :return: The documents of this KnowledgeDocumentPresentation.
        :rtype: list[PresentedKnowledgeDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents: List['PresentedKnowledgeDocument']) -> None:
        """
        Sets the documents of this KnowledgeDocumentPresentation.
        The presented documents

        :param documents: The documents of this KnowledgeDocumentPresentation.
        :type: list[PresentedKnowledgeDocument]
        """
        

        self._documents = documents

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this KnowledgeDocumentPresentation.
        The search that surfaced the documents that were presented.

        :return: The search_id of this KnowledgeDocumentPresentation.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this KnowledgeDocumentPresentation.
        The search that surfaced the documents that were presented.

        :param search_id: The search_id of this KnowledgeDocumentPresentation.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def query_type(self) -> str:
        """
        Gets the query_type of this KnowledgeDocumentPresentation.
        The type of the query that surfaced the documents.

        :return: The query_type of this KnowledgeDocumentPresentation.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this KnowledgeDocumentPresentation.
        The type of the query that surfaced the documents.

        :param query_type: The query_type of this KnowledgeDocumentPresentation.
        :type: str
        """
        if isinstance(query_type, int):
            query_type = str(query_type)
        allowed_values = ["Unknown", "Article", "AutoSearch", "Category", "ManualSearch", "Recommendation", "Suggestion", "ExpandedArticle"]
        if query_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_type -> " + query_type)
            self._query_type = "outdated_sdk_version"
        else:
            self._query_type = query_type

    @property
    def surfacing_method(self) -> str:
        """
        Gets the surfacing_method of this KnowledgeDocumentPresentation.
        The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown.

        :return: The surfacing_method of this KnowledgeDocumentPresentation.
        :rtype: str
        """
        return self._surfacing_method

    @surfacing_method.setter
    def surfacing_method(self, surfacing_method: str) -> None:
        """
        Sets the surfacing_method of this KnowledgeDocumentPresentation.
        The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown.

        :param surfacing_method: The surfacing_method of this KnowledgeDocumentPresentation.
        :type: str
        """
        if isinstance(surfacing_method, int):
            surfacing_method = str(surfacing_method)
        allowed_values = ["Unknown", "Article", "Snippet", "Highlight", "Generative"]
        if surfacing_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for surfacing_method -> " + surfacing_method)
            self._surfacing_method = "outdated_sdk_version"
        else:
            self._surfacing_method = surfacing_method

    @property
    def session_id(self) -> str:
        """
        Gets the session_id of this KnowledgeDocumentPresentation.
        Knowledge session ID.

        :return: The session_id of this KnowledgeDocumentPresentation.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str) -> None:
        """
        Sets the session_id of this KnowledgeDocumentPresentation.
        Knowledge session ID.

        :param session_id: The session_id of this KnowledgeDocumentPresentation.
        :type: str
        """
        

        self._session_id = session_id

    @property
    def conversation_context(self) -> 'KnowledgeConversationContext':
        """
        Gets the conversation_context of this KnowledgeDocumentPresentation.
        Conversation context information if the documents were presented in the context of a conversation.

        :return: The conversation_context of this KnowledgeDocumentPresentation.
        :rtype: KnowledgeConversationContext
        """
        return self._conversation_context

    @conversation_context.setter
    def conversation_context(self, conversation_context: 'KnowledgeConversationContext') -> None:
        """
        Sets the conversation_context of this KnowledgeDocumentPresentation.
        Conversation context information if the documents were presented in the context of a conversation.

        :param conversation_context: The conversation_context of this KnowledgeDocumentPresentation.
        :type: KnowledgeConversationContext
        """
        

        self._conversation_context = conversation_context

    @property
    def application(self) -> 'KnowledgeSearchClientApplication':
        """
        Gets the application of this KnowledgeDocumentPresentation.
        The client application in which the documents were presented.

        :return: The application of this KnowledgeDocumentPresentation.
        :rtype: KnowledgeSearchClientApplication
        """
        return self._application

    @application.setter
    def application(self, application: 'KnowledgeSearchClientApplication') -> None:
        """
        Sets the application of this KnowledgeDocumentPresentation.
        The client application in which the documents were presented.

        :param application: The application of this KnowledgeDocumentPresentation.
        :type: KnowledgeSearchClientApplication
        """
        

        self._application = application

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

