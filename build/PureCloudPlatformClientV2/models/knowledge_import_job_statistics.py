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


class KnowledgeImportJobStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeImportJobStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count_document_import_activity_create': 'int',
            'count_document_import_activity_update': 'int',
            'count_document_state_draft': 'int',
            'count_document_state_published': 'int',
            'count_document_validation_success': 'int',
            'count_document_validation_failure': 'int',
            'count_document_import_success': 'int',
            'count_document_import_failure': 'int',
            'count_category_validation_success': 'int',
            'count_category_validation_failure': 'int',
            'count_category_import_success': 'int',
            'count_category_import_failure': 'int',
            'count_label_validation_success': 'int',
            'count_label_validation_failure': 'int',
            'count_label_import_success': 'int',
            'count_label_import_failure': 'int',
            'migration_detected': 'bool'
        }

        self.attribute_map = {
            'count_document_import_activity_create': 'countDocumentImportActivityCreate',
            'count_document_import_activity_update': 'countDocumentImportActivityUpdate',
            'count_document_state_draft': 'countDocumentStateDraft',
            'count_document_state_published': 'countDocumentStatePublished',
            'count_document_validation_success': 'countDocumentValidationSuccess',
            'count_document_validation_failure': 'countDocumentValidationFailure',
            'count_document_import_success': 'countDocumentImportSuccess',
            'count_document_import_failure': 'countDocumentImportFailure',
            'count_category_validation_success': 'countCategoryValidationSuccess',
            'count_category_validation_failure': 'countCategoryValidationFailure',
            'count_category_import_success': 'countCategoryImportSuccess',
            'count_category_import_failure': 'countCategoryImportFailure',
            'count_label_validation_success': 'countLabelValidationSuccess',
            'count_label_validation_failure': 'countLabelValidationFailure',
            'count_label_import_success': 'countLabelImportSuccess',
            'count_label_import_failure': 'countLabelImportFailure',
            'migration_detected': 'migrationDetected'
        }

        self._count_document_import_activity_create = None
        self._count_document_import_activity_update = None
        self._count_document_state_draft = None
        self._count_document_state_published = None
        self._count_document_validation_success = None
        self._count_document_validation_failure = None
        self._count_document_import_success = None
        self._count_document_import_failure = None
        self._count_category_validation_success = None
        self._count_category_validation_failure = None
        self._count_category_import_success = None
        self._count_category_import_failure = None
        self._count_label_validation_success = None
        self._count_label_validation_failure = None
        self._count_label_import_success = None
        self._count_label_import_failure = None
        self._migration_detected = None

    @property
    def count_document_import_activity_create(self) -> int:
        """
        Gets the count_document_import_activity_create of this KnowledgeImportJobStatistics.
        Number of documents will be created by the import.

        :return: The count_document_import_activity_create of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_import_activity_create

    @count_document_import_activity_create.setter
    def count_document_import_activity_create(self, count_document_import_activity_create: int) -> None:
        """
        Sets the count_document_import_activity_create of this KnowledgeImportJobStatistics.
        Number of documents will be created by the import.

        :param count_document_import_activity_create: The count_document_import_activity_create of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_import_activity_create = count_document_import_activity_create

    @property
    def count_document_import_activity_update(self) -> int:
        """
        Gets the count_document_import_activity_update of this KnowledgeImportJobStatistics.
        Number of documents will be updated by the import.

        :return: The count_document_import_activity_update of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_import_activity_update

    @count_document_import_activity_update.setter
    def count_document_import_activity_update(self, count_document_import_activity_update: int) -> None:
        """
        Sets the count_document_import_activity_update of this KnowledgeImportJobStatistics.
        Number of documents will be updated by the import.

        :param count_document_import_activity_update: The count_document_import_activity_update of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_import_activity_update = count_document_import_activity_update

    @property
    def count_document_state_draft(self) -> int:
        """
        Gets the count_document_state_draft of this KnowledgeImportJobStatistics.
        Number of documents will be imported as draft.

        :return: The count_document_state_draft of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_state_draft

    @count_document_state_draft.setter
    def count_document_state_draft(self, count_document_state_draft: int) -> None:
        """
        Sets the count_document_state_draft of this KnowledgeImportJobStatistics.
        Number of documents will be imported as draft.

        :param count_document_state_draft: The count_document_state_draft of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_state_draft = count_document_state_draft

    @property
    def count_document_state_published(self) -> int:
        """
        Gets the count_document_state_published of this KnowledgeImportJobStatistics.
        Number of documents will be imported as published.

        :return: The count_document_state_published of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_state_published

    @count_document_state_published.setter
    def count_document_state_published(self, count_document_state_published: int) -> None:
        """
        Sets the count_document_state_published of this KnowledgeImportJobStatistics.
        Number of documents will be imported as published.

        :param count_document_state_published: The count_document_state_published of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_state_published = count_document_state_published

    @property
    def count_document_validation_success(self) -> int:
        """
        Gets the count_document_validation_success of this KnowledgeImportJobStatistics.
        Number of documents that validated successfully for import.

        :return: The count_document_validation_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_validation_success

    @count_document_validation_success.setter
    def count_document_validation_success(self, count_document_validation_success: int) -> None:
        """
        Sets the count_document_validation_success of this KnowledgeImportJobStatistics.
        Number of documents that validated successfully for import.

        :param count_document_validation_success: The count_document_validation_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_validation_success = count_document_validation_success

    @property
    def count_document_validation_failure(self) -> int:
        """
        Gets the count_document_validation_failure of this KnowledgeImportJobStatistics.
        Number of documents that failed validation for import.

        :return: The count_document_validation_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_validation_failure

    @count_document_validation_failure.setter
    def count_document_validation_failure(self, count_document_validation_failure: int) -> None:
        """
        Sets the count_document_validation_failure of this KnowledgeImportJobStatistics.
        Number of documents that failed validation for import.

        :param count_document_validation_failure: The count_document_validation_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_validation_failure = count_document_validation_failure

    @property
    def count_document_import_success(self) -> int:
        """
        Gets the count_document_import_success of this KnowledgeImportJobStatistics.
        Number of imported documents.

        :return: The count_document_import_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_import_success

    @count_document_import_success.setter
    def count_document_import_success(self, count_document_import_success: int) -> None:
        """
        Sets the count_document_import_success of this KnowledgeImportJobStatistics.
        Number of imported documents.

        :param count_document_import_success: The count_document_import_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_import_success = count_document_import_success

    @property
    def count_document_import_failure(self) -> int:
        """
        Gets the count_document_import_failure of this KnowledgeImportJobStatistics.
        Number of documents failed to import.

        :return: The count_document_import_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_document_import_failure

    @count_document_import_failure.setter
    def count_document_import_failure(self, count_document_import_failure: int) -> None:
        """
        Sets the count_document_import_failure of this KnowledgeImportJobStatistics.
        Number of documents failed to import.

        :param count_document_import_failure: The count_document_import_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_document_import_failure = count_document_import_failure

    @property
    def count_category_validation_success(self) -> int:
        """
        Gets the count_category_validation_success of this KnowledgeImportJobStatistics.
        Number of categories that validated successfully for import.

        :return: The count_category_validation_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_category_validation_success

    @count_category_validation_success.setter
    def count_category_validation_success(self, count_category_validation_success: int) -> None:
        """
        Sets the count_category_validation_success of this KnowledgeImportJobStatistics.
        Number of categories that validated successfully for import.

        :param count_category_validation_success: The count_category_validation_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_category_validation_success = count_category_validation_success

    @property
    def count_category_validation_failure(self) -> int:
        """
        Gets the count_category_validation_failure of this KnowledgeImportJobStatistics.
        Number of categories that failed validation for import.

        :return: The count_category_validation_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_category_validation_failure

    @count_category_validation_failure.setter
    def count_category_validation_failure(self, count_category_validation_failure: int) -> None:
        """
        Sets the count_category_validation_failure of this KnowledgeImportJobStatistics.
        Number of categories that failed validation for import.

        :param count_category_validation_failure: The count_category_validation_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_category_validation_failure = count_category_validation_failure

    @property
    def count_category_import_success(self) -> int:
        """
        Gets the count_category_import_success of this KnowledgeImportJobStatistics.
        Number of imported categories.

        :return: The count_category_import_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_category_import_success

    @count_category_import_success.setter
    def count_category_import_success(self, count_category_import_success: int) -> None:
        """
        Sets the count_category_import_success of this KnowledgeImportJobStatistics.
        Number of imported categories.

        :param count_category_import_success: The count_category_import_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_category_import_success = count_category_import_success

    @property
    def count_category_import_failure(self) -> int:
        """
        Gets the count_category_import_failure of this KnowledgeImportJobStatistics.
        Number of categories failed to import.

        :return: The count_category_import_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_category_import_failure

    @count_category_import_failure.setter
    def count_category_import_failure(self, count_category_import_failure: int) -> None:
        """
        Sets the count_category_import_failure of this KnowledgeImportJobStatistics.
        Number of categories failed to import.

        :param count_category_import_failure: The count_category_import_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_category_import_failure = count_category_import_failure

    @property
    def count_label_validation_success(self) -> int:
        """
        Gets the count_label_validation_success of this KnowledgeImportJobStatistics.
        Number of labels that validated successfully for import.

        :return: The count_label_validation_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_label_validation_success

    @count_label_validation_success.setter
    def count_label_validation_success(self, count_label_validation_success: int) -> None:
        """
        Sets the count_label_validation_success of this KnowledgeImportJobStatistics.
        Number of labels that validated successfully for import.

        :param count_label_validation_success: The count_label_validation_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_label_validation_success = count_label_validation_success

    @property
    def count_label_validation_failure(self) -> int:
        """
        Gets the count_label_validation_failure of this KnowledgeImportJobStatistics.
        Number of labels that failed validation for import.

        :return: The count_label_validation_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_label_validation_failure

    @count_label_validation_failure.setter
    def count_label_validation_failure(self, count_label_validation_failure: int) -> None:
        """
        Sets the count_label_validation_failure of this KnowledgeImportJobStatistics.
        Number of labels that failed validation for import.

        :param count_label_validation_failure: The count_label_validation_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_label_validation_failure = count_label_validation_failure

    @property
    def count_label_import_success(self) -> int:
        """
        Gets the count_label_import_success of this KnowledgeImportJobStatistics.
        Number of imported labels.

        :return: The count_label_import_success of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_label_import_success

    @count_label_import_success.setter
    def count_label_import_success(self, count_label_import_success: int) -> None:
        """
        Sets the count_label_import_success of this KnowledgeImportJobStatistics.
        Number of imported labels.

        :param count_label_import_success: The count_label_import_success of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_label_import_success = count_label_import_success

    @property
    def count_label_import_failure(self) -> int:
        """
        Gets the count_label_import_failure of this KnowledgeImportJobStatistics.
        Number of labels failed to import.

        :return: The count_label_import_failure of this KnowledgeImportJobStatistics.
        :rtype: int
        """
        return self._count_label_import_failure

    @count_label_import_failure.setter
    def count_label_import_failure(self, count_label_import_failure: int) -> None:
        """
        Sets the count_label_import_failure of this KnowledgeImportJobStatistics.
        Number of labels failed to import.

        :param count_label_import_failure: The count_label_import_failure of this KnowledgeImportJobStatistics.
        :type: int
        """
        

        self._count_label_import_failure = count_label_import_failure

    @property
    def migration_detected(self) -> bool:
        """
        Gets the migration_detected of this KnowledgeImportJobStatistics.
        Shows whether the import treated as migration or not.

        :return: The migration_detected of this KnowledgeImportJobStatistics.
        :rtype: bool
        """
        return self._migration_detected

    @migration_detected.setter
    def migration_detected(self, migration_detected: bool) -> None:
        """
        Sets the migration_detected of this KnowledgeImportJobStatistics.
        Shows whether the import treated as migration or not.

        :param migration_detected: The migration_detected of this KnowledgeImportJobStatistics.
        :type: bool
        """
        

        self._migration_detected = migration_detected

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

