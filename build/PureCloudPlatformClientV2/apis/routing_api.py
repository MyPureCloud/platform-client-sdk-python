# coding: utf-8

"""
RoutingApi.py
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
from ..models import AgentDirectRoutingBackupSettings
from ..models import AgentMaxUtilizationResponse
from ..models import AssessmentJobListing
from ..models import AssessmentListing
from ..models import AssistantQueue
from ..models import AvailableMediaTypeEntityListing
from ..models import BenefitAssessment
from ..models import BenefitAssessmentJob
from ..models import ComparisonPeriod
from ..models import ComparisonPeriodListing
from ..models import ContactCenterSettings
from ..models import CreateBenefitAssessmentJobRequest
from ..models import CreateBenefitAssessmentRequest
from ..models import CreatePredictorRequest
from ..models import CreateQueueRequest
from ..models import CreateUtilizationLabelRequest
from ..models import CreateUtilizationTagRequest
from ..models import EmailOutboundDomainResult
from ..models import EmailSetup
from ..models import ErrorBody
from ..models import EstimatedWaitTimePredictions
from ..models import IdentityResolutionConfig
from ..models import IdentityResolutionQueueConfig
from ..models import InboundDomain
from ..models import InboundDomainEntityListing
from ..models import InboundDomainPatchRequest
from ..models import InboundRoute
from ..models import InboundRouteEntityListing
from ..models import KeyPerformanceIndicator
from ..models import Language
from ..models import LanguageEntityListing
from ..models import OutboundDomain
from ..models import OutboundDomainEntityListing
from ..models import OutboundDomainRequest
from ..models import PatchPredictorRequest
from ..models import Predictor
from ..models import PredictorListing
from ..models import PredictorModelFeatureListing
from ..models import PredictorModels
from ..models import Queue
from ..models import QueueEntityListing
from ..models import QueueMember
from ..models import QueueMemberEntityListing
from ..models import QueueMemberEntityListingV1
from ..models import QueueObservationQuery
from ..models import QueueObservationQueryResponse
from ..models import QueueRequest
from ..models import Recipient
from ..models import RecipientListing
from ..models import RecipientRequest
from ..models import RoutingActivityQuery
from ..models import RoutingActivityResponse
from ..models import RoutingConversationAttributesRequest
from ..models import RoutingConversationAttributesResponse
from ..models import RoutingSettings
from ..models import RoutingSkill
from ..models import SMSAvailablePhoneNumberEntityListing
from ..models import SkillEntityListing
from ..models import SkillGroup
from ..models import SkillGroupEntityListing
from ..models import SkillGroupMemberDivisionList
from ..models import SkillGroupMemberDivisions
from ..models import SkillGroupMemberEntityListing
from ..models import SkillGroupWithMemberDivisions
from ..models import SmsAddress
from ..models import SmsAddressEntityListing
from ..models import SmsAddressProvision
from ..models import SmsAlphanumericProvision
from ..models import SmsPhoneNumber
from ..models import SmsPhoneNumberEntityListing
from ..models import SmsPhoneNumberImport
from ..models import SmsPhoneNumberPatchRequest
from ..models import SmsPhoneNumberProvision
from ..models import TestMessage
from ..models import TranscriptionSettings
from ..models import UpdateUtilizationLabelRequest
from ..models import UserLanguageEntityListing
from ..models import UserQueue
from ..models import UserQueueEntityListing
from ..models import UserRoutingLanguage
from ..models import UserRoutingLanguagePost
from ..models import UserRoutingSkill
from ..models import UserRoutingSkillPost
from ..models import UserSkillEntityListing
from ..models import UserSkillGroupEntityListing
from ..models import UtilizationLabel
from ..models import UtilizationLabelEntityListing
from ..models import UtilizationRequest
from ..models import UtilizationResponse
from ..models import UtilizationTag
from ..models import UtilizationTagEntityListing
from ..models import WrapUpCodeReference
from ..models import WrapupCode
from ..models import WrapupCodeEntityListing
from ..models import WrapupCodeRequest
from ..models import WritableEntity

class RoutingApi(object):
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

    def delete_routing_assessment(self, assessment_id: str, **kwargs) -> None:
        """
        Delete single benefit assessment.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_assessment(assessment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str assessment_id: Benefit Assessment ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assessment_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_assessment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'assessment_id' is set
        if ('assessment_id' not in params) or (params['assessment_id'] is None):
            raise ValueError("Missing the required parameter `assessment_id` when calling `delete_routing_assessment`")


        resource_path = '/api/v2/routing/assessments/{assessmentId}'.replace('{format}', 'json')
        path_params = {}
        if 'assessment_id' in params:
            path_params['assessmentId'] = params['assessment_id']

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

    def delete_routing_directroutingbackup_settings_me(self, **kwargs) -> None:
        """
        Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_directroutingbackup_settings_me(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_directroutingbackup_settings_me" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/directroutingbackup/settings/me'.replace('{format}', 'json')
        path_params = {}

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

    def delete_routing_email_domain(self, domain_id: str, **kwargs) -> None:
        """
        Delete a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_email_domain(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_email_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `delete_routing_email_domain`")


        resource_path = '/api/v2/routing/email/domains/{domainId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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

    def delete_routing_email_domain_route(self, domain_name: str, route_id: str, **kwargs) -> None:
        """
        Delete a route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_email_domain_route(domain_name, route_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param str route_id: route ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'route_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_email_domain_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `delete_routing_email_domain_route`")
        # verify the required parameter 'route_id' is set
        if ('route_id' not in params) or (params['route_id'] is None):
            raise ValueError("Missing the required parameter `route_id` when calling `delete_routing_email_domain_route`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes/{routeId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']
        if 'route_id' in params:
            path_params['routeId'] = params['route_id']

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

    def delete_routing_email_outbound_domain(self, domain_id: str, **kwargs) -> None:
        """
        Delete an outbound domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_email_outbound_domain(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_email_outbound_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `delete_routing_email_outbound_domain`")


        resource_path = '/api/v2/routing/email/outbound/domains/{domainId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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

    def delete_routing_language(self, language_id: str, **kwargs) -> None:
        """
        Delete a routing language
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_language(language_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str language_id: Language ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_language" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'language_id' is set
        if ('language_id' not in params) or (params['language_id'] is None):
            raise ValueError("Missing the required parameter `language_id` when calling `delete_routing_language`")


        resource_path = '/api/v2/routing/languages/{languageId}'.replace('{format}', 'json')
        path_params = {}
        if 'language_id' in params:
            path_params['languageId'] = params['language_id']

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

    def delete_routing_predictor(self, predictor_id: str, **kwargs) -> None:
        """
        Delete single predictor.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_predictor(predictor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str predictor_id: Predictor ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predictor_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_predictor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'predictor_id' is set
        if ('predictor_id' not in params) or (params['predictor_id'] is None):
            raise ValueError("Missing the required parameter `predictor_id` when calling `delete_routing_predictor`")


        resource_path = '/api/v2/routing/predictors/{predictorId}'.replace('{format}', 'json')
        path_params = {}
        if 'predictor_id' in params:
            path_params['predictorId'] = params['predictor_id']

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

    def delete_routing_queue(self, queue_id: str, **kwargs) -> None:
        """
        Delete a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_queue(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param bool force_delete: forceDelete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'force_delete']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_queue" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `delete_routing_queue`")


        resource_path = '/api/v2/routing/queues/{queueId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'force_delete' in params:
            query_params['forceDelete'] = params['force_delete']

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

    def delete_routing_queue_member(self, queue_id: str, member_id: str, **kwargs) -> None:
        """
        Delete a queue member.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_queue_member(queue_id, member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str member_id: Member ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'member_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_queue_member" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `delete_routing_queue_member`")
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `delete_routing_queue_member`")


        resource_path = '/api/v2/routing/queues/{queueId}/members/{memberId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']

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

    @deprecated("delete_routing_queue_user is deprecated")
    def delete_routing_queue_user(self, queue_id: str, member_id: str, **kwargs) -> None:
        """
        DEPRECATED: use DELETE /routing/queues/{queueId}/members/{memberId}.  Delete queue member.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_queue_user(queue_id, member_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str member_id: Member ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'member_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_queue_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `delete_routing_queue_user`")
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `delete_routing_queue_user`")


        resource_path = '/api/v2/routing/queues/{queueId}/users/{memberId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']

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

    def delete_routing_queue_wrapupcode(self, queue_id: str, code_id: str, **kwargs) -> None:
        """
        Delete a wrap-up code from a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_queue_wrapupcode(queue_id, code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str code_id: Code ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_queue_wrapupcode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `delete_routing_queue_wrapupcode`")
        # verify the required parameter 'code_id' is set
        if ('code_id' not in params) or (params['code_id'] is None):
            raise ValueError("Missing the required parameter `code_id` when calling `delete_routing_queue_wrapupcode`")


        resource_path = '/api/v2/routing/queues/{queueId}/wrapupcodes/{codeId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'code_id' in params:
            path_params['codeId'] = params['code_id']

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

    def delete_routing_settings(self, **kwargs) -> None:
        """
        Delete an organization's routing settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/settings'.replace('{format}', 'json')
        path_params = {}

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

    def delete_routing_skill(self, skill_id: str, **kwargs) -> None:
        """
        Delete Routing Skill
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_skill(skill_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_id: Skill ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_skill" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `delete_routing_skill`")


        resource_path = '/api/v2/routing/skills/{skillId}'.replace('{format}', 'json')
        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

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

    def delete_routing_skillgroup(self, skill_group_id: str, **kwargs) -> None:
        """
        Remove skill group definition
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_skillgroup(skill_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_skillgroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `delete_routing_skillgroup`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

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

    def delete_routing_sms_address(self, address_id: str, **kwargs) -> None:
        """
        Delete an Address by Id for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_sms_address(address_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str address_id: Address ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_sms_address" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'address_id' is set
        if ('address_id' not in params) or (params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `delete_routing_sms_address`")


        resource_path = '/api/v2/routing/sms/addresses/{addressId}'.replace('{format}', 'json')
        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']

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

    def delete_routing_sms_phonenumber(self, phone_number_id: str, **kwargs) -> None:
        """
        Delete a phone number provisioned for SMS.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_sms_phonenumber(phone_number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number_id: phone number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_sms_phonenumber" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params) or (params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `delete_routing_sms_phonenumber`")


        resource_path = '/api/v2/routing/sms/phonenumbers/{phoneNumberId}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']

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

    def delete_routing_user_directroutingbackup_settings(self, user_id: str, **kwargs) -> None:
        """
        Delete the user's Direct Routing Backup settings and revert to the Direct Routing Queue default.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_user_directroutingbackup_settings(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_user_directroutingbackup_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_routing_user_directroutingbackup_settings`")


        resource_path = '/api/v2/routing/users/{userId}/directroutingbackup/settings'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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

    def delete_routing_user_utilization(self, user_id: str, **kwargs) -> None:
        """
        Delete the user's max utilization settings and revert to the organization-wide default.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_user_utilization(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_user_utilization" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_routing_user_utilization`")


        resource_path = '/api/v2/routing/users/{userId}/utilization'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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

    def delete_routing_utilization(self, **kwargs) -> None:
        """
        Delete the organization-wide max utilization settings and revert to the system default.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_utilization(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_utilization" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/utilization'.replace('{format}', 'json')
        path_params = {}

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

    def delete_routing_utilization_label(self, label_id: str, **kwargs) -> None:
        """
        Delete a utilization label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_utilization_label(label_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str label_id: Utilization Label ID (required)
        :param bool force_delete: Remove all label usages (if found) without warning
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label_id', 'force_delete']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_utilization_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `delete_routing_utilization_label`")


        resource_path = '/api/v2/routing/utilization/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']

        query_params = {}
        if 'force_delete' in params:
            query_params['forceDelete'] = params['force_delete']

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

    def delete_routing_utilization_tag(self, tag_id: str, **kwargs) -> None:
        """
        Delete an utilization tag
        
	    delete_routing_utilization_tag is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_utilization_tag(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: Utilization Tag ID (required)
        :param bool force_delete: Remove all tag usages (if found) without warning
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'force_delete']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_utilization_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params) or (params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `delete_routing_utilization_tag`")


        resource_path = '/api/v2/routing/utilization/tags/{tagId}'.replace('{format}', 'json')
        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']

        query_params = {}
        if 'force_delete' in params:
            query_params['forceDelete'] = params['force_delete']

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

    def delete_routing_wrapupcode(self, code_id: str, **kwargs) -> None:
        """
        Delete wrap-up code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_routing_wrapupcode(code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code_id: Wrapup Code ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_routing_wrapupcode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'code_id' is set
        if ('code_id' not in params) or (params['code_id'] is None):
            raise ValueError("Missing the required parameter `code_id` when calling `delete_routing_wrapupcode`")


        resource_path = '/api/v2/routing/wrapupcodes/{codeId}'.replace('{format}', 'json')
        path_params = {}
        if 'code_id' in params:
            path_params['codeId'] = params['code_id']

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

    def delete_user_routinglanguage(self, user_id: str, language_id: str, **kwargs) -> None:
        """
        Remove a routing language from a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_routinglanguage(user_id, language_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param str language_id: languageId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'language_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_routinglanguage" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_routinglanguage`")
        # verify the required parameter 'language_id' is set
        if ('language_id' not in params) or (params['language_id'] is None):
            raise ValueError("Missing the required parameter `language_id` when calling `delete_user_routinglanguage`")


        resource_path = '/api/v2/users/{userId}/routinglanguages/{languageId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'language_id' in params:
            path_params['languageId'] = params['language_id']

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

    def delete_user_routingskill(self, user_id: str, skill_id: str, **kwargs) -> None:
        """
        Remove a routing skill from a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_routingskill(user_id, skill_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param str skill_id: skillId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'skill_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_routingskill" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_routingskill`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `delete_user_routingskill`")


        resource_path = '/api/v2/users/{userId}/routingskills/{skillId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

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

    def get_routing_assessment(self, assessment_id: str, **kwargs) -> 'BenefitAssessment':
        """
        Retrieve a single benefit assessment.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_assessment(assessment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str assessment_id: Benefit Assessment ID (required)
        :return: BenefitAssessment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assessment_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_assessment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'assessment_id' is set
        if ('assessment_id' not in params) or (params['assessment_id'] is None):
            raise ValueError("Missing the required parameter `assessment_id` when calling `get_routing_assessment`")


        resource_path = '/api/v2/routing/assessments/{assessmentId}'.replace('{format}', 'json')
        path_params = {}
        if 'assessment_id' in params:
            path_params['assessmentId'] = params['assessment_id']

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
                                            response_type='BenefitAssessment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_assessments(self, **kwargs) -> 'AssessmentListing':
        """
        Retrieve all benefit assessments.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_assessments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 200. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 200.
        :param list[str] queue_id: Queue ID(s) to filter assessments by.
        :return: AssessmentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['before', 'after', 'limit', 'page_size', 'queue_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_assessments" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/assessments'.replace('{format}', 'json')
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
        if 'queue_id' in params:
            query_params['queueId'] = params['queue_id']

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
                                            response_type='AssessmentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_assessments_job(self, job_id: str, **kwargs) -> 'BenefitAssessmentJob':
        """
        Retrieve a single benefit assessments job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_assessments_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: Benefit Assessment Job ID (required)
        :return: BenefitAssessmentJob
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_assessments_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_routing_assessments_job`")


        resource_path = '/api/v2/routing/assessments/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
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
                                            response_type='BenefitAssessmentJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_assessments_jobs(self, **kwargs) -> 'AssessmentJobListing':
        """
        Retrieve all benefit assessment jobs.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_assessments_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] division_id: Division ID(s) to filter assessment jobs by.
        :return: AssessmentJobListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_assessments_jobs" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/assessments/jobs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']

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
                                            response_type='AssessmentJobListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_availablemediatypes(self, **kwargs) -> 'AvailableMediaTypeEntityListing':
        """
        Get available media types
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_availablemediatypes(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AvailableMediaTypeEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_availablemediatypes" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/availablemediatypes'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='AvailableMediaTypeEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_directroutingbackup_settings_me(self, **kwargs) -> 'AgentDirectRoutingBackupSettings':
        """
        Get the user's Direct Routing Backup settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_directroutingbackup_settings_me(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AgentDirectRoutingBackupSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_directroutingbackup_settings_me" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/directroutingbackup/settings/me'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='AgentDirectRoutingBackupSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_domain(self, domain_id: str, **kwargs) -> 'InboundDomain':
        """
        Get domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_domain(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: InboundDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_routing_email_domain`")


        resource_path = '/api/v2/routing/email/domains/{domainId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='InboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_domain_route(self, domain_name: str, route_id: str, **kwargs) -> 'InboundRoute':
        """
        Get a route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_domain_route(domain_name, route_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param str route_id: route ID (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: InboundRoute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'route_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_domain_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `get_routing_email_domain_route`")
        # verify the required parameter 'route_id' is set
        if ('route_id' not in params) or (params['route_id'] is None):
            raise ValueError("Missing the required parameter `route_id` when calling `get_routing_email_domain_route`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes/{routeId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']
        if 'route_id' in params:
            path_params['routeId'] = params['route_id']

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
                                            response_type='InboundRoute',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_domain_route_identityresolution(self, domain_name: str, route_id: str, **kwargs) -> 'IdentityResolutionConfig':
        """
        Get a route identity resolution setting.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_domain_route_identityresolution(domain_name, route_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param str route_id: route ID (required)
        :return: IdentityResolutionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'route_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_domain_route_identityresolution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `get_routing_email_domain_route_identityresolution`")
        # verify the required parameter 'route_id' is set
        if ('route_id' not in params) or (params['route_id'] is None):
            raise ValueError("Missing the required parameter `route_id` when calling `get_routing_email_domain_route_identityresolution`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes/{routeId}/identityresolution'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']
        if 'route_id' in params:
            path_params['routeId'] = params['route_id']

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
                                            response_type='IdentityResolutionConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_domain_routes(self, domain_name: str, **kwargs) -> 'InboundRouteEntityListing':
        """
        Get routes
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_domain_routes(domain_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str pattern: Filter routes by the route's pattern property
        :param list[str] expand: Which fields, if any, to expand
        :return: InboundRouteEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'page_size', 'page_number', 'pattern', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_domain_routes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `get_routing_email_domain_routes`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'pattern' in params:
            query_params['pattern'] = params['pattern']
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
                                            response_type='InboundRouteEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_domains(self, **kwargs) -> 'InboundDomainEntityListing':
        """
        Get domains
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_domains(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param bool exclude_status: Exclude MX record data
        :param str filter: Optional search filter that, if defined, use the **filter** syntax, eg: **mySearchedPattern**. Note that **** is considered no filter.
        :return: InboundDomainEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'exclude_status', 'filter']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_domains" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/email/domains'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'exclude_status' in params:
            query_params['excludeStatus'] = params['exclude_status']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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
                                            response_type='InboundDomainEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_outbound_domain(self, domain_id: str, **kwargs) -> 'OutboundDomain':
        """
        Get domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_outbound_domain(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: OutboundDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_outbound_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_routing_email_outbound_domain`")


        resource_path = '/api/v2/routing/email/outbound/domains/{domainId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='OutboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_outbound_domain_activation(self, domain_id: str, **kwargs) -> 'EmailOutboundDomainResult':
        """
        Get activation status (cname + dkim) of an outbound domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_outbound_domain_activation(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: EmailOutboundDomainResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_outbound_domain_activation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_routing_email_outbound_domain_activation`")


        resource_path = '/api/v2/routing/email/outbound/domains/{domainId}/activation'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='EmailOutboundDomainResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_outbound_domain_search(self, domain_id: str, **kwargs) -> 'OutboundDomain':
        """
        Search a domain across organizations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_outbound_domain_search(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: OutboundDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_outbound_domain_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `get_routing_email_outbound_domain_search`")


        resource_path = '/api/v2/routing/email/outbound/domains/{domainId}/search'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='OutboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_outbound_domains(self, **kwargs) -> 'OutboundDomainEntityListing':
        """
        Get outbound domains
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_outbound_domains(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str filter: Optional search filter that, if defined, use the **filter** syntax, eg: **mySearchedPattern**. Note that **** is considered no filter.
        :return: OutboundDomainEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'filter']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_outbound_domains" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/email/outbound/domains'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'filter' in params:
            query_params['filter'] = params['filter']

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
                                            response_type='OutboundDomainEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_email_setup(self, **kwargs) -> 'EmailSetup':
        """
        Get email setup
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_email_setup(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EmailSetup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_email_setup" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/email/setup'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='EmailSetup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_language(self, language_id: str, **kwargs) -> 'Language':
        """
        Get a routing language
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_language(language_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str language_id: Language ID (required)
        :return: Language
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_language" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'language_id' is set
        if ('language_id' not in params) or (params['language_id'] is None):
            raise ValueError("Missing the required parameter `language_id` when calling `get_routing_language`")


        resource_path = '/api/v2/routing/languages/{languageId}'.replace('{format}', 'json')
        path_params = {}
        if 'language_id' in params:
            path_params['languageId'] = params['language_id']

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
                                            response_type='Language',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_languages(self, **kwargs) -> 'LanguageEntityListing':
        """
        Get the list of supported languages.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_languages(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_order: Ascending or descending sort order
        :param str name: Name
        :param list[str] id: id
        :return: LanguageEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_order', 'name', 'id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_languages" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/languages'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']

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
                                            response_type='LanguageEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_message_recipient(self, recipient_id: str, **kwargs) -> 'Recipient':
        """
        Get a recipient
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_message_recipient(recipient_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recipient_id: Recipient ID (required)
        :return: Recipient
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recipient_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_message_recipient" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recipient_id' is set
        if ('recipient_id' not in params) or (params['recipient_id'] is None):
            raise ValueError("Missing the required parameter `recipient_id` when calling `get_routing_message_recipient`")


        resource_path = '/api/v2/routing/message/recipients/{recipientId}'.replace('{format}', 'json')
        path_params = {}
        if 'recipient_id' in params:
            path_params['recipientId'] = params['recipient_id']

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
                                            response_type='Recipient',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_message_recipients(self, **kwargs) -> 'RecipientListing':
        """
        Get recipients
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_message_recipients(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messenger_type: Messenger Type
        :param str name: Recipient Name
        :param int page_size: Page size
        :param int page_number: Page number
        :return: RecipientListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messenger_type', 'name', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_message_recipients" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/message/recipients'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'messenger_type' in params:
            query_params['messengerType'] = params['messenger_type']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']

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
                                            response_type='RecipientListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_predictor(self, predictor_id: str, **kwargs) -> 'Predictor':
        """
        Retrieve a single predictor.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_predictor(predictor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str predictor_id: Predictor ID (required)
        :return: Predictor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predictor_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_predictor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'predictor_id' is set
        if ('predictor_id' not in params) or (params['predictor_id'] is None):
            raise ValueError("Missing the required parameter `predictor_id` when calling `get_routing_predictor`")


        resource_path = '/api/v2/routing/predictors/{predictorId}'.replace('{format}', 'json')
        path_params = {}
        if 'predictor_id' in params:
            path_params['predictorId'] = params['predictor_id']

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
                                            response_type='Predictor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_predictor_model_features(self, predictor_id: str, model_id: str, **kwargs) -> 'PredictorModelFeatureListing':
        """
        Retrieve Predictor Model Features.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_predictor_model_features(predictor_id, model_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str predictor_id: Predictor ID (required)
        :param str model_id: Model ID (required)
        :return: PredictorModelFeatureListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predictor_id', 'model_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_predictor_model_features" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'predictor_id' is set
        if ('predictor_id' not in params) or (params['predictor_id'] is None):
            raise ValueError("Missing the required parameter `predictor_id` when calling `get_routing_predictor_model_features`")
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params) or (params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `get_routing_predictor_model_features`")


        resource_path = '/api/v2/routing/predictors/{predictorId}/models/{modelId}/features'.replace('{format}', 'json')
        path_params = {}
        if 'predictor_id' in params:
            path_params['predictorId'] = params['predictor_id']
        if 'model_id' in params:
            path_params['modelId'] = params['model_id']

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
                                            response_type='PredictorModelFeatureListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_predictor_models(self, predictor_id: str, **kwargs) -> 'PredictorModels':
        """
        Retrieve Predictor Models and Top Features.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_predictor_models(predictor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str predictor_id: Predictor ID (required)
        :return: PredictorModels
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predictor_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_predictor_models" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'predictor_id' is set
        if ('predictor_id' not in params) or (params['predictor_id'] is None):
            raise ValueError("Missing the required parameter `predictor_id` when calling `get_routing_predictor_models`")


        resource_path = '/api/v2/routing/predictors/{predictorId}/models'.replace('{format}', 'json')
        path_params = {}
        if 'predictor_id' in params:
            path_params['predictorId'] = params['predictor_id']

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
                                            response_type='PredictorModels',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_predictors(self, **kwargs) -> 'PredictorListing':
        """
        Retrieve all predictors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_predictors(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str before: The cursor that points to the start of the set of entities that has been returned.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str limit: Number of entities to return. Maximum of 200. Deprecated in favour of pageSize
        :param str page_size: Number of entities to return. Maximum of 200.
        :param list[str] queue_id: Comma-separated list of queue Ids to filter by.
        :return: PredictorListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['before', 'after', 'limit', 'page_size', 'queue_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_predictors" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/predictors'.replace('{format}', 'json')
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
        if 'queue_id' in params:
            query_params['queueId'] = params['queue_id']

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
                                            response_type='PredictorListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_predictors_keyperformanceindicators(self, **kwargs) -> List['KeyPerformanceIndicator']:
        """
        Get a list of Key Performance Indicators
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_predictors_keyperformanceindicators(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kpi_group: The Group of Key Performance Indicators to return
        :param list[str] expand: Parameter to request additional data to return in KPI payload
        :return: list[KeyPerformanceIndicator]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kpi_group', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_predictors_keyperformanceindicators" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/predictors/keyperformanceindicators'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'kpi_group' in params:
            query_params['kpiGroup'] = params['kpi_group']
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
                                            response_type='list[KeyPerformanceIndicator]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue(self, queue_id: str, **kwargs) -> 'Queue':
        """
        Get details about this queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[str] expand: Which fields, if any, to expand
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue`")


        resource_path = '/api/v2/routing/queues/{queueId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='Queue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_assistant(self, queue_id: str, **kwargs) -> 'AssistantQueue':
        """
        Get an assistant associated with a queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_assistant(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str expand: Which fields, if any, to expand.
        :return: AssistantQueue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_assistant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_assistant`")


        resource_path = '/api/v2/routing/queues/{queueId}/assistant'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='AssistantQueue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_comparisonperiod(self, queue_id: str, comparison_period_id: str, **kwargs) -> 'ComparisonPeriod':
        """
        Get a Comparison Period.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_comparisonperiod(queue_id, comparison_period_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue id (required)
        :param str comparison_period_id: ComparisonPeriod id (required)
        :return: ComparisonPeriod
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'comparison_period_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_comparisonperiod" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_comparisonperiod`")
        # verify the required parameter 'comparison_period_id' is set
        if ('comparison_period_id' not in params) or (params['comparison_period_id'] is None):
            raise ValueError("Missing the required parameter `comparison_period_id` when calling `get_routing_queue_comparisonperiod`")


        resource_path = '/api/v2/routing/queues/{queueId}/comparisonperiods/{comparisonPeriodId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'comparison_period_id' in params:
            path_params['comparisonPeriodId'] = params['comparison_period_id']

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
                                            response_type='ComparisonPeriod',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_comparisonperiods(self, queue_id: str, **kwargs) -> 'ComparisonPeriodListing':
        """
        Get list of comparison periods
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_comparisonperiods(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue id (required)
        :return: ComparisonPeriodListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_comparisonperiods" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_comparisonperiods`")


        resource_path = '/api/v2/routing/queues/{queueId}/comparisonperiods'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='ComparisonPeriodListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_estimatedwaittime(self, queue_id: str, **kwargs) -> 'EstimatedWaitTimePredictions':
        """
        Get Estimated Wait Time
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_estimatedwaittime(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: queueId (required)
        :param str conversation_id: conversationId
        :return: EstimatedWaitTimePredictions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'conversation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_estimatedwaittime" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_estimatedwaittime`")


        resource_path = '/api/v2/routing/queues/{queueId}/estimatedwaittime'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'conversation_id' in params:
            query_params['conversationId'] = params['conversation_id']

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
                                            response_type='EstimatedWaitTimePredictions',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_identityresolution(self, queue_id: str, **kwargs) -> 'IdentityResolutionQueueConfig':
        """
        Get Queue IdentityResolution Settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_identityresolution(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :return: IdentityResolutionQueueConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_identityresolution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_identityresolution`")


        resource_path = '/api/v2/routing/queues/{queueId}/identityresolution'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='IdentityResolutionQueueConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_mediatype_estimatedwaittime(self, queue_id: str, media_type: str, **kwargs) -> 'EstimatedWaitTimePredictions':
        """
        Get Estimated Wait Time
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_mediatype_estimatedwaittime(queue_id, media_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: queueId (required)
        :param str media_type: mediaType (required)
        :param str label_id: Unique id that represents the interaction label used with media type for EWT calculation
        :return: EstimatedWaitTimePredictions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'media_type', 'label_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_mediatype_estimatedwaittime" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_mediatype_estimatedwaittime`")
        # verify the required parameter 'media_type' is set
        if ('media_type' not in params) or (params['media_type'] is None):
            raise ValueError("Missing the required parameter `media_type` when calling `get_routing_queue_mediatype_estimatedwaittime`")


        resource_path = '/api/v2/routing/queues/{queueId}/mediatypes/{mediaType}/estimatedwaittime'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'media_type' in params:
            path_params['mediaType'] = params['media_type']

        query_params = {}
        if 'label_id' in params:
            query_params['labelId'] = params['label_id']

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
                                            response_type='EstimatedWaitTimePredictions',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_members(self, queue_id: str, **kwargs) -> 'QueueMemberEntityListing':
        """
        Get the members of this queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_members(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param int page_number: 
        :param int page_size: Max value is 100
        :param str sort_order: Note: results are sorted by name.
        :param list[str] expand: Which fields, if any, to expand.
        :param str name: Filter by queue member name (contains-style search)
        :param list[str] profile_skills: Filter by profile skill (contains-style search)
        :param list[str] skills: Filter by skill (contains-style search)
        :param list[str] languages: Filter by language (contains-style search)
        :param list[str] routing_status: Filter by routing status
        :param list[str] presence: Filter by presence
        :param str member_by: Filter by member type
        :param bool joined: Filter by joined status
        :return: QueueMemberEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'page_number', 'page_size', 'sort_order', 'expand', 'name', 'profile_skills', 'skills', 'languages', 'routing_status', 'presence', 'member_by', 'joined']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_members" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_members`")


        resource_path = '/api/v2/routing/queues/{queueId}/members'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'profile_skills' in params:
            query_params['profileSkills'] = params['profile_skills']
        if 'skills' in params:
            query_params['skills'] = params['skills']
        if 'languages' in params:
            query_params['languages'] = params['languages']
        if 'routing_status' in params:
            query_params['routingStatus'] = params['routing_status']
        if 'presence' in params:
            query_params['presence'] = params['presence']
        if 'member_by' in params:
            query_params['memberBy'] = params['member_by']
        if 'joined' in params:
            query_params['joined'] = params['joined']

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
                                            response_type='QueueMemberEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_routing_queue_users is deprecated")
    def get_routing_queue_users(self, queue_id: str, **kwargs) -> 'QueueMemberEntityListingV1':
        """
        DEPRECATED: use GET /routing/queues/{queueId}/members.  Get the members of this queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_users(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param int page_number: 
        :param int page_size: Max value is 100
        :param str sort_order: Note: results are sorted by name.
        :param list[str] expand: Which fields, if any, to expand.
        :param bool joined: Filter by joined status
        :param str name: Filter by queue member name
        :param list[str] profile_skills: Filter by profile skill
        :param list[str] skills: Filter by skill
        :param list[str] languages: Filter by language
        :param list[str] routing_status: Filter by routing status
        :param list[str] presence: Filter by presence
        :return: QueueMemberEntityListingV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'page_number', 'page_size', 'sort_order', 'expand', 'joined', 'name', 'profile_skills', 'skills', 'languages', 'routing_status', 'presence']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_users`")


        resource_path = '/api/v2/routing/queues/{queueId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'joined' in params:
            query_params['joined'] = params['joined']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'profile_skills' in params:
            query_params['profileSkills'] = params['profile_skills']
        if 'skills' in params:
            query_params['skills'] = params['skills']
        if 'languages' in params:
            query_params['languages'] = params['languages']
        if 'routing_status' in params:
            query_params['routingStatus'] = params['routing_status']
        if 'presence' in params:
            query_params['presence'] = params['presence']

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
                                            response_type='QueueMemberEntityListingV1',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queue_wrapupcodes(self, queue_id: str, **kwargs) -> 'WrapupCodeEntityListing':
        """
        Get the wrap-up codes for a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queue_wrapupcodes(queue_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str name: Wrapup code's name (trailing asterisks allowed)
        :return: WrapupCodeEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'page_size', 'page_number', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queue_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_routing_queue_wrapupcodes`")


        resource_path = '/api/v2/routing/queues/{queueId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='WrapupCodeEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queues(self, **kwargs) -> 'QueueEntityListing':
        """
        Get list of queues.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queues(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :param str sort_order: Note: results are sorted by name.
        :param str name: Include only queues with the given name (leading and trailing asterisks allowed)
        :param list[str] id: Include only queues with the specified ID(s)
        :param list[str] division_id: Include only queues in the specified division ID(s)
        :param list[str] peer_id: Include only queues with the specified peer ID(s)
        :param str canned_response_library_id: Include only queues explicitly associated with the specified canned response library ID
        :param bool has_peer: Include only queues with a peer ID
        :param list[str] expand: Which fields, if any, to expand
        :return: QueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'sort_order', 'name', 'id', 'division_id', 'peer_id', 'canned_response_library_id', 'has_peer', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queues" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/queues'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']
        if 'peer_id' in params:
            query_params['peerId'] = params['peer_id']
        if 'canned_response_library_id' in params:
            query_params['cannedResponseLibraryId'] = params['canned_response_library_id']
        if 'has_peer' in params:
            query_params['hasPeer'] = params['has_peer']
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
                                            response_type='QueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queues_divisionviews(self, **kwargs) -> 'QueueEntityListing':
        """
        Get a paged listing of simplified queue objects, filterable by name, queue ID(s), or division ID(s).
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queues_divisionviews(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size [max value is 100]
        :param int page_number: Page number [max value is 5]
        :param str sort_by: Sort by
        :param str sort_order: Sort order
        :param str name: Name
        :param list[str] id: Queue ID(s)
        :param list[str] division_id: Division ID(s)
        :return: QueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_by', 'sort_order', 'name', 'id', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queues_divisionviews" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/queues/divisionviews'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']

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
                                            response_type='QueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queues_divisionviews_all(self, **kwargs) -> 'QueueEntityListing':
        """
        Get a paged listing of simplified queue objects, sorted by name.  Can be used to get a digest of all queues in an organization.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queues_divisionviews_all(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size [max value is 500]
        :param int page_number: Page number
        :param str sort_order: Sort order
        :return: QueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queues_divisionviews_all" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/queues/divisionviews/all'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='QueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_queues_me(self, **kwargs) -> 'UserQueueEntityListing':
        """
        Get a paged listing of queues the user is a member of.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_queues_me(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :param bool joined: Filter by joined status.
        :param str sort_order: Note: results are sorted by name.
        :return: UserQueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'joined', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_queues_me" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/queues/me'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'joined' in params:
            query_params['joined'] = params['joined']
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
                                            response_type='UserQueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_settings(self, **kwargs) -> 'RoutingSettings':
        """
        Get an organization's routing settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RoutingSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/settings'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='RoutingSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_settings_contactcenter(self, **kwargs) -> 'ContactCenterSettings':
        """
        Get Contact Center Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_settings_contactcenter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ContactCenterSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_settings_contactcenter" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/settings/contactcenter'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='ContactCenterSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_settings_transcription(self, **kwargs) -> 'TranscriptionSettings':
        """
        Get Transcription Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_settings_transcription(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: TranscriptionSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_settings_transcription" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/settings/transcription'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='TranscriptionSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skill(self, skill_id: str, **kwargs) -> 'RoutingSkill':
        """
        Get Routing Skill
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skill(skill_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_id: Skill ID (required)
        :return: RoutingSkill
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skill" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `get_routing_skill`")


        resource_path = '/api/v2/routing/skills/{skillId}'.replace('{format}', 'json')
        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

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
                                            response_type='RoutingSkill',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skillgroup(self, skill_group_id: str, **kwargs) -> 'SkillGroup':
        """
        Get skill group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skillgroup(skill_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :return: SkillGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skillgroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `get_routing_skillgroup`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

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
                                            response_type='SkillGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skillgroup_members(self, skill_group_id: str, **kwargs) -> 'SkillGroupMemberEntityListing':
        """
        Get skill group members
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skillgroup_members(skill_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :param int page_size: Page size
        :param str after: The cursor that points to the next item
        :param str before: The cursor that points to the previous item
        :param str expand: Expand the name on each user
        :return: SkillGroupMemberEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id', 'page_size', 'after', 'before', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skillgroup_members" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `get_routing_skillgroup_members`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}/members'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'before' in params:
            query_params['before'] = params['before']
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
                                            response_type='SkillGroupMemberEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skillgroup_members_divisions(self, skill_group_id: str, **kwargs) -> 'SkillGroupMemberDivisionList':
        """
        Get list of member divisions for this skill group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skillgroup_members_divisions(skill_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :param str expand: Expand the name on each user
        :return: SkillGroupMemberDivisionList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skillgroup_members_divisions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `get_routing_skillgroup_members_divisions`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}/members/divisions'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

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
                                            response_type='SkillGroupMemberDivisionList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skillgroups(self, **kwargs) -> 'SkillGroupEntityListing':
        """
        Get skill group listing
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skillgroups(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param str name: Return only skill group names whose names start with this value (case-insensitive matching)
        :param str after: The cursor that points to the next item
        :param str before: The cursor that points to the previous item
        :return: SkillGroupEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'name', 'after', 'before']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skillgroups" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/skillgroups'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'before' in params:
            query_params['before'] = params['before']

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
                                            response_type='SkillGroupEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_skills(self, **kwargs) -> 'SkillEntityListing':
        """
        Get the list of routing skills.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_skills(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str name: Filter for results that start with this value
        :param list[str] id: id
        :return: SkillEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'name', 'id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_skills" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/skills'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']

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
                                            response_type='SkillEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_address(self, address_id: str, **kwargs) -> 'SmsAddress':
        """
        Get an Address by Id for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_address(address_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str address_id: Address ID (required)
        :return: SmsAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_address" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'address_id' is set
        if ('address_id' not in params) or (params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `get_routing_sms_address`")


        resource_path = '/api/v2/routing/sms/addresses/{addressId}'.replace('{format}', 'json')
        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']

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
                                            response_type='SmsAddress',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_addresses(self, **kwargs) -> 'SmsAddressEntityListing':
        """
        Get a list of Addresses for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_addresses(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: SmsAddressEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_addresses" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/sms/addresses'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']

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
                                            response_type='SmsAddressEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_availablephonenumbers(self, country_code: str, phone_number_type: str, **kwargs) -> 'SMSAvailablePhoneNumberEntityListing':
        """
        Get a list of available phone numbers for SMS provisioning.
        This request will return up to 30 random phone numbers matching the criteria specified.  To get additional phone numbers repeat the request.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_availablephonenumbers(country_code, phone_number_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code: The ISO 3166-1 alpha-2 country code of the county for which available phone numbers should be returned (required)
        :param str phone_number_type: Type of available phone numbers searched (required)
        :param str region: Region/province/state that can be used to restrict the numbers returned
        :param str city: City that can be used to restrict the numbers returned
        :param str area_code: Area code that can be used to restrict the numbers returned
        :param str pattern: A pattern to match phone numbers. Valid characters are '*' and [0-9a-zA-Z]. The '*' character will match any single digit.
        :param str address_requirement: This indicates whether the phone number requires to have an Address registered.
        :return: SMSAvailablePhoneNumberEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'phone_number_type', 'region', 'city', 'area_code', 'pattern', 'address_requirement']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_availablephonenumbers" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'country_code' is set
        if ('country_code' not in params) or (params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_routing_sms_availablephonenumbers`")
        # verify the required parameter 'phone_number_type' is set
        if ('phone_number_type' not in params) or (params['phone_number_type'] is None):
            raise ValueError("Missing the required parameter `phone_number_type` when calling `get_routing_sms_availablephonenumbers`")


        resource_path = '/api/v2/routing/sms/availablephonenumbers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'country_code' in params:
            query_params['countryCode'] = params['country_code']
        if 'region' in params:
            query_params['region'] = params['region']
        if 'city' in params:
            query_params['city'] = params['city']
        if 'area_code' in params:
            query_params['areaCode'] = params['area_code']
        if 'phone_number_type' in params:
            query_params['phoneNumberType'] = params['phone_number_type']
        if 'pattern' in params:
            query_params['pattern'] = params['pattern']
        if 'address_requirement' in params:
            query_params['addressRequirement'] = params['address_requirement']

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
                                            response_type='SMSAvailablePhoneNumberEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_identityresolution_phonenumber(self, address_id: str, **kwargs) -> 'IdentityResolutionConfig':
        """
        Get a SMS identity resolution settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_identityresolution_phonenumber(address_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str address_id: Address ID (required)
        :return: IdentityResolutionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_identityresolution_phonenumber" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'address_id' is set
        if ('address_id' not in params) or (params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `get_routing_sms_identityresolution_phonenumber`")


        resource_path = '/api/v2/routing/sms/identityresolution/phonenumbers/{addressId}'.replace('{format}', 'json')
        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']

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
                                            response_type='IdentityResolutionConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_phonenumber(self, phone_number_id: str, **kwargs) -> 'SmsPhoneNumber':
        """
        Get a phone number provisioned for SMS.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_phonenumber(phone_number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number_id: phone number (required)
        :param str expand: Expand response with additional information
        :return: SmsPhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_phonenumber" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params) or (params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `get_routing_sms_phonenumber`")


        resource_path = '/api/v2/routing/sms/phonenumbers/{phoneNumberId}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']

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
                                            response_type='SmsPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_sms_phonenumbers(self, **kwargs) -> 'SmsPhoneNumberEntityListing':
        """
        Get a list of provisioned phone numbers.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_sms_phonenumbers(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number: Filter on phone number address. Allowable characters are the digits '0-9' and the wild card character '\\*'. If just digits are present, a contains search is done on the address pattern. For example, '317' could be matched anywhere in the address. An '\\*' will match multiple digits. For example, to match a specific area code within the US a pattern like '1317*' could be used.
        :param list[str] phone_number_type: Filter on phone number type
        :param list[str] phone_number_status: Filter on phone number status
        :param list[str] country_code: Filter on country code
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_by: Optional field to sort results
        :param str sort_order: Sort order
        :param str language: A language tag (which is sometimes referred to as a \"locale identifier\") to use to localize country field and sort operations
        :param str integration_id: Filter on the Genesys Cloud integration id to which the phone number belongs to
        :param str supported_content_id: Filter based on the supported content ID
        :param list[str] expand: Which fields, if any, to expand
        :return: SmsPhoneNumberEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number', 'phone_number_type', 'phone_number_status', 'country_code', 'page_size', 'page_number', 'sort_by', 'sort_order', 'language', 'integration_id', 'supported_content_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_sms_phonenumbers" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/sms/phonenumbers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'phone_number' in params:
            query_params['phoneNumber'] = params['phone_number']
        if 'phone_number_type' in params:
            query_params['phoneNumberType'] = params['phone_number_type']
        if 'phone_number_status' in params:
            query_params['phoneNumberStatus'] = params['phone_number_status']
        if 'country_code' in params:
            query_params['countryCode'] = params['country_code']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'language' in params:
            query_params['language'] = params['language']
        if 'integration_id' in params:
            query_params['integration.id'] = params['integration_id']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
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
                                            response_type='SmsPhoneNumberEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_user_directroutingbackup_settings(self, user_id: str, **kwargs) -> 'AgentDirectRoutingBackupSettings':
        """
        Get the user's Direct Routing Backup settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_user_directroutingbackup_settings(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :return: AgentDirectRoutingBackupSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_user_directroutingbackup_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_routing_user_directroutingbackup_settings`")


        resource_path = '/api/v2/routing/users/{userId}/directroutingbackup/settings'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='AgentDirectRoutingBackupSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_user_utilization(self, user_id: str, **kwargs) -> 'AgentMaxUtilizationResponse':
        """
        Get the user's max utilization settings.  If not configured, the organization-wide default is returned.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_user_utilization(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :return: AgentMaxUtilizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_user_utilization" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_routing_user_utilization`")


        resource_path = '/api/v2/routing/users/{userId}/utilization'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='AgentMaxUtilizationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization(self, **kwargs) -> 'UtilizationResponse':
        """
        Get the organization-wide max utilization settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UtilizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/utilization'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='UtilizationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_label(self, label_id: str, **kwargs) -> 'UtilizationLabel':
        """
        Get details about this utilization label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_label(label_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str label_id: Utilization Label ID (required)
        :return: UtilizationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `get_routing_utilization_label`")


        resource_path = '/api/v2/routing/utilization/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
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
                                            response_type='UtilizationLabel',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_label_agents(self, label_id: str, **kwargs) -> List[object]:
        """
        Get list of agent ids associated with a utilization label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_label_agents(label_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str label_id: Utilization Label ID (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_label_agents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `get_routing_utilization_label_agents`")


        resource_path = '/api/v2/routing/utilization/labels/{labelId}/agents'.replace('{format}', 'json')
        path_params = {}
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
                                            response_type='list[object]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_labels(self, **kwargs) -> 'UtilizationLabelEntityListing':
        """
        Get list of utilization labels
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_labels(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_order: Sort order by name
        :param str name: Utilization label's name (Wildcard is supported, e.g., 'label1*', '*label*'
        :return: UtilizationLabelEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_order', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_labels" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/utilization/labels'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
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
                                            response_type='UtilizationLabelEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_tag(self, tag_id: str, **kwargs) -> 'UtilizationTag':
        """
        Get details about this utilization tag
        
	    get_routing_utilization_tag is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_tag(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: Utilization Tag ID (required)
        :return: UtilizationTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params) or (params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `get_routing_utilization_tag`")


        resource_path = '/api/v2/routing/utilization/tags/{tagId}'.replace('{format}', 'json')
        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']

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
                                            response_type='UtilizationTag',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_tag_agents(self, tag_id: str, **kwargs) -> List[object]:
        """
        Get list of agent ids associated with a utilization tag
        
	    get_routing_utilization_tag_agents is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_tag_agents(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: Utilization Tag ID (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_tag_agents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params) or (params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `get_routing_utilization_tag_agents`")


        resource_path = '/api/v2/routing/utilization/tags/{tagId}/agents'.replace('{format}', 'json')
        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']

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
                                            response_type='list[object]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_utilization_tags(self, **kwargs) -> 'UtilizationTagEntityListing':
        """
        Get list of utilization tags
        
	    get_routing_utilization_tags is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_utilization_tags(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_order: Sort order by name
        :param str name: Utilization tag's name (Wildcard is supported, e.g., 'tag1*')
        :return: UtilizationTagEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_order', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_utilization_tags" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/utilization/tags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
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
                                            response_type='UtilizationTagEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_wrapupcode(self, code_id: str, **kwargs) -> 'WrapupCode':
        """
        Get details about this wrap-up code.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_wrapupcode(code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code_id: Wrapup Code ID (required)
        :return: WrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_wrapupcode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'code_id' is set
        if ('code_id' not in params) or (params['code_id'] is None):
            raise ValueError("Missing the required parameter `code_id` when calling `get_routing_wrapupcode`")


        resource_path = '/api/v2/routing/wrapupcodes/{codeId}'.replace('{format}', 'json')
        path_params = {}
        if 'code_id' in params:
            path_params['codeId'] = params['code_id']

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
                                            response_type='WrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_wrapupcodes(self, **kwargs) -> 'WrapupCodeEntityListing':
        """
        Get list of wrapup codes.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_wrapupcodes(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_by: Sort by
        :param str sort_order: Sort order
        :param str name: Wrapup code's name ('Sort by' param is ignored unless this field is provided)
        :param list[str] id: Filter by wrapup code ID(s)
        :param list[str] division_id: Filter by division ID(s)
        :return: WrapupCodeEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_by', 'sort_order', 'name', 'id', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/wrapupcodes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']

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
                                            response_type='WrapupCodeEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_wrapupcodes_divisionview(self, code_id: str, **kwargs) -> 'WrapupCode':
        """
        Get a simplified wrap-up code.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_wrapupcodes_divisionview(code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code_id: Wrapup Code ID (required)
        :return: WrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_wrapupcodes_divisionview" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'code_id' is set
        if ('code_id' not in params) or (params['code_id'] is None):
            raise ValueError("Missing the required parameter `code_id` when calling `get_routing_wrapupcodes_divisionview`")


        resource_path = '/api/v2/routing/wrapupcodes/divisionviews/{codeId}'.replace('{format}', 'json')
        path_params = {}
        if 'code_id' in params:
            path_params['codeId'] = params['code_id']

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
                                            response_type='WrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_routing_wrapupcodes_divisionviews(self, **kwargs) -> 'WrapupCodeEntityListing':
        """
        Get a paged listing of simplified wrapup code objects, filterable by name, wrapup code ID(s), or division ID(s).
        Specifying both name and ID parameters is not supported.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_routing_wrapupcodes_divisionviews(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str name: Name (trailing asterisks allowed)
        :param list[str] id: Wrapup code ID(s)
        :param list[str] division_id: Division ID(s)
        :param str include_state: Wrapup code state(s) to include
        :return: WrapupCodeEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'name', 'id', 'division_id', 'include_state']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_routing_wrapupcodes_divisionviews" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/wrapupcodes/divisionviews'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']
        if 'include_state' in params:
            query_params['includeState'] = params['include_state']

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
                                            response_type='WrapupCodeEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_user_queues(self, user_id: str, **kwargs) -> 'UserQueueEntityListing':
        """
        Get queues for user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_queues(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :param bool joined: Is joined to the queue
        :param list[str] division_id: Division ID(s)
        :return: UserQueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'page_size', 'page_number', 'joined', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_queues" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_queues`")


        resource_path = '/api/v2/users/{userId}/queues'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'joined' in params:
            query_params['joined'] = params['joined']
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']

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
                                            response_type='UserQueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_user_routinglanguages(self, user_id: str, **kwargs) -> 'UserLanguageEntityListing':
        """
        List routing languages assigned to a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_routinglanguages(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_order: Ascending or descending sort order
        :return: UserLanguageEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'page_size', 'page_number', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_routinglanguages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_routinglanguages`")


        resource_path = '/api/v2/users/{userId}/routinglanguages'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='UserLanguageEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_user_routingskills(self, user_id: str, **kwargs) -> 'UserSkillEntityListing':
        """
        List routing skills assigned to a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_routingskills(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str sort_order: Ascending or descending sort order
        :return: UserSkillEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'page_size', 'page_number', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_routingskills" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_routingskills`")


        resource_path = '/api/v2/users/{userId}/routingskills'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='UserSkillEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_user_skillgroups(self, user_id: str, **kwargs) -> 'UserSkillGroupEntityListing':
        """
        Get skill groups for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_skillgroups(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param int page_size: Page size
        :param str after: The cursor that points to the next page
        :param str before: The cursor that points to the previous page
        :return: UserSkillGroupEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'page_size', 'after', 'before']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_skillgroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_skillgroups`")


        resource_path = '/api/v2/users/{userId}/skillgroups'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'before' in params:
            query_params['before'] = params['before']

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
                                            response_type='UserSkillGroupEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_conversation(self, conversation_id: str, body: 'RoutingConversationAttributesRequest', **kwargs) -> 'RoutingConversationAttributesResponse':
        """
        Update attributes of an in-queue conversation
        Returns an object indicating the updated values of all settable attributes. Supported attributes: skillIds, languageId, and priority.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_conversation(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: Conversation ID (required)
        :param RoutingConversationAttributesRequest body: Conversation Attributes (required)
        :return: RoutingConversationAttributesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_conversation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_routing_conversation`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_conversation`")


        resource_path = '/api/v2/routing/conversations/{conversationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']

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
                                            response_type='RoutingConversationAttributesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_email_domain(self, domain_id: str, body: 'InboundDomainPatchRequest', **kwargs) -> 'InboundDomain':
        """
        Update domain settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_email_domain(domain_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :param InboundDomainPatchRequest body: Domain settings (required)
        :return: InboundDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_email_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `patch_routing_email_domain`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_email_domain`")


        resource_path = '/api/v2/routing/email/domains/{domainId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='InboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_email_domain_validate(self, domain_id: str, body: 'InboundDomainPatchRequest', **kwargs) -> 'InboundDomain':
        """
        Validate domain settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_email_domain_validate(domain_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :param InboundDomainPatchRequest body: Domain settings (required)
        :return: InboundDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_email_domain_validate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `patch_routing_email_domain_validate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_email_domain_validate`")


        resource_path = '/api/v2/routing/email/domains/{domainId}/validate'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='InboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_predictor(self, predictor_id: str, **kwargs) -> 'Predictor':
        """
        Update single predictor.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_predictor(predictor_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str predictor_id: Predictor ID (required)
        :param PatchPredictorRequest body: 
        :return: Predictor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['predictor_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_predictor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'predictor_id' is set
        if ('predictor_id' not in params) or (params['predictor_id'] is None):
            raise ValueError("Missing the required parameter `predictor_id` when calling `patch_routing_predictor`")


        resource_path = '/api/v2/routing/predictors/{predictorId}'.replace('{format}', 'json')
        path_params = {}
        if 'predictor_id' in params:
            path_params['predictorId'] = params['predictor_id']

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
                                            response_type='Predictor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_queue_member(self, queue_id: str, member_id: str, body: 'QueueMember', **kwargs) -> None:
        """
        Update the ring number OR joined status for a queue member.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_queue_member(queue_id, member_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str member_id: Member ID (required)
        :param QueueMember body: Queue Member (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'member_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_queue_member" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `patch_routing_queue_member`")
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `patch_routing_queue_member`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_queue_member`")


        resource_path = '/api/v2/routing/queues/{queueId}/members/{memberId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']

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

    def patch_routing_queue_members(self, queue_id: str, body: List['QueueMember'], **kwargs) -> 'QueueMemberEntityListing':
        """
        Join or unjoin a set of up to 100 users for a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_queue_members(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[QueueMember] body: Queue Members (required)
        :return: QueueMemberEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_queue_members" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `patch_routing_queue_members`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_queue_members`")


        resource_path = '/api/v2/routing/queues/{queueId}/members'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='QueueMemberEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("patch_routing_queue_user is deprecated")
    def patch_routing_queue_user(self, queue_id: str, member_id: str, body: 'QueueMember', **kwargs) -> None:
        """
        DEPRECATED: use PATCH /routing/queues/{queueId}/members/{memberId}.  Update the ring number OR joined status for a User in a Queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_queue_user(queue_id, member_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str member_id: Member ID (required)
        :param QueueMember body: Queue Member (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'member_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_queue_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `patch_routing_queue_user`")
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params) or (params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `patch_routing_queue_user`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_queue_user`")


        resource_path = '/api/v2/routing/queues/{queueId}/users/{memberId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']

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

    @deprecated("patch_routing_queue_users is deprecated")
    def patch_routing_queue_users(self, queue_id: str, body: List['QueueMember'], **kwargs) -> 'QueueMemberEntityListingV1':
        """
        DEPRECATED: use PATCH /routing/queues/{queueId}/members.  Join or unjoin a set of users for a queue.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_queue_users(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[QueueMember] body: Queue Members (required)
        :return: QueueMemberEntityListingV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_queue_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `patch_routing_queue_users`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_queue_users`")


        resource_path = '/api/v2/routing/queues/{queueId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='QueueMemberEntityListingV1',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_settings_contactcenter(self, body: 'ContactCenterSettings', **kwargs) -> None:
        """
        Update Contact Center Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_settings_contactcenter(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ContactCenterSettings body: Contact Center Settings (required)
        :return: None
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
                    " to method patch_routing_settings_contactcenter" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_settings_contactcenter`")


        resource_path = '/api/v2/routing/settings/contactcenter'.replace('{format}', 'json')
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

    def patch_routing_settings_transcription(self, body: 'TranscriptionSettings', **kwargs) -> 'TranscriptionSettings':
        """
        Patch Transcription Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_settings_transcription(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranscriptionSettings body: Organization Settings (required)
        :return: TranscriptionSettings
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
                    " to method patch_routing_settings_transcription" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_settings_transcription`")


        resource_path = '/api/v2/routing/settings/transcription'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TranscriptionSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_skillgroup(self, skill_group_id: str, body: 'SkillGroup', **kwargs) -> 'SkillGroup':
        """
        Update skill group definition
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_skillgroup(skill_group_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :param SkillGroup body: Update skill groups (required)
        :return: SkillGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_skillgroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `patch_routing_skillgroup`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_skillgroup`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

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
                                            response_type='SkillGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_routing_sms_phonenumber(self, phone_number_id: str, body: 'SmsPhoneNumberPatchRequest', **kwargs) -> 'SmsPhoneNumber':
        """
        Update a phone number provisioned for SMS.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_routing_sms_phonenumber(phone_number_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number_id: phone number (required)
        :param SmsPhoneNumberPatchRequest body: SmsPhoneNumberPatchRequest (required)
        :return: SmsPhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_routing_sms_phonenumber" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_number_id' is set
        if ('phone_number_id' not in params) or (params['phone_number_id'] is None):
            raise ValueError("Missing the required parameter `phone_number_id` when calling `patch_routing_sms_phonenumber`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_routing_sms_phonenumber`")


        resource_path = '/api/v2/routing/sms/phonenumbers/{phoneNumberId}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_number_id' in params:
            path_params['phoneNumberId'] = params['phone_number_id']

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
                                            response_type='SmsPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_queue(self, queue_id: str, user_id: str, body: 'UserQueue', **kwargs) -> 'UserQueue':
        """
        Join or unjoin a queue for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_queue(queue_id, user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param str user_id: User ID (required)
        :param UserQueue body: Queue Member (required)
        :return: UserQueue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_queue" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `patch_user_queue`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_queue`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_queue`")


        resource_path = '/api/v2/users/{userId}/queues/{queueId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserQueue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_queues(self, user_id: str, body: List['UserQueue'], **kwargs) -> 'UserQueueEntityListing':
        """
        Join or unjoin a set of queues for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_queues(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param list[UserQueue] body: User Queues (required)
        :param list[str] division_id: Division ID(s)
        :return: UserQueueEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_queues" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_queues`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_queues`")


        resource_path = '/api/v2/users/{userId}/queues'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'division_id' in params:
            query_params['divisionId'] = params['division_id']

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
                                            response_type='UserQueueEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_routinglanguage(self, user_id: str, language_id: str, body: 'UserRoutingLanguage', **kwargs) -> 'UserRoutingLanguage':
        """
        Update an assigned routing language's proficiency
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_routinglanguage(user_id, language_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param str language_id: languageId (required)
        :param UserRoutingLanguage body: Language (required)
        :return: UserRoutingLanguage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'language_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_routinglanguage" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_routinglanguage`")
        # verify the required parameter 'language_id' is set
        if ('language_id' not in params) or (params['language_id'] is None):
            raise ValueError("Missing the required parameter `language_id` when calling `patch_user_routinglanguage`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_routinglanguage`")


        resource_path = '/api/v2/users/{userId}/routinglanguages/{languageId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'language_id' in params:
            path_params['languageId'] = params['language_id']

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
                                            response_type='UserRoutingLanguage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_routinglanguages_bulk(self, user_id: str, body: List['UserRoutingLanguagePost'], **kwargs) -> 'UserLanguageEntityListing':
        """
        Assign multiple routing languages to a user. Max 50 routing languages in request body
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_routinglanguages_bulk(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param list[UserRoutingLanguagePost] body: Language (required)
        :return: UserLanguageEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_routinglanguages_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_routinglanguages_bulk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_routinglanguages_bulk`")


        resource_path = '/api/v2/users/{userId}/routinglanguages/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserLanguageEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_routingskills_bulk(self, user_id: str, body: List['UserRoutingSkillPost'], **kwargs) -> 'UserSkillEntityListing':
        """
        Assign multiple routing skills to a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_routingskills_bulk(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param list[UserRoutingSkillPost] body: Skill (required)
        :return: UserSkillEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_routingskills_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_routingskills_bulk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_routingskills_bulk`")


        resource_path = '/api/v2/users/{userId}/routingskills/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserSkillEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_queues_observations_query(self, body: 'QueueObservationQuery', **kwargs) -> 'QueueObservationQueryResponse':
        """
        Query for queue observations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_queues_observations_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param QueueObservationQuery body: query (required)
        :return: QueueObservationQueryResponse
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
                    " to method post_analytics_queues_observations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_queues_observations_query`")


        resource_path = '/api/v2/analytics/queues/observations/query'.replace('{format}', 'json')
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
                                            response_type='QueueObservationQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_routing_activity_query(self, body: 'RoutingActivityQuery', **kwargs) -> 'RoutingActivityResponse':
        """
        Query for user activity observations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_routing_activity_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RoutingActivityQuery body: query (required)
        :param int page_size: The desired page size
        :param int page_number: The desired page number
        :return: RoutingActivityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_routing_activity_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_routing_activity_query`")


        resource_path = '/api/v2/analytics/routing/activity/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']

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
                                            response_type='RoutingActivityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_assessments(self, **kwargs) -> 'BenefitAssessment':
        """
        Create a benefit assessment.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_assessments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBenefitAssessmentRequest body: 
        :return: BenefitAssessment
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
                    " to method post_routing_assessments" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/assessments'.replace('{format}', 'json')
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
                                            response_type='BenefitAssessment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_assessments_jobs(self, **kwargs) -> 'BenefitAssessmentJob':
        """
        Create a benefit assessment job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_assessments_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBenefitAssessmentJobRequest body: 
        :return: BenefitAssessmentJob
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
                    " to method post_routing_assessments_jobs" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/assessments/jobs'.replace('{format}', 'json')
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
                                            response_type='BenefitAssessmentJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_email_domain_routes(self, domain_name: str, body: 'InboundRoute', **kwargs) -> 'InboundRoute':
        """
        Create a route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_email_domain_routes(domain_name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param InboundRoute body: Route (required)
        :return: InboundRoute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_email_domain_routes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `post_routing_email_domain_routes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_email_domain_routes`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']

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
                                            response_type='InboundRoute',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_email_domain_testconnection(self, domain_id: str, **kwargs) -> 'TestMessage':
        """
        Tests the custom SMTP server integration connection set on this domain
        The request body is optional. If omitted, this endpoint will just test the connection of the Custom SMTP Server. If the body is specified, there will be an attempt to send an email message to the server.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_email_domain_testconnection(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :param TestMessage body: TestMessage
        :return: TestMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_email_domain_testconnection" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `post_routing_email_domain_testconnection`")


        resource_path = '/api/v2/routing/email/domains/{domainId}/testconnection'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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
                                            response_type='TestMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_email_domains(self, body: 'InboundDomain', **kwargs) -> 'InboundDomain':
        """
        Create a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_email_domains(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param InboundDomain body: Domain (required)
        :return: InboundDomain
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
                    " to method post_routing_email_domains" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_email_domains`")


        resource_path = '/api/v2/routing/email/domains'.replace('{format}', 'json')
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
                                            response_type='InboundDomain',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_email_outbound_domains(self, body: 'OutboundDomainRequest', **kwargs) -> 'EmailOutboundDomainResult':
        """
        Create a domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_email_outbound_domains(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OutboundDomainRequest body: Domain (required)
        :return: EmailOutboundDomainResult
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
                    " to method post_routing_email_outbound_domains" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_email_outbound_domains`")


        resource_path = '/api/v2/routing/email/outbound/domains'.replace('{format}', 'json')
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
                                            response_type='EmailOutboundDomainResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_email_outbound_domains_simulated(self, body: 'OutboundDomainRequest', **kwargs) -> 'EmailOutboundDomainResult':
        """
        Create a simulated domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_email_outbound_domains_simulated(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OutboundDomainRequest body: Domain (required)
        :return: EmailOutboundDomainResult
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
                    " to method post_routing_email_outbound_domains_simulated" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_email_outbound_domains_simulated`")


        resource_path = '/api/v2/routing/email/outbound/domains/simulated'.replace('{format}', 'json')
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
                                            response_type='EmailOutboundDomainResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_languages(self, body: 'Language', **kwargs) -> 'Language':
        """
        Create Language
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_languages(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Language body: Language (required)
        :return: Language
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
                    " to method post_routing_languages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_languages`")


        resource_path = '/api/v2/routing/languages'.replace('{format}', 'json')
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
                                            response_type='Language',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_predictors(self, **kwargs) -> 'Predictor':
        """
        Create a predictor.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_predictors(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreatePredictorRequest body: 
        :return: Predictor
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
                    " to method post_routing_predictors" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/routing/predictors'.replace('{format}', 'json')
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
                                            response_type='Predictor',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_queue_members(self, queue_id: str, body: List['WritableEntity'], **kwargs) -> None:
        """
        Bulk add or delete up to 100 queue members
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_queue_members(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[WritableEntity] body: Queue Members (required)
        :param bool delete: True to delete queue members
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body', 'delete']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_queue_members" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `post_routing_queue_members`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_queue_members`")


        resource_path = '/api/v2/routing/queues/{queueId}/members'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'delete' in params:
            query_params['delete'] = params['delete']

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

    @deprecated("post_routing_queue_users is deprecated")
    def post_routing_queue_users(self, queue_id: str, body: List['WritableEntity'], **kwargs) -> None:
        """
        DEPRECATED: use POST /routing/queues/{queueId}/members.  Bulk add or delete up to 100 queue members.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_queue_users(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[WritableEntity] body: Queue Members (required)
        :param bool delete: True to delete queue members
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body', 'delete']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_queue_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `post_routing_queue_users`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_queue_users`")


        resource_path = '/api/v2/routing/queues/{queueId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

        query_params = {}
        if 'delete' in params:
            query_params['delete'] = params['delete']

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

    def post_routing_queue_wrapupcodes(self, queue_id: str, body: List['WrapUpCodeReference'], **kwargs) -> List['WrapupCode']:
        """
        Add up to 100 wrap-up codes to a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_queue_wrapupcodes(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param list[WrapUpCodeReference] body: List of wrapup codes (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_queue_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `post_routing_queue_wrapupcodes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_queue_wrapupcodes`")


        resource_path = '/api/v2/routing/queues/{queueId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_queues(self, body: 'CreateQueueRequest', **kwargs) -> 'Queue':
        """
        Create a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_queues(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateQueueRequest body: Queue (required)
        :return: Queue
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
                    " to method post_routing_queues" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_queues`")


        resource_path = '/api/v2/routing/queues'.replace('{format}', 'json')
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
                                            response_type='Queue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_skillgroup_members_divisions(self, skill_group_id: str, **kwargs) -> None:
        """
        Add or remove member divisions for this skill group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_skillgroup_members_divisions(skill_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str skill_group_id: Skill Group ID (required)
        :param SkillGroupMemberDivisions body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_routing_skillgroup_members_divisions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'skill_group_id' is set
        if ('skill_group_id' not in params) or (params['skill_group_id'] is None):
            raise ValueError("Missing the required parameter `skill_group_id` when calling `post_routing_skillgroup_members_divisions`")


        resource_path = '/api/v2/routing/skillgroups/{skillGroupId}/members/divisions'.replace('{format}', 'json')
        path_params = {}
        if 'skill_group_id' in params:
            path_params['skillGroupId'] = params['skill_group_id']

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

    def post_routing_skillgroups(self, body: 'SkillGroupWithMemberDivisions', **kwargs) -> 'SkillGroupWithMemberDivisions':
        """
        Create a skill group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_skillgroups(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SkillGroupWithMemberDivisions body: Create skill group (required)
        :return: SkillGroupWithMemberDivisions
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
                    " to method post_routing_skillgroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_skillgroups`")


        resource_path = '/api/v2/routing/skillgroups'.replace('{format}', 'json')
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
                                            response_type='SkillGroupWithMemberDivisions',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_skills(self, body: 'RoutingSkill', **kwargs) -> 'RoutingSkill':
        """
        Create Skill
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_skills(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RoutingSkill body: Skill (required)
        :return: RoutingSkill
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
                    " to method post_routing_skills" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_skills`")


        resource_path = '/api/v2/routing/skills'.replace('{format}', 'json')
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
                                            response_type='RoutingSkill',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_sms_addresses(self, body: 'SmsAddressProvision', **kwargs) -> 'SmsAddress':
        """
        Provision an Address for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_sms_addresses(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SmsAddressProvision body: SmsAddress (required)
        :return: SmsAddress
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
                    " to method post_routing_sms_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_sms_addresses`")


        resource_path = '/api/v2/routing/sms/addresses'.replace('{format}', 'json')
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
                                            response_type='SmsAddress',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_sms_phonenumbers(self, body: 'SmsPhoneNumberProvision', **kwargs) -> 'SmsPhoneNumber':
        """
        Provision a phone number for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_sms_phonenumbers(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SmsPhoneNumberProvision body: SmsPhoneNumber (required)
        :return: SmsPhoneNumber
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
                    " to method post_routing_sms_phonenumbers" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_sms_phonenumbers`")


        resource_path = '/api/v2/routing/sms/phonenumbers'.replace('{format}', 'json')
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
                                            response_type='SmsPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_sms_phonenumbers_alphanumeric(self, body: 'SmsAlphanumericProvision', **kwargs) -> 'SmsPhoneNumber':
        """
        Provision an alphanumeric number for SMS
        
	    post_routing_sms_phonenumbers_alphanumeric is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_sms_phonenumbers_alphanumeric(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SmsAlphanumericProvision body: SmsPhoneNumber (required)
        :return: SmsPhoneNumber
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
                    " to method post_routing_sms_phonenumbers_alphanumeric" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_sms_phonenumbers_alphanumeric`")


        resource_path = '/api/v2/routing/sms/phonenumbers/alphanumeric'.replace('{format}', 'json')
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
                                            response_type='SmsPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_sms_phonenumbers_import(self, body: 'SmsPhoneNumberImport', **kwargs) -> 'SmsPhoneNumber':
        """
        Imports a phone number for SMS
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_sms_phonenumbers_import(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SmsPhoneNumberImport body: SmsPhoneNumber (required)
        :return: SmsPhoneNumber
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
                    " to method post_routing_sms_phonenumbers_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_sms_phonenumbers_import`")


        resource_path = '/api/v2/routing/sms/phonenumbers/import'.replace('{format}', 'json')
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
                                            response_type='SmsPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_utilization_labels(self, body: 'CreateUtilizationLabelRequest', **kwargs) -> 'UtilizationLabel':
        """
        Create a utilization label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_utilization_labels(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateUtilizationLabelRequest body: UtilizationLabel (required)
        :return: UtilizationLabel
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
                    " to method post_routing_utilization_labels" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_utilization_labels`")


        resource_path = '/api/v2/routing/utilization/labels'.replace('{format}', 'json')
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
                                            response_type='UtilizationLabel',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_utilization_tags(self, body: 'CreateUtilizationTagRequest', **kwargs) -> 'UtilizationTag':
        """
        Create an utilization tag
        
	    post_routing_utilization_tags is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_utilization_tags(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateUtilizationTagRequest body: UtilizationTag (required)
        :return: UtilizationTag
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
                    " to method post_routing_utilization_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_utilization_tags`")


        resource_path = '/api/v2/routing/utilization/tags'.replace('{format}', 'json')
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
                                            response_type='UtilizationTag',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_routing_wrapupcodes(self, body: 'WrapupCodeRequest', **kwargs) -> 'WrapupCode':
        """
        Create a wrap-up code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_routing_wrapupcodes(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WrapupCodeRequest body: WrapupCode (required)
        :return: WrapupCode
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
                    " to method post_routing_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_routing_wrapupcodes`")


        resource_path = '/api/v2/routing/wrapupcodes'.replace('{format}', 'json')
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
                                            response_type='WrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_user_routinglanguages(self, user_id: str, body: 'UserRoutingLanguagePost', **kwargs) -> 'UserRoutingLanguage':
        """
        Assign a routing language to a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_user_routinglanguages(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param UserRoutingLanguagePost body: Language (required)
        :return: UserRoutingLanguage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_routinglanguages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_user_routinglanguages`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_user_routinglanguages`")


        resource_path = '/api/v2/users/{userId}/routinglanguages'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserRoutingLanguage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_user_routingskills(self, user_id: str, body: 'UserRoutingSkillPost', **kwargs) -> 'UserRoutingSkill':
        """
        Assign a routing skill to a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_user_routingskills(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param UserRoutingSkillPost body: Skill (required)
        :return: UserRoutingSkill
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_routingskills" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_user_routingskills`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_user_routingskills`")


        resource_path = '/api/v2/users/{userId}/routingskills'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserRoutingSkill',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_directroutingbackup_settings_me(self, body: 'AgentDirectRoutingBackupSettings', **kwargs) -> 'AgentDirectRoutingBackupSettings':
        """
        Update the user's Direct Routing Backup settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_directroutingbackup_settings_me(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentDirectRoutingBackupSettings body: directRoutingBackup (required)
        :return: AgentDirectRoutingBackupSettings
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
                    " to method put_routing_directroutingbackup_settings_me" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_directroutingbackup_settings_me`")


        resource_path = '/api/v2/routing/directroutingbackup/settings/me'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AgentDirectRoutingBackupSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_email_domain_route(self, domain_name: str, route_id: str, body: 'InboundRoute', **kwargs) -> 'InboundRoute':
        """
        Update a route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_email_domain_route(domain_name, route_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param str route_id: route ID (required)
        :param InboundRoute body: Route (required)
        :return: InboundRoute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'route_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_email_domain_route" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `put_routing_email_domain_route`")
        # verify the required parameter 'route_id' is set
        if ('route_id' not in params) or (params['route_id'] is None):
            raise ValueError("Missing the required parameter `route_id` when calling `put_routing_email_domain_route`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_email_domain_route`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes/{routeId}'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']
        if 'route_id' in params:
            path_params['routeId'] = params['route_id']

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
                                            response_type='InboundRoute',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_email_domain_route_identityresolution(self, domain_name: str, route_id: str, body: 'IdentityResolutionConfig', **kwargs) -> 'IdentityResolutionConfig':
        """
        Update identity resolution settings for a route.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_email_domain_route_identityresolution(domain_name, route_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_name: email domain (required)
        :param str route_id: route ID (required)
        :param IdentityResolutionConfig body:  (required)
        :return: IdentityResolutionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_name', 'route_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_email_domain_route_identityresolution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_name' is set
        if ('domain_name' not in params) or (params['domain_name'] is None):
            raise ValueError("Missing the required parameter `domain_name` when calling `put_routing_email_domain_route_identityresolution`")
        # verify the required parameter 'route_id' is set
        if ('route_id' not in params) or (params['route_id'] is None):
            raise ValueError("Missing the required parameter `route_id` when calling `put_routing_email_domain_route_identityresolution`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_email_domain_route_identityresolution`")


        resource_path = '/api/v2/routing/email/domains/{domainName}/routes/{routeId}/identityresolution'.replace('{format}', 'json')
        path_params = {}
        if 'domain_name' in params:
            path_params['domainName'] = params['domain_name']
        if 'route_id' in params:
            path_params['routeId'] = params['route_id']

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
                                            response_type='IdentityResolutionConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_email_outbound_domain_activation(self, domain_id: str, **kwargs) -> 'EmailOutboundDomainResult':
        """
        Request an activation status (cname + dkim) update of an outbound domain
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_email_outbound_domain_activation(domain_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain_id: domain ID (required)
        :return: EmailOutboundDomainResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_email_outbound_domain_activation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params) or (params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `put_routing_email_outbound_domain_activation`")


        resource_path = '/api/v2/routing/email/outbound/domains/{domainId}/activation'.replace('{format}', 'json')
        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EmailOutboundDomainResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_message_recipient(self, recipient_id: str, body: 'RecipientRequest', **kwargs) -> 'Recipient':
        """
        Update a recipient
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_message_recipient(recipient_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recipient_id: Recipient ID (required)
        :param RecipientRequest body: Recipient (required)
        :return: Recipient
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recipient_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_message_recipient" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recipient_id' is set
        if ('recipient_id' not in params) or (params['recipient_id'] is None):
            raise ValueError("Missing the required parameter `recipient_id` when calling `put_routing_message_recipient`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_message_recipient`")


        resource_path = '/api/v2/routing/message/recipients/{recipientId}'.replace('{format}', 'json')
        path_params = {}
        if 'recipient_id' in params:
            path_params['recipientId'] = params['recipient_id']

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
                                            response_type='Recipient',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_queue(self, queue_id: str, body: 'QueueRequest', **kwargs) -> 'Queue':
        """
        Update a queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_queue(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param QueueRequest body: Queue (required)
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_queue" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `put_routing_queue`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_queue`")


        resource_path = '/api/v2/routing/queues/{queueId}'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='Queue',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_queue_identityresolution(self, queue_id: str, body: 'IdentityResolutionQueueConfig', **kwargs) -> 'IdentityResolutionQueueConfig':
        """
        Update Queue IdentityResolution Settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_queue_identityresolution(queue_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str queue_id: Queue ID (required)
        :param IdentityResolutionQueueConfig body:  (required)
        :return: IdentityResolutionQueueConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_queue_identityresolution" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params) or (params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `put_routing_queue_identityresolution`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_queue_identityresolution`")


        resource_path = '/api/v2/routing/queues/{queueId}/identityresolution'.replace('{format}', 'json')
        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']

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
                                            response_type='IdentityResolutionQueueConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_settings(self, body: 'RoutingSettings', **kwargs) -> 'RoutingSettings':
        """
        Update an organization's routing settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_settings(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RoutingSettings body: Organization Settings (required)
        :return: RoutingSettings
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
                    " to method put_routing_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_settings`")


        resource_path = '/api/v2/routing/settings'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RoutingSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_settings_transcription(self, body: 'TranscriptionSettings', **kwargs) -> 'TranscriptionSettings':
        """
        Update Transcription Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_settings_transcription(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranscriptionSettings body: Organization Settings (required)
        :return: TranscriptionSettings
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
                    " to method put_routing_settings_transcription" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_settings_transcription`")


        resource_path = '/api/v2/routing/settings/transcription'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TranscriptionSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_sms_identityresolution_phonenumber(self, address_id: str, body: 'IdentityResolutionConfig', **kwargs) -> 'IdentityResolutionConfig':
        """
        Update an SMS identity resolution settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_sms_identityresolution_phonenumber(address_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str address_id: Address ID (required)
        :param IdentityResolutionConfig body:  (required)
        :return: IdentityResolutionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_sms_identityresolution_phonenumber" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'address_id' is set
        if ('address_id' not in params) or (params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `put_routing_sms_identityresolution_phonenumber`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_sms_identityresolution_phonenumber`")


        resource_path = '/api/v2/routing/sms/identityresolution/phonenumbers/{addressId}'.replace('{format}', 'json')
        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']

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
                                            response_type='IdentityResolutionConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_user_directroutingbackup_settings(self, user_id: str, body: 'AgentDirectRoutingBackupSettings', **kwargs) -> 'AgentDirectRoutingBackupSettings':
        """
        Update the user's Direct Routing Backup settings.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_user_directroutingbackup_settings(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param AgentDirectRoutingBackupSettings body: directRoutingBackup (required)
        :return: AgentDirectRoutingBackupSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_user_directroutingbackup_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `put_routing_user_directroutingbackup_settings`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_user_directroutingbackup_settings`")


        resource_path = '/api/v2/routing/users/{userId}/directroutingbackup/settings'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='AgentDirectRoutingBackupSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_user_utilization(self, user_id: str, body: 'UtilizationRequest', **kwargs) -> 'AgentMaxUtilizationResponse':
        """
        Update the user's max utilization settings.  Include only those media types requiring custom configuration.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_user_utilization(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param UtilizationRequest body: utilization (required)
        :return: AgentMaxUtilizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_user_utilization" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `put_routing_user_utilization`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_user_utilization`")


        resource_path = '/api/v2/routing/users/{userId}/utilization'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='AgentMaxUtilizationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_utilization(self, body: 'UtilizationRequest', **kwargs) -> 'UtilizationResponse':
        """
        Update the organization-wide max utilization settings.  Include only those media types requiring custom configuration.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_utilization(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UtilizationRequest body: utilization (required)
        :return: UtilizationResponse
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
                    " to method put_routing_utilization" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_utilization`")


        resource_path = '/api/v2/routing/utilization'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UtilizationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_utilization_label(self, label_id: str, body: 'UpdateUtilizationLabelRequest', **kwargs) -> 'UtilizationLabel':
        """
        Update a utilization label
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_utilization_label(label_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str label_id: Utilization Label ID (required)
        :param UpdateUtilizationLabelRequest body: UtilizationLabel (required)
        :return: UtilizationLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_utilization_label" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'label_id' is set
        if ('label_id' not in params) or (params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `put_routing_utilization_label`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_utilization_label`")


        resource_path = '/api/v2/routing/utilization/labels/{labelId}'.replace('{format}', 'json')
        path_params = {}
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UtilizationLabel',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_routing_wrapupcode(self, code_id: str, body: 'WrapupCodeRequest', **kwargs) -> 'WrapupCode':
        """
        Update wrap-up code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_routing_wrapupcode(code_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str code_id: Wrapup Code ID (required)
        :param WrapupCodeRequest body: WrapupCode (required)
        :return: WrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_routing_wrapupcode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'code_id' is set
        if ('code_id' not in params) or (params['code_id'] is None):
            raise ValueError("Missing the required parameter `code_id` when calling `put_routing_wrapupcode`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_routing_wrapupcode`")


        resource_path = '/api/v2/routing/wrapupcodes/{codeId}'.replace('{format}', 'json')
        path_params = {}
        if 'code_id' in params:
            path_params['codeId'] = params['code_id']

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
                                            response_type='WrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_user_routingskill(self, user_id: str, skill_id: str, body: 'UserRoutingSkill', **kwargs) -> 'UserRoutingSkill':
        """
        Update an assigned routing skill's proficiency
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_user_routingskill(user_id, skill_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param str skill_id: skillId (required)
        :param UserRoutingSkill body: Skill (required)
        :return: UserRoutingSkill
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'skill_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_user_routingskill" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `put_user_routingskill`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `put_user_routingskill`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_user_routingskill`")


        resource_path = '/api/v2/users/{userId}/routingskills/{skillId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

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
                                            response_type='UserRoutingSkill',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_user_routingskills_bulk(self, user_id: str, body: List['UserRoutingSkillPost'], **kwargs) -> 'UserSkillEntityListing':
        """
        Assign multiple routing skills to a user, replacing any current assignments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_user_routingskills_bulk(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param list[UserRoutingSkillPost] body: Skill (required)
        :return: UserSkillEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_user_routingskills_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `put_user_routingskills_bulk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_user_routingskills_bulk`")


        resource_path = '/api/v2/users/{userId}/routingskills/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='UserSkillEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
