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
    from . import UserReference

class ListedDictionaryFeedback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ListedDictionaryFeedback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'term': 'str',
            'dialect': 'str',
            'boost_value': 'float',
            'source': 'str',
            'date_created': 'datetime',
            'created_by': 'UserReference',
            'date_modified': 'datetime',
            'modified_by': 'UserReference',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'term': 'term',
            'dialect': 'dialect',
            'boost_value': 'boostValue',
            'source': 'source',
            'date_created': 'dateCreated',
            'created_by': 'createdBy',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._term = None
        self._dialect = None
        self._boost_value = None
        self._source = None
        self._date_created = None
        self._created_by = None
        self._date_modified = None
        self._modified_by = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ListedDictionaryFeedback.
        The globally unique identifier for the object.

        :return: The id of this ListedDictionaryFeedback.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ListedDictionaryFeedback.
        The globally unique identifier for the object.

        :param id: The id of this ListedDictionaryFeedback.
        :type: str
        """
        

        self._id = id

    @property
    def term(self) -> str:
        """
        Gets the term of this ListedDictionaryFeedback.
        The dictionary term which needs to be added to dictionary feedback system

        :return: The term of this ListedDictionaryFeedback.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term: str) -> None:
        """
        Sets the term of this ListedDictionaryFeedback.
        The dictionary term which needs to be added to dictionary feedback system

        :param term: The term of this ListedDictionaryFeedback.
        :type: str
        """
        

        self._term = term

    @property
    def dialect(self) -> str:
        """
        Gets the dialect of this ListedDictionaryFeedback.
        The dialect for the given term, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard

        :return: The dialect of this ListedDictionaryFeedback.
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect: str) -> None:
        """
        Sets the dialect of this ListedDictionaryFeedback.
        The dialect for the given term, dialect format is {language}-{country} where language follows ISO 639-1 standard and country follows ISO 3166-1 alpha 2 standard

        :param dialect: The dialect of this ListedDictionaryFeedback.
        :type: str
        """
        

        self._dialect = dialect

    @property
    def boost_value(self) -> float:
        """
        Gets the boost_value of this ListedDictionaryFeedback.
        A weighted value assigned to a phrase. The higher the value, the higher the likelihood that the system will choose the word or phrase from the possible alternatives. Boost range is from 1.0 to 10.0. Default is 2.0

        :return: The boost_value of this ListedDictionaryFeedback.
        :rtype: float
        """
        return self._boost_value

    @boost_value.setter
    def boost_value(self, boost_value: float) -> None:
        """
        Sets the boost_value of this ListedDictionaryFeedback.
        A weighted value assigned to a phrase. The higher the value, the higher the likelihood that the system will choose the word or phrase from the possible alternatives. Boost range is from 1.0 to 10.0. Default is 2.0

        :param boost_value: The boost_value of this ListedDictionaryFeedback.
        :type: float
        """
        

        self._boost_value = boost_value

    @property
    def source(self) -> str:
        """
        Gets the source of this ListedDictionaryFeedback.
        The source of the given dictionary feedback

        :return: The source of this ListedDictionaryFeedback.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        Sets the source of this ListedDictionaryFeedback.
        The source of the given dictionary feedback

        :param source: The source of this ListedDictionaryFeedback.
        :type: str
        """
        if isinstance(source, int):
            source = str(source)
        allowed_values = ["Manual"]
        if source.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for source -> " + source)
            self._source = "outdated_sdk_version"
        else:
            self._source = source

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this ListedDictionaryFeedback.
        The Timestamp when dictionary feedback created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this ListedDictionaryFeedback.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this ListedDictionaryFeedback.
        The Timestamp when dictionary feedback created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this ListedDictionaryFeedback.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def created_by(self) -> 'UserReference':
        """
        Gets the created_by of this ListedDictionaryFeedback.
        The Id of the user who created the dictionary feedback

        :return: The created_by of this ListedDictionaryFeedback.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'UserReference') -> None:
        """
        Sets the created_by of this ListedDictionaryFeedback.
        The Id of the user who created the dictionary feedback

        :param created_by: The created_by of this ListedDictionaryFeedback.
        :type: UserReference
        """
        

        self._created_by = created_by

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this ListedDictionaryFeedback.
        The Timestamp when dictionary feedback modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this ListedDictionaryFeedback.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this ListedDictionaryFeedback.
        The Timestamp when dictionary feedback modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this ListedDictionaryFeedback.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> 'UserReference':
        """
        Gets the modified_by of this ListedDictionaryFeedback.
        The Id of the user who modified the dictionary feedback

        :return: The modified_by of this ListedDictionaryFeedback.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'UserReference') -> None:
        """
        Sets the modified_by of this ListedDictionaryFeedback.
        The Id of the user who modified the dictionary feedback

        :param modified_by: The modified_by of this ListedDictionaryFeedback.
        :type: UserReference
        """
        

        self._modified_by = modified_by

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ListedDictionaryFeedback.
        The URI for this object

        :return: The self_uri of this ListedDictionaryFeedback.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ListedDictionaryFeedback.
        The URI for this object

        :param self_uri: The self_uri of this ListedDictionaryFeedback.
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
