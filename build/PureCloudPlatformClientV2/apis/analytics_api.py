# coding: utf-8

"""
AnalyticsApi.py
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

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from ..utils import deprecated

from typing import List
from typing import Dict
from typing import Any

from ..models import Empty
from ..models import ActionAggregateQueryResponse
from ..models import ActionAggregationQuery
from ..models import ActionAsyncAggregateQueryResponse
from ..models import ActionAsyncAggregationQuery
from ..models import AnalyticsConversationAsyncQueryResponse
from ..models import AnalyticsConversationQueryResponse
from ..models import AnalyticsConversationWithoutAttributes
from ..models import AnalyticsConversationWithoutAttributesMultiGetResponse
from ..models import AnalyticsDataRetentionResponse
from ..models import AnalyticsReportingSettings
from ..models import AnalyticsUserDetailsAsyncQueryResponse
from ..models import AnalyticsUserDetailsQueryResponse
from ..models import AsyncConversationQuery
from ..models import AsyncQueryResponse
from ..models import AsyncQueryStatus
from ..models import AsyncUserDetailsQuery
from ..models import BotAggregateQueryResponse
from ..models import BotAggregationQuery
from ..models import BotAsyncAggregateQueryResponse
from ..models import BotAsyncAggregationQuery
from ..models import ConversationActivityQuery
from ..models import ConversationActivityResponse
from ..models import ConversationAggregateQueryResponse
from ..models import ConversationAggregationQuery
from ..models import ConversationAsyncAggregateQueryResponse
from ..models import ConversationAsyncAggregationQuery
from ..models import ConversationQuery
from ..models import DataAvailabilityResponse
from ..models import ErrorBody
from ..models import EvaluationAggregateQueryResponse
from ..models import EvaluationAggregationQuery
from ..models import EvaluationAsyncAggregateQueryResponse
from ..models import EvaluationAsyncAggregationQuery
from ..models import FlowActivityQuery
from ..models import FlowActivityResponse
from ..models import FlowAggregateQueryResponse
from ..models import FlowAggregationQuery
from ..models import FlowAsyncAggregateQueryResponse
from ..models import FlowAsyncAggregationQuery
from ..models import FlowObservationQuery
from ..models import FlowObservationQueryResponse
from ..models import JourneyAggregateQueryResponse
from ..models import JourneyAggregationQuery
from ..models import JourneyAsyncAggregateQueryResponse
from ..models import JourneyAsyncAggregationQuery
from ..models import KnowledgeAggregateQueryResponse
from ..models import KnowledgeAggregationQuery
from ..models import KnowledgeAsyncAggregateQueryResponse
from ..models import KnowledgeAsyncAggregationQuery
from ..models import PropertyIndexRequest
from ..models import QueueObservationQuery
from ..models import QueueObservationQueryResponse
from ..models import ReportMetaData
from ..models import ReportMetaDataEntityListing
from ..models import ReportRunEntry
from ..models import ReportRunEntryEntityDomainListing
from ..models import ReportSchedule
from ..models import ReportScheduleEntityListing
from ..models import ReportingExportJobListing
from ..models import ReportingExportJobRequest
from ..models import ReportingExportJobResponse
from ..models import ReportingExportMetadataJobListing
from ..models import ReportingTurnsResponse
from ..models import ResolutionAsyncAggregateQueryResponse
from ..models import ResolutionAsyncAggregationQuery
from ..models import RoutingActivityQuery
from ..models import RoutingActivityResponse
from ..models import RunNowResponse
from ..models import SurveyAggregateQueryResponse
from ..models import SurveyAggregationQuery
from ..models import SurveyAsyncAggregateQueryResponse
from ..models import SurveyAsyncAggregationQuery
from ..models import TaskManagementAggregateQueryResponse
from ..models import TaskManagementAggregationQuery
from ..models import TaskManagementAsyncAggregateQueryResponse
from ..models import TaskManagementAsyncAggregationQuery
from ..models import TeamActivityQuery
from ..models import TeamActivityResponse
from ..models import TranscriptAggregateQueryResponse
from ..models import TranscriptAggregationQuery
from ..models import TranscriptAsyncAggregateQueryResponse
from ..models import TranscriptAsyncAggregationQuery
from ..models import TranscriptConversationDetailSearchRequest
from ..models import UpdateAnalyticsDataRetentionRequest
from ..models import UserActivityQuery
from ..models import UserActivityResponse
from ..models import UserAggregateQueryResponse
from ..models import UserAggregationQuery
from ..models import UserAsyncAggregateQueryResponse
from ..models import UserAsyncAggregationQuery
from ..models import UserDetailsQuery
from ..models import UserObservationQuery
from ..models import UserObservationQueryResponse

class AnalyticsApi(object):
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

    def delete_analytics_conversations_details_job(self, job_id: str, **kwargs) -> None:
        """
        Delete/cancel an async details job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_analytics_conversations_details_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_analytics_conversations_details_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `delete_analytics_conversations_details_job`")


        resource_path = '/api/v2/analytics/conversations/details/jobs/{jobId}'.replace('{format}', 'json')
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

    def delete_analytics_reporting_schedule(self, schedule_id: str, **kwargs) -> None:
        """
        Delete a scheduled report job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_analytics_reporting_schedule(schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_analytics_reporting_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `delete_analytics_reporting_schedule`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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

    def delete_analytics_users_details_job(self, job_id: str, **kwargs) -> None:
        """
        Delete/cancel an async request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_analytics_users_details_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_analytics_users_details_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `delete_analytics_users_details_job`")


        resource_path = '/api/v2/analytics/users/details/jobs/{jobId}'.replace('{format}', 'json')
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

    def get_analytics_actions_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for action aggregates
        
	    get_analytics_actions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_actions_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_actions_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_actions_aggregates_job`")


        resource_path = '/api/v2/analytics/actions/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_actions_aggregates_job_results(self, job_id: str, **kwargs) -> 'ActionAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_actions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_actions_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: ActionAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_actions_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_actions_aggregates_job_results`")


        resource_path = '/api/v2/analytics/actions/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='ActionAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_botflow_reportingturns(self, bot_flow_id: str, **kwargs) -> 'ReportingTurnsResponse':
        """
        Get Reporting Turns.
        Returns the reporting turns grouped by session, in reverse chronological order from the date the session was created, with the reporting turns from the most recent session appearing at the start of the list. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. Note: resources returned by this endpoint do not persist indefinitely, as they auto delete after a predefined period.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_botflow_reportingturns(bot_flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bot_flow_id: ID of the bot flow. (required)
        :param str after: The cursor that points to the ID of the last item in the list of entities that has been returned.
        :param str page_size: Max number of entities to return. Maximum of 250
        :param str interval: Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: '2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07'. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss
        :param str action_id: Optional action ID to get the reporting turns associated to a particular flow action
        :param str session_id: Optional session ID to get the reporting turns for a particular session. Specifying a session ID alongside an action ID or a language or any ask action results is not allowed.
        :param str language: Optional language code to get the reporting turns for a particular language
        :param str ask_action_results: Optional case-insensitive comma separated list of ask action results to filter the reporting turns.
        :return: ReportingTurnsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bot_flow_id', 'after', 'page_size', 'interval', 'action_id', 'session_id', 'language', 'ask_action_results']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_botflow_reportingturns" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bot_flow_id' is set
        if ('bot_flow_id' not in params) or (params['bot_flow_id'] is None):
            raise ValueError("Missing the required parameter `bot_flow_id` when calling `get_analytics_botflow_reportingturns`")


        resource_path = '/api/v2/analytics/botflows/{botFlowId}/reportingturns'.replace('{format}', 'json')
        path_params = {}
        if 'bot_flow_id' in params:
            path_params['botFlowId'] = params['bot_flow_id']

        query_params = {}
        if 'after' in params:
            query_params['after'] = params['after']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'interval' in params:
            query_params['interval'] = params['interval']
        if 'action_id' in params:
            query_params['actionId'] = params['action_id']
        if 'session_id' in params:
            query_params['sessionId'] = params['session_id']
        if 'language' in params:
            query_params['language'] = params['language']
        if 'ask_action_results' in params:
            query_params['askActionResults'] = params['ask_action_results']

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
                                            response_type='ReportingTurnsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_bots_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for bot aggregates
        
	    get_analytics_bots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_bots_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_bots_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_bots_aggregates_job`")


        resource_path = '/api/v2/analytics/bots/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_bots_aggregates_job_results(self, job_id: str, **kwargs) -> 'BotAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_bots_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_bots_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: BotAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_bots_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_bots_aggregates_job_results`")


        resource_path = '/api/v2/analytics/bots/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='BotAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversation_details(self, conversation_id: str, **kwargs) -> 'AnalyticsConversationWithoutAttributes':
        """
        Get a conversation by id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversation_details(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: AnalyticsConversationWithoutAttributes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversation_details" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_analytics_conversation_details`")


        resource_path = '/api/v2/analytics/conversations/{conversationId}/details'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']

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
                                            response_type='AnalyticsConversationWithoutAttributes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for conversation aggregates
        
	    get_analytics_conversations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_conversations_aggregates_job`")


        resource_path = '/api/v2/analytics/conversations/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_aggregates_job_results(self, job_id: str, **kwargs) -> 'ConversationAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_conversations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: ConversationAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_conversations_aggregates_job_results`")


        resource_path = '/api/v2/analytics/conversations/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='ConversationAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_details(self, **kwargs) -> 'AnalyticsConversationWithoutAttributesMultiGetResponse':
        """
        Gets multiple conversations by id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_details(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] id: Comma-separated conversation ids
        :return: AnalyticsConversationWithoutAttributesMultiGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_details" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/conversations/details'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
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
                                            response_type='AnalyticsConversationWithoutAttributesMultiGetResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_details_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for conversation details
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_details_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_details_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_conversations_details_job`")


        resource_path = '/api/v2/analytics/conversations/details/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_details_job_results(self, job_id: str, **kwargs) -> 'AnalyticsConversationAsyncQueryResponse':
        """
        Fetch a page of results for an async details job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_details_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Indicates where to resume query results (not required for first page)
        :param int page_size: The desired maximum number of results
        :return: AnalyticsConversationAsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_details_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_conversations_details_job_results`")


        resource_path = '/api/v2/analytics/conversations/details/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']
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
                                            response_type='AnalyticsConversationAsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_conversations_details_jobs_availability(self, **kwargs) -> 'DataAvailabilityResponse':
        """
        Lookup the datalake availability date and time
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_conversations_details_jobs_availability(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: DataAvailabilityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_conversations_details_jobs_availability" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/conversations/details/jobs/availability'.replace('{format}', 'json')
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
                                            response_type='DataAvailabilityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_dataretention_settings(self, **kwargs) -> 'AnalyticsDataRetentionResponse':
        """
        Get analytics data retention setting
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_dataretention_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AnalyticsDataRetentionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_dataretention_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/dataretention/settings'.replace('{format}', 'json')
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
                                            response_type='AnalyticsDataRetentionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_evaluations_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for evaluation aggregates
        
	    get_analytics_evaluations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_evaluations_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_evaluations_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_evaluations_aggregates_job`")


        resource_path = '/api/v2/analytics/evaluations/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_evaluations_aggregates_job_results(self, job_id: str, **kwargs) -> 'EvaluationAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_evaluations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_evaluations_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: EvaluationAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_evaluations_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_evaluations_aggregates_job_results`")


        resource_path = '/api/v2/analytics/evaluations/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='EvaluationAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_flows_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for Flow aggregates
        
	    get_analytics_flows_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_flows_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_flows_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_flows_aggregates_job`")


        resource_path = '/api/v2/analytics/flows/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_flows_aggregates_job_results(self, job_id: str, **kwargs) -> 'FlowAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_flows_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_flows_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: FlowAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_flows_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_flows_aggregates_job_results`")


        resource_path = '/api/v2/analytics/flows/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='FlowAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_journeys_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for journey aggregates
        
	    get_analytics_journeys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_journeys_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_journeys_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_journeys_aggregates_job`")


        resource_path = '/api/v2/analytics/journeys/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_journeys_aggregates_job_results(self, job_id: str, **kwargs) -> 'JourneyAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_journeys_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_journeys_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: JourneyAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_journeys_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_journeys_aggregates_job_results`")


        resource_path = '/api/v2/analytics/journeys/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='JourneyAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_knowledge_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for knowledge aggregates
        
	    get_analytics_knowledge_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_knowledge_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_knowledge_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_knowledge_aggregates_job`")


        resource_path = '/api/v2/analytics/knowledge/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_knowledge_aggregates_job_results(self, job_id: str, **kwargs) -> 'KnowledgeAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_knowledge_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_knowledge_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: KnowledgeAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_knowledge_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_knowledge_aggregates_job_results`")


        resource_path = '/api/v2/analytics/knowledge/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='KnowledgeAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_exports(self, **kwargs) -> 'ReportingExportJobListing':
        """
        Get all view export requests for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_exports(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :return: ReportingExportJobListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_exports" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/exports'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='ReportingExportJobListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_exports_metadata(self, **kwargs) -> 'ReportingExportMetadataJobListing':
        """
        Get all export metadata
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_exports_metadata(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ReportingExportMetadataJobListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_exports_metadata" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/exports/metadata'.replace('{format}', 'json')
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
                                            response_type='ReportingExportMetadataJobListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_metadata(self, **kwargs) -> 'ReportMetaDataEntityListing':
        """
        Get list of reporting metadata.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_metadata(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :param str locale: Locale
        :return: ReportMetaDataEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size', 'locale']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_metadata" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/metadata'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'locale' in params:
            query_params['locale'] = params['locale']

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
                                            response_type='ReportMetaDataEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_report_id_metadata(self, report_id: str, **kwargs) -> 'ReportMetaData':
        """
        Get a reporting metadata.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_report_id_metadata(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_id: Report ID (required)
        :param str locale: Locale
        :return: ReportMetaData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_id', 'locale']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_report_id_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'report_id' is set
        if ('report_id' not in params) or (params['report_id'] is None):
            raise ValueError("Missing the required parameter `report_id` when calling `get_analytics_reporting_report_id_metadata`")


        resource_path = '/api/v2/analytics/reporting/{reportId}/metadata'.replace('{format}', 'json')
        path_params = {}
        if 'report_id' in params:
            path_params['reportId'] = params['report_id']

        query_params = {}
        if 'locale' in params:
            query_params['locale'] = params['locale']

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
                                            response_type='ReportMetaData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_reportformats(self, **kwargs) -> List[str]:
        """
        Get a list of report formats
        Get a list of report formats.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_reportformats(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_reportformats" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/reportformats'.replace('{format}', 'json')
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
                                            response_type='list[str]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_schedule(self, schedule_id: str, **kwargs) -> 'ReportSchedule':
        """
        Get a scheduled report job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_schedule(schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :return: ReportSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_analytics_reporting_schedule`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='ReportSchedule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_schedule_history(self, schedule_id: str, **kwargs) -> 'ReportRunEntryEntityDomainListing':
        """
        Get list of completed scheduled report jobs.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_schedule_history(schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :param int page_number: 
        :param int page_size: 
        :return: ReportRunEntryEntityDomainListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id', 'page_number', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_schedule_history" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_analytics_reporting_schedule_history`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}/history'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='ReportRunEntryEntityDomainListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_schedule_history_latest(self, schedule_id: str, **kwargs) -> 'ReportRunEntry':
        """
        Get most recently completed scheduled report job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_schedule_history_latest(schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :return: ReportRunEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_schedule_history_latest" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_analytics_reporting_schedule_history_latest`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}/history/latest'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='ReportRunEntry',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_schedule_history_run_id(self, run_id: str, schedule_id: str, **kwargs) -> 'ReportRunEntry':
        """
        A completed scheduled report job
        A completed scheduled report job.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_schedule_history_run_id(run_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str run_id: Run ID (required)
        :param str schedule_id: Schedule ID (required)
        :return: ReportRunEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['run_id', 'schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_schedule_history_run_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'run_id' is set
        if ('run_id' not in params) or (params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `get_analytics_reporting_schedule_history_run_id`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_analytics_reporting_schedule_history_run_id`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}/history/{runId}'.replace('{format}', 'json')
        path_params = {}
        if 'run_id' in params:
            path_params['runId'] = params['run_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='ReportRunEntry',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_schedules(self, **kwargs) -> 'ReportScheduleEntityListing':
        """
        Get a list of scheduled report jobs
        Get a list of scheduled report jobs.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_schedules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :return: ReportScheduleEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_schedules" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/schedules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
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
                                            response_type='ReportScheduleEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_settings(self, **kwargs) -> 'AnalyticsReportingSettings':
        """
        Get AnalyticsReportingSettings for an organization
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AnalyticsReportingSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/settings'.replace('{format}', 'json')
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
                                            response_type='AnalyticsReportingSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_timeperiods(self, **kwargs) -> List[str]:
        """
        Get a list of report time periods.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_timeperiods(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_timeperiods" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/timeperiods'.replace('{format}', 'json')
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
                                            response_type='list[str]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_resolutions_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for resolution aggregates
        
	    get_analytics_resolutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_resolutions_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_resolutions_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_resolutions_aggregates_job`")


        resource_path = '/api/v2/analytics/resolutions/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_resolutions_aggregates_job_results(self, job_id: str, **kwargs) -> 'ResolutionAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_resolutions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_resolutions_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: ResolutionAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_resolutions_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_resolutions_aggregates_job_results`")


        resource_path = '/api/v2/analytics/resolutions/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='ResolutionAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_surveys_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for survey aggregates
        
	    get_analytics_surveys_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_surveys_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_surveys_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_surveys_aggregates_job`")


        resource_path = '/api/v2/analytics/surveys/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_surveys_aggregates_job_results(self, job_id: str, **kwargs) -> 'SurveyAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_surveys_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_surveys_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: SurveyAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_surveys_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_surveys_aggregates_job_results`")


        resource_path = '/api/v2/analytics/surveys/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='SurveyAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_taskmanagement_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for task management aggregates
        
	    get_analytics_taskmanagement_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_taskmanagement_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_taskmanagement_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_taskmanagement_aggregates_job`")


        resource_path = '/api/v2/analytics/taskmanagement/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_taskmanagement_aggregates_job_results(self, job_id: str, **kwargs) -> 'TaskManagementAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async task management query
        
	    get_analytics_taskmanagement_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_taskmanagement_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: TaskManagementAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_taskmanagement_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_taskmanagement_aggregates_job_results`")


        resource_path = '/api/v2/analytics/taskmanagement/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='TaskManagementAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_transcripts_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for transcript aggregates
        
	    get_analytics_transcripts_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_transcripts_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_transcripts_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_transcripts_aggregates_job`")


        resource_path = '/api/v2/analytics/transcripts/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_transcripts_aggregates_job_results(self, job_id: str, **kwargs) -> 'TranscriptAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_transcripts_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_transcripts_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: TranscriptAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_transcripts_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_transcripts_aggregates_job_results`")


        resource_path = '/api/v2/analytics/transcripts/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='TranscriptAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_users_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for user aggregates
        
	    get_analytics_users_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_users_aggregates_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_users_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_users_aggregates_job`")


        resource_path = '/api/v2/analytics/users/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_users_aggregates_job_results(self, job_id: str, **kwargs) -> 'UserAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_users_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_users_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: UserAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_users_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_users_aggregates_job_results`")


        resource_path = '/api/v2/analytics/users/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']

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
                                            response_type='UserAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_users_details_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for user details
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_users_details_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: AsyncQueryStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_users_details_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_users_details_job`")


        resource_path = '/api/v2/analytics/users/details/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_users_details_job_results(self, job_id: str, **kwargs) -> 'AnalyticsUserDetailsAsyncQueryResponse':
        """
        Fetch a page of results for an async query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_users_details_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Indicates where to resume query results (not required for first page)
        :param int page_size: The desired maximum number of results
        :return: AnalyticsUserDetailsAsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_users_details_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_users_details_job_results`")


        resource_path = '/api/v2/analytics/users/details/jobs/{jobId}/results'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']
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
                                            response_type='AnalyticsUserDetailsAsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_users_details_jobs_availability(self, **kwargs) -> 'DataAvailabilityResponse':
        """
        Lookup the datalake availability date and time
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_users_details_jobs_availability(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: DataAvailabilityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_users_details_jobs_availability" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/users/details/jobs/availability'.replace('{format}', 'json')
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
                                            response_type='DataAvailabilityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_analytics_reporting_settings(self, body: 'AnalyticsReportingSettings', **kwargs) -> 'AnalyticsReportingSettings':
        """
        Patch AnalyticsReportingSettings values for an organization
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_analytics_reporting_settings(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AnalyticsReportingSettings body: AnalyticsReportingSettingsRequest (required)
        :return: AnalyticsReportingSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_analytics_reporting_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_analytics_reporting_settings`")


        resource_path = '/api/v2/analytics/reporting/settings'.replace('{format}', 'json')
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
                                            response_type='AnalyticsReportingSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_actions_aggregates_jobs(self, body: 'ActionAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for action aggregates asynchronously
        
	    post_analytics_actions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_actions_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ActionAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_actions_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_actions_aggregates_jobs`")


        resource_path = '/api/v2/analytics/actions/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_actions_aggregates_query(self, body: 'ActionAggregationQuery', **kwargs) -> 'ActionAggregateQueryResponse':
        """
        Query for action aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_actions_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ActionAggregationQuery body: query (required)
        :return: ActionAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_actions_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_actions_aggregates_query`")


        resource_path = '/api/v2/analytics/actions/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='ActionAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_bots_aggregates_jobs(self, body: 'BotAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for bot aggregates asynchronously
        
	    post_analytics_bots_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_bots_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BotAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_bots_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_bots_aggregates_jobs`")


        resource_path = '/api/v2/analytics/bots/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_bots_aggregates_query(self, body: 'BotAggregationQuery', **kwargs) -> 'BotAggregateQueryResponse':
        """
        Query for bot aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_bots_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BotAggregationQuery body: query (required)
        :return: BotAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_bots_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_bots_aggregates_query`")


        resource_path = '/api/v2/analytics/bots/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='BotAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversation_details_properties(self, conversation_id: str, body: 'PropertyIndexRequest', **kwargs) -> 'PropertyIndexRequest':
        """
        Index conversation properties
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversation_details_properties(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param PropertyIndexRequest body: request (required)
        :return: PropertyIndexRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversation_details_properties" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_analytics_conversation_details_properties`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversation_details_properties`")


        resource_path = '/api/v2/analytics/conversations/{conversationId}/details/properties'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PropertyIndexRequest',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_activity_query(self, body: 'ConversationActivityQuery', **kwargs) -> 'ConversationActivityResponse':
        """
        Query for conversation activity observations
        
	    post_analytics_conversations_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_activity_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationActivityQuery body: query (required)
        :param int page_size: The desired page size
        :param int page_number: The desired page number
        :return: ConversationActivityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_activity_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_activity_query`")


        resource_path = '/api/v2/analytics/conversations/activity/query'.replace('{format}', 'json')
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
                                            response_type='ConversationActivityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_aggregates_jobs(self, body: 'ConversationAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for conversation aggregates asynchronously
        
	    post_analytics_conversations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_aggregates_jobs`")


        resource_path = '/api/v2/analytics/conversations/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_aggregates_query(self, body: 'ConversationAggregationQuery', **kwargs) -> 'ConversationAggregateQueryResponse':
        """
        Query for conversation aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationAggregationQuery body: query (required)
        :return: ConversationAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_aggregates_query`")


        resource_path = '/api/v2/analytics/conversations/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='ConversationAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_details_jobs(self, body: 'AsyncConversationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for conversation details asynchronously
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_details_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AsyncConversationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_details_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_details_jobs`")


        resource_path = '/api/v2/analytics/conversations/details/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_details_query(self, body: 'ConversationQuery', **kwargs) -> 'AnalyticsConversationQueryResponse':
        """
        Query for conversation details
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_details_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationQuery body: query (required)
        :return: AnalyticsConversationQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_details_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_details_query`")


        resource_path = '/api/v2/analytics/conversations/details/query'.replace('{format}', 'json')
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
                                            response_type='AnalyticsConversationQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_conversations_transcripts_query(self, body: 'TranscriptConversationDetailSearchRequest', **kwargs) -> 'AnalyticsConversationWithoutAttributesMultiGetResponse':
        """
        Search resources.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_conversations_transcripts_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranscriptConversationDetailSearchRequest body: Search request options (required)
        :return: AnalyticsConversationWithoutAttributesMultiGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_conversations_transcripts_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_conversations_transcripts_query`")


        resource_path = '/api/v2/analytics/conversations/transcripts/query'.replace('{format}', 'json')
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
                                            response_type='AnalyticsConversationWithoutAttributesMultiGetResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_evaluations_aggregates_jobs(self, body: 'EvaluationAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for evaluation aggregates asynchronously
        
	    post_analytics_evaluations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_evaluations_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EvaluationAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_evaluations_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_evaluations_aggregates_jobs`")


        resource_path = '/api/v2/analytics/evaluations/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_evaluations_aggregates_query(self, body: 'EvaluationAggregationQuery', **kwargs) -> 'EvaluationAggregateQueryResponse':
        """
        Query for evaluation aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_evaluations_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EvaluationAggregationQuery body: query (required)
        :return: EvaluationAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_evaluations_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_evaluations_aggregates_query`")


        resource_path = '/api/v2/analytics/evaluations/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='EvaluationAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_flows_activity_query(self, body: 'FlowActivityQuery', **kwargs) -> 'FlowActivityResponse':
        """
        Query for flow activity observations
        
	    post_analytics_flows_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flows_activity_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowActivityQuery body: query (required)
        :param int page_size: The desired page size
        :param int page_number: The desired page number
        :return: FlowActivityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_flows_activity_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flows_activity_query`")


        resource_path = '/api/v2/analytics/flows/activity/query'.replace('{format}', 'json')
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
                                            response_type='FlowActivityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_flows_aggregates_jobs(self, body: 'FlowAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for flow aggregates asynchronously
        
	    post_analytics_flows_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flows_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_flows_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flows_aggregates_jobs`")


        resource_path = '/api/v2/analytics/flows/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_flows_aggregates_query(self, body: 'FlowAggregationQuery', **kwargs) -> 'FlowAggregateQueryResponse':
        """
        Query for flow aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flows_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowAggregationQuery body: query (required)
        :return: FlowAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_flows_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flows_aggregates_query`")


        resource_path = '/api/v2/analytics/flows/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='FlowAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_flows_observations_query(self, body: 'FlowObservationQuery', **kwargs) -> 'FlowObservationQueryResponse':
        """
        Query for flow observations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flows_observations_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowObservationQuery body: query (required)
        :return: FlowObservationQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_flows_observations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flows_observations_query`")


        resource_path = '/api/v2/analytics/flows/observations/query'.replace('{format}', 'json')
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
                                            response_type='FlowObservationQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_journeys_aggregates_jobs(self, body: 'JourneyAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for journey aggregates asynchronously
        
	    post_analytics_journeys_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_journeys_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param JourneyAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_journeys_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_journeys_aggregates_jobs`")


        resource_path = '/api/v2/analytics/journeys/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_journeys_aggregates_query(self, body: 'JourneyAggregationQuery', **kwargs) -> 'JourneyAggregateQueryResponse':
        """
        Query for journey aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_journeys_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param JourneyAggregationQuery body: query (required)
        :return: JourneyAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_journeys_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_journeys_aggregates_query`")


        resource_path = '/api/v2/analytics/journeys/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='JourneyAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_knowledge_aggregates_jobs(self, body: 'KnowledgeAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for knowledge aggregates asynchronously
        
	    post_analytics_knowledge_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_knowledge_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KnowledgeAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_knowledge_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_knowledge_aggregates_jobs`")


        resource_path = '/api/v2/analytics/knowledge/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_knowledge_aggregates_query(self, body: 'KnowledgeAggregationQuery', **kwargs) -> 'KnowledgeAggregateQueryResponse':
        """
        Query for knowledge aggregates
        
	    post_analytics_knowledge_aggregates_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_knowledge_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param KnowledgeAggregationQuery body: query (required)
        :return: KnowledgeAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_knowledge_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_knowledge_aggregates_query`")


        resource_path = '/api/v2/analytics/knowledge/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='KnowledgeAggregateQueryResponse',
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
        for key, val in iteritems(params['kwargs']):
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

    def post_analytics_reporting_exports(self, body: 'ReportingExportJobRequest', **kwargs) -> 'ReportingExportJobResponse':
        """
        Generate a view export request
        This API creates a reporting export but the desired way to export analytics data is to use the analytics query APIs instead

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_exports(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportingExportJobRequest body: ReportingExportJobRequest (required)
        :return: ReportingExportJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_reporting_exports" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_reporting_exports`")


        resource_path = '/api/v2/analytics/reporting/exports'.replace('{format}', 'json')
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
                                            response_type='ReportingExportJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_reporting_schedule_runreport(self, schedule_id: str, **kwargs) -> 'RunNowResponse':
        """
        Place a scheduled report immediately into the reporting queue
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_schedule_runreport(schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :return: RunNowResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_reporting_schedule_runreport" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_analytics_reporting_schedule_runreport`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}/runreport'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='RunNowResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_reporting_schedules(self, body: 'ReportSchedule', **kwargs) -> 'ReportSchedule':
        """
        Create a scheduled report job
        Create a scheduled report job.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_schedules(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReportSchedule body: ReportSchedule (required)
        :return: ReportSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_reporting_schedules" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_reporting_schedules`")


        resource_path = '/api/v2/analytics/reporting/schedules'.replace('{format}', 'json')
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
                                            response_type='ReportSchedule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_resolutions_aggregates_jobs(self, body: 'ResolutionAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for resolution aggregates asynchronously
        
	    post_analytics_resolutions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_resolutions_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ResolutionAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_resolutions_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_resolutions_aggregates_jobs`")


        resource_path = '/api/v2/analytics/resolutions/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_routing_activity_query(self, body: 'RoutingActivityQuery', **kwargs) -> 'RoutingActivityResponse':
        """
        Query for user activity observations
        
	    post_analytics_routing_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

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
        for key, val in iteritems(params['kwargs']):
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

    def post_analytics_surveys_aggregates_jobs(self, body: 'SurveyAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for survey aggregates asynchronously
        
	    post_analytics_surveys_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_surveys_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SurveyAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_surveys_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_surveys_aggregates_jobs`")


        resource_path = '/api/v2/analytics/surveys/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_surveys_aggregates_query(self, body: 'SurveyAggregationQuery', **kwargs) -> 'SurveyAggregateQueryResponse':
        """
        Query for survey aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_surveys_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SurveyAggregationQuery body: query (required)
        :return: SurveyAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_surveys_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_surveys_aggregates_query`")


        resource_path = '/api/v2/analytics/surveys/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='SurveyAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_taskmanagement_aggregates_jobs(self, body: 'TaskManagementAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for task management aggregates asynchronously
        
	    post_analytics_taskmanagement_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_taskmanagement_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TaskManagementAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_taskmanagement_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_taskmanagement_aggregates_jobs`")


        resource_path = '/api/v2/analytics/taskmanagement/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_taskmanagement_aggregates_query(self, body: 'TaskManagementAggregationQuery', **kwargs) -> 'TaskManagementAggregateQueryResponse':
        """
        Query for task management aggregates
        
	    post_analytics_taskmanagement_aggregates_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_taskmanagement_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TaskManagementAggregationQuery body: query (required)
        :return: TaskManagementAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_taskmanagement_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_taskmanagement_aggregates_query`")


        resource_path = '/api/v2/analytics/taskmanagement/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='TaskManagementAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_teams_activity_query(self, body: 'TeamActivityQuery', **kwargs) -> 'TeamActivityResponse':
        """
        Query for team activity observations
        
	    post_analytics_teams_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_teams_activity_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TeamActivityQuery body: query (required)
        :param int page_size: The desired page size
        :param int page_number: The desired page number
        :return: TeamActivityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_teams_activity_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_teams_activity_query`")


        resource_path = '/api/v2/analytics/teams/activity/query'.replace('{format}', 'json')
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
                                            response_type='TeamActivityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_transcripts_aggregates_jobs(self, body: 'TranscriptAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for transcript aggregates asynchronously
        
	    post_analytics_transcripts_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_transcripts_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranscriptAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_transcripts_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_transcripts_aggregates_jobs`")


        resource_path = '/api/v2/analytics/transcripts/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_transcripts_aggregates_query(self, body: 'TranscriptAggregationQuery', **kwargs) -> 'TranscriptAggregateQueryResponse':
        """
        Query for transcript aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_transcripts_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranscriptAggregationQuery body: query (required)
        :return: TranscriptAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_transcripts_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_transcripts_aggregates_query`")


        resource_path = '/api/v2/analytics/transcripts/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='TranscriptAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_activity_query(self, body: 'UserActivityQuery', **kwargs) -> 'UserActivityResponse':
        """
        Query for user activity observations
        
	    post_analytics_users_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_activity_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserActivityQuery body: query (required)
        :param int page_size: The desired page size
        :param int page_number: The desired page number
        :return: UserActivityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_activity_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_activity_query`")


        resource_path = '/api/v2/analytics/users/activity/query'.replace('{format}', 'json')
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
                                            response_type='UserActivityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_aggregates_jobs(self, body: 'UserAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for user aggregates asynchronously
        
	    post_analytics_users_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_aggregates_jobs`")


        resource_path = '/api/v2/analytics/users/aggregates/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_aggregates_query(self, body: 'UserAggregationQuery', **kwargs) -> 'UserAggregateQueryResponse':
        """
        Query for user aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserAggregationQuery body: query (required)
        :return: UserAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_aggregates_query`")


        resource_path = '/api/v2/analytics/users/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='UserAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_details_jobs(self, body: 'AsyncUserDetailsQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for user details asynchronously
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_details_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AsyncUserDetailsQuery body: query (required)
        :return: AsyncQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_details_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_details_jobs`")


        resource_path = '/api/v2/analytics/users/details/jobs'.replace('{format}', 'json')
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
                                            response_type='AsyncQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_details_query(self, body: 'UserDetailsQuery', **kwargs) -> 'AnalyticsUserDetailsQueryResponse':
        """
        Query for user details
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_details_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserDetailsQuery body: query (required)
        :return: AnalyticsUserDetailsQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_details_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_details_query`")


        resource_path = '/api/v2/analytics/users/details/query'.replace('{format}', 'json')
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
                                            response_type='AnalyticsUserDetailsQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_users_observations_query(self, body: 'UserObservationQuery', **kwargs) -> 'UserObservationQueryResponse':
        """
        Query for user observations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_users_observations_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserObservationQuery body: query (required)
        :return: UserObservationQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_users_observations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_users_observations_query`")


        resource_path = '/api/v2/analytics/users/observations/query'.replace('{format}', 'json')
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
                                            response_type='UserObservationQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_analytics_dataretention_settings(self, body: 'UpdateAnalyticsDataRetentionRequest', **kwargs) -> 'AnalyticsDataRetentionResponse':
        """
        Update analytics data retention setting
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_analytics_dataretention_settings(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateAnalyticsDataRetentionRequest body: retentionDays (required)
        :return: AnalyticsDataRetentionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_analytics_dataretention_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_analytics_dataretention_settings`")


        resource_path = '/api/v2/analytics/dataretention/settings'.replace('{format}', 'json')
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
                                            response_type='AnalyticsDataRetentionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_analytics_reporting_schedule(self, schedule_id: str, body: 'ReportSchedule', **kwargs) -> 'ReportSchedule':
        """
        Update a scheduled report job.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_analytics_reporting_schedule(schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str schedule_id: Schedule ID (required)
        :param ReportSchedule body: ReportSchedule (required)
        :return: ReportSchedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_analytics_reporting_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `put_analytics_reporting_schedule`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_analytics_reporting_schedule`")


        resource_path = '/api/v2/analytics/reporting/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='ReportSchedule',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
