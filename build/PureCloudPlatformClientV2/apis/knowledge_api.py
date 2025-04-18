# coding: utf-8

"""
KnowledgeApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

from datetime import datetime
from datetime import date

from ..configuration import Configuration
from ..api_client import ApiClient
from ..utils import deprecated

from typing import List
from typing import Dict
from typing import Any

from ..models import Empty
from ..models import BulkResponse
from ..models import CategoryCreateRequest
from ..models import CategoryListing
from ..models import CategoryResponse
from ..models import CategoryResponseListing
from ..models import CategoryUpdateRequest
from ..models import CreateUploadSourceUrlJobRequest
from ..models import CreateUploadSourceUrlJobResponse
from ..models import DocumentListing
from ..models import DocumentVariationRequest
from ..models import DocumentVariationResponse
from ..models import DocumentVariationResponseListing
from ..models import ErrorBody
from ..models import GetUploadSourceUrlJobStatusResponse
from ..models import GuestCategoryResponseListing
from ..models import ImportStatusRequest
from ..models import KnowledgeAnswerDocumentsResponse
from ..models import KnowledgeBase
from ..models import KnowledgeBaseCreateRequest
from ..models import KnowledgeBaseListing
from ..models import KnowledgeBaseUpdateRequest
from ..models import KnowledgeCategory
from ..models import KnowledgeCategoryRequest
from ..models import KnowledgeDocument
from ..models import KnowledgeDocumentBulkRemoveRequest
from ..models import KnowledgeDocumentBulkRequest
from ..models import KnowledgeDocumentBulkUpdateRequest
from ..models import KnowledgeDocumentBulkVersionAddRequest
from ..models import KnowledgeDocumentContentUpload
from ..models import KnowledgeDocumentCopy
from ..models import KnowledgeDocumentCreateRequest
from ..models import KnowledgeDocumentFeedback
from ..models import KnowledgeDocumentFeedbackResponse
from ..models import KnowledgeDocumentFeedbackResponseListing
from ..models import KnowledgeDocumentFeedbackUpdateRequest
from ..models import KnowledgeDocumentGuestSearch
from ..models import KnowledgeDocumentGuestSearchRequest
from ..models import KnowledgeDocumentPresentation
from ..models import KnowledgeDocumentQuery
from ..models import KnowledgeDocumentQueryResponse
from ..models import KnowledgeDocumentReq
from ..models import KnowledgeDocumentRequest
from ..models import KnowledgeDocumentResponse
from ..models import KnowledgeDocumentResponseListing
from ..models import KnowledgeDocumentSearch
from ..models import KnowledgeDocumentSearchRequest
from ..models import KnowledgeDocumentSuggestion
from ..models import KnowledgeDocumentSuggestionRequest
from ..models import KnowledgeDocumentVersion
from ..models import KnowledgeDocumentVersionListing
from ..models import KnowledgeDocumentVersionVariation
from ..models import KnowledgeDocumentVersionVariationListing
from ..models import KnowledgeDocumentView
from ..models import KnowledgeDocumentsAnswerFilter
from ..models import KnowledgeExportJobRequest
from ..models import KnowledgeExportJobResponse
from ..models import KnowledgeExtendedCategory
from ..models import KnowledgeGuestAnswerDocumentsResponse
from ..models import KnowledgeGuestDocumentCopy
from ..models import KnowledgeGuestDocumentFeedback
from ..models import KnowledgeGuestDocumentPresentation
from ..models import KnowledgeGuestDocumentResponse
from ..models import KnowledgeGuestDocumentResponseListing
from ..models import KnowledgeGuestDocumentSuggestion
from ..models import KnowledgeGuestDocumentSuggestionRequest
from ..models import KnowledgeGuestDocumentView
from ..models import KnowledgeGuestSession
from ..models import KnowledgeImport
from ..models import KnowledgeImportJobRequest
from ..models import KnowledgeImportJobResponse
from ..models import KnowledgeIntegrationOptionsResponse
from ..models import KnowledgeParseJobRequest
from ..models import KnowledgeParseJobRequestImport
from ..models import KnowledgeParseJobRequestPatch
from ..models import KnowledgeParseJobResponse
from ..models import KnowledgeSearchRequest
from ..models import KnowledgeSearchResponse
from ..models import KnowledgeSyncJobRequest
from ..models import KnowledgeSyncJobResponse
from ..models import KnowledgeTraining
from ..models import LabelCreateRequest
from ..models import LabelListing
from ..models import LabelResponse
from ..models import LabelUpdateRequest
from ..models import OperationCreatorUserResponse
from ..models import OperationListing
from ..models import SalesforceSourceRequest
from ..models import SalesforceSourceResponse
from ..models import SearchUpdateRequest
from ..models import ServiceNowSourceRequest
from ..models import ServiceNowSourceResponse
from ..models import SourceBaseResponse
from ..models import SourceSyncResponse
from ..models import SyncStatusRequest
from ..models import TrainingListing
from ..models import UnansweredGroup
from ..models import UnansweredGroups
from ..models import UnansweredPhraseGroup
from ..models import UnansweredPhraseGroupPatchRequestBody
from ..models import UnansweredPhraseGroupUpdateResponse
from ..models import UploadUrlRequest
from ..models import UploadUrlResponse

class KnowledgeApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_knowledge_knowledgebase(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeBase':
        """
        Delete knowledge base
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :return: KnowledgeBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeBase',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_category(self, knowledge_base_id: str, category_id: str, **kwargs) -> 'CategoryResponse':
        """
        Delete category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_category(knowledge_base_id, category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str category_id: Category ID (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'category_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_category`")
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `delete_knowledge_knowledgebase_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_document(self, knowledge_base_id: str, document_id: str, **kwargs) -> None:
        """
        Delete document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_document(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_document`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_knowledge_knowledgebase_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_document_variation(self, document_variation_id: str, document_id: str, knowledge_base_id: str, **kwargs) -> None:
        """
        Delete a variation for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_variation_id: Globally unique identifier for a document variation. (required)
        :param str document_id: Globally unique identifier for a document. (required)
        :param str knowledge_base_id: Globally unique identifier for a knowledge base. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_variation_id', 'document_id', 'knowledge_base_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_document_variation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_variation_id' is set
        if ('document_variation_id' not in params) or (params['document_variation_id'] is None):
            raise ValueError("Missing the required parameter `document_variation_id` when calling `delete_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_document_variation`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_variation_id' in params:
            path_params['documentVariationId'] = params['document_variation_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_export_job(self, knowledge_base_id: str, export_job_id: str, **kwargs) -> None:
        """
        Delete export job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str export_job_id: Export job ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'export_job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_export_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_export_job`")
        # verify the required parameter 'export_job_id' is set
        if ('export_job_id' not in params) or (params['export_job_id'] is None):
            raise ValueError("Missing the required parameter `export_job_id` when calling `delete_knowledge_knowledgebase_export_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs/{exportJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'export_job_id' in params:
            path_params['exportJobId'] = params['export_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_import_job(self, knowledge_base_id: str, import_job_id: str, **kwargs) -> None:
        """
        Delete import job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str import_job_id: Import job ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'import_job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_import_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_import_job`")
        # verify the required parameter 'import_job_id' is set
        if ('import_job_id' not in params) or (params['import_job_id'] is None):
            raise ValueError("Missing the required parameter `import_job_id` when calling `delete_knowledge_knowledgebase_import_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'import_job_id' in params:
            path_params['importJobId'] = params['import_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_label(self, knowledge_base_id: str, label_id: str, **kwargs) -> 'LabelResponse':
        """
        Delete label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_label(knowledge_base_id, label_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str label_id: Label ID (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'label_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_label`")
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `delete_knowledge_knowledgebase_label`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LabelResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("delete_knowledge_knowledgebase_language_category is deprecated")
    def delete_knowledge_knowledgebase_language_category(self, category_id: str, knowledge_base_id: str, language_code: str, **kwargs) -> 'KnowledgeCategory':
        """
        Delete category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str category_id: Category ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :return: KnowledgeCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'knowledge_base_id', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_language_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `delete_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `delete_knowledge_knowledgebase_language_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeCategory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("delete_knowledge_knowledgebase_language_document is deprecated")
    def delete_knowledge_knowledgebase_language_document(self, document_id: str, knowledge_base_id: str, language_code: str, **kwargs) -> 'KnowledgeDocument':
        """
        Delete document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :return: KnowledgeDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'knowledge_base_id', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_language_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `delete_knowledge_knowledgebase_language_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("delete_knowledge_knowledgebase_language_documents_import is deprecated")
    def delete_knowledge_knowledgebase_language_documents_import(self, knowledge_base_id: str, language_code: str, import_id: str, **kwargs) -> None:
        """
        Delete import operation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str import_id: Import ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'import_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_language_documents_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `delete_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params) or (params['import_id'] is None):
            raise ValueError("Missing the required parameter `import_id` when calling `delete_knowledge_knowledgebase_language_documents_import`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'import_id' in params:
            path_params['importId'] = params['import_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_sources_salesforce_source_id(self, knowledge_base_id: str, source_id: str, **kwargs) -> None:
        """
        Delete Salesforce Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_sources_salesforce_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_sources_salesforce_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `delete_knowledge_knowledgebase_sources_salesforce_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_sources_servicenow_source_id(self, knowledge_base_id: str, source_id: str, **kwargs) -> None:
        """
        Delete ServiceNow Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_sources_servicenow_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_sources_servicenow_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `delete_knowledge_knowledgebase_sources_servicenow_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_knowledge_knowledgebase_synchronize_job(self, knowledge_base_id: str, sync_job_id: str, **kwargs) -> None:
        """
        Delete synchronization job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str sync_job_id: Synchronization job ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'sync_job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledge_knowledgebase_synchronize_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `delete_knowledge_knowledgebase_synchronize_job`")
        # verify the required parameter 'sync_job_id' is set
        if ('sync_job_id' not in params) or (params['sync_job_id'] is None):
            raise ValueError("Missing the required parameter `sync_job_id` when calling `delete_knowledge_knowledgebase_synchronize_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'sync_job_id' in params:
            path_params['syncJobId'] = params['sync_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_guest_session_categories(self, session_id: str, **kwargs) -> 'GuestCategoryResponseListing':
        """
        Get categories
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_guest_session_categories(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str parent_id: If specified, retrieves the children categories by parent category ID.
        :param bool is_root: If specified, retrieves only the root categories.
        :param str name: Filter to return the categories that starts with the given category name.
        :param str sort_by: Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically
        :param str expand: The specified entity attribute will be filled. Supported value:\"Ancestors\": every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors.
        :param bool include_document_count: If specified, retrieves the number of documents related to category.
        :return: GuestCategoryResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'before', 'after', 'page_size', 'parent_id', 'is_root', 'name', 'sort_by', 'expand', 'include_document_count']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_guest_session_categories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_knowledge_guest_session_categories`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'parent_id' in params:
            query_params['parentId'] = params['parent_id']
        if 'is_root' in params:
            query_params['isRoot'] = params['is_root']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'include_document_count' in params:
            query_params['includeDocumentCount'] = params['include_document_count']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GuestCategoryResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_guest_session_document(self, session_id: str, document_id: str, **kwargs) -> 'KnowledgeGuestDocumentResponse':
        """
        Get a knowledge document by ID.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_guest_session_document(session_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str document_id: Document ID (required)
        :return: KnowledgeGuestDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'document_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_guest_session_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_knowledge_guest_session_document`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_guest_session_document`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestDocumentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_guest_session_documents(self, session_id: str, **kwargs) -> 'KnowledgeGuestDocumentResponseListing':
        """
        Get documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_guest_session_documents(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param list[str] category_id: If specified, retrieves documents associated with category ids, comma separated values expected.
        :param int page_size: Number of entities to return. Maximum of 200.
        :return: KnowledgeGuestDocumentResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'category_id', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_guest_session_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_knowledge_guest_session_documents`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}
        if 'category_id' in params:
            query_params['categoryId'] = params['category_id']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestDocumentResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_integration_options(self, integration_id: str, **kwargs) -> 'KnowledgeIntegrationOptionsResponse':
        """
        Get sync options available for a knowledge-connect integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_integration_options(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param list[str] knowledge_base_ids: Narrowing down filtering option results by knowledge base.
        :return: KnowledgeIntegrationOptionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'knowledge_base_ids']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_integration_options" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_knowledge_integration_options`")


        resource_path = '/api/v2/knowledge/integrations/{integrationId}/options'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}
        if 'knowledge_base_ids' in params:
            query_params['knowledgeBaseIds'] = params['knowledge_base_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeIntegrationOptionsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeBase':
        """
        Get knowledge base
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :return: KnowledgeBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeBase',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_categories(self, knowledge_base_id: str, **kwargs) -> 'CategoryResponseListing':
        """
        Get categories
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_categories(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str parent_id: If specified, retrieves the children categories by parent category ID.
        :param bool is_root: If specified, retrieves only the root categories.
        :param str name: Filter to return the categories that starts with the given category name.
        :param str sort_by: Name: sort by category names alphabetically; Hierarchy: sort by the full path of hierarchical category names alphabetically
        :param str expand: The specified entity attribute will be filled. Supported value:\"Ancestors\": every ancestors will be filled via the parent attribute recursively,but only the id, name, parentId will be present for the ancestors.
        :param bool include_document_count: If specified, retrieves the number of documents related to category.
        :return: CategoryResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'before', 'after', 'page_size', 'parent_id', 'is_root', 'name', 'sort_by', 'expand', 'include_document_count']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_categories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_categories`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'parent_id' in params:
            query_params['parentId'] = params['parent_id']
        if 'is_root' in params:
            query_params['isRoot'] = params['is_root']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'include_document_count' in params:
            query_params['includeDocumentCount'] = params['include_document_count']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_category(self, knowledge_base_id: str, category_id: str, **kwargs) -> 'CategoryResponse':
        """
        Get category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_category(knowledge_base_id, category_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str category_id: Category ID (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'category_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_category`")
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_knowledge_knowledgebase_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document(self, knowledge_base_id: str, document_id: str, **kwargs) -> 'KnowledgeDocumentResponse':
        """
        Get document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected. Max No. of variations that can be returned on expand is 20.
        :param str state: \"when state is \"Draft\", draft version of the document is returned,otherwise by default published version is returned in the response.
        :return: KnowledgeDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'expand', 'state']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'state' in params:
            query_params['state'] = params['state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_feedback(self, knowledge_base_id: str, document_id: str, **kwargs) -> 'KnowledgeDocumentFeedbackResponseListing':
        """
        Get a list of feedback records given on a document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param bool only_commented: If true, only feedback records that have comment are returned. If false, feedback records with and without comment are returned. Default: false.
        :param str document_version_id: Document version ID to filter by. Supported only if onlyCommented=true is set.
        :param str document_variation_id: Document variation ID to filter by. Supported only if onlyCommented=true is set.
        :param str app_type: Application type to filter by. Supported only if onlyCommented=true is set.
        :param str query_type: Query type to filter by. Supported only if onlyCommented=true is set.
        :param str user_id: The ID of the user, who created the feedback, to filter by. Supported only if onlyCommented=true is set.
        :param str queue_id: Queue ID to filter by. Supported only if onlyCommented=true is set.
        :param str state: State to filter by. Supported only if onlyCommented=true is set. Default: Final
        :return: KnowledgeDocumentFeedbackResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'before', 'after', 'page_size', 'only_commented', 'document_version_id', 'document_variation_id', 'app_type', 'query_type', 'user_id', 'queue_id', 'state']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_feedback" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_feedback`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_feedback`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'only_commented' in params:
            query_params['onlyCommented'] = params['only_commented']
        if 'document_version_id' in params:
            query_params['documentVersionId'] = params['document_version_id']
        if 'document_variation_id' in params:
            query_params['documentVariationId'] = params['document_variation_id']
        if 'app_type' in params:
            query_params['appType'] = params['app_type']
        if 'query_type' in params:
            query_params['queryType'] = params['query_type']
        if 'user_id' in params:
            query_params['userId'] = params['user_id']
        if 'queue_id' in params:
            query_params['queueId'] = params['queue_id']
        if 'state' in params:
            query_params['state'] = params['state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentFeedbackResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_feedback_feedback_id(self, knowledge_base_id: str, document_id: str, feedback_id: str, **kwargs) -> 'KnowledgeDocumentFeedbackResponse':
        """
        Get a single feedback record given on a document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param str feedback_id: Feedback ID. (required)
        :return: KnowledgeDocumentFeedbackResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'feedback_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_feedback_feedback_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_feedback_feedback_id`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_feedback_feedback_id`")
        # verify the required parameter 'feedback_id' is set
        if ('feedback_id' not in params) or (params['feedback_id'] is None):
            raise ValueError("Missing the required parameter `feedback_id` when calling `get_knowledge_knowledgebase_document_feedback_feedback_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback/{feedbackId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'feedback_id' in params:
            path_params['feedbackId'] = params['feedback_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentFeedbackResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_variation(self, document_variation_id: str, document_id: str, knowledge_base_id: str, **kwargs) -> 'DocumentVariationResponse':
        """
        Get a variation for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_variation_id: Globally unique identifier for a document variation. (required)
        :param str document_id: Globally unique identifier for a document. (required)
        :param str knowledge_base_id: Globally unique identifier for a knowledge base. (required)
        :param str document_state: The state of the document.
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: DocumentVariationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_variation_id', 'document_id', 'knowledge_base_id', 'document_state', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_variation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_variation_id' is set
        if ('document_variation_id' not in params) or (params['document_variation_id'] is None):
            raise ValueError("Missing the required parameter `document_variation_id` when calling `get_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_variation`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_variation_id' in params:
            path_params['documentVariationId'] = params['document_variation_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'document_state' in params:
            query_params['documentState'] = params['document_state']
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentVariationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_variations(self, knowledge_base_id: str, document_id: str, **kwargs) -> 'DocumentVariationResponseListing':
        """
        Get variations for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str document_state: The state of the document.
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: DocumentVariationResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'before', 'after', 'page_size', 'document_state', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_variations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_variations`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_variations`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'document_state' in params:
            query_params['documentState'] = params['document_state']
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentVariationResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_version(self, knowledge_base_id: str, document_id: str, version_id: str, **kwargs) -> 'KnowledgeDocumentVersion':
        """
        Get document version.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_version(knowledge_base_id, document_id, version_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param str version_id: Globally unique identifier for the document version. (required)
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: KnowledgeDocumentVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'version_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_version" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_version`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_version`")
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params) or (params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_knowledge_knowledgebase_document_version`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentVersion',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_version_variation(self, knowledge_base_id: str, document_id: str, version_id: str, variation_id: str, **kwargs) -> 'KnowledgeDocumentVersionVariation':
        """
        Get variation for the given document version.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_version_variation(knowledge_base_id, document_id, version_id, variation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param str version_id: Globally unique identifier for the document version. (required)
        :param str variation_id: Globally unique identifier for the document version variation. (required)
        :return: KnowledgeDocumentVersionVariation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'version_id', 'variation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_version_variation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_version_variation`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_version_variation`")
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params) or (params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_knowledge_knowledgebase_document_version_variation`")
        # verify the required parameter 'variation_id' is set
        if ('variation_id' not in params) or (params['variation_id'] is None):
            raise ValueError("Missing the required parameter `variation_id` when calling `get_knowledge_knowledgebase_document_version_variation`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId}/variations/{variationId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']
        if 'variation_id' in params:
            path_params['variationId'] = params['variation_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentVersionVariation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_version_variations(self, knowledge_base_id: str, document_id: str, version_id: str, **kwargs) -> 'KnowledgeDocumentVersionVariationListing':
        """
        Get variations for the given document version.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_version_variations(knowledge_base_id, document_id, version_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param str version_id: Globally unique identifier for the document version. (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :return: KnowledgeDocumentVersionVariationListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'version_id', 'before', 'after', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_version_variations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_version_variations`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_version_variations`")
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params) or (params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_knowledge_knowledgebase_document_version_variations`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions/{versionId}/variations'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentVersionVariationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_document_versions(self, knowledge_base_id: str, document_id: str, **kwargs) -> 'KnowledgeDocumentVersionListing':
        """
        Get document versions.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: KnowledgeDocumentVersionListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'before', 'after', 'page_size', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_document_versions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_document_versions`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_document_versions`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentVersionListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_documents(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeDocumentResponseListing':
        """
        Get documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_documents(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str interval: Retrieves the documents modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ
        :param list[str] document_id: Retrieves the specified documents, comma separated values expected.
        :param list[str] category_id: If specified, retrieves documents associated with category ids, comma separated values expected.
        :param bool include_subcategories: Works along with 'categoryId' query parameter. If specified, retrieves documents associated with category ids and its children categories.
        :param bool include_drafts: If includeDrafts is true, Documents in the draft state are also returned in the response.
        :param list[str] label_ids: If specified, retrieves documents associated with label ids, comma separated values expected.
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :param list[str] external_ids: If specified, retrieves documents associated with external ids, comma separated values expected.
        :return: KnowledgeDocumentResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'before', 'after', 'page_size', 'interval', 'document_id', 'category_id', 'include_subcategories', 'include_drafts', 'label_ids', 'expand', 'external_ids']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_documents`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'interval' in params:
            query_params['interval'] = params['interval']
        if 'document_id' in params:
            query_params['documentId'] = params['document_id']
        if 'category_id' in params:
            query_params['categoryId'] = params['category_id']
        if 'include_subcategories' in params:
            query_params['includeSubcategories'] = params['include_subcategories']
        if 'include_drafts' in params:
            query_params['includeDrafts'] = params['include_drafts']
        if 'label_ids' in params:
            query_params['labelIds'] = params['label_ids']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'external_ids' in params:
            query_params['externalIds'] = params['external_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_export_job(self, knowledge_base_id: str, export_job_id: str, **kwargs) -> 'KnowledgeExportJobResponse':
        """
        Get export job report
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_export_job(knowledge_base_id, export_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str export_job_id: Export job ID (required)
        :return: KnowledgeExportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'export_job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_export_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_export_job`")
        # verify the required parameter 'export_job_id' is set
        if ('export_job_id' not in params) or (params['export_job_id'] is None):
            raise ValueError("Missing the required parameter `export_job_id` when calling `get_knowledge_knowledgebase_export_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs/{exportJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'export_job_id' in params:
            path_params['exportJobId'] = params['export_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeExportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_import_job(self, knowledge_base_id: str, import_job_id: str, **kwargs) -> 'KnowledgeImportJobResponse':
        """
        Get import job report
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str import_job_id: Import job ID (required)
        :param list[str] expand: If expand contains 'urls' downloadURL and failedEntitiesURL will be filled.
        :return: KnowledgeImportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'import_job_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_import_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_import_job`")
        # verify the required parameter 'import_job_id' is set
        if ('import_job_id' not in params) or (params['import_job_id'] is None):
            raise ValueError("Missing the required parameter `import_job_id` when calling `get_knowledge_knowledgebase_import_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'import_job_id' in params:
            path_params['importJobId'] = params['import_job_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_label(self, knowledge_base_id: str, label_id: str, **kwargs) -> 'LabelResponse':
        """
        Get label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_label(knowledge_base_id, label_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str label_id: Label ID (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'label_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_label`")
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `get_knowledge_knowledgebase_label`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LabelResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_labels(self, knowledge_base_id: str, **kwargs) -> 'LabelListing':
        """
        Get labels
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_labels(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str name: Filter to return the labels that contains the given phrase in the name.
        :param bool include_document_count: If specified, retrieves the number of documents related to label.
        :return: LabelListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'before', 'after', 'page_size', 'name', 'include_document_count']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_labels" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_labels`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'include_document_count' in params:
            query_params['includeDocumentCount'] = params['include_document_count']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LabelListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_categories is deprecated")
    def get_knowledge_knowledgebase_language_categories(self, knowledge_base_id: str, language_code: str, **kwargs) -> 'CategoryListing':
        """
        Get categories
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 200. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str name: Filter to return the categories that starts with the given category name.
        :return: CategoryListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'before', 'after', 'limit', 'page_size', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_categories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_categories`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_categories`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'name' in params:
            query_params['name'] = params['name']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_category is deprecated")
    def get_knowledge_knowledgebase_language_category(self, category_id: str, knowledge_base_id: str, language_code: str, **kwargs) -> 'KnowledgeExtendedCategory':
        """
        Get category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str category_id: Category ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :return: KnowledgeExtendedCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'knowledge_base_id', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeExtendedCategory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_document is deprecated")
    def get_knowledge_knowledgebase_language_document(self, document_id: str, knowledge_base_id: str, language_code: str, **kwargs) -> 'KnowledgeDocument':
        """
        Get document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :return: KnowledgeDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'knowledge_base_id', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_document_upload is deprecated")
    def get_knowledge_knowledgebase_language_document_upload(self, document_id: str, knowledge_base_id: str, language_code: str, upload_id: str, **kwargs) -> 'KnowledgeDocumentContentUpload':
        """
        Get document content upload status
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_document_upload(document_id, knowledge_base_id, language_code, upload_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str upload_id: UploadId (required)
        :return: KnowledgeDocumentContentUpload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'knowledge_base_id', 'language_code', 'upload_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_document_upload" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_knowledge_knowledgebase_language_document_upload`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_document_upload`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_document_upload`")
        # verify the required parameter 'upload_id' is set
        if ('upload_id' not in params) or (params['upload_id'] is None):
            raise ValueError("Missing the required parameter `upload_id` when calling `get_knowledge_knowledgebase_language_document_upload`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}/uploads/{uploadId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'upload_id' in params:
            path_params['uploadId'] = params['upload_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentContentUpload',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_documents is deprecated")
    def get_knowledge_knowledgebase_language_documents(self, knowledge_base_id: str, language_code: str, **kwargs) -> 'DocumentListing':
        """
        Get documents
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 200. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str categories: Filter by categories ids, comma separated values expected.
        :param str title: Filter by document title.
        :param str sort_by: Sort by.
        :param str sort_order: Sort Order.
        :param list[str] document_ids: Comma-separated list of document identifiers to fetch by.
        :return: DocumentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'before', 'after', 'limit', 'page_size', 'categories', 'title', 'sort_by', 'sort_order', 'document_ids']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_documents`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_documents`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'categories' in params:
            query_params['categories'] = params['categories']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'document_ids' in params:
            query_params['documentIds'] = params['document_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_documents_import is deprecated")
    def get_knowledge_knowledgebase_language_documents_import(self, knowledge_base_id: str, language_code: str, import_id: str, **kwargs) -> 'KnowledgeImport':
        """
        Get import operation report
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str import_id: Import ID (required)
        :return: KnowledgeImport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'import_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_documents_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params) or (params['import_id'] is None):
            raise ValueError("Missing the required parameter `import_id` when calling `get_knowledge_knowledgebase_language_documents_import`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'import_id' in params:
            path_params['importId'] = params['import_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_training is deprecated")
    def get_knowledge_knowledgebase_language_training(self, knowledge_base_id: str, language_code: str, training_id: str, **kwargs) -> 'KnowledgeTraining':
        """
        Get training detail
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_training(knowledge_base_id, language_code, training_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str training_id: Training ID (required)
        :return: KnowledgeTraining
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'training_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_training" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_training`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_training`")
        # verify the required parameter 'training_id' is set
        if ('training_id' not in params) or (params['training_id'] is None):
            raise ValueError("Missing the required parameter `training_id` when calling `get_knowledge_knowledgebase_language_training`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings/{trainingId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'training_id' in params:
            path_params['trainingId'] = params['training_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeTraining',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_knowledge_knowledgebase_language_trainings is deprecated")
    def get_knowledge_knowledgebase_language_trainings(self, knowledge_base_id: str, language_code: str, **kwargs) -> 'TrainingListing':
        """
        Get all trainings information for a knowledgebase
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 200. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str knowledge_documents_state: Return the training with the specified state of the trained documents.
        :return: TrainingListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'before', 'after', 'limit', 'page_size', 'knowledge_documents_state']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_language_trainings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_language_trainings`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `get_knowledge_knowledgebase_language_trainings`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'knowledge_documents_state' in params:
            query_params['knowledgeDocumentsState'] = params['knowledge_documents_state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TrainingListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_operations(self, knowledge_base_id: str, **kwargs) -> 'OperationListing':
        """
        Get operations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_operations(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str page_size: Number of entities to return. Maximum of 200.
        :param list[str] user_id: If specified, retrieves operations associated with user ids, comma separated values expected.
        :param list[str] type: If specified, retrieves operations with specified operation type, comma separated values expected.
        :param list[str] status: If specified, retrieves operations with specified operation status, comma separated values expected.
        :param str interval: Retrieves the operations modified in specified date and time range. If the after and before cursor parameters are within this interval, it would return valid data, otherwise it throws an error.The dates in the interval are represented in ISO-8601 format: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ
        :param list[str] source_id: If specified, retrieves operations associated with source ids, comma separated values expected.
        :return: OperationListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'before', 'after', 'page_size', 'user_id', 'type', 'status', 'interval', 'source_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_operations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_operations`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/operations'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'user_id' in params:
            query_params['userId'] = params['user_id']
        if 'type' in params:
            query_params['type'] = params['type']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'interval' in params:
            query_params['interval'] = params['interval']
        if 'source_id' in params:
            query_params['sourceId'] = params['source_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OperationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_operations_users_query(self, knowledge_base_id: str, **kwargs) -> 'OperationCreatorUserResponse':
        """
        Get ids of operation creator users and oauth clients
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_operations_users_query(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :return: OperationCreatorUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_operations_users_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_operations_users_query`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/operations/users/query'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OperationCreatorUserResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_parse_job(self, knowledge_base_id: str, parse_job_id: str, **kwargs) -> 'KnowledgeParseJobResponse':
        """
        Get parse job report
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str parse_job_id: Parse job ID (required)
        :param list[str] expand: If expand contains 'urls' downloadURL and failedEntitiesURL will be filled.
        :return: KnowledgeParseJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'parse_job_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_parse_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_parse_job`")
        # verify the required parameter 'parse_job_id' is set
        if ('parse_job_id' not in params) or (params['parse_job_id'] is None):
            raise ValueError("Missing the required parameter `parse_job_id` when calling `get_knowledge_knowledgebase_parse_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'parse_job_id' in params:
            path_params['parseJobId'] = params['parse_job_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeParseJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_sources(self, knowledge_base_id: str, **kwargs) -> List['SourceBaseResponse']:
        """
        Get Knowledge integration sources
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_sources(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str type: If specified, retrieves integration sources with specified integration type.
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :param list[str] ids: If specified, retrieves integration sources with specified IDs.
        :return: list[SourceBaseResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'type', 'expand', 'ids']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_sources" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_sources`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'ids' in params:
            query_params['ids'] = params['ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[SourceBaseResponse]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_sources_salesforce_source_id(self, knowledge_base_id: str, source_id: str, **kwargs) -> 'SalesforceSourceResponse':
        """
        Get Salesforce Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: SalesforceSourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_sources_salesforce_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_sources_salesforce_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_knowledge_knowledgebase_sources_salesforce_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SalesforceSourceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_sources_servicenow_source_id(self, knowledge_base_id: str, source_id: str, **kwargs) -> 'ServiceNowSourceResponse':
        """
        Get ServiceNow Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param list[str] expand: The specified entity attributes will be filled. Comma separated values expected.
        :return: ServiceNowSourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_sources_servicenow_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_sources_servicenow_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_knowledge_knowledgebase_sources_servicenow_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ServiceNowSourceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_synchronize_job(self, knowledge_base_id: str, sync_job_id: str, **kwargs) -> 'KnowledgeSyncJobResponse':
        """
        Get synchronization job report
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str sync_job_id: Synchronization job ID (required)
        :return: KnowledgeSyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'sync_job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_synchronize_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_synchronize_job`")
        # verify the required parameter 'sync_job_id' is set
        if ('sync_job_id' not in params) or (params['sync_job_id'] is None):
            raise ValueError("Missing the required parameter `sync_job_id` when calling `get_knowledge_knowledgebase_synchronize_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'sync_job_id' in params:
            path_params['syncJobId'] = params['sync_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSyncJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_unanswered_group(self, knowledge_base_id: str, group_id: str, **kwargs) -> 'UnansweredGroup':
        """
        Get knowledge base unanswered group for a particular groupId
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_unanswered_group(knowledge_base_id, group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str group_id: The ID of the group to be retrieved. (required)
        :param str app: The app value to be used for filtering phrases.
        :param date date_start: The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :param date date_end: The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :return: UnansweredGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'group_id', 'app', 'date_start', 'date_end']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_unanswered_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_unanswered_group`")
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_knowledge_knowledgebase_unanswered_group`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']

        query_params = {}
        if 'app' in params:
            query_params['app'] = params['app']
        if 'date_start' in params:
            query_params['dateStart'] = params['date_start']
        if 'date_end' in params:
            query_params['dateEnd'] = params['date_end']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnansweredGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_unanswered_group_phrasegroup(self, knowledge_base_id: str, group_id: str, phrase_group_id: str, **kwargs) -> 'UnansweredPhraseGroup':
        """
        Get knowledge base unanswered phrase group for a particular phraseGroupId
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str group_id: The ID of the group to be retrieved. (required)
        :param str phrase_group_id: The ID of the phraseGroup to be retrieved. (required)
        :param str app: The app value to be used for filtering phrases.
        :param date date_start: The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :param date date_end: The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :return: UnansweredPhraseGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'group_id', 'phrase_group_id', 'app', 'date_start', 'date_end']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_unanswered_group_phrasegroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_unanswered_group_phrasegroup`")
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_knowledge_knowledgebase_unanswered_group_phrasegroup`")
        # verify the required parameter 'phrase_group_id' is set
        if ('phrase_group_id' not in params) or (params['phrase_group_id'] is None):
            raise ValueError("Missing the required parameter `phrase_group_id` when calling `get_knowledge_knowledgebase_unanswered_group_phrasegroup`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId}/phrasegroups/{phraseGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']
        if 'phrase_group_id' in params:
            path_params['phraseGroupId'] = params['phrase_group_id']

        query_params = {}
        if 'app' in params:
            query_params['app'] = params['app']
        if 'date_start' in params:
            query_params['dateStart'] = params['date_start']
        if 'date_end' in params:
            query_params['dateEnd'] = params['date_end']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnansweredPhraseGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_unanswered_groups(self, knowledge_base_id: str, **kwargs) -> 'UnansweredGroups':
        """
        Get knowledge base unanswered groups
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_unanswered_groups(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str app: The app value to be used for filtering phrases.
        :param date date_start: The start date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :param date date_end: The end date to be used for filtering phrases. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
        :return: UnansweredGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'app', 'date_start', 'date_end']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_unanswered_groups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_unanswered_groups`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'app' in params:
            query_params['app'] = params['app']
        if 'date_start' in params:
            query_params['dateStart'] = params['date_start']
        if 'date_end' in params:
            query_params['dateEnd'] = params['date_end']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnansweredGroups',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebase_uploads_urls_job(self, knowledge_base_id: str, job_id: str, **kwargs) -> 'GetUploadSourceUrlJobStatusResponse':
        """
        Get content upload from URL job status
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebase_uploads_urls_job(knowledge_base_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str job_id: Upload job ID (required)
        :return: GetUploadSourceUrlJobStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebase_uploads_urls_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `get_knowledge_knowledgebase_uploads_urls_job`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_knowledge_knowledgebase_uploads_urls_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/uploads/urls/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='GetUploadSourceUrlJobStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_knowledge_knowledgebases(self, **kwargs) -> 'KnowledgeBaseListing':
        """
        Get knowledge bases
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_knowledge_knowledgebases(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 100. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 100.
        :param str name: Filter by Name.
        :param str core_language: Filter by core language.
        :param bool published: Filter by published status.
        :param str sort_by: Sort by.
        :param str sort_order: Sort Order.
        :return: KnowledgeBaseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['before', 'after', 'limit', 'page_size', 'name', 'core_language', 'published', 'sort_by', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledge_knowledgebases" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/knowledge/knowledgebases'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'before' in params:
            query_params['before'] = params['before']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'core_language' in params:
            query_params['coreLanguage'] = params['core_language']
        if 'published' in params:
            query_params['published'] = params['published']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeBaseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_guest_session_documents_search_search_id(self, session_id: str, search_id: str, body: 'SearchUpdateRequest', **kwargs) -> None:
        """
        Update search result.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_guest_session_documents_search_search_id(session_id, search_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str search_id: Search Result ID (required)
        :param SearchUpdateRequest body:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'search_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_guest_session_documents_search_search_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `patch_knowledge_guest_session_documents_search_search_id`")
        # verify the required parameter 'search_id' is set
        if ('search_id' not in params) or (params['search_id'] is None):
            raise ValueError("Missing the required parameter `search_id` when calling `patch_knowledge_guest_session_documents_search_search_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_guest_session_documents_search_search_id`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/search/{searchId}'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'search_id' in params:
            path_params['searchId'] = params['search_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase(self, knowledge_base_id: str, body: 'KnowledgeBaseUpdateRequest', **kwargs) -> 'KnowledgeBase':
        """
        Update knowledge base
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeBaseUpdateRequest body:  (required)
        :return: KnowledgeBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeBase',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_category(self, knowledge_base_id: str, category_id: str, body: 'CategoryUpdateRequest', **kwargs) -> 'CategoryResponse':
        """
        Update category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_category(knowledge_base_id, category_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str category_id: Category ID (required)
        :param CategoryUpdateRequest body:  (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'category_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_category`")
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `patch_knowledge_knowledgebase_category`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_document(self, knowledge_base_id: str, document_id: str, body: 'KnowledgeDocumentReq', **kwargs) -> 'KnowledgeDocumentResponse':
        """
        Update document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_document(knowledge_base_id, document_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param KnowledgeDocumentReq body:  (required)
        :return: KnowledgeDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_document`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `patch_knowledge_knowledgebase_document`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_document_feedback_feedback_id(self, knowledge_base_id: str, document_id: str, feedback_id: str, **kwargs) -> 'KnowledgeDocumentFeedbackResponse':
        """
        Update feedback on a document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_document_feedback_feedback_id(knowledge_base_id, document_id, feedback_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param str feedback_id: Feedback ID. (required)
        :param KnowledgeDocumentFeedbackUpdateRequest body: 
        :return: KnowledgeDocumentFeedbackResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'feedback_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_document_feedback_feedback_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_document_feedback_feedback_id`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `patch_knowledge_knowledgebase_document_feedback_feedback_id`")
        # verify the required parameter 'feedback_id' is set
        if ('feedback_id' not in params) or (params['feedback_id'] is None):
            raise ValueError("Missing the required parameter `feedback_id` when calling `patch_knowledge_knowledgebase_document_feedback_feedback_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback/{feedbackId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'feedback_id' in params:
            path_params['feedbackId'] = params['feedback_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentFeedbackResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_document_variation(self, document_variation_id: str, document_id: str, knowledge_base_id: str, body: 'DocumentVariationRequest', **kwargs) -> 'DocumentVariationResponse':
        """
        Update a variation for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_document_variation(document_variation_id, document_id, knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_variation_id: Globally unique identifier for a document variation. (required)
        :param str document_id: Globally unique identifier for a document. (required)
        :param str knowledge_base_id: Globally unique identifier for a knowledge base. (required)
        :param DocumentVariationRequest body:  (required)
        :return: DocumentVariationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_variation_id', 'document_id', 'knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_document_variation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_variation_id' is set
        if ('document_variation_id' not in params) or (params['document_variation_id'] is None):
            raise ValueError("Missing the required parameter `document_variation_id` when calling `patch_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `patch_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_document_variation`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_document_variation`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations/{documentVariationId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_variation_id' in params:
            path_params['documentVariationId'] = params['document_variation_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentVariationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_documents_search_search_id(self, knowledge_base_id: str, search_id: str, **kwargs) -> None:
        """
        Update search result.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_documents_search_search_id(knowledge_base_id, search_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: The ID of knowledge base containing the documents to query. (required)
        :param str search_id: Search Result ID (required)
        :param SearchUpdateRequest body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'search_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_documents_search_search_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_documents_search_search_id`")
        # verify the required parameter 'search_id' is set
        if ('search_id' not in params) or (params['search_id'] is None):
            raise ValueError("Missing the required parameter `search_id` when calling `patch_knowledge_knowledgebase_documents_search_search_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search/{searchId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'search_id' in params:
            path_params['searchId'] = params['search_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_import_job(self, knowledge_base_id: str, import_job_id: str, body: 'ImportStatusRequest', **kwargs) -> 'KnowledgeImportJobResponse':
        """
        Start import job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_import_job(knowledge_base_id, import_job_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str import_job_id: Import job ID (required)
        :param ImportStatusRequest body:  (required)
        :return: KnowledgeImportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'import_job_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_import_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_import_job`")
        # verify the required parameter 'import_job_id' is set
        if ('import_job_id' not in params) or (params['import_job_id'] is None):
            raise ValueError("Missing the required parameter `import_job_id` when calling `patch_knowledge_knowledgebase_import_job`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_import_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs/{importJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'import_job_id' in params:
            path_params['importJobId'] = params['import_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_label(self, knowledge_base_id: str, label_id: str, body: 'LabelUpdateRequest', **kwargs) -> 'LabelResponse':
        """
        Update label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_label(knowledge_base_id, label_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str label_id: Label ID (required)
        :param LabelUpdateRequest body:  (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'label_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_label`")
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `patch_knowledge_knowledgebase_label`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_label`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LabelResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("patch_knowledge_knowledgebase_language_category is deprecated")
    def patch_knowledge_knowledgebase_language_category(self, category_id: str, knowledge_base_id: str, language_code: str, body: 'KnowledgeCategoryRequest', **kwargs) -> 'KnowledgeExtendedCategory':
        """
        Update category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_language_category(category_id, knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str category_id: Category ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeCategoryRequest body:  (required)
        :return: KnowledgeExtendedCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_language_category" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'category_id' is set
        if ('category_id' not in params) or (params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `patch_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `patch_knowledge_knowledgebase_language_category`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_language_category`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories/{categoryId}'.replace('{format}', 'json')
        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeExtendedCategory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("patch_knowledge_knowledgebase_language_document is deprecated")
    def patch_knowledge_knowledgebase_language_document(self, document_id: str, knowledge_base_id: str, language_code: str, body: 'KnowledgeDocumentRequest', **kwargs) -> 'KnowledgeDocument':
        """
        Update document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_language_document(document_id, knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeDocumentRequest body:  (required)
        :return: KnowledgeDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_language_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `patch_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `patch_knowledge_knowledgebase_language_document`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_language_document`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("patch_knowledge_knowledgebase_language_documents is deprecated")
    def patch_knowledge_knowledgebase_language_documents(self, knowledge_base_id: str, language_code: str, body: List['KnowledgeDocumentBulkRequest'], **kwargs) -> 'DocumentListing':
        """
        Update documents collection
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param list[KnowledgeDocumentBulkRequest] body:  (required)
        :return: DocumentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_language_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_language_documents`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `patch_knowledge_knowledgebase_language_documents`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_language_documents`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("patch_knowledge_knowledgebase_language_documents_import is deprecated")
    def patch_knowledge_knowledgebase_language_documents_import(self, knowledge_base_id: str, language_code: str, import_id: str, body: 'ImportStatusRequest', **kwargs) -> 'KnowledgeImport':
        """
        Start import operation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_language_documents_import(knowledge_base_id, language_code, import_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str import_id: Import ID (required)
        :param ImportStatusRequest body:  (required)
        :return: KnowledgeImport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'import_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_language_documents_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `patch_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params) or (params['import_id'] is None):
            raise ValueError("Missing the required parameter `import_id` when calling `patch_knowledge_knowledgebase_language_documents_import`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_language_documents_import`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports/{importId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'import_id' in params:
            path_params['importId'] = params['import_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_parse_job(self, knowledge_base_id: str, parse_job_id: str, body: 'KnowledgeParseJobRequestPatch', **kwargs) -> None:
        """
        Send update to the parse operation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_parse_job(knowledge_base_id, parse_job_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str parse_job_id: Parse job ID (required)
        :param KnowledgeParseJobRequestPatch body:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'parse_job_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_parse_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_parse_job`")
        # verify the required parameter 'parse_job_id' is set
        if ('parse_job_id' not in params) or (params['parse_job_id'] is None):
            raise ValueError("Missing the required parameter `parse_job_id` when calling `patch_knowledge_knowledgebase_parse_job`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_parse_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'parse_job_id' in params:
            path_params['parseJobId'] = params['parse_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_synchronize_job(self, knowledge_base_id: str, sync_job_id: str, body: 'SyncStatusRequest', **kwargs) -> 'KnowledgeSyncJobResponse':
        """
        Update synchronization job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_synchronize_job(knowledge_base_id, sync_job_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str sync_job_id: Synchronization job ID (required)
        :param SyncStatusRequest body:  (required)
        :return: KnowledgeSyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'sync_job_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_synchronize_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_synchronize_job`")
        # verify the required parameter 'sync_job_id' is set
        if ('sync_job_id' not in params) or (params['sync_job_id'] is None):
            raise ValueError("Missing the required parameter `sync_job_id` when calling `patch_knowledge_knowledgebase_synchronize_job`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_synchronize_job`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs/{syncJobId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'sync_job_id' in params:
            path_params['syncJobId'] = params['sync_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSyncJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_knowledge_knowledgebase_unanswered_group_phrasegroup(self, knowledge_base_id: str, group_id: str, phrase_group_id: str, body: 'UnansweredPhraseGroupPatchRequestBody', **kwargs) -> 'UnansweredPhraseGroupUpdateResponse':
        """
        Update a Knowledge base unanswered phrase group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_knowledge_knowledgebase_unanswered_group_phrasegroup(knowledge_base_id, group_id, phrase_group_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str group_id: The ID of the group to be updated. (required)
        :param str phrase_group_id: The ID of the phraseGroup to be updated. (required)
        :param UnansweredPhraseGroupPatchRequestBody body: Request body of the update unanswered group endpoint. (required)
        :return: UnansweredPhraseGroupUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'group_id', 'phrase_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_knowledge_knowledgebase_unanswered_group_phrasegroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `patch_knowledge_knowledgebase_unanswered_group_phrasegroup`")
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `patch_knowledge_knowledgebase_unanswered_group_phrasegroup`")
        # verify the required parameter 'phrase_group_id' is set
        if ('phrase_group_id' not in params) or (params['phrase_group_id'] is None):
            raise ValueError("Missing the required parameter `phrase_group_id` when calling `patch_knowledge_knowledgebase_unanswered_group_phrasegroup`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_knowledge_knowledgebase_unanswered_group_phrasegroup`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/unanswered/groups/{groupId}/phrasegroups/{phraseGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']
        if 'phrase_group_id' in params:
            path_params['phraseGroupId'] = params['phrase_group_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UnansweredPhraseGroupUpdateResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_documentuploads(self, body: 'UploadUrlRequest', **kwargs) -> 'UploadUrlResponse':
        """
        Creates a presigned URL for uploading a knowledge import file with a set of documents
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_documentuploads(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UploadUrlRequest body: query (required)
        :return: UploadUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_documentuploads" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_documentuploads`")


        resource_path = '/api/v2/knowledge/documentuploads'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UploadUrlResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_document_copies(self, session_id: str, document_id: str, **kwargs) -> None:
        """
        Indicate that the document was copied by the user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_document_copies(session_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str document_id: Document ID (required)
        :param KnowledgeGuestDocumentCopy body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_document_copies" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_document_copies`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_guest_session_document_copies`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/copies'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_document_feedback(self, session_id: str, document_id: str, **kwargs) -> 'KnowledgeGuestDocumentFeedback':
        """
        Give feedback on a document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_document_feedback(session_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str document_id: Document ID. (required)
        :param KnowledgeGuestDocumentFeedback body: 
        :return: KnowledgeGuestDocumentFeedback
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_document_feedback" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_document_feedback`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_guest_session_document_feedback`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/feedback'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestDocumentFeedback',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_document_views(self, session_id: str, document_id: str, **kwargs) -> None:
        """
        Create view event for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_document_views(session_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param str document_id: Document ID (required)
        :param KnowledgeGuestDocumentView body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_document_views" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_document_views`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_guest_session_document_views`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/{documentId}/views'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_documents_answers(self, session_id: str, body: 'KnowledgeDocumentsAnswerFilter', **kwargs) -> 'KnowledgeGuestAnswerDocumentsResponse':
        """
        Answer documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_documents_answers(session_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param KnowledgeDocumentsAnswerFilter body:  (required)
        :return: KnowledgeGuestAnswerDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_documents_answers" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_documents_answers`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_guest_session_documents_answers`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/answers'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestAnswerDocumentsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_documents_presentations(self, session_id: str, **kwargs) -> None:
        """
        Indicate that documents were presented to the user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_documents_presentations(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param KnowledgeGuestDocumentPresentation body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_documents_presentations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_documents_presentations`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/presentations'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_documents_search(self, session_id: str, **kwargs) -> 'KnowledgeDocumentGuestSearch':
        """
        Search the documents in a guest session.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_documents_search(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param list[str] expand: Fields, if any, to expand for each document in the search result matching the query.
        :param KnowledgeDocumentGuestSearchRequest body: 
        :return: KnowledgeDocumentGuestSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'expand', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_documents_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_documents_search`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/search'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentGuestSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_session_documents_search_suggestions(self, session_id: str, **kwargs) -> 'KnowledgeGuestDocumentSuggestion':
        """
        Query the knowledge documents to provide suggestions for auto completion.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_session_documents_search_suggestions(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: Knowledge guest session ID. (required)
        :param KnowledgeGuestDocumentSuggestionRequest body: 
        :return: KnowledgeGuestDocumentSuggestion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_session_documents_search_suggestions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `post_knowledge_guest_session_documents_search_suggestions`")


        resource_path = '/api/v2/knowledge/guest/sessions/{sessionId}/documents/search/suggestions'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestDocumentSuggestion',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_guest_sessions(self, body: 'KnowledgeGuestSession', **kwargs) -> 'KnowledgeGuestSession':
        """
        Create guest session
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_guest_sessions(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KnowledgeGuestSession body:  (required)
        :return: KnowledgeGuestSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_guest_sessions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_guest_sessions`")


        resource_path = '/api/v2/knowledge/guest/sessions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeGuestSession',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_categories(self, knowledge_base_id: str, body: 'CategoryCreateRequest', **kwargs) -> 'CategoryResponse':
        """
        Create new category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_categories(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param CategoryCreateRequest body:  (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_categories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_categories`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_categories`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CategoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_document_copies(self, knowledge_base_id: str, document_id: str, **kwargs) -> None:
        """
        Indicate that the document was copied by the user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_document_copies(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param KnowledgeDocumentCopy body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_document_copies" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_document_copies`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_document_copies`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/copies'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_document_feedback(self, knowledge_base_id: str, document_id: str, **kwargs) -> 'KnowledgeDocumentFeedbackResponse':
        """
        Give feedback on a document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_document_feedback(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param KnowledgeDocumentFeedback body: 
        :return: KnowledgeDocumentFeedbackResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_document_feedback" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_document_feedback`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_document_feedback`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/feedback'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentFeedbackResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_document_variations(self, knowledge_base_id: str, document_id: str, body: 'DocumentVariationRequest', **kwargs) -> 'DocumentVariationResponse':
        """
        Create a variation for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_document_variations(knowledge_base_id, document_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param DocumentVariationRequest body:  (required)
        :return: DocumentVariationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_document_variations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_document_variations`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_document_variations`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_document_variations`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/variations'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DocumentVariationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_document_versions(self, knowledge_base_id: str, document_id: str, body: 'KnowledgeDocumentVersion', **kwargs) -> 'KnowledgeDocumentVersion':
        """
        Creates or restores a document version.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_document_versions(knowledge_base_id, document_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Globally unique identifier for the knowledge base. (required)
        :param str document_id: Globally unique identifier for the document. (required)
        :param KnowledgeDocumentVersion body:  (required)
        :return: KnowledgeDocumentVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_document_versions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_document_versions`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_document_versions`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_document_versions`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/versions'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentVersion',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_document_views(self, knowledge_base_id: str, document_id: str, **kwargs) -> None:
        """
        Create view for a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_document_views(knowledge_base_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param str document_id: Document ID. (required)
        :param KnowledgeDocumentView body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_document_views" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_document_views`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_document_views`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/{documentId}/views'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents(self, knowledge_base_id: str, body: 'KnowledgeDocumentCreateRequest', **kwargs) -> 'KnowledgeDocumentResponse':
        """
        Create document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeDocumentCreateRequest body:  (required)
        :return: KnowledgeDocumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_documents`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_answers(self, knowledge_base_id: str, body: 'KnowledgeDocumentsAnswerFilter', **kwargs) -> 'KnowledgeAnswerDocumentsResponse':
        """
        Answer documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_answers(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeDocumentsAnswerFilter body:  (required)
        :return: KnowledgeAnswerDocumentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_answers" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_answers`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_documents_answers`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/answers'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeAnswerDocumentsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_bulk_remove(self, knowledge_base_id: str, body: 'KnowledgeDocumentBulkRemoveRequest', **kwargs) -> 'BulkResponse':
        """
        Bulk remove documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_bulk_remove(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeDocumentBulkRemoveRequest body:  (required)
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_bulk_remove" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_bulk_remove`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_documents_bulk_remove`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/bulk/remove'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BulkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_bulk_update(self, knowledge_base_id: str, body: 'KnowledgeDocumentBulkUpdateRequest', **kwargs) -> 'BulkResponse':
        """
        Bulk update documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_bulk_update(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeDocumentBulkUpdateRequest body:  (required)
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_bulk_update" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_bulk_update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_documents_bulk_update`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/bulk/update'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BulkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_presentations(self, knowledge_base_id: str, **kwargs) -> None:
        """
        Indicate that documents were presented to the user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_presentations(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID. (required)
        :param KnowledgeDocumentPresentation body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_presentations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_presentations`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/presentations'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_query(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeDocumentQueryResponse':
        """
        Query for knowledge documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_query(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge Base ID (required)
        :param list[str] expand: Fields, if any, to expand for each document in the search result matching the query.
        :param KnowledgeDocumentQuery body: 
        :return: KnowledgeDocumentQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'expand', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_query`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/query'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_search(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeDocumentSearch':
        """
        Search the documents in a knowledge base.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_search(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: The ID of knowledge base containing the documents to query. (required)
        :param list[str] expand: Fields, if any, to expand for each document in the search result matching the query.
        :param KnowledgeDocumentSearchRequest body: 
        :return: KnowledgeDocumentSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'expand', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_search`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_search_suggestions(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeDocumentSuggestion':
        """
        Query the knowledge documents to provide suggestions for auto completion.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_search_suggestions(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: The ID of knowledge base containing the documents to query. (required)
        :param KnowledgeDocumentSuggestionRequest body: 
        :return: KnowledgeDocumentSuggestion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_search_suggestions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_search_suggestions`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/search/suggestions'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentSuggestion',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_documents_versions_bulk_add(self, knowledge_base_id: str, body: 'KnowledgeDocumentBulkVersionAddRequest', **kwargs) -> 'BulkResponse':
        """
        Bulk add document versions.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_documents_versions_bulk_add(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeDocumentBulkVersionAddRequest body:  (required)
        :return: BulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_documents_versions_bulk_add" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_documents_versions_bulk_add`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_documents_versions_bulk_add`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/documents/versions/bulk/add'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BulkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_export_jobs(self, knowledge_base_id: str, body: 'KnowledgeExportJobRequest', **kwargs) -> 'KnowledgeExportJobResponse':
        """
        Create export job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_export_jobs(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeExportJobRequest body:  (required)
        :return: KnowledgeExportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_export_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_export_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_export_jobs`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/export/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeExportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_import_jobs(self, knowledge_base_id: str, body: 'KnowledgeImportJobRequest', **kwargs) -> 'KnowledgeImportJobResponse':
        """
        Create import job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_import_jobs(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeImportJobRequest body:  (required)
        :return: KnowledgeImportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_import_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_import_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_import_jobs`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/import/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_labels(self, knowledge_base_id: str, body: 'LabelCreateRequest', **kwargs) -> 'LabelResponse':
        """
        Create new label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_labels(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param LabelCreateRequest body:  (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_labels" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_labels`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_labels`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/labels'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LabelResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_categories is deprecated")
    def post_knowledge_knowledgebase_language_categories(self, knowledge_base_id: str, language_code: str, body: 'KnowledgeCategoryRequest', **kwargs) -> 'KnowledgeExtendedCategory':
        """
        Create new category
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_categories(knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeCategoryRequest body:  (required)
        :return: KnowledgeExtendedCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_categories" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_categories`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_categories`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_language_categories`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeExtendedCategory',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_document_uploads is deprecated")
    def post_knowledge_knowledgebase_language_document_uploads(self, document_id: str, knowledge_base_id: str, language_code: str, body: 'KnowledgeDocumentContentUpload', **kwargs) -> 'KnowledgeDocumentContentUpload':
        """
        Upload Article Content
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_document_uploads(document_id, knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeDocumentContentUpload body:  (required)
        :return: KnowledgeDocumentContentUpload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_document_uploads" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `post_knowledge_knowledgebase_language_document_uploads`")
        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_document_uploads`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_document_uploads`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_language_document_uploads`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/{documentId}/uploads'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocumentContentUpload',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_documents is deprecated")
    def post_knowledge_knowledgebase_language_documents(self, knowledge_base_id: str, language_code: str, body: 'KnowledgeDocumentRequest', **kwargs) -> 'KnowledgeDocument':
        """
        Create document
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_documents(knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeDocumentRequest body:  (required)
        :return: KnowledgeDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_documents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_documents`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_documents`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_language_documents`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_documents_imports is deprecated")
    def post_knowledge_knowledgebase_language_documents_imports(self, knowledge_base_id: str, language_code: str, body: 'KnowledgeImport', **kwargs) -> 'KnowledgeImport':
        """
        Create import operation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_documents_imports(knowledge_base_id, language_code, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param KnowledgeImport body:  (required)
        :return: KnowledgeImport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_documents_imports" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_documents_imports`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_documents_imports`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_language_documents_imports`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/documents/imports'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeImport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_training_promote is deprecated")
    def post_knowledge_knowledgebase_language_training_promote(self, knowledge_base_id: str, language_code: str, training_id: str, **kwargs) -> 'KnowledgeTraining':
        """
        Promote trained documents from draft state to active.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_training_promote(knowledge_base_id, language_code, training_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :param str training_id: Training ID (required)
        :return: KnowledgeTraining
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code', 'training_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_training_promote" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_training_promote`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_training_promote`")
        # verify the required parameter 'training_id' is set
        if ('training_id' not in params) or (params['training_id'] is None):
            raise ValueError("Missing the required parameter `training_id` when calling `post_knowledge_knowledgebase_language_training_promote`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings/{trainingId}/promote'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']
        if 'training_id' in params:
            path_params['trainingId'] = params['training_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeTraining',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_language_trainings is deprecated")
    def post_knowledge_knowledgebase_language_trainings(self, knowledge_base_id: str, language_code: str, **kwargs) -> 'KnowledgeTraining':
        """
        Trigger training
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_language_trainings(knowledge_base_id, language_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str language_code: Language code, format: iso2-LOCALE (required)
        :return: KnowledgeTraining
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'language_code']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_language_trainings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_language_trainings`")
        # verify the required parameter 'language_code' is set
        if ('language_code' not in params) or (params['language_code'] is None):
            raise ValueError("Missing the required parameter `language_code` when calling `post_knowledge_knowledgebase_language_trainings`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/languages/{languageCode}/trainings'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'language_code' in params:
            path_params['languageCode'] = params['language_code']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeTraining',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_parse_job_import(self, knowledge_base_id: str, parse_job_id: str, body: 'KnowledgeParseJobRequestImport', **kwargs) -> None:
        """
        Import the parsed articles
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_parse_job_import(knowledge_base_id, parse_job_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str parse_job_id: Parse job ID (required)
        :param KnowledgeParseJobRequestImport body:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'parse_job_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_parse_job_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_parse_job_import`")
        # verify the required parameter 'parse_job_id' is set
        if ('parse_job_id' not in params) or (params['parse_job_id'] is None):
            raise ValueError("Missing the required parameter `parse_job_id` when calling `post_knowledge_knowledgebase_parse_job_import`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_parse_job_import`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs/{parseJobId}/import'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'parse_job_id' in params:
            path_params['parseJobId'] = params['parse_job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_parse_jobs(self, knowledge_base_id: str, body: 'KnowledgeParseJobRequest', **kwargs) -> 'KnowledgeParseJobResponse':
        """
        Create parse job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_parse_jobs(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeParseJobRequest body:  (required)
        :return: KnowledgeParseJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_parse_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_parse_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_parse_jobs`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/parse/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeParseJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_knowledge_knowledgebase_search is deprecated")
    def post_knowledge_knowledgebase_search(self, knowledge_base_id: str, **kwargs) -> 'KnowledgeSearchResponse':
        """
        Search Documents
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_search(knowledge_base_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeSearchRequest body: 
        :return: KnowledgeSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_search`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/search'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSearchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_sources_salesforce(self, knowledge_base_id: str, body: 'SalesforceSourceRequest', **kwargs) -> 'KnowledgeSyncJobResponse':
        """
        Create Salesforce Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_sources_salesforce(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param SalesforceSourceRequest body:  (required)
        :return: KnowledgeSyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_sources_salesforce" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_sources_salesforce`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_sources_salesforce`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSyncJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_sources_salesforce_source_id_sync(self, knowledge_base_id: str, source_id: str, **kwargs) -> 'SourceSyncResponse':
        """
        Start sync on Salesforce Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_sources_salesforce_source_id_sync(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param object body: 
        :return: SourceSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_sources_salesforce_source_id_sync" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_sources_salesforce_source_id_sync`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `post_knowledge_knowledgebase_sources_salesforce_source_id_sync`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId}/sync'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SourceSyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_sources_servicenow(self, knowledge_base_id: str, body: 'ServiceNowSourceRequest', **kwargs) -> 'KnowledgeSyncJobResponse':
        """
        Create ServiceNow Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_sources_servicenow(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param ServiceNowSourceRequest body:  (required)
        :return: KnowledgeSyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_sources_servicenow" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_sources_servicenow`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_sources_servicenow`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSyncJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_sources_servicenow_source_id_sync(self, knowledge_base_id: str, source_id: str, **kwargs) -> 'SourceSyncResponse':
        """
        Start synchronization on ServiceNow Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_sources_servicenow_source_id_sync(knowledge_base_id, source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param object body: 
        :return: SourceSyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_sources_servicenow_source_id_sync" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_sources_servicenow_source_id_sync`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `post_knowledge_knowledgebase_sources_servicenow_source_id_sync`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId}/sync'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SourceSyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_synchronize_jobs(self, knowledge_base_id: str, body: 'KnowledgeSyncJobRequest', **kwargs) -> 'KnowledgeSyncJobResponse':
        """
        Create synchronization job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_synchronize_jobs(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param KnowledgeSyncJobRequest body:  (required)
        :return: KnowledgeSyncJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_synchronize_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_synchronize_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_synchronize_jobs`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/synchronize/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeSyncJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebase_uploads_urls_jobs(self, knowledge_base_id: str, body: 'CreateUploadSourceUrlJobRequest', **kwargs) -> 'CreateUploadSourceUrlJobResponse':
        """
        Create content upload from URL job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebase_uploads_urls_jobs(knowledge_base_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param CreateUploadSourceUrlJobRequest body: uploadRequest (required)
        :return: CreateUploadSourceUrlJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebase_uploads_urls_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `post_knowledge_knowledgebase_uploads_urls_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebase_uploads_urls_jobs`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/uploads/urls/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateUploadSourceUrlJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_knowledge_knowledgebases(self, body: 'KnowledgeBaseCreateRequest', **kwargs) -> 'KnowledgeBase':
        """
        Create new knowledge base
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_knowledge_knowledgebases(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KnowledgeBaseCreateRequest body:  (required)
        :return: KnowledgeBase
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_knowledge_knowledgebases" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_knowledge_knowledgebases`")


        resource_path = '/api/v2/knowledge/knowledgebases'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='KnowledgeBase',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_knowledge_knowledgebase_sources_salesforce_source_id(self, knowledge_base_id: str, source_id: str, body: 'SalesforceSourceRequest', **kwargs) -> 'SalesforceSourceResponse':
        """
        Update Salesforce Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_knowledge_knowledgebase_sources_salesforce_source_id(knowledge_base_id, source_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param SalesforceSourceRequest body:  (required)
        :return: SalesforceSourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_knowledge_knowledgebase_sources_salesforce_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `put_knowledge_knowledgebase_sources_salesforce_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `put_knowledge_knowledgebase_sources_salesforce_source_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_knowledge_knowledgebase_sources_salesforce_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/salesforce/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SalesforceSourceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_knowledge_knowledgebase_sources_servicenow_source_id(self, knowledge_base_id: str, source_id: str, body: 'ServiceNowSourceRequest', **kwargs) -> 'ServiceNowSourceResponse':
        """
        Update ServiceNow Knowledge integration source
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_knowledge_knowledgebase_sources_servicenow_source_id(knowledge_base_id, source_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str knowledge_base_id: Knowledge base ID (required)
        :param str source_id: Source ID (required)
        :param ServiceNowSourceRequest body:  (required)
        :return: ServiceNowSourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['knowledge_base_id', 'source_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_knowledge_knowledgebase_sources_servicenow_source_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'knowledge_base_id' is set
        if ('knowledge_base_id' not in params) or (params['knowledge_base_id'] is None):
            raise ValueError("Missing the required parameter `knowledge_base_id` when calling `put_knowledge_knowledgebase_sources_servicenow_source_id`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `put_knowledge_knowledgebase_sources_servicenow_source_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_knowledge_knowledgebase_sources_servicenow_source_id`")


        resource_path = '/api/v2/knowledge/knowledgebases/{knowledgeBaseId}/sources/servicenow/{sourceId}'.replace('{format}', 'json')
        path_params = {}
        if 'knowledge_base_id' in params:
            path_params['knowledgeBaseId'] = params['knowledge_base_id']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ServiceNowSourceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
