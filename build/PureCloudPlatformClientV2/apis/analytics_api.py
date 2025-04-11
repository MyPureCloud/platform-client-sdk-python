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
from ..models import AgentCopilotAggregateQueryResponse
from ..models import AgentCopilotAggregationQuery
from ..models import AgentCopilotAsyncAggregateQueryResponse
from ..models import AgentCopilotAsyncAggregationQuery
from ..models import AgentStateCountsRequest
from ..models import AgentStateQueryRequest
from ..models import AnalyticsAgentStateAgentResponse
from ..models import AnalyticsAgentStateCountsResponse
from ..models import AnalyticsAgentStateQueryResponse
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
from ..models import DashboardConfigurationBulkRequest
from ..models import DashboardConfigurationListing
from ..models import DashboardConfigurationQueryRequest
from ..models import DashboardUser
from ..models import DashboardUserListing
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
from ..models import FlowExecutionAggregateQueryResponse
from ..models import FlowExecutionAggregationQuery
from ..models import FlowExecutionAsyncAggregateQueryResponse
from ..models import FlowExecutionAsyncAggregationQuery
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
from ..models import RateLimitAggregateQueryResponse
from ..models import RateLimitAggregationQuery
from ..models import ReportingExportJobListing
from ..models import ReportingExportJobRequest
from ..models import ReportingExportJobResponse
from ..models import ReportingExportMetadataJobListing
from ..models import ReportingTurnsResponse
from ..models import ResolutionAggregateQueryResponse
from ..models import ResolutionAggregationQuery
from ..models import ResolutionAsyncAggregateQueryResponse
from ..models import ResolutionAsyncAggregationQuery
from ..models import RoutingActivityQuery
from ..models import RoutingActivityResponse
from ..models import SessionsResponse
from ..models import SummaryAggregateQueryResponse
from ..models import SummaryAggregationQuery
from ..models import SummaryAsyncAggregateQueryResponse
from ..models import SummaryAsyncAggregationQuery
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def get_analytics_agent_status(self, user_id: str, **kwargs) -> 'AnalyticsAgentStateAgentResponse':
        """
        Get an agent and their active sessions by user ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_agent_status(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: userId (required)
        :return: AnalyticsAgentStateAgentResponse
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
                    " to method get_analytics_agent_status" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_analytics_agent_status`")


        resource_path = '/api/v2/analytics/agents/{userId}/status'.replace('{format}', 'json')
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
                                            response_type='AnalyticsAgentStateAgentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_agentcopilots_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for agent copilot aggregates
        
	    get_analytics_agentcopilots_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_agentcopilots_aggregates_job(job_id, callback=callback_function)

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
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_agentcopilots_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_agentcopilots_aggregates_job`")


        resource_path = '/api/v2/analytics/agentcopilots/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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

    def get_analytics_agentcopilots_aggregates_job_results(self, job_id: str, **kwargs) -> 'AgentCopilotAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_agentcopilots_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_agentcopilots_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: AgentCopilotAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_agentcopilots_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_agentcopilots_aggregates_job_results`")


        resource_path = '/api/v2/analytics/agentcopilots/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
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
                                            response_type='AgentCopilotAsyncAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_botflow_divisions_reportingturns(self, bot_flow_id: str, **kwargs) -> 'ReportingTurnsResponse':
        """
        Get Reporting Turns (division aware).
        Returns the reporting turns for the specified flow, filtered by the clients divisions and grouped by session, in reverse chronological order from the date the session was created, with the reporting turns from the most recent session appearing at the start of the list. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_botflow_divisions_reportingturns(bot_flow_id, callback=callback_function)

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
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_botflow_divisions_reportingturns" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bot_flow_id' is set
        if ('bot_flow_id' not in params) or (params['bot_flow_id'] is None):
            raise ValueError("Missing the required parameter `bot_flow_id` when calling `get_analytics_botflow_divisions_reportingturns`")


        resource_path = '/api/v2/analytics/botflows/{botFlowId}/divisions/reportingturns'.replace('{format}', 'json')
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

    @deprecated("get_analytics_botflow_reportingturns is deprecated")
    def get_analytics_botflow_reportingturns(self, bot_flow_id: str, **kwargs) -> 'ReportingTurnsResponse':
        """
        Get Reporting Turns.
        Deprecated: Please use GET /analytics/botflows/{botFlowId}/divisions/reportingturns instead. Returns the reporting turns grouped by session, in reverse chronological order from the date the session was created, with the reporting turns from the most recent session appearing at the start of the list. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

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
        for key, val in params['kwargs'].items():
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

    def get_analytics_botflow_sessions(self, bot_flow_id: str, **kwargs) -> 'SessionsResponse':
        """
        Get Bot Flow Sessions.
        Returns the bot flow sessions in reverse chronological order from the date they were created. It is expected that the client will URL encode the request URI once only. For pagination, clients should keep sending requests using the value of 'nextUri' in the response, until it's no longer present, only then have all items have been returned. The 'nextUri' value in the response is already URL encoded (so it doesn't need to be encoded again). Note: resources returned by this endpoint are not persisted indefinitely, as they are deleted after approximately, but not before, 10 days.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_botflow_sessions(bot_flow_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bot_flow_id: ID of the bot flow. (required)
        :param str after: The cursor that points to the ID of the last item in the list of entities that has been returned.
        :param str page_size: Max number of entities to return. Maximum of 250
        :param str interval: Date range filter based on the date the individual resources were completed. UTC is the default if no TZ is supplied, however alternate timezones can be used e.g: '2022-11-22T09:11:11.111+08:00/2022-11-30T07:17:44.586-07'. . Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss
        :param str bot_result_categories: Optional case-insensitive comma separated list of Bot Result Categories to filter sessions by.
        :param str end_language: Optional case-insensitive language code to filter sessions by the language the sessions ended in.
        :return: SessionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bot_flow_id', 'after', 'page_size', 'interval', 'bot_result_categories', 'end_language']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_botflow_sessions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bot_flow_id' is set
        if ('bot_flow_id' not in params) or (params['bot_flow_id'] is None):
            raise ValueError("Missing the required parameter `bot_flow_id` when calling `get_analytics_botflow_sessions`")


        resource_path = '/api/v2/analytics/botflows/{botFlowId}/sessions'.replace('{format}', 'json')
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
        if 'bot_result_categories' in params:
            query_params['botResultCategories'] = params['bot_result_categories']
        if 'end_language' in params:
            query_params['endLanguage'] = params['end_language']

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
                                            response_type='SessionsResponse',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def get_analytics_flowexecutions_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for flow execution aggregates
        
	    get_analytics_flowexecutions_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_flowexecutions_aggregates_job(job_id, callback=callback_function)

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
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_flowexecutions_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_flowexecutions_aggregates_job`")


        resource_path = '/api/v2/analytics/flowexecutions/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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

    def get_analytics_flowexecutions_aggregates_job_results(self, job_id: str, **kwargs) -> 'FlowExecutionAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_flowexecutions_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_flowexecutions_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: FlowExecutionAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_flowexecutions_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_flowexecutions_aggregates_job_results`")


        resource_path = '/api/v2/analytics/flowexecutions/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
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
                                            response_type='FlowExecutionAsyncAggregateQueryResponse',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def get_analytics_reporting_dashboards_user(self, user_id: str, **kwargs) -> 'DashboardUser':
        """
        Get dashboards summary for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_dashboards_user(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :return: DashboardUser
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
                    " to method get_analytics_reporting_dashboards_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_analytics_reporting_dashboards_user`")


        resource_path = '/api/v2/analytics/reporting/dashboards/users/{userId}'.replace('{format}', 'json')
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
                                            response_type='DashboardUser',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_dashboards_users(self, **kwargs) -> 'DashboardUserListing':
        """
        Get dashboards summary for users in a org
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_dashboards_users(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sort_by: 
        :param int page_number: 
        :param int page_size: 
        :param list[str] id: A list of user IDs to fetch by bulk
        :param str state: Only list users of this state
        :param bool deleted_only: Only list users with deleted dashboards
        :return: DashboardUserListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort_by', 'page_number', 'page_size', 'id', 'state', 'deleted_only']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_dashboards_users" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/analytics/reporting/dashboards/users'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'state' in params:
            query_params['state'] = params['state']
        if 'deleted_only' in params:
            query_params['deletedOnly'] = params['deleted_only']

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
                                            response_type='DashboardUserListing',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def get_analytics_reporting_settings_dashboards_query(self, dashboard_type: str, dashboard_access_filter: str, **kwargs) -> 'DashboardConfigurationListing':
        """
        Get list of dashboard configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_settings_dashboards_query(dashboard_type, dashboard_access_filter, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_type: List dashboard of given type (required)
        :param str dashboard_access_filter: Filter dashboard based on the owner of dashboard (required)
        :param str name: name of the dashboard
        :param str dashboard_state: List dashboard of given state
        :param str sort_by: 
        :param int page_number: 
        :param int page_size: 
        :return: DashboardConfigurationListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_type', 'dashboard_access_filter', 'name', 'dashboard_state', 'sort_by', 'page_number', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_settings_dashboards_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_type' is set
        if ('dashboard_type' not in params) or (params['dashboard_type'] is None):
            raise ValueError("Missing the required parameter `dashboard_type` when calling `get_analytics_reporting_settings_dashboards_query`")
        # verify the required parameter 'dashboard_access_filter' is set
        if ('dashboard_access_filter' not in params) or (params['dashboard_access_filter'] is None):
            raise ValueError("Missing the required parameter `dashboard_access_filter` when calling `get_analytics_reporting_settings_dashboards_query`")


        resource_path = '/api/v2/analytics/reporting/settings/dashboards/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'name' in params:
            query_params['name'] = params['name']
        if 'dashboard_type' in params:
            query_params['dashboardType'] = params['dashboard_type']
        if 'dashboard_state' in params:
            query_params['dashboardState'] = params['dashboard_state']
        if 'dashboard_access_filter' in params:
            query_params['dashboardAccessFilter'] = params['dashboard_access_filter']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
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
                                            response_type='DashboardConfigurationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_analytics_reporting_settings_user_dashboards(self, user_id: str, **kwargs) -> 'DashboardConfigurationListing':
        """
        Get list of dashboards for an user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_reporting_settings_user_dashboards(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: User ID (required)
        :param str sort_by: 
        :param int page_number: 
        :param int page_size: 
        :param bool public_only: If true, retrieve only public dashboards
        :param bool favorite_only: If true, retrieve only favorite dashboards
        :param bool deleted_only: If true, retrieve only deleted dashboards that are still recoverable
        :param str name: retrieve dashboards that match with given name
        :return: DashboardConfigurationListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'sort_by', 'page_number', 'page_size', 'public_only', 'favorite_only', 'deleted_only', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_reporting_settings_user_dashboards" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_analytics_reporting_settings_user_dashboards`")


        resource_path = '/api/v2/analytics/reporting/settings/users/{userId}/dashboards'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'public_only' in params:
            query_params['publicOnly'] = params['public_only']
        if 'favorite_only' in params:
            query_params['favoriteOnly'] = params['favorite_only']
        if 'deleted_only' in params:
            query_params['deletedOnly'] = params['deleted_only']
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
                                            response_type='DashboardConfigurationListing',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def get_analytics_summaries_aggregates_job(self, job_id: str, **kwargs) -> 'AsyncQueryStatus':
        """
        Get status for async query for summary aggregates
        
	    get_analytics_summaries_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_summaries_aggregates_job(job_id, callback=callback_function)

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
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_summaries_aggregates_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_summaries_aggregates_job`")


        resource_path = '/api/v2/analytics/summaries/aggregates/jobs/{jobId}'.replace('{format}', 'json')
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

    def get_analytics_summaries_aggregates_job_results(self, job_id: str, **kwargs) -> 'SummaryAsyncAggregateQueryResponse':
        """
        Fetch a page of results for an async aggregates query
        
	    get_analytics_summaries_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_analytics_summaries_aggregates_job_results(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :param str cursor: Cursor token to retrieve next page
        :return: SummaryAsyncAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytics_summaries_aggregates_job_results" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_analytics_summaries_aggregates_job_results`")


        resource_path = '/api/v2/analytics/summaries/aggregates/jobs/{jobId}/results'.replace('{format}', 'json')
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
                                            response_type='SummaryAsyncAggregateQueryResponse',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def post_analytics_agentcopilots_aggregates_jobs(self, body: 'AgentCopilotAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for agent copilot aggregates asynchronously
        
	    post_analytics_agentcopilots_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_agentcopilots_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentCopilotAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
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
                    " to method post_analytics_agentcopilots_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_agentcopilots_aggregates_jobs`")


        resource_path = '/api/v2/analytics/agentcopilots/aggregates/jobs'.replace('{format}', 'json')
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

    def post_analytics_agentcopilots_aggregates_query(self, body: 'AgentCopilotAggregationQuery', **kwargs) -> 'AgentCopilotAggregateQueryResponse':
        """
        Query for agent copilot aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_agentcopilots_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentCopilotAggregationQuery body: query (required)
        :return: AgentCopilotAggregateQueryResponse
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
                    " to method post_analytics_agentcopilots_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_agentcopilots_aggregates_query`")


        resource_path = '/api/v2/analytics/agentcopilots/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='AgentCopilotAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_agents_status_counts(self, body: 'AgentStateCountsRequest', **kwargs) -> 'AnalyticsAgentStateCountsResponse':
        """
        Count agents by segment type
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_agents_status_counts(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentStateCountsRequest body: query (required)
        :return: AnalyticsAgentStateCountsResponse
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
                    " to method post_analytics_agents_status_counts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_agents_status_counts`")


        resource_path = '/api/v2/analytics/agents/status/counts'.replace('{format}', 'json')
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
                                            response_type='AnalyticsAgentStateCountsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_agents_status_query(self, body: 'AgentStateQueryRequest', **kwargs) -> 'AnalyticsAgentStateQueryResponse':
        """
        Retrieve the top 50 agents matching the query filters
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_agents_status_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentStateQueryRequest body: query (required)
        :return: AnalyticsAgentStateQueryResponse
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
                    " to method post_analytics_agents_status_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_agents_status_query`")


        resource_path = '/api/v2/analytics/agents/status/query'.replace('{format}', 'json')
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
                                            response_type='AnalyticsAgentStateQueryResponse',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def post_analytics_flowexecutions_aggregates_jobs(self, body: 'FlowExecutionAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for flow execution aggregates asynchronously
        
	    post_analytics_flowexecutions_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flowexecutions_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowExecutionAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
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
                    " to method post_analytics_flowexecutions_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flowexecutions_aggregates_jobs`")


        resource_path = '/api/v2/analytics/flowexecutions/aggregates/jobs'.replace('{format}', 'json')
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

    def post_analytics_flowexecutions_aggregates_query(self, body: 'FlowExecutionAggregationQuery', **kwargs) -> 'FlowExecutionAggregateQueryResponse':
        """
        Query for flow execution aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_flowexecutions_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FlowExecutionAggregationQuery body: query (required)
        :return: FlowExecutionAggregateQueryResponse
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
                    " to method post_analytics_flowexecutions_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_flowexecutions_aggregates_query`")


        resource_path = '/api/v2/analytics/flowexecutions/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='FlowExecutionAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_flows_activity_query(self, body: 'FlowActivityQuery', **kwargs) -> 'FlowActivityResponse':
        """
        Query for flow activity observations
        

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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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

    def post_analytics_ratelimits_aggregates_query(self, body: 'RateLimitAggregationQuery', **kwargs) -> 'RateLimitAggregateQueryResponse':
        """
        Query for limits rate limit aggregates. Data populated when limits reach 90% of the maximum. Not a source of truth for limits hit but a best effort estimate.
        The 'max' property can be used to determine estimated rate limit value hit. See https://developer.genesys.cloud/organization/organization/limits#available-limits for limits that are trackable (Operational Events Enabled).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_ratelimits_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RateLimitAggregationQuery body: query (required)
        :return: RateLimitAggregateQueryResponse
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
                    " to method post_analytics_ratelimits_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_ratelimits_aggregates_query`")


        resource_path = '/api/v2/analytics/ratelimits/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='RateLimitAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_reporting_dashboards_users_bulk_remove(self, body: List['str'], **kwargs) -> None:
        """
        Bulk soft delete dashboards owned by other user(s)
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_dashboards_users_bulk_remove(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] body: List of userIds (required)
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
                    " to method post_analytics_reporting_dashboards_users_bulk_remove" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_reporting_dashboards_users_bulk_remove`")


        resource_path = '/api/v2/analytics/reporting/dashboards/users/bulk/remove'.replace('{format}', 'json')
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
                                            response_type=None,
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
        for key, val in params['kwargs'].items():
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

    def post_analytics_reporting_settings_dashboards_bulk_remove(self, body: 'DashboardConfigurationBulkRequest', **kwargs) -> None:
        """
        Bulk soft delete dashboard configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_settings_dashboards_bulk_remove(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DashboardConfigurationBulkRequest body:  (required)
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
                    " to method post_analytics_reporting_settings_dashboards_bulk_remove" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_reporting_settings_dashboards_bulk_remove`")


        resource_path = '/api/v2/analytics/reporting/settings/dashboards/bulk/remove'.replace('{format}', 'json')
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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_reporting_settings_dashboards_query(self, body: 'DashboardConfigurationQueryRequest', **kwargs) -> 'DashboardConfigurationListing':
        """
        Query dashboard configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_reporting_settings_dashboards_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DashboardConfigurationQueryRequest body:  (required)
        :return: DashboardConfigurationListing
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
                    " to method post_analytics_reporting_settings_dashboards_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_reporting_settings_dashboards_query`")


        resource_path = '/api/v2/analytics/reporting/settings/dashboards/query'.replace('{format}', 'json')
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
                                            response_type='DashboardConfigurationListing',
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
        for key, val in params['kwargs'].items():
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

    def post_analytics_resolutions_aggregates_query(self, body: 'ResolutionAggregationQuery', **kwargs) -> 'ResolutionAggregateQueryResponse':
        """
        Query for resolution aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_resolutions_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ResolutionAggregationQuery body: query (required)
        :return: ResolutionAggregateQueryResponse
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
                    " to method post_analytics_resolutions_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_resolutions_aggregates_query`")


        resource_path = '/api/v2/analytics/resolutions/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='ResolutionAggregateQueryResponse',
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

    def post_analytics_summaries_aggregates_jobs(self, body: 'SummaryAsyncAggregationQuery', **kwargs) -> 'AsyncQueryResponse':
        """
        Query for summary aggregates asynchronously
        
	    post_analytics_summaries_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_summaries_aggregates_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SummaryAsyncAggregationQuery body: query (required)
        :return: AsyncQueryResponse
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
                    " to method post_analytics_summaries_aggregates_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_summaries_aggregates_jobs`")


        resource_path = '/api/v2/analytics/summaries/aggregates/jobs'.replace('{format}', 'json')
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

    def post_analytics_summaries_aggregates_query(self, body: 'SummaryAggregationQuery', **kwargs) -> 'SummaryAggregateQueryResponse':
        """
        Query for summary aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_summaries_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SummaryAggregationQuery body: query (required)
        :return: SummaryAggregateQueryResponse
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
                    " to method post_analytics_summaries_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_summaries_aggregates_query`")


        resource_path = '/api/v2/analytics/summaries/aggregates/query'.replace('{format}', 'json')
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
                                            response_type='SummaryAggregateQueryResponse',
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
        for key, val in params['kwargs'].items():
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
