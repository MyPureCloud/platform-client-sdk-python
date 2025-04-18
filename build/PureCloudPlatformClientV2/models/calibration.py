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
    from . import ConversationReference
    from . import Evaluation
    from . import EvaluationForm
    from . import User

class Calibration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Calibration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'calibrator': 'User',
            'agent': 'User',
            'conversation': 'ConversationReference',
            'evaluation_form': 'EvaluationForm',
            'context_id': 'str',
            'average_score': 'int',
            'high_score': 'int',
            'low_score': 'int',
            'created_date': 'datetime',
            'evaluations': 'list[Evaluation]',
            'evaluators': 'list[User]',
            'scoring_index': 'Evaluation',
            'expert_evaluator': 'User',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'calibrator': 'calibrator',
            'agent': 'agent',
            'conversation': 'conversation',
            'evaluation_form': 'evaluationForm',
            'context_id': 'contextId',
            'average_score': 'averageScore',
            'high_score': 'highScore',
            'low_score': 'lowScore',
            'created_date': 'createdDate',
            'evaluations': 'evaluations',
            'evaluators': 'evaluators',
            'scoring_index': 'scoringIndex',
            'expert_evaluator': 'expertEvaluator',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._calibrator = None
        self._agent = None
        self._conversation = None
        self._evaluation_form = None
        self._context_id = None
        self._average_score = None
        self._high_score = None
        self._low_score = None
        self._created_date = None
        self._evaluations = None
        self._evaluators = None
        self._scoring_index = None
        self._expert_evaluator = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Calibration.
        The globally unique identifier for the object.

        :return: The id of this Calibration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Calibration.
        The globally unique identifier for the object.

        :param id: The id of this Calibration.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Calibration.


        :return: The name of this Calibration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Calibration.


        :param name: The name of this Calibration.
        :type: str
        """
        

        self._name = name

    @property
    def calibrator(self) -> 'User':
        """
        Gets the calibrator of this Calibration.


        :return: The calibrator of this Calibration.
        :rtype: User
        """
        return self._calibrator

    @calibrator.setter
    def calibrator(self, calibrator: 'User') -> None:
        """
        Sets the calibrator of this Calibration.


        :param calibrator: The calibrator of this Calibration.
        :type: User
        """
        

        self._calibrator = calibrator

    @property
    def agent(self) -> 'User':
        """
        Gets the agent of this Calibration.


        :return: The agent of this Calibration.
        :rtype: User
        """
        return self._agent

    @agent.setter
    def agent(self, agent: 'User') -> None:
        """
        Sets the agent of this Calibration.


        :param agent: The agent of this Calibration.
        :type: User
        """
        

        self._agent = agent

    @property
    def conversation(self) -> 'ConversationReference':
        """
        Gets the conversation of this Calibration.


        :return: The conversation of this Calibration.
        :rtype: ConversationReference
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'ConversationReference') -> None:
        """
        Sets the conversation of this Calibration.


        :param conversation: The conversation of this Calibration.
        :type: ConversationReference
        """
        

        self._conversation = conversation

    @property
    def evaluation_form(self) -> 'EvaluationForm':
        """
        Gets the evaluation_form of this Calibration.


        :return: The evaluation_form of this Calibration.
        :rtype: EvaluationForm
        """
        return self._evaluation_form

    @evaluation_form.setter
    def evaluation_form(self, evaluation_form: 'EvaluationForm') -> None:
        """
        Sets the evaluation_form of this Calibration.


        :param evaluation_form: The evaluation_form of this Calibration.
        :type: EvaluationForm
        """
        

        self._evaluation_form = evaluation_form

    @property
    def context_id(self) -> str:
        """
        Gets the context_id of this Calibration.


        :return: The context_id of this Calibration.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id: str) -> None:
        """
        Sets the context_id of this Calibration.


        :param context_id: The context_id of this Calibration.
        :type: str
        """
        

        self._context_id = context_id

    @property
    def average_score(self) -> int:
        """
        Gets the average_score of this Calibration.


        :return: The average_score of this Calibration.
        :rtype: int
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score: int) -> None:
        """
        Sets the average_score of this Calibration.


        :param average_score: The average_score of this Calibration.
        :type: int
        """
        

        self._average_score = average_score

    @property
    def high_score(self) -> int:
        """
        Gets the high_score of this Calibration.


        :return: The high_score of this Calibration.
        :rtype: int
        """
        return self._high_score

    @high_score.setter
    def high_score(self, high_score: int) -> None:
        """
        Sets the high_score of this Calibration.


        :param high_score: The high_score of this Calibration.
        :type: int
        """
        

        self._high_score = high_score

    @property
    def low_score(self) -> int:
        """
        Gets the low_score of this Calibration.


        :return: The low_score of this Calibration.
        :rtype: int
        """
        return self._low_score

    @low_score.setter
    def low_score(self, low_score: int) -> None:
        """
        Sets the low_score of this Calibration.


        :param low_score: The low_score of this Calibration.
        :type: int
        """
        

        self._low_score = low_score

    @property
    def created_date(self) -> datetime:
        """
        Gets the created_date of this Calibration.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this Calibration.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime) -> None:
        """
        Sets the created_date of this Calibration.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this Calibration.
        :type: datetime
        """
        

        self._created_date = created_date

    @property
    def evaluations(self) -> List['Evaluation']:
        """
        Gets the evaluations of this Calibration.


        :return: The evaluations of this Calibration.
        :rtype: list[Evaluation]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations: List['Evaluation']) -> None:
        """
        Sets the evaluations of this Calibration.


        :param evaluations: The evaluations of this Calibration.
        :type: list[Evaluation]
        """
        

        self._evaluations = evaluations

    @property
    def evaluators(self) -> List['User']:
        """
        Gets the evaluators of this Calibration.


        :return: The evaluators of this Calibration.
        :rtype: list[User]
        """
        return self._evaluators

    @evaluators.setter
    def evaluators(self, evaluators: List['User']) -> None:
        """
        Sets the evaluators of this Calibration.


        :param evaluators: The evaluators of this Calibration.
        :type: list[User]
        """
        

        self._evaluators = evaluators

    @property
    def scoring_index(self) -> 'Evaluation':
        """
        Gets the scoring_index of this Calibration.


        :return: The scoring_index of this Calibration.
        :rtype: Evaluation
        """
        return self._scoring_index

    @scoring_index.setter
    def scoring_index(self, scoring_index: 'Evaluation') -> None:
        """
        Sets the scoring_index of this Calibration.


        :param scoring_index: The scoring_index of this Calibration.
        :type: Evaluation
        """
        

        self._scoring_index = scoring_index

    @property
    def expert_evaluator(self) -> 'User':
        """
        Gets the expert_evaluator of this Calibration.


        :return: The expert_evaluator of this Calibration.
        :rtype: User
        """
        return self._expert_evaluator

    @expert_evaluator.setter
    def expert_evaluator(self, expert_evaluator: 'User') -> None:
        """
        Sets the expert_evaluator of this Calibration.


        :param expert_evaluator: The expert_evaluator of this Calibration.
        :type: User
        """
        

        self._expert_evaluator = expert_evaluator

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Calibration.
        The URI for this object

        :return: The self_uri of this Calibration.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Calibration.
        The URI for this object

        :param self_uri: The self_uri of this Calibration.
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

