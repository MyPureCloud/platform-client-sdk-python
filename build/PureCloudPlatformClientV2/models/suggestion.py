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
    from . import AddressableEntityRef
    from . import Article
    from . import Faq
    from . import SuggestionCannedResponse
    from . import SuggestionContext
    from . import SuggestionKnowledgeArticle
    from . import SuggestionKnowledgeSearch
    from . import SuggestionScript

class Suggestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Suggestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'faq': 'Faq',
            'article': 'Article',
            'date_created': 'datetime',
            'answer_record_id': 'str',
            'trigger_type': 'str',
            'context': 'SuggestionContext',
            'state': 'str',
            'knowledge_search': 'SuggestionKnowledgeSearch',
            'knowledge_article': 'SuggestionKnowledgeArticle',
            'canned_response': 'SuggestionCannedResponse',
            'script': 'SuggestionScript',
            'self_uri': 'str',
            'conversation': 'AddressableEntityRef',
            'assistant': 'AddressableEntityRef'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'faq': 'faq',
            'article': 'article',
            'date_created': 'dateCreated',
            'answer_record_id': 'answerRecordId',
            'trigger_type': 'triggerType',
            'context': 'context',
            'state': 'state',
            'knowledge_search': 'knowledgeSearch',
            'knowledge_article': 'knowledgeArticle',
            'canned_response': 'cannedResponse',
            'script': 'script',
            'self_uri': 'selfUri',
            'conversation': 'conversation',
            'assistant': 'assistant'
        }

        self._id = None
        self._type = None
        self._faq = None
        self._article = None
        self._date_created = None
        self._answer_record_id = None
        self._trigger_type = None
        self._context = None
        self._state = None
        self._knowledge_search = None
        self._knowledge_article = None
        self._canned_response = None
        self._script = None
        self._self_uri = None
        self._conversation = None
        self._assistant = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Suggestion.
        The globally unique identifier for the object.

        :return: The id of this Suggestion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Suggestion.
        The globally unique identifier for the object.

        :param id: The id of this Suggestion.
        :type: str
        """
        

        self._id = id

    @property
    def type(self) -> str:
        """
        Gets the type of this Suggestion.
        The type of the documents for which the suggestion is.

        :return: The type of this Suggestion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Suggestion.
        The type of the documents for which the suggestion is.

        :param type: The type of this Suggestion.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Faq", "Article", "KnowledgeArticle", "KnowledgeSearch", "CannedResponse", "Script"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def faq(self) -> 'Faq':
        """
        Gets the faq of this Suggestion.
        The Faq from the knowledgebase that was provided as the suggestion.

        :return: The faq of this Suggestion.
        :rtype: Faq
        """
        return self._faq

    @faq.setter
    def faq(self, faq: 'Faq') -> None:
        """
        Sets the faq of this Suggestion.
        The Faq from the knowledgebase that was provided as the suggestion.

        :param faq: The faq of this Suggestion.
        :type: Faq
        """
        

        self._faq = faq

    @property
    def article(self) -> 'Article':
        """
        Gets the article of this Suggestion.
        The article from the knowledgebase that was provided as the suggestion.

        :return: The article of this Suggestion.
        :rtype: Article
        """
        return self._article

    @article.setter
    def article(self, article: 'Article') -> None:
        """
        Sets the article of this Suggestion.
        The article from the knowledgebase that was provided as the suggestion.

        :param article: The article of this Suggestion.
        :type: Article
        """
        

        self._article = article

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Suggestion.
        Date when the suggestion was created. For example: yyyy-MM-ddTHH:mm:ss.SSZ. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Suggestion.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Suggestion.
        Date when the suggestion was created. For example: yyyy-MM-ddTHH:mm:ss.SSZ. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Suggestion.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def answer_record_id(self) -> str:
        """
        Gets the answer_record_id of this Suggestion.
        The ID of the knowledge search that provided the suggestion.

        :return: The answer_record_id of this Suggestion.
        :rtype: str
        """
        return self._answer_record_id

    @answer_record_id.setter
    def answer_record_id(self, answer_record_id: str) -> None:
        """
        Sets the answer_record_id of this Suggestion.
        The ID of the knowledge search that provided the suggestion.

        :param answer_record_id: The answer_record_id of this Suggestion.
        :type: str
        """
        

        self._answer_record_id = answer_record_id

    @property
    def trigger_type(self) -> str:
        """
        Gets the trigger_type of this Suggestion.
        The trigger type of the suggestion.

        :return: The trigger_type of this Suggestion.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type: str) -> None:
        """
        Sets the trigger_type of this Suggestion.
        The trigger type of the suggestion.

        :param trigger_type: The trigger_type of this Suggestion.
        :type: str
        """
        if isinstance(trigger_type, int):
            trigger_type = str(trigger_type)
        allowed_values = ["Unknown", "Fallback", "ConversationStart", "ConversationTransfer", "ConversationEnd", "Intent"]
        if trigger_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for trigger_type -> " + trigger_type)
            self._trigger_type = "outdated_sdk_version"
        else:
            self._trigger_type = trigger_type

    @property
    def context(self) -> 'SuggestionContext':
        """
        Gets the context of this Suggestion.
        The conversation context in which the suggestion was raised.

        :return: The context of this Suggestion.
        :rtype: SuggestionContext
        """
        return self._context

    @context.setter
    def context(self, context: 'SuggestionContext') -> None:
        """
        Sets the context of this Suggestion.
        The conversation context in which the suggestion was raised.

        :param context: The context of this Suggestion.
        :type: SuggestionContext
        """
        

        self._context = context

    @property
    def state(self) -> str:
        """
        Gets the state of this Suggestion.
        The state of the suggestion.

        :return: The state of this Suggestion.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Suggestion.
        The state of the suggestion.

        :param state: The state of this Suggestion.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Suggested", "Accepted", "Dismissed", "Failed"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def knowledge_search(self) -> 'SuggestionKnowledgeSearch':
        """
        Gets the knowledge_search of this Suggestion.
        The suggested knowledge search result that was provided as the suggestion.

        :return: The knowledge_search of this Suggestion.
        :rtype: SuggestionKnowledgeSearch
        """
        return self._knowledge_search

    @knowledge_search.setter
    def knowledge_search(self, knowledge_search: 'SuggestionKnowledgeSearch') -> None:
        """
        Sets the knowledge_search of this Suggestion.
        The suggested knowledge search result that was provided as the suggestion.

        :param knowledge_search: The knowledge_search of this Suggestion.
        :type: SuggestionKnowledgeSearch
        """
        

        self._knowledge_search = knowledge_search

    @property
    def knowledge_article(self) -> 'SuggestionKnowledgeArticle':
        """
        Gets the knowledge_article of this Suggestion.
        The suggested knowledge article that was provided as the suggestion.

        :return: The knowledge_article of this Suggestion.
        :rtype: SuggestionKnowledgeArticle
        """
        return self._knowledge_article

    @knowledge_article.setter
    def knowledge_article(self, knowledge_article: 'SuggestionKnowledgeArticle') -> None:
        """
        Sets the knowledge_article of this Suggestion.
        The suggested knowledge article that was provided as the suggestion.

        :param knowledge_article: The knowledge_article of this Suggestion.
        :type: SuggestionKnowledgeArticle
        """
        

        self._knowledge_article = knowledge_article

    @property
    def canned_response(self) -> 'SuggestionCannedResponse':
        """
        Gets the canned_response of this Suggestion.
        The suggested canned response that was provided as the suggestion.

        :return: The canned_response of this Suggestion.
        :rtype: SuggestionCannedResponse
        """
        return self._canned_response

    @canned_response.setter
    def canned_response(self, canned_response: 'SuggestionCannedResponse') -> None:
        """
        Sets the canned_response of this Suggestion.
        The suggested canned response that was provided as the suggestion.

        :param canned_response: The canned_response of this Suggestion.
        :type: SuggestionCannedResponse
        """
        

        self._canned_response = canned_response

    @property
    def script(self) -> 'SuggestionScript':
        """
        Gets the script of this Suggestion.
        The suggested script that was provided as the suggestion.

        :return: The script of this Suggestion.
        :rtype: SuggestionScript
        """
        return self._script

    @script.setter
    def script(self, script: 'SuggestionScript') -> None:
        """
        Sets the script of this Suggestion.
        The suggested script that was provided as the suggestion.

        :param script: The script of this Suggestion.
        :type: SuggestionScript
        """
        

        self._script = script

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Suggestion.
        The URI for this object

        :return: The self_uri of this Suggestion.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Suggestion.
        The URI for this object

        :param self_uri: The self_uri of this Suggestion.
        :type: str
        """
        

        self._self_uri = self_uri

    @property
    def conversation(self) -> 'AddressableEntityRef':
        """
        Gets the conversation of this Suggestion.
        The conversation that the suggestions correspond to.

        :return: The conversation of this Suggestion.
        :rtype: AddressableEntityRef
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'AddressableEntityRef') -> None:
        """
        Sets the conversation of this Suggestion.
        The conversation that the suggestions correspond to.

        :param conversation: The conversation of this Suggestion.
        :type: AddressableEntityRef
        """
        

        self._conversation = conversation

    @property
    def assistant(self) -> 'AddressableEntityRef':
        """
        Gets the assistant of this Suggestion.
        The assistant that was used to provide the suggestions.

        :return: The assistant of this Suggestion.
        :rtype: AddressableEntityRef
        """
        return self._assistant

    @assistant.setter
    def assistant(self, assistant: 'AddressableEntityRef') -> None:
        """
        Sets the assistant of this Suggestion.
        The assistant that was used to provide the suggestions.

        :param assistant: The assistant of this Suggestion.
        :type: AddressableEntityRef
        """
        

        self._assistant = assistant

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
