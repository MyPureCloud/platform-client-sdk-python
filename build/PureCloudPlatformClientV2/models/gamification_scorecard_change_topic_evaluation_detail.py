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


class GamificationScorecardChangeTopicEvaluationDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GamificationScorecardChangeTopicEvaluationDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'evaluation_id': 'str',
            'conversation_id': 'str',
            'conversation_date': 'str',
            'form_name': 'str',
            'points': 'int',
            'max_points': 'int',
            'evaluation_score': 'int',
            'evaluation_score_double': 'float',
            'media_types': 'list[str]'
        }

        self.attribute_map = {
            'evaluation_id': 'evaluationId',
            'conversation_id': 'conversationId',
            'conversation_date': 'conversationDate',
            'form_name': 'formName',
            'points': 'points',
            'max_points': 'maxPoints',
            'evaluation_score': 'evaluationScore',
            'evaluation_score_double': 'evaluationScoreDouble',
            'media_types': 'mediaTypes'
        }

        self._evaluation_id = None
        self._conversation_id = None
        self._conversation_date = None
        self._form_name = None
        self._points = None
        self._max_points = None
        self._evaluation_score = None
        self._evaluation_score_double = None
        self._media_types = None

    @property
    def evaluation_id(self) -> str:
        """
        Gets the evaluation_id of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The evaluation_id of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: str
        """
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, evaluation_id: str) -> None:
        """
        Sets the evaluation_id of this GamificationScorecardChangeTopicEvaluationDetail.


        :param evaluation_id: The evaluation_id of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: str
        """
        

        self._evaluation_id = evaluation_id

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The conversation_id of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this GamificationScorecardChangeTopicEvaluationDetail.


        :param conversation_id: The conversation_id of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def conversation_date(self) -> str:
        """
        Gets the conversation_date of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The conversation_date of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: str
        """
        return self._conversation_date

    @conversation_date.setter
    def conversation_date(self, conversation_date: str) -> None:
        """
        Sets the conversation_date of this GamificationScorecardChangeTopicEvaluationDetail.


        :param conversation_date: The conversation_date of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: str
        """
        

        self._conversation_date = conversation_date

    @property
    def form_name(self) -> str:
        """
        Gets the form_name of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The form_name of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: str
        """
        return self._form_name

    @form_name.setter
    def form_name(self, form_name: str) -> None:
        """
        Sets the form_name of this GamificationScorecardChangeTopicEvaluationDetail.


        :param form_name: The form_name of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: str
        """
        

        self._form_name = form_name

    @property
    def points(self) -> int:
        """
        Gets the points of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The points of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points: int) -> None:
        """
        Sets the points of this GamificationScorecardChangeTopicEvaluationDetail.


        :param points: The points of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: int
        """
        

        self._points = points

    @property
    def max_points(self) -> int:
        """
        Gets the max_points of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The max_points of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: int
        """
        return self._max_points

    @max_points.setter
    def max_points(self, max_points: int) -> None:
        """
        Sets the max_points of this GamificationScorecardChangeTopicEvaluationDetail.


        :param max_points: The max_points of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: int
        """
        

        self._max_points = max_points

    @property
    def evaluation_score(self) -> int:
        """
        Gets the evaluation_score of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The evaluation_score of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: int
        """
        return self._evaluation_score

    @evaluation_score.setter
    def evaluation_score(self, evaluation_score: int) -> None:
        """
        Sets the evaluation_score of this GamificationScorecardChangeTopicEvaluationDetail.


        :param evaluation_score: The evaluation_score of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: int
        """
        

        self._evaluation_score = evaluation_score

    @property
    def evaluation_score_double(self) -> float:
        """
        Gets the evaluation_score_double of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The evaluation_score_double of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: float
        """
        return self._evaluation_score_double

    @evaluation_score_double.setter
    def evaluation_score_double(self, evaluation_score_double: float) -> None:
        """
        Sets the evaluation_score_double of this GamificationScorecardChangeTopicEvaluationDetail.


        :param evaluation_score_double: The evaluation_score_double of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: float
        """
        

        self._evaluation_score_double = evaluation_score_double

    @property
    def media_types(self) -> List[str]:
        """
        Gets the media_types of this GamificationScorecardChangeTopicEvaluationDetail.


        :return: The media_types of this GamificationScorecardChangeTopicEvaluationDetail.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types: List[str]) -> None:
        """
        Sets the media_types of this GamificationScorecardChangeTopicEvaluationDetail.


        :param media_types: The media_types of this GamificationScorecardChangeTopicEvaluationDetail.
        :type: list[str]
        """
        

        self._media_types = media_types

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

