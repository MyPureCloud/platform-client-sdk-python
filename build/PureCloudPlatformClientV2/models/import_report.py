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

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ImportReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ImportReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[ImportError]',
            'validated': 'ResultCounters',
            'imported': 'ResultCounters',
            'total_documents': 'int'
        }

        self.attribute_map = {
            'errors': 'errors',
            'validated': 'validated',
            'imported': 'imported',
            'total_documents': 'totalDocuments'
        }

        self._errors = None
        self._validated = None
        self._imported = None
        self._total_documents = None

    @property
    def errors(self):
        """
        Gets the errors of this ImportReport.


        :return: The errors of this ImportReport.
        :rtype: list[ImportError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ImportReport.


        :param errors: The errors of this ImportReport.
        :type: list[ImportError]
        """
        
        self._errors = errors

    @property
    def validated(self):
        """
        Gets the validated of this ImportReport.


        :return: The validated of this ImportReport.
        :rtype: ResultCounters
        """
        return self._validated

    @validated.setter
    def validated(self, validated):
        """
        Sets the validated of this ImportReport.


        :param validated: The validated of this ImportReport.
        :type: ResultCounters
        """
        
        self._validated = validated

    @property
    def imported(self):
        """
        Gets the imported of this ImportReport.


        :return: The imported of this ImportReport.
        :rtype: ResultCounters
        """
        return self._imported

    @imported.setter
    def imported(self, imported):
        """
        Sets the imported of this ImportReport.


        :param imported: The imported of this ImportReport.
        :type: ResultCounters
        """
        
        self._imported = imported

    @property
    def total_documents(self):
        """
        Gets the total_documents of this ImportReport.


        :return: The total_documents of this ImportReport.
        :rtype: int
        """
        return self._total_documents

    @total_documents.setter
    def total_documents(self, total_documents):
        """
        Sets the total_documents of this ImportReport.


        :param total_documents: The total_documents of this ImportReport.
        :type: int
        """
        
        self._total_documents = total_documents

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
