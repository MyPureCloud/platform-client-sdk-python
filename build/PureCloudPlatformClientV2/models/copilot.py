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
    from . import AnswerGenerationConfig
    from . import KnowledgeAnswerConfig
    from . import NluConfig
    from . import RuleEngineConfig
    from . import SummaryGenerationConfig
    from . import WrapupCodePredictionConfig

class Copilot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Copilot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'live_on_queue': 'bool',
            'default_language': 'str',
            'knowledge_answer_config': 'KnowledgeAnswerConfig',
            'summary_generation_config': 'SummaryGenerationConfig',
            'wrapup_code_prediction_config': 'WrapupCodePredictionConfig',
            'answer_generation_config': 'AnswerGenerationConfig',
            'nlu_engine_type': 'str',
            'nlu_config': 'NluConfig',
            'rule_engine_config': 'RuleEngineConfig',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'live_on_queue': 'liveOnQueue',
            'default_language': 'defaultLanguage',
            'knowledge_answer_config': 'knowledgeAnswerConfig',
            'summary_generation_config': 'summaryGenerationConfig',
            'wrapup_code_prediction_config': 'wrapupCodePredictionConfig',
            'answer_generation_config': 'answerGenerationConfig',
            'nlu_engine_type': 'nluEngineType',
            'nlu_config': 'nluConfig',
            'rule_engine_config': 'ruleEngineConfig',
            'self_uri': 'selfUri'
        }

        self._enabled = None
        self._live_on_queue = None
        self._default_language = None
        self._knowledge_answer_config = None
        self._summary_generation_config = None
        self._wrapup_code_prediction_config = None
        self._answer_generation_config = None
        self._nlu_engine_type = None
        self._nlu_config = None
        self._rule_engine_config = None
        self._self_uri = None

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this Copilot.
        Copilot is enabled.

        :return: The enabled of this Copilot.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this Copilot.
        Copilot is enabled.

        :param enabled: The enabled of this Copilot.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def live_on_queue(self) -> bool:
        """
        Gets the live_on_queue of this Copilot.
        Copilot is live on selected queue.

        :return: The live_on_queue of this Copilot.
        :rtype: bool
        """
        return self._live_on_queue

    @live_on_queue.setter
    def live_on_queue(self, live_on_queue: bool) -> None:
        """
        Sets the live_on_queue of this Copilot.
        Copilot is live on selected queue.

        :param live_on_queue: The live_on_queue of this Copilot.
        :type: bool
        """
        

        self._live_on_queue = live_on_queue

    @property
    def default_language(self) -> str:
        """
        Gets the default_language of this Copilot.
        Copilot default language, e.g. [en-US, es-US, es-ES]. Once set, it can not be modified.

        :return: The default_language of this Copilot.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language: str) -> None:
        """
        Sets the default_language of this Copilot.
        Copilot default language, e.g. [en-US, es-US, es-ES]. Once set, it can not be modified.

        :param default_language: The default_language of this Copilot.
        :type: str
        """
        

        self._default_language = default_language

    @property
    def knowledge_answer_config(self) -> 'KnowledgeAnswerConfig':
        """
        Gets the knowledge_answer_config of this Copilot.
        Knowledge answer configuration.

        :return: The knowledge_answer_config of this Copilot.
        :rtype: KnowledgeAnswerConfig
        """
        return self._knowledge_answer_config

    @knowledge_answer_config.setter
    def knowledge_answer_config(self, knowledge_answer_config: 'KnowledgeAnswerConfig') -> None:
        """
        Sets the knowledge_answer_config of this Copilot.
        Knowledge answer configuration.

        :param knowledge_answer_config: The knowledge_answer_config of this Copilot.
        :type: KnowledgeAnswerConfig
        """
        

        self._knowledge_answer_config = knowledge_answer_config

    @property
    def summary_generation_config(self) -> 'SummaryGenerationConfig':
        """
        Gets the summary_generation_config of this Copilot.
        Copilot generated summary configuration.

        :return: The summary_generation_config of this Copilot.
        :rtype: SummaryGenerationConfig
        """
        return self._summary_generation_config

    @summary_generation_config.setter
    def summary_generation_config(self, summary_generation_config: 'SummaryGenerationConfig') -> None:
        """
        Sets the summary_generation_config of this Copilot.
        Copilot generated summary configuration.

        :param summary_generation_config: The summary_generation_config of this Copilot.
        :type: SummaryGenerationConfig
        """
        

        self._summary_generation_config = summary_generation_config

    @property
    def wrapup_code_prediction_config(self) -> 'WrapupCodePredictionConfig':
        """
        Gets the wrapup_code_prediction_config of this Copilot.
        Copilot generated wrapup code prediction configuration.

        :return: The wrapup_code_prediction_config of this Copilot.
        :rtype: WrapupCodePredictionConfig
        """
        return self._wrapup_code_prediction_config

    @wrapup_code_prediction_config.setter
    def wrapup_code_prediction_config(self, wrapup_code_prediction_config: 'WrapupCodePredictionConfig') -> None:
        """
        Sets the wrapup_code_prediction_config of this Copilot.
        Copilot generated wrapup code prediction configuration.

        :param wrapup_code_prediction_config: The wrapup_code_prediction_config of this Copilot.
        :type: WrapupCodePredictionConfig
        """
        

        self._wrapup_code_prediction_config = wrapup_code_prediction_config

    @property
    def answer_generation_config(self) -> 'AnswerGenerationConfig':
        """
        Gets the answer_generation_config of this Copilot.
        Answer generation configuration.

        :return: The answer_generation_config of this Copilot.
        :rtype: AnswerGenerationConfig
        """
        return self._answer_generation_config

    @answer_generation_config.setter
    def answer_generation_config(self, answer_generation_config: 'AnswerGenerationConfig') -> None:
        """
        Sets the answer_generation_config of this Copilot.
        Answer generation configuration.

        :param answer_generation_config: The answer_generation_config of this Copilot.
        :type: AnswerGenerationConfig
        """
        

        self._answer_generation_config = answer_generation_config

    @property
    def nlu_engine_type(self) -> str:
        """
        Gets the nlu_engine_type of this Copilot.
        Language understanding engine type.

        :return: The nlu_engine_type of this Copilot.
        :rtype: str
        """
        return self._nlu_engine_type

    @nlu_engine_type.setter
    def nlu_engine_type(self, nlu_engine_type: str) -> None:
        """
        Sets the nlu_engine_type of this Copilot.
        Language understanding engine type.

        :param nlu_engine_type: The nlu_engine_type of this Copilot.
        :type: str
        """
        if isinstance(nlu_engine_type, int):
            nlu_engine_type = str(nlu_engine_type)
        allowed_values = ["NluV3"]
        if nlu_engine_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for nlu_engine_type -> " + nlu_engine_type)
            self._nlu_engine_type = "outdated_sdk_version"
        else:
            self._nlu_engine_type = nlu_engine_type

    @property
    def nlu_config(self) -> 'NluConfig':
        """
        Gets the nlu_config of this Copilot.
        NLU configuration.

        :return: The nlu_config of this Copilot.
        :rtype: NluConfig
        """
        return self._nlu_config

    @nlu_config.setter
    def nlu_config(self, nlu_config: 'NluConfig') -> None:
        """
        Sets the nlu_config of this Copilot.
        NLU configuration.

        :param nlu_config: The nlu_config of this Copilot.
        :type: NluConfig
        """
        

        self._nlu_config = nlu_config

    @property
    def rule_engine_config(self) -> 'RuleEngineConfig':
        """
        Gets the rule_engine_config of this Copilot.
        Rule engine configuration.

        :return: The rule_engine_config of this Copilot.
        :rtype: RuleEngineConfig
        """
        return self._rule_engine_config

    @rule_engine_config.setter
    def rule_engine_config(self, rule_engine_config: 'RuleEngineConfig') -> None:
        """
        Sets the rule_engine_config of this Copilot.
        Rule engine configuration.

        :param rule_engine_config: The rule_engine_config of this Copilot.
        :type: RuleEngineConfig
        """
        

        self._rule_engine_config = rule_engine_config

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Copilot.
        The URI for this object

        :return: The self_uri of this Copilot.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Copilot.
        The URI for this object

        :param self_uri: The self_uri of this Copilot.
        :type: str
        """
        

        self._self_uri = self_uri

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
