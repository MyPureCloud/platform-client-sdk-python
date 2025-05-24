# coding: utf-8

"""
WorkforceManagementApi.py
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
from ..models import ActivityCodeContainer
from ..models import ActivityPlanJobListing
from ..models import ActivityPlanJobResponse
from ..models import ActivityPlanListing
from ..models import ActivityPlanResponse
from ..models import ActivityPlanRunJobResponse
from ..models import AddAdherenceExplanationAdminRequest
from ..models import AddAdherenceExplanationAgentRequest
from ..models import AddShiftTradeRequest
from ..models import AddWorkPlanRotationRequest
from ..models import AdherenceExplanationAsyncResponse
from ..models import AdherenceExplanationJob
from ..models import AdherenceExplanationResponse
from ..models import AdminAgentWorkPlanPreferenceResponse
from ..models import AdminBulkUpdateAlternativeShiftTradeStateRequest
from ..models import AdminTimeOffRequestPatch
from ..models import AgentIntegrationsRequest
from ..models import AgentIntegrationsResponse
from ..models import AgentManagementUnitReference
from ..models import AgentPossibleWorkShiftsRequest
from ..models import AgentPossibleWorkShiftsResponse
from ..models import AgentQueryAdherenceExplanationsRequest
from ..models import AgentQueryAdherenceExplanationsResponse
from ..models import AgentTimeOffRequestPatch
from ..models import AgentUpdateAlternativeShiftTradeRequest
from ..models import AgentWorkPlanBiddingPreferenceResponse
from ..models import AgentWorkPlanBids
from ..models import AgentWorkPlanListResponse
from ..models import AgentsBidAssignedWorkPlanOverrideRequest
from ..models import AgentsIntegrationsListing
from ..models import AgentsWorkPlansResponse
from ..models import AlternativeShiftAsyncResponse
from ..models import AlternativeShiftBuSettingsResponse
from ..models import AlternativeShiftJobResponse
from ..models import AlternativeShiftOffersRequest
from ..models import AlternativeShiftSearchOffersRequest
from ..models import AlternativeShiftTradeResponse
from ..models import AsyncForecastOperationResult
from ..models import AsyncIntradayResponse
from ..models import AvailableTimeOffRequest
from ..models import AvailableTimeOffResponse
from ..models import BuAgentScheduleHistoryResponse
from ..models import BuAlternativeShiftJobResponse
from ..models import BuAsyncAgentSchedulesQueryResponse
from ..models import BuAsyncAgentSchedulesSearchResponse
from ..models import BuAsyncScheduleResponse
from ..models import BuAsyncScheduleRunResponse
from ..models import BuCopyScheduleRequest
from ..models import BuCreateBlankScheduleRequest
from ..models import BuCreateTimeOffLimitRequest
from ..models import BuCreateTimeOffPlanRequest
from ..models import BuCurrentAgentScheduleSearchResponse
from ..models import BuForecastGenerationResult
from ..models import BuForecastResultResponse
from ..models import BuForecastStaffingRequirementsResultResponse
from ..models import BuGenerateScheduleRequest
from ..models import BuGetCurrentAgentScheduleRequest
from ..models import BuHeadcountForecastResponse
from ..models import BuListAlternativeShiftTradesResponse
from ..models import BuQueryAdherenceExplanationsRequest
from ..models import BuQueryAdherenceExplanationsResponse
from ..models import BuQueryAgentSchedulesRequest
from ..models import BuRescheduleRequest
from ..models import BuRescheduleResult
from ..models import BuScheduleListing
from ..models import BuScheduleMetadata
from ..models import BuScheduleRun
from ..models import BuScheduleRunListing
from ..models import BuSearchAgentSchedulesRequest
from ..models import BuSetTimeOffLimitValuesRequest
from ..models import BuShortTermForecast
from ..models import BuShortTermForecastListing
from ..models import BuTimeOffLimitListing
from ..models import BuTimeOffLimitResponse
from ..models import BuTimeOffLimitValuesResponse
from ..models import BuTimeOffPlanListing
from ..models import BuTimeOffPlanResponse
from ..models import BuUpdateTimeOffPlanRequest
from ..models import BulkShiftTradeStateUpdateRequest
from ..models import BulkUpdateShiftTradeStateResponse
from ..models import BusinessUnitActivityCode
from ..models import BusinessUnitActivityCodeListing
from ..models import BusinessUnitListing
from ..models import BusinessUnitResponse
from ..models import CalendarUrlResponse
from ..models import ContinuousForecastGetSessionResponse
from ..models import ContinuousForecastSessionResponse
from ..models import ContinuousForecastSnapshotResponse
from ..models import CopyBuForecastRequest
from ..models import CopyWorkPlan
from ..models import CopyWorkPlanBid
from ..models import CopyWorkPlanRotationRequest
from ..models import CreateActivityCodeRequest
from ..models import CreateActivityPlanRequest
from ..models import CreateAdminTimeOffRequest
from ..models import CreateAgentTimeOffRequest
from ..models import CreateAlternativeShiftTradeRequest
from ..models import CreateBusinessUnitRequest
from ..models import CreateManagementUnitApiRequest
from ..models import CreatePlanningGroupRequest
from ..models import CreateServiceGoalTemplate
from ..models import CreateStaffingGroupRequest
from ..models import CreateTimeOffLimitRequest
from ..models import CreateTimeOffPlanRequest
from ..models import CreateWorkPlan
from ..models import CreateWorkPlanBid
from ..models import CurrentUserScheduleRequestBody
from ..models import CurrentUserTimeOffIntegrationStatusRequest
from ..models import EntityListing
from ..models import ErrorBody
from ..models import EstimateAvailableTimeOffRequest
from ..models import EstimateAvailableTimeOffResponse
from ..models import ForecastPlanningGroupsResponse
from ..models import GenerateBuForecastRequest
from ..models import GetAgentsWorkPlansRequest
from ..models import HistoricalImportDeleteFilesJobRequest
from ..models import HistoricalImportDeleteFilesJobResponse
from ..models import HistoricalImportDeleteJobResponse
from ..models import HistoricalImportOverallDeleteStatusResponse
from ..models import HistoricalImportStatusJobResponse
from ..models import HistoricalImportStatusListing
from ..models import HrisTimeOffTypesJobResponse
from ..models import HrisTimeOffTypesResponse
from ..models import ImportForecastResponse
from ..models import ImportForecastUploadResponse
from ..models import ImportScheduleUploadResponse
from ..models import IntradayPlanningGroupRequest
from ..models import ListAlternativeShiftTradesResponse
from ..models import LongTermForecastResultResponse
from ..models import ManagementUnit
from ..models import ManagementUnitListing
from ..models import MatchShiftTradeRequest
from ..models import MatchShiftTradeResponse
from ..models import MoveAgentsRequest
from ..models import MoveAgentsResponse
from ..models import MoveManagementUnitRequest
from ..models import MoveManagementUnitResponse
from ..models import NotificationsResponse
from ..models import PatchBuScheduleRunRequest
from ..models import PatchShiftTradeRequest
from ..models import PerformancePredictionRecalculationResponse
from ..models import PerformancePredictionRecalculationUploadResponse
from ..models import PerformancePredictionResponse
from ..models import PlanningGroup
from ..models import PlanningGroupList
from ..models import ProcessScheduleUpdateUploadRequest
from ..models import QueryAdherenceExplanationsResponse
from ..models import QueryAgentsIntegrationsRequest
from ..models import QueryTimeOffIntegrationStatusRequest
from ..models import QueryTimeOffLimitValuesRequest
from ..models import QueryTimeOffLimitValuesResponse
from ..models import QueryUserStaffingGroupListRequest
from ..models import QueryWaitlistPositionsRequest
from ..models import ScheduleGenerationResult
from ..models import ScheduleUploadProcessingResponse
from ..models import SchedulingStatusResponse
from ..models import SearchAlternativeShiftTradesRequest
from ..models import SearchShiftTradesRequest
from ..models import SearchShiftTradesResponse
from ..models import ServiceGoalTemplate
from ..models import ServiceGoalTemplateList
from ..models import SetTimeOffIntegrationStatusRequest
from ..models import SetTimeOffLimitValuesRequest
from ..models import ShiftTradeListResponse
from ..models import ShiftTradeMatchesSummaryResponse
from ..models import ShiftTradeResponse
from ..models import StaffingGroupListing
from ..models import StaffingGroupResponse
from ..models import TimeOffBalanceJobResponse
from ..models import TimeOffBalanceRequest
from ..models import TimeOffBalancesResponse
from ..models import TimeOffIntegrationStatusResponseListing
from ..models import TimeOffLimit
from ..models import TimeOffLimitListing
from ..models import TimeOffPlan
from ..models import TimeOffPlanListing
from ..models import TimeOffRequestList
from ..models import TimeOffRequestListing
from ..models import TimeOffRequestQueryBody
from ..models import TimeOffRequestResponse
from ..models import UpdateActivityCodeRequest
from ..models import UpdateActivityPlanRequest
from ..models import UpdateAdherenceExplanationStatusRequest
from ..models import UpdateAgentWorkPlanBiddingPreference
from ..models import UpdateAlternativeShiftBuSettingsRequest
from ..models import UpdateBusinessUnitRequest
from ..models import UpdateManagementUnitRequest
from ..models import UpdateMuAgentWorkPlansBatchRequest
from ..models import UpdateMuAgentWorkPlansBatchResponse
from ..models import UpdateMuAgentsRequest
from ..models import UpdateNotificationsRequest
from ..models import UpdateNotificationsResponse
from ..models import UpdatePlanningGroupRequest
from ..models import UpdateScheduleUploadResponse
from ..models import UpdateServiceGoalTemplate
from ..models import UpdateStaffingGroupRequest
from ..models import UpdateTimeOffLimitRequest
from ..models import UpdateTimeOffPlanRequest
from ..models import UpdateWorkPlanBid
from ..models import UpdateWorkPlanRotationRequest
from ..models import UploadUrlRequestBody
from ..models import UserListScheduleRequestBody
from ..models import UserScheduleAdherence
from ..models import UserScheduleAdherenceListing
from ..models import UserScheduleContainer
from ..models import UserStaffingGroupListing
from ..models import UserTimeOffIntegrationStatusResponse
from ..models import UserTimeOffIntegrationStatusResponseListing
from ..models import ValidateWorkPlanResponse
from ..models import ValidationServiceAsyncResponse
from ..models import ValidationServiceRequest
from ..models import WaitlistPositionListing
from ..models import WeekScheduleListResponse
from ..models import WeekScheduleResponse
from ..models import WeekShiftTradeListResponse
from ..models import WfmAgent
from ..models import WfmHistoricalAdherenceBulkQuery
from ..models import WfmHistoricalAdherenceBulkResponse
from ..models import WfmHistoricalAdherenceQuery
from ..models import WfmHistoricalAdherenceQueryForTeams
from ..models import WfmHistoricalAdherenceQueryForUsers
from ..models import WfmHistoricalAdherenceResponse
from ..models import WfmHistoricalShrinkageRequest
from ..models import WfmHistoricalShrinkageResponse
from ..models import WfmHistoricalShrinkageTeamsRequest
from ..models import WfmIntegrationListing
from ..models import WfmIntradayPlanningGroupListing
from ..models import WfmProcessUploadRequest
from ..models import WfmUserEntityListing
from ..models import WorkPlan
from ..models import WorkPlanBid
from ..models import WorkPlanBidGroupCreate
from ..models import WorkPlanBidGroupResponse
from ..models import WorkPlanBidGroupSummaryList
from ..models import WorkPlanBidGroupUpdate
from ..models import WorkPlanBidListResponse
from ..models import WorkPlanBidRanks
from ..models import WorkPlanListResponse
from ..models import WorkPlanRotationListResponse
from ..models import WorkPlanRotationResponse
from ..models import WorkPlanValidationRequest

class WorkforceManagementApi(object):
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

    def delete_workforcemanagement_businessunit(self, business_unit_id: str, **kwargs) -> None:
        """
        Delete business unit
        A business unit cannot be deleted if it contains one or more management units

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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

    def delete_workforcemanagement_businessunit_activitycode(self, business_unit_id: str, activity_code_id: str, **kwargs) -> None:
        """
        Deletes an activity code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param str activity_code_id: The ID of the activity code to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_activitycode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_activitycode`")
        # verify the required parameter 'activity_code_id' is set
        if ('activity_code_id' not in params) or (params['activity_code_id'] is None):
            raise ValueError("Missing the required parameter `activity_code_id` when calling `delete_workforcemanagement_businessunit_activitycode`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_code_id' in params:
            path_params['activityCodeId'] = params['activity_code_id']

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

    def delete_workforcemanagement_businessunit_planninggroup(self, business_unit_id: str, planning_group_id: str, **kwargs) -> None:
        """
        Deletes the planning group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str planning_group_id: The ID of a planning group to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'planning_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_planninggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_planninggroup`")
        # verify the required parameter 'planning_group_id' is set
        if ('planning_group_id' not in params) or (params['planning_group_id'] is None):
            raise ValueError("Missing the required parameter `planning_group_id` when calling `delete_workforcemanagement_businessunit_planninggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'planning_group_id' in params:
            path_params['planningGroupId'] = params['planning_group_id']

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

    def delete_workforcemanagement_businessunit_scheduling_run(self, business_unit_id: str, run_id: str, **kwargs) -> None:
        """
        Cancel a scheduling run
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str run_id: The ID of the schedule run (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'run_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_scheduling_run" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_scheduling_run`")
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params) or (params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `delete_workforcemanagement_businessunit_scheduling_run`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'run_id' in params:
            path_params['runId'] = params['run_id']

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

    def delete_workforcemanagement_businessunit_servicegoaltemplate(self, business_unit_id: str, service_goal_template_id: str, **kwargs) -> None:
        """
        Delete a service goal template
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str service_goal_template_id: The ID of the service goal template to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'service_goal_template_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_servicegoaltemplate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_servicegoaltemplate`")
        # verify the required parameter 'service_goal_template_id' is set
        if ('service_goal_template_id' not in params) or (params['service_goal_template_id'] is None):
            raise ValueError("Missing the required parameter `service_goal_template_id` when calling `delete_workforcemanagement_businessunit_servicegoaltemplate`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'service_goal_template_id' in params:
            path_params['serviceGoalTemplateId'] = params['service_goal_template_id']

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

    def delete_workforcemanagement_businessunit_staffinggroup(self, business_unit_id: str, staffing_group_id: str, **kwargs) -> None:
        """
        Deletes a staffing group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str staffing_group_id: The ID of the staffing group to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'staffing_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_staffinggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_staffinggroup`")
        # verify the required parameter 'staffing_group_id' is set
        if ('staffing_group_id' not in params) or (params['staffing_group_id'] is None):
            raise ValueError("Missing the required parameter `staffing_group_id` when calling `delete_workforcemanagement_businessunit_staffinggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'staffing_group_id' in params:
            path_params['staffingGroupId'] = params['staffing_group_id']

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

    def delete_workforcemanagement_businessunit_timeofflimit(self, business_unit_id: str, time_off_limit_id: str, **kwargs) -> None:
        """
        Deletes a time-off limit object
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_limit_id: The ID of the time-off limit object to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_limit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_timeofflimit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_timeofflimit`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `delete_workforcemanagement_businessunit_timeofflimit`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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

    def delete_workforcemanagement_businessunit_timeoffplan(self, business_unit_id: str, time_off_plan_id: str, **kwargs) -> None:
        """
        Deletes a time-off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_plan_id: The ID of the time-off plan to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `delete_workforcemanagement_businessunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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

    def delete_workforcemanagement_businessunit_week_schedule(self, business_unit_id: str, week_id: date, schedule_id: str, **kwargs) -> 'BuAsyncScheduleResponse':
        """
        Delete a schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :return: BuAsyncScheduleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_week_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_week_schedule`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `delete_workforcemanagement_businessunit_week_schedule`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `delete_workforcemanagement_businessunit_week_schedule`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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
                                            response_type='BuAsyncScheduleResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_workforcemanagement_businessunit_week_shorttermforecast(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> None:
        """
        Delete a short term forecast
        Must not be tied to any schedules

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_week_shorttermforecast" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_week_shorttermforecast`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `delete_workforcemanagement_businessunit_week_shorttermforecast`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `delete_workforcemanagement_businessunit_week_shorttermforecast`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

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

    def delete_workforcemanagement_businessunit_workplanbid(self, business_unit_id: str, bid_id: str, **kwargs) -> None:
        """
        Delete a work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The ID of the work plan bid (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_workplanbid" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_workplanbid`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `delete_workforcemanagement_businessunit_workplanbid`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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

    def delete_workforcemanagement_businessunit_workplanbid_group(self, business_unit_id: str, bid_id: str, bid_group_id: str, **kwargs) -> None:
        """
        Delete a bid group by bid group Id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param str bid_group_id: Work Plan Bid Group id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'bid_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_businessunit_workplanbid_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `delete_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_group_id' is set
        if ('bid_group_id' not in params) or (params['bid_group_id'] is None):
            raise ValueError("Missing the required parameter `bid_group_id` when calling `delete_workforcemanagement_businessunit_workplanbid_group`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']
        if 'bid_group_id' in params:
            path_params['bidGroupId'] = params['bid_group_id']

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

    def delete_workforcemanagement_calendar_url_ics(self, **kwargs) -> None:
        """
        Disable generated calendar link for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_calendar_url_ics(callback=callback_function)

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
                    " to method delete_workforcemanagement_calendar_url_ics" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/calendar/url/ics'.replace('{format}', 'json')
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

    def delete_workforcemanagement_managementunit(self, management_unit_id: str, **kwargs) -> None:
        """
        Delete management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_managementunit(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_managementunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `delete_workforcemanagement_managementunit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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

    def delete_workforcemanagement_managementunit_timeofflimit(self, management_unit_id: str, time_off_limit_id: str, **kwargs) -> None:
        """
        Deletes a time off limit object
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str time_off_limit_id: The ID of the time off limit object to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_limit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_managementunit_timeofflimit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `delete_workforcemanagement_managementunit_timeofflimit`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `delete_workforcemanagement_managementunit_timeofflimit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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

    def delete_workforcemanagement_managementunit_timeoffplan(self, management_unit_id: str, time_off_plan_id: str, **kwargs) -> None:
        """
        Deletes a time off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param str time_off_plan_id: The ID of the time off plan to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_managementunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `delete_workforcemanagement_managementunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `delete_workforcemanagement_managementunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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

    def delete_workforcemanagement_managementunit_workplan(self, management_unit_id: str, work_plan_id: str, **kwargs) -> None:
        """
        Delete a work plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_id: The ID of the work plan to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_managementunit_workplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `delete_workforcemanagement_managementunit_workplan`")
        # verify the required parameter 'work_plan_id' is set
        if ('work_plan_id' not in params) or (params['work_plan_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_id` when calling `delete_workforcemanagement_managementunit_workplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_id' in params:
            path_params['workPlanId'] = params['work_plan_id']

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

    def delete_workforcemanagement_managementunit_workplanrotation(self, management_unit_id: str, work_plan_rotation_id: str, **kwargs) -> None:
        """
        Delete a work plan rotation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_rotation_id: The ID of the work plan rotation to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_rotation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workforcemanagement_managementunit_workplanrotation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `delete_workforcemanagement_managementunit_workplanrotation`")
        # verify the required parameter 'work_plan_rotation_id' is set
        if ('work_plan_rotation_id' not in params) or (params['work_plan_rotation_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_rotation_id` when calling `delete_workforcemanagement_managementunit_workplanrotation`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_rotation_id' in params:
            path_params['workPlanRotationId'] = params['work_plan_rotation_id']

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

    def get_workforcemanagement_adherence(self, user_id: List['str'], **kwargs) -> List['UserScheduleAdherence']:
        """
        Get a list of UserScheduleAdherence records for the requested users
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_adherence(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] user_id: User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request (required)
        :return: list[UserScheduleAdherence]
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
                    " to method get_workforcemanagement_adherence" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_workforcemanagement_adherence`")


        resource_path = '/api/v2/workforcemanagement/adherence'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'user_id' in params:
            query_params['userId'] = params['user_id']

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
                                            response_type='list[UserScheduleAdherence]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_adherence_explanation(self, explanation_id: str, **kwargs) -> 'AdherenceExplanationResponse':
        """
        Get an adherence explanation for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_adherence_explanation(explanation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str explanation_id: The ID of the explanation to update (required)
        :return: AdherenceExplanationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['explanation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_adherence_explanation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'explanation_id' is set
        if ('explanation_id' not in params) or (params['explanation_id'] is None):
            raise ValueError("Missing the required parameter `explanation_id` when calling `get_workforcemanagement_adherence_explanation`")


        resource_path = '/api/v2/workforcemanagement/adherence/explanations/{explanationId}'.replace('{format}', 'json')
        path_params = {}
        if 'explanation_id' in params:
            path_params['explanationId'] = params['explanation_id']

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
                                            response_type='AdherenceExplanationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_adherence_explanations_job(self, job_id: str, **kwargs) -> 'AdherenceExplanationJob':
        """
        Query the status of an adherence explanation operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_adherence_explanations_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job (required)
        :return: AdherenceExplanationJob
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
                    " to method get_workforcemanagement_adherence_explanations_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_adherence_explanations_job`")


        resource_path = '/api/v2/workforcemanagement/adherence/explanations/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AdherenceExplanationJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_adherence_historical_bulk_job(self, job_id: str, **kwargs) -> 'WfmHistoricalAdherenceBulkResponse':
        """
        Request to fetch the status of the historical adherence bulk job. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_adherence_historical_bulk_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: ID of the job to get (required)
        :return: WfmHistoricalAdherenceBulkResponse
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
                    " to method get_workforcemanagement_adherence_historical_bulk_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_adherence_historical_bulk_job`")


        resource_path = '/api/v2/workforcemanagement/adherence/historical/bulk/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='WfmHistoricalAdherenceBulkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_adherence_historical_job(self, job_id: str, **kwargs) -> 'WfmHistoricalAdherenceResponse':
        """
        Query the status of a historical adherence request operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_adherence_historical_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: WfmHistoricalAdherenceResponse
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
                    " to method get_workforcemanagement_adherence_historical_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_adherence_historical_job`")


        resource_path = '/api/v2/workforcemanagement/adherence/historical/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='WfmHistoricalAdherenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_agent_adherence_explanation(self, agent_id: str, explanation_id: str, **kwargs) -> 'AdherenceExplanationResponse':
        """
        Get an adherence explanation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent to query (required)
        :param str explanation_id: The ID of the explanation to update (required)
        :return: AdherenceExplanationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'explanation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_agent_adherence_explanation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_workforcemanagement_agent_adherence_explanation`")
        # verify the required parameter 'explanation_id' is set
        if ('explanation_id' not in params) or (params['explanation_id'] is None):
            raise ValueError("Missing the required parameter `explanation_id` when calling `get_workforcemanagement_agent_adherence_explanation`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/{explanationId}'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']
        if 'explanation_id' in params:
            path_params['explanationId'] = params['explanation_id']

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
                                            response_type='AdherenceExplanationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_agent_managementunit(self, agent_id: str, **kwargs) -> 'AgentManagementUnitReference':
        """
        Get the management unit to which the agent belongs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_agent_managementunit(agent_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent to look up (required)
        :return: AgentManagementUnitReference
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_agent_managementunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_workforcemanagement_agent_managementunit`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/managementunit'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='AgentManagementUnitReference',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_agents_me_managementunit(self, **kwargs) -> 'AgentManagementUnitReference':
        """
        Get the management unit to which the currently logged in agent belongs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_agents_me_managementunit(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AgentManagementUnitReference
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
                    " to method get_workforcemanagement_agents_me_managementunit" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/agents/me/managementunit'.replace('{format}', 'json')
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
                                            response_type='AgentManagementUnitReference',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_offers_job(self, job_id: str, **kwargs) -> 'AlternativeShiftJobResponse':
        """
        Query the status of an alternative shift offers operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_offers_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job (required)
        :return: AlternativeShiftJobResponse
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
                    " to method get_workforcemanagement_alternativeshifts_offers_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_alternativeshifts_offers_job`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/offers/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_offers_search_job(self, job_id: str, **kwargs) -> 'AlternativeShiftJobResponse':
        """
        Query the status of an alternative shift search offers operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_offers_search_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job (required)
        :return: AlternativeShiftJobResponse
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
                    " to method get_workforcemanagement_alternativeshifts_offers_search_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_alternativeshifts_offers_search_job`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/offers/search/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_settings(self, **kwargs) -> 'AlternativeShiftBuSettingsResponse':
        """
        Get alternative shifts settings from the current logged in agent’s business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AlternativeShiftBuSettingsResponse
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
                    " to method get_workforcemanagement_alternativeshifts_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/alternativeshifts/settings'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftBuSettingsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_trade(self, trade_id: str, **kwargs) -> 'AlternativeShiftTradeResponse':
        """
        Get my alternative shift trade by trade ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_trade(trade_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str trade_id: The ID of the alternative shift trade (required)
        :return: AlternativeShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trade_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_alternativeshifts_trade" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'trade_id' is set
        if ('trade_id' not in params) or (params['trade_id'] is None):
            raise ValueError("Missing the required parameter `trade_id` when calling `get_workforcemanagement_alternativeshifts_trade`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades/{tradeId}'.replace('{format}', 'json')
        path_params = {}
        if 'trade_id' in params:
            path_params['tradeId'] = params['trade_id']

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
                                            response_type='AlternativeShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_trades(self, **kwargs) -> 'ListAlternativeShiftTradesResponse':
        """
        Get a list of my alternative shifts trades
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_trades(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :return: ListAlternativeShiftTradesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['force_async']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_alternativeshifts_trades" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='ListAlternativeShiftTradesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_trades_job(self, job_id: str, **kwargs) -> 'AlternativeShiftJobResponse':
        """
        Query the status of an alternative shift trades operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_trades_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job (required)
        :return: AlternativeShiftJobResponse
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
                    " to method get_workforcemanagement_alternativeshifts_trades_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_alternativeshifts_trades_job`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_alternativeshifts_trades_state_job(self, job_id: str, **kwargs) -> 'AlternativeShiftJobResponse':
        """
        Query the status of an alternative shift trade state operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_alternativeshifts_trades_state_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job (required)
        :return: AlternativeShiftJobResponse
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
                    " to method get_workforcemanagement_alternativeshifts_trades_state_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_alternativeshifts_trades_state_job`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades/state/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit(self, business_unit_id: str, **kwargs) -> 'BusinessUnitResponse':
        """
        Get business unit
        Expanding \"settings\" will retrieve all settings.  All other expands will retrieve only the requested settings field(s).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param list[str] expand: Include to access additional data on the business unit
        :return: BusinessUnitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BusinessUnitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activitycode(self, business_unit_id: str, activity_code_id: str, **kwargs) -> 'BusinessUnitActivityCode':
        """
        Get an activity code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param str activity_code_id: The ID of the activity code to fetch (required)
        :return: BusinessUnitActivityCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_code_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activitycode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activitycode`")
        # verify the required parameter 'activity_code_id' is set
        if ('activity_code_id' not in params) or (params['activity_code_id'] is None):
            raise ValueError("Missing the required parameter `activity_code_id` when calling `get_workforcemanagement_businessunit_activitycode`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_code_id' in params:
            path_params['activityCodeId'] = params['activity_code_id']

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
                                            response_type='BusinessUnitActivityCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activitycodes(self, business_unit_id: str, **kwargs) -> 'BusinessUnitActivityCodeListing':
        """
        Get activity codes
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activitycodes(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: BusinessUnitActivityCodeListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activitycodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activitycodes`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BusinessUnitActivityCodeListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activityplan(self, business_unit_id: str, activity_plan_id: str, **kwargs) -> 'ActivityPlanResponse':
        """
        Get an activity plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str activity_plan_id: The ID of the activity plan to fetch (required)
        :return: ActivityPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activityplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activityplan`")
        # verify the required parameter 'activity_plan_id' is set
        if ('activity_plan_id' not in params) or (params['activity_plan_id'] is None):
            raise ValueError("Missing the required parameter `activity_plan_id` when calling `get_workforcemanagement_businessunit_activityplan`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_plan_id' in params:
            path_params['activityPlanId'] = params['activity_plan_id']

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
                                            response_type='ActivityPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activityplan_runs_job(self, business_unit_id: str, activity_plan_id: str, job_id: str, **kwargs) -> 'ActivityPlanRunJobResponse':
        """
        Gets an activity plan run job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activityplan_runs_job(business_unit_id, activity_plan_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str activity_plan_id: The ID of the activity plan associated with the run job (required)
        :param str job_id: The ID of the activity plan run job (required)
        :return: ActivityPlanRunJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_plan_id', 'job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activityplan_runs_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activityplan_runs_job`")
        # verify the required parameter 'activity_plan_id' is set
        if ('activity_plan_id' not in params) or (params['activity_plan_id'] is None):
            raise ValueError("Missing the required parameter `activity_plan_id` when calling `get_workforcemanagement_businessunit_activityplan_runs_job`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_businessunit_activityplan_runs_job`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}/runs/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_plan_id' in params:
            path_params['activityPlanId'] = params['activity_plan_id']
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
                                            response_type='ActivityPlanRunJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activityplans(self, business_unit_id: str, **kwargs) -> 'ActivityPlanListing':
        """
        Get activity plans
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activityplans(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str state: Optionally filter by activity plan state
        :return: ActivityPlanListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'state']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activityplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activityplans`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
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
                                            response_type='ActivityPlanListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_activityplans_jobs(self, business_unit_id: str, **kwargs) -> 'ActivityPlanJobListing':
        """
        Gets the latest job for all activity plans in the business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_activityplans_jobs(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :return: ActivityPlanJobListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_activityplans_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_activityplans_jobs`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='ActivityPlanJobListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_alternativeshifts_settings(self, business_unit_id: str, **kwargs) -> 'AlternativeShiftBuSettingsResponse':
        """
        Get alternative shifts settings for a business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :return: AlternativeShiftBuSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_alternativeshifts_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_alternativeshifts_settings`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/settings'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='AlternativeShiftBuSettingsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_alternativeshifts_trade(self, business_unit_id: str, trade_id: str, **kwargs) -> 'AlternativeShiftTradeResponse':
        """
        Get an alternative shifts trade in a business unit for a given trade ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_alternativeshifts_trade(business_unit_id, trade_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str trade_id: The ID of the alternative shift trade (required)
        :return: AlternativeShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'trade_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_alternativeshifts_trade" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_alternativeshifts_trade`")
        # verify the required parameter 'trade_id' is set
        if ('trade_id' not in params) or (params['trade_id'] is None):
            raise ValueError("Missing the required parameter `trade_id` when calling `get_workforcemanagement_businessunit_alternativeshifts_trade`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/{tradeId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'trade_id' in params:
            path_params['tradeId'] = params['trade_id']

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
                                            response_type='AlternativeShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_alternativeshifts_trades_search_job(self, business_unit_id: str, job_id: str, **kwargs) -> 'BuAlternativeShiftJobResponse':
        """
        Query the status of an alternative shift search trade operation. Only the user who started the operation can query the status
        Job details are only retained if the initial request returned a 202 ACCEPTED response

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_alternativeshifts_trades_search_job(business_unit_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str job_id: The ID of the job (required)
        :return: BuAlternativeShiftJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'job_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_alternativeshifts_trades_search_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_alternativeshifts_trades_search_job`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_businessunit_alternativeshifts_trades_search_job`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/search/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
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
                                            response_type='BuAlternativeShiftJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_intraday_planninggroups(self, business_unit_id: str, date: date, **kwargs) -> 'WfmIntradayPlanningGroupListing':
        """
        Get intraday planning groups for the given date
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_intraday_planninggroups(business_unit_id, date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date date: yyyy-MM-dd date string interpreted in the configured business unit time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :return: WfmIntradayPlanningGroupListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'date']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_intraday_planninggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_intraday_planninggroups`")
        # verify the required parameter 'date' is set
        if ('date' not in params) or (params['date'] is None):
            raise ValueError("Missing the required parameter `date` when calling `get_workforcemanagement_businessunit_intraday_planninggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/intraday/planninggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'date' in params:
            query_params['date'] = params['date']

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
                                            response_type='WfmIntradayPlanningGroupListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_mainforecast_continuousforecast_session(self, business_unit_id: str, **kwargs) -> 'ContinuousForecastGetSessionResponse':
        """
        Get the latest session for the business unit ID
        
	    get_workforcemanagement_businessunit_mainforecast_continuousforecast_session is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id:  (required)
        :return: ContinuousForecastGetSessionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_mainforecast_continuousforecast_session" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='ContinuousForecastGetSessionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id(self, business_unit_id: str, session_id: str, **kwargs) -> 'ContinuousForecastSessionResponse':
        """
        Get the session details for the session ID
        
	    get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id(business_unit_id, session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id:  (required)
        :param str session_id:  (required)
        :return: ContinuousForecastSessionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'session_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id`")
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session/{sessionId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

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
                                            response_type='ContinuousForecastSessionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id(self, business_unit_id: str, session_id: str, snapshot_id: str, **kwargs) -> 'ContinuousForecastSnapshotResponse':
        """
        Get the snapshot details for the snapshot ID
        
	    get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id(business_unit_id, session_id, snapshot_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id:  (required)
        :param str session_id:  (required)
        :param str snapshot_id:  (required)
        :return: ContinuousForecastSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'session_id', 'snapshot_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id`")
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id`")
        # verify the required parameter 'snapshot_id' is set
        if ('snapshot_id' not in params) or (params['snapshot_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_id` when calling `get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session/{sessionId}/snapshot/{snapshotId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']
        if 'snapshot_id' in params:
            path_params['snapshotId'] = params['snapshot_id']

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
                                            response_type='ContinuousForecastSnapshotResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_managementunits(self, business_unit_id: str, **kwargs) -> 'ManagementUnitListing':
        """
        Get all authorized management units in the business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_managementunits(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param str feature: If specified, the list of management units for which the user is authorized to use the requested feature will be returned
        :param str division_id: If specified, the list of management units belonging to the specified division will be returned
        :return: ManagementUnitListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'feature', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_managementunits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_managementunits`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/managementunits'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'feature' in params:
            query_params['feature'] = params['feature']
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
                                            response_type='ManagementUnitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_planninggroup(self, business_unit_id: str, planning_group_id: str, **kwargs) -> 'PlanningGroup':
        """
        Get a planning group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str planning_group_id: The ID of a planning group to fetch (required)
        :return: PlanningGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'planning_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_planninggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_planninggroup`")
        # verify the required parameter 'planning_group_id' is set
        if ('planning_group_id' not in params) or (params['planning_group_id'] is None):
            raise ValueError("Missing the required parameter `planning_group_id` when calling `get_workforcemanagement_businessunit_planninggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'planning_group_id' in params:
            path_params['planningGroupId'] = params['planning_group_id']

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
                                            response_type='PlanningGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_planninggroups(self, business_unit_id: str, **kwargs) -> 'PlanningGroupList':
        """
        Gets list of planning groups
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_planninggroups(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :return: PlanningGroupList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_planninggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_planninggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='PlanningGroupList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_scheduling_run(self, business_unit_id: str, run_id: str, **kwargs) -> 'BuScheduleRun':
        """
        Get a scheduling run
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str run_id: The ID of the schedule run (required)
        :return: BuScheduleRun
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'run_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_scheduling_run" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_scheduling_run`")
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params) or (params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `get_workforcemanagement_businessunit_scheduling_run`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'run_id' in params:
            path_params['runId'] = params['run_id']

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
                                            response_type='BuScheduleRun',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_scheduling_run_result(self, business_unit_id: str, run_id: str, management_unit_ids: List['str'], expand: List['str'], **kwargs) -> 'BuRescheduleResult':
        """
        Get the result of a rescheduling operation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_scheduling_run_result(business_unit_id, run_id, management_unit_ids, expand, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str run_id: The ID of the schedule run (required)
        :param list[str] management_unit_ids: The IDs of the management units for which to fetch the reschedule results (required)
        :param list[str] expand: The fields to expand. Omitting will return an empty response (required)
        :return: BuRescheduleResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'run_id', 'management_unit_ids', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_scheduling_run_result" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_scheduling_run_result`")
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params) or (params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `get_workforcemanagement_businessunit_scheduling_run_result`")
        # verify the required parameter 'management_unit_ids' is set
        if ('management_unit_ids' not in params) or (params['management_unit_ids'] is None):
            raise ValueError("Missing the required parameter `management_unit_ids` when calling `get_workforcemanagement_businessunit_scheduling_run_result`")
        # verify the required parameter 'expand' is set
        if ('expand' not in params) or (params['expand'] is None):
            raise ValueError("Missing the required parameter `expand` when calling `get_workforcemanagement_businessunit_scheduling_run_result`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId}/result'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'run_id' in params:
            path_params['runId'] = params['run_id']

        query_params = {}
        if 'management_unit_ids' in params:
            query_params['managementUnitIds'] = params['management_unit_ids']
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
                                            response_type='BuRescheduleResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_scheduling_runs(self, business_unit_id: str, **kwargs) -> 'BuScheduleRunListing':
        """
        Get the list of scheduling runs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_scheduling_runs(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :return: BuScheduleRunListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_scheduling_runs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_scheduling_runs`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BuScheduleRunListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_servicegoaltemplate(self, business_unit_id: str, service_goal_template_id: str, **kwargs) -> 'ServiceGoalTemplate':
        """
        Get a service goal template
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str service_goal_template_id: The ID of a service goal template to fetch (required)
        :param list[str] expand: Include to access additional data on the service goal template
        :return: ServiceGoalTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'service_goal_template_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_servicegoaltemplate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_servicegoaltemplate`")
        # verify the required parameter 'service_goal_template_id' is set
        if ('service_goal_template_id' not in params) or (params['service_goal_template_id'] is None):
            raise ValueError("Missing the required parameter `service_goal_template_id` when calling `get_workforcemanagement_businessunit_servicegoaltemplate`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'service_goal_template_id' in params:
            path_params['serviceGoalTemplateId'] = params['service_goal_template_id']

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
                                            response_type='ServiceGoalTemplate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_servicegoaltemplates(self, business_unit_id: str, **kwargs) -> 'ServiceGoalTemplateList':
        """
        Gets list of service goal templates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param list[str] expand: Include to access additional data on the service goal template
        :return: ServiceGoalTemplateList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_servicegoaltemplates" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_servicegoaltemplates`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='ServiceGoalTemplateList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_staffinggroup(self, business_unit_id: str, staffing_group_id: str, **kwargs) -> 'StaffingGroupResponse':
        """
        Gets a staffing group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str staffing_group_id: The ID of the staffing group to fetch (required)
        :return: StaffingGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'staffing_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_staffinggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_staffinggroup`")
        # verify the required parameter 'staffing_group_id' is set
        if ('staffing_group_id' not in params) or (params['staffing_group_id'] is None):
            raise ValueError("Missing the required parameter `staffing_group_id` when calling `get_workforcemanagement_businessunit_staffinggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'staffing_group_id' in params:
            path_params['staffingGroupId'] = params['staffing_group_id']

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
                                            response_type='StaffingGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_staffinggroups(self, business_unit_id: str, **kwargs) -> 'StaffingGroupListing':
        """
        Gets a list of staffing groups
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_staffinggroups(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str management_unit_id: The ID of the management unit to get management unit specific staffing groups
        :return: StaffingGroupListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_staffinggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_staffinggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'management_unit_id' in params:
            query_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='StaffingGroupListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_timeofflimit(self, business_unit_id: str, time_off_limit_id: str, **kwargs) -> 'BuTimeOffLimitResponse':
        """
        Gets a time-off limit object
        Returns properties of time-off limit object, but not daily values

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_limit_id: The ID of the time-off limit to fetch (required)
        :return: BuTimeOffLimitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_limit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_timeofflimit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_timeofflimit`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `get_workforcemanagement_businessunit_timeofflimit`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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
                                            response_type='BuTimeOffLimitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_timeofflimits(self, business_unit_id: str, **kwargs) -> 'BuTimeOffLimitListing':
        """
        Gets a list of time-off limit objects
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_timeofflimits(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str management_unit_id: The ID of the management unit to get management unit specific time-off limit objects
        :return: BuTimeOffLimitListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_timeofflimits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_timeofflimits`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'management_unit_id' in params:
            query_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='BuTimeOffLimitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_timeoffplan(self, business_unit_id: str, time_off_plan_id: str, **kwargs) -> 'BuTimeOffPlanResponse':
        """
        Gets a time-off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_plan_id: The ID of the time-off plan to fetch (required)
        :return: BuTimeOffPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `get_workforcemanagement_businessunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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
                                            response_type='BuTimeOffPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_timeoffplans(self, business_unit_id: str, **kwargs) -> 'BuTimeOffPlanListing':
        """
        Gets a list of time-off plans
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_timeoffplans(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str management_unit_id: The ID of the management unit to get management unit specific staffing groups
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: BuTimeOffPlanListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'management_unit_id', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_timeoffplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_timeoffplans`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'management_unit_id' in params:
            query_params['managementUnitId'] = params['management_unit_id']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuTimeOffPlanListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule(self, business_unit_id: str, week_id: date, schedule_id: str, **kwargs) -> 'BuScheduleMetadata':
        """
        Get the metadata for the schedule, describing which management units and agents are in the scheduleSchedule data can then be loaded with the query route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param str expand: expand
        :return: BuScheduleMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

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
                                            response_type='BuScheduleMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule_generationresults(self, business_unit_id: str, week_id: date, schedule_id: str, **kwargs) -> 'ScheduleGenerationResult':
        """
        Get the generation results for a generated schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule_generationresults(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :return: ScheduleGenerationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule_generationresults" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule_generationresults`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule_generationresults`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule_generationresults`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/generationresults'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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
                                            response_type='ScheduleGenerationResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule_headcountforecast(self, business_unit_id: str, week_id: date, schedule_id: str, **kwargs) -> 'BuHeadcountForecastResponse':
        """
        Get the headcount forecast by planning group for the schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule_headcountforecast(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param bool force_download: Whether to force the result to come via download url.  For testing purposes only
        :return: BuHeadcountForecastResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'force_download']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule_headcountforecast" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule_headcountforecast`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule_headcountforecast`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule_headcountforecast`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/headcountforecast'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

        query_params = {}
        if 'force_download' in params:
            query_params['forceDownload'] = params['force_download']

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
                                            response_type='BuHeadcountForecastResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule_history_agent(self, business_unit_id: str, week_id: date, schedule_id: str, agent_id: str, **kwargs) -> 'BuAgentScheduleHistoryResponse':
        """
        Loads agent's schedule history.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule_history_agent(business_unit_id, week_id, schedule_id, agent_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param str agent_id: THe ID of the agent (required)
        :return: BuAgentScheduleHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'agent_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule_history_agent" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule_history_agent`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule_history_agent`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule_history_agent`")
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_workforcemanagement_businessunit_week_schedule_history_agent`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/history/agents/{agentId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='BuAgentScheduleHistoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule_performancepredictions(self, business_unit_id: str, week_id: str, schedule_id: str, **kwargs) -> 'PerformancePredictionResponse':
        """
        Get the performance prediction for the associated schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule_performancepredictions(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the performance prediction belongs (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format (required)
        :param str schedule_id: The ID of the schedule the performance prediction belongs to (required)
        :return: PerformancePredictionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule_performancepredictions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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
                                            response_type='PerformancePredictionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation(self, business_unit_id: str, week_id: str, schedule_id: str, recalculation_id: str, **kwargs) -> 'PerformancePredictionRecalculationResponse':
        """
        Get recalculated performance prediction result
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation(business_unit_id, week_id, schedule_id, recalculation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the performance prediction belongs (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format (required)
        :param str schedule_id: The ID of the schedule the recalculation belongs to (required)
        :param str recalculation_id: The ID of the recalculation request (required)
        :return: PerformancePredictionRecalculationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'recalculation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation`")
        # verify the required parameter 'recalculation_id' is set
        if ('recalculation_id' not in params) or (params['recalculation_id'] is None):
            raise ValueError("Missing the required parameter `recalculation_id` when calling `get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations/{recalculationId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']
        if 'recalculation_id' in params:
            path_params['recalculationId'] = params['recalculation_id']

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
                                            response_type='PerformancePredictionRecalculationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_schedules(self, business_unit_id: str, week_id: str, **kwargs) -> 'BuScheduleListing':
        """
        Get the list of week schedules for the specified week
        Use \"recent\" (without quotes) for the `weekId` path parameter to fetch all forecasts for +/- 26 weeks from the current date. Response will include any schedule which spans the specified week

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format, or 'recent' (without quotes) to get recent schedules (required)
        :param bool include_only_published: includeOnlyPublished
        :param str expand: expand
        :return: BuScheduleListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'include_only_published', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_schedules" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_schedules`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_businessunit_week_schedules`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

        query_params = {}
        if 'include_only_published' in params:
            query_params['includeOnlyPublished'] = params['include_only_published']
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
                                            response_type='BuScheduleListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'BuShortTermForecast':
        """
        Get a short term forecast
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :param list[str] expand: Include to access additional data on the forecast
        :return: BuShortTermForecast
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

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
                                            response_type='BuShortTermForecast',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast_data(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'BuForecastResultResponse':
        """
        Get the result of a short term forecast calculation
        Includes modifications unless you pass the doNotApplyModifications query parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast_data(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :param int week_number: The week number to fetch (for multi-week forecasts)
        :param bool force_download_service: Force the result of this operation to be sent via download service.  For testing/app development purposes
        :return: BuForecastResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id', 'week_number', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast_data" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_data`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_data`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_data`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/data'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

        query_params = {}
        if 'week_number' in params:
            query_params['weekNumber'] = params['week_number']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuForecastResultResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast_generationresults(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'BuForecastGenerationResult':
        """
        Gets the forecast generation results
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast_generationresults(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :return: BuForecastGenerationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast_generationresults" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_generationresults`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_generationresults`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_generationresults`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/generationresults'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

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
                                            response_type='BuForecastGenerationResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'LongTermForecastResultResponse':
        """
        Get the result of a long term forecast calculation
        Includes modifications unless you pass the doNotApplyModifications query parameter

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service.  For testing/app development purposes
        :return: LongTermForecastResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/longtermforecastdata'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='LongTermForecastResultResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'ForecastPlanningGroupsResponse':
        """
        Gets the forecast planning group snapshot
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :return: ForecastPlanningGroupsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/planninggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

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
                                            response_type='ForecastPlanningGroupsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement(self, business_unit_id: str, week_date_id: date, forecast_id: str, **kwargs) -> 'BuForecastStaffingRequirementsResultResponse':
        """
        Get the staffing requirement by planning group for a forecast
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement(business_unit_id, week_date_id, forecast_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast (required)
        :param list[str] week_numbers: The week numbers to fetch (for multi-week forecasts) staffing requirements. Returns all week data if the list is not specified
        :return: BuForecastStaffingRequirementsResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id', 'week_numbers']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/staffingrequirement'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

        query_params = {}
        if 'week_numbers' in params:
            query_params['weekNumbers'] = params['week_numbers']

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
                                            response_type='BuForecastStaffingRequirementsResultResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_week_shorttermforecasts(self, business_unit_id: str, week_date_id: str, **kwargs) -> 'BuShortTermForecastListing':
        """
        Get short term forecasts
        Use \"recent\" (without quotes) for the `weekDateId` path parameter to fetch all forecasts for +/- 26 weeks from the current date. Response will include any forecast which spans the specified week

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_week_shorttermforecasts(business_unit_id, week_date_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param str week_date_id: The week start date of the forecast in yyyy-MM-dd format or 'recent' (without quotes) to fetch recent forecasts (required)
        :return: BuShortTermForecastListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_week_shorttermforecasts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecasts`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_businessunit_week_shorttermforecasts`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

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
                                            response_type='BuShortTermForecastListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_workplanbid(self, business_unit_id: str, bid_id: str, **kwargs) -> 'WorkPlanBid':
        """
        Get a work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The id of the workplanbid (required)
        :return: WorkPlanBid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_workplanbid" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_workplanbid`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_businessunit_workplanbid`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='WorkPlanBid',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_workplanbid_group(self, business_unit_id: str, bid_id: str, bid_group_id: str, **kwargs) -> 'WorkPlanBidGroupResponse':
        """
        Get a bid group by bid group Id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param str bid_group_id: Work Plan Bid Group id (required)
        :return: WorkPlanBidGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'bid_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_workplanbid_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_group_id' is set
        if ('bid_group_id' not in params) or (params['bid_group_id'] is None):
            raise ValueError("Missing the required parameter `bid_group_id` when calling `get_workforcemanagement_businessunit_workplanbid_group`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']
        if 'bid_group_id' in params:
            path_params['bidGroupId'] = params['bid_group_id']

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
                                            response_type='WorkPlanBidGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_workplanbid_group_preferences(self, business_unit_id: str, bid_id: str, bid_group_id: str, **kwargs) -> 'AdminAgentWorkPlanPreferenceResponse':
        """
        Gets the work plan preferences of all the agents in the work plan bid group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param str bid_group_id: The ID of the work plan bid group (required)
        :return: AdminAgentWorkPlanPreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'bid_group_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_workplanbid_group_preferences" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_workplanbid_group_preferences`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_businessunit_workplanbid_group_preferences`")
        # verify the required parameter 'bid_group_id' is set
        if ('bid_group_id' not in params) or (params['bid_group_id'] is None):
            raise ValueError("Missing the required parameter `bid_group_id` when calling `get_workforcemanagement_businessunit_workplanbid_group_preferences`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}/preferences'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']
        if 'bid_group_id' in params:
            path_params['bidGroupId'] = params['bid_group_id']

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
                                            response_type='AdminAgentWorkPlanPreferenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_workplanbid_groups_summary(self, business_unit_id: str, bid_id: str, **kwargs) -> 'WorkPlanBidGroupSummaryList':
        """
        Get summary of bid groups that belong to a work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_workplanbid_groups_summary(business_unit_id, bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :return: WorkPlanBidGroupSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_workplanbid_groups_summary" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_workplanbid_groups_summary`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_businessunit_workplanbid_groups_summary`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/summary'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='WorkPlanBidGroupSummaryList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunit_workplanbids(self, business_unit_id: str, **kwargs) -> 'WorkPlanBidListResponse':
        """
        Get list of work plan bids
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunit_workplanbids(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :return: WorkPlanBidListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunit_workplanbids" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_workforcemanagement_businessunit_workplanbids`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='WorkPlanBidListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunits(self, **kwargs) -> 'BusinessUnitListing':
        """
        Get business units
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunits(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str feature: If specified, the list of business units for which the user is authorized to use the requested feature will be returned
        :param str division_id: If specified, the list of business units belonging to the specified division will be returned
        :return: BusinessUnitListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_businessunits" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/businessunits'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'feature' in params:
            query_params['feature'] = params['feature']
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
                                            response_type='BusinessUnitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_businessunits_divisionviews(self, **kwargs) -> 'BusinessUnitListing':
        """
        Get business units across divisions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_businessunits_divisionviews(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] division_id: The divisionIds to filter by. If omitted, will return business units in all divisions
        :return: BusinessUnitListing
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
                    " to method get_workforcemanagement_businessunits_divisionviews" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/businessunits/divisionviews'.replace('{format}', 'json')
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
                                            response_type='BusinessUnitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_calendar_data_ics(self, calendar_id: str, **kwargs) -> str:
        """
        Get ics formatted calendar based on shareable link
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_calendar_data_ics(calendar_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str calendar_id: The id of the ics-formatted calendar (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['calendar_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_calendar_data_ics" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'calendar_id' is set
        if ('calendar_id' not in params) or (params['calendar_id'] is None):
            raise ValueError("Missing the required parameter `calendar_id` when calling `get_workforcemanagement_calendar_data_ics`")


        resource_path = '/api/v2/workforcemanagement/calendar/data/ics'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'calendar_id' in params:
            query_params['calendarId'] = params['calendar_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/calendar'])
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_calendar_url_ics(self, **kwargs) -> 'CalendarUrlResponse':
        """
        Get existing calendar link for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_calendar_url_ics(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CalendarUrlResponse
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
                    " to method get_workforcemanagement_calendar_url_ics" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/calendar/url/ics'.replace('{format}', 'json')
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
                                            response_type='CalendarUrlResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_historicaldata_bulk_remove_job(self, job_id: str, **kwargs) -> 'HistoricalImportDeleteFilesJobResponse':
        """
        Retrieves delete job status for historical data imports associated with the job id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_historicaldata_bulk_remove_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The job ID of the historical data delete request (required)
        :return: HistoricalImportDeleteFilesJobResponse
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
                    " to method get_workforcemanagement_historicaldata_bulk_remove_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_historicaldata_bulk_remove_job`")


        resource_path = '/api/v2/workforcemanagement/historicaldata/bulk/remove/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportDeleteFilesJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_historicaldata_bulk_remove_jobs(self, **kwargs) -> 'HistoricalImportOverallDeleteStatusResponse':
        """
        Retrieves all delete job status for historical data
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_historicaldata_bulk_remove_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HistoricalImportOverallDeleteStatusResponse
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
                    " to method get_workforcemanagement_historicaldata_bulk_remove_jobs" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/bulk/remove/jobs'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportOverallDeleteStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_workforcemanagement_historicaldata_deletejob is deprecated")
    def get_workforcemanagement_historicaldata_deletejob(self, **kwargs) -> 'HistoricalImportDeleteJobResponse':
        """
        Retrieves delete job status for historical data imports of the organization.
        Deprecated: Please use GET /workforcemanagement/historicaldata/bulk/remove/jobs instead.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_historicaldata_deletejob(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HistoricalImportDeleteJobResponse
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
                    " to method get_workforcemanagement_historicaldata_deletejob" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/deletejob'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportDeleteJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_historicaldata_importstatus(self, **kwargs) -> 'HistoricalImportStatusListing':
        """
        Retrieves status of the historical data imports of the organization
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_historicaldata_importstatus(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HistoricalImportStatusListing
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
                    " to method get_workforcemanagement_historicaldata_importstatus" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/importstatus'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportStatusListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_historicaldata_importstatus_job_id(self, job_id: str, **kwargs) -> 'HistoricalImportStatusJobResponse':
        """
        Retrieves status of the historical data imports associated with job id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_historicaldata_importstatus_job_id(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The job Id of the historical data import request (required)
        :return: HistoricalImportStatusJobResponse
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
                    " to method get_workforcemanagement_historicaldata_importstatus_job_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_historicaldata_importstatus_job_id`")


        resource_path = '/api/v2/workforcemanagement/historicaldata/importstatus/{jobId}'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportStatusJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_integrations_hris(self, **kwargs) -> 'WfmIntegrationListing':
        """
        Get integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_integrations_hris(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: WfmIntegrationListing
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
                    " to method get_workforcemanagement_integrations_hris" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/integrations/hris'.replace('{format}', 'json')
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
                                            response_type='WfmIntegrationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_integrations_hris_timeofftypes_job(self, job_id: str, **kwargs) -> 'HrisTimeOffTypesJobResponse':
        """
        Query the results of time off types job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_integrations_hris_timeofftypes_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job. (required)
        :return: HrisTimeOffTypesJobResponse
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
                    " to method get_workforcemanagement_integrations_hris_timeofftypes_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_integrations_hris_timeofftypes_job`")


        resource_path = '/api/v2/workforcemanagement/integrations/hris/timeofftypes/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='HrisTimeOffTypesJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit(self, management_unit_id: str, **kwargs) -> 'ManagementUnit':
        """
        Get management unit
        settings.shortTermForecasting is deprecated and now lives on the business unit

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param list[str] expand: 
        :return: ManagementUnit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='ManagementUnit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_workforcemanagement_managementunit_activitycodes is deprecated")
    def get_workforcemanagement_managementunit_activitycodes(self, management_unit_id: str, **kwargs) -> 'ActivityCodeContainer':
        """
        Deprecated: Instead use /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes. Get the list of activity codes
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_activitycodes(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :return: ActivityCodeContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_activitycodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_activitycodes`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/activitycodes'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='ActivityCodeContainer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_adherence(self, management_unit_id: str, **kwargs) -> 'UserScheduleAdherenceListing':
        """
        Get a list of user schedule adherence records for the requested management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_adherence(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service.  For testing/app development purposes
        :return: UserScheduleAdherenceListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_adherence" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_adherence`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/adherence'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='UserScheduleAdherenceListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_agent(self, management_unit_id: str, agent_id: str, **kwargs) -> 'WfmAgent':
        """
        Get data for agent in the management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_agent(management_unit_id, agent_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str agent_id: The agent id (required)
        :param bool exclude_capabilities: Excludes all capabilities of the agent such as queues, languages, and skills
        :param list[str] expand: 
        :return: WfmAgent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'agent_id', 'exclude_capabilities', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_agent" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_agent`")
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_workforcemanagement_managementunit_agent`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/{agentId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

        query_params = {}
        if 'exclude_capabilities' in params:
            query_params['excludeCapabilities'] = params['exclude_capabilities']
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
                                            response_type='WfmAgent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_agent_shifttrades(self, management_unit_id: str, agent_id: str, **kwargs) -> 'ShiftTradeListResponse':
        """
        Gets all the shift trades for a given agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_agent_shifttrades(management_unit_id, agent_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str agent_id: The agent id (required)
        :return: ShiftTradeListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'agent_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_agent_shifttrades" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_agent_shifttrades`")
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `get_workforcemanagement_managementunit_agent_shifttrades`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/{agentId}/shifttrades'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='ShiftTradeListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_shifttrades_matched(self, management_unit_id: str, **kwargs) -> 'ShiftTradeMatchesSummaryResponse':
        """
        Gets a summary of all shift trades in the matched state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_shifttrades_matched(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :return: ShiftTradeMatchesSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_shifttrades_matched" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_shifttrades_matched`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/shifttrades/matched'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='ShiftTradeMatchesSummaryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_shifttrades_users(self, management_unit_id: str, **kwargs) -> 'WfmUserEntityListing':
        """
        Gets list of users available for whom you can send direct shift trade requests
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_shifttrades_users(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :return: WfmUserEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_shifttrades_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_shifttrades_users`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/shifttrades/users'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WfmUserEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_timeofflimit(self, management_unit_id: str, time_off_limit_id: str, **kwargs) -> 'TimeOffLimit':
        """
        Gets a time off limit object
        Returns properties of time off limit object, but not daily values.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str time_off_limit_id: The ID of the time off limit to fetch (required)
        :return: TimeOffLimit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_limit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_timeofflimit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_timeofflimit`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `get_workforcemanagement_managementunit_timeofflimit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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
                                            response_type='TimeOffLimit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_timeofflimits(self, management_unit_id: str, **kwargs) -> 'TimeOffLimitListing':
        """
        Gets a list of time off limit objects under management unit.
        Currently only one time off limit object is allowed under management unit, so the list contains either 0 or 1 element.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_timeofflimits(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :return: TimeOffLimitListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_timeofflimits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_timeofflimits`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='TimeOffLimitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_timeoffplan(self, management_unit_id: str, time_off_plan_id: str, **kwargs) -> 'TimeOffPlan':
        """
        Gets a time off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param str time_off_plan_id: The ID of the time off plan to fetch (required)
        :return: TimeOffPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `get_workforcemanagement_managementunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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
                                            response_type='TimeOffPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_timeoffplans(self, management_unit_id: str, **kwargs) -> 'TimeOffPlanListing':
        """
        Gets a list of time off plans
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_timeoffplans(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :return: TimeOffPlanListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_timeoffplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_timeoffplans`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='TimeOffPlanListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_user_timeoffrequest(self, management_unit_id: str, user_id: str, time_off_request_id: str, **kwargs) -> 'TimeOffRequestResponse':
        """
        Get a time off request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str user_id: The userId to whom the Time Off Request applies. (required)
        :param str time_off_request_id: Time Off Request Id (required)
        :return: TimeOffRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'time_off_request_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_user_timeoffrequest" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest`")
        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='TimeOffRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits(self, management_unit_id: str, user_id: str, time_off_request_id: str, **kwargs) -> 'QueryTimeOffLimitValuesResponse':
        """
        Retrieves time off limit, allocated and waitlisted values according to specific time off request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits(management_unit_id, user_id, time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str user_id: The userId to whom the time off request applies. (required)
        :param str time_off_request_id: The ID of the time off request, which dates and activityCodeId determine limit values to retrieve (required)
        :return: QueryTimeOffLimitValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'time_off_request_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits`")
        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}/timeofflimits'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='QueryTimeOffLimitValuesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_user_timeoffrequests(self, management_unit_id: str, user_id: str, **kwargs) -> 'TimeOffRequestList':
        """
        Get a list of time off requests for a given user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_user_timeoffrequests(management_unit_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str user_id: The userId to whom the Time Off Request applies. (required)
        :return: TimeOffRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_user_timeoffrequests" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequests`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_workforcemanagement_managementunit_user_timeoffrequests`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
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
                                            response_type='TimeOffRequestList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_users(self, management_unit_id: str, **kwargs) -> 'WfmUserEntityListing':
        """
        Get users in the management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_users(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :return: WfmUserEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_users" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_users`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WfmUserEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_workforcemanagement_managementunit_week_schedule is deprecated")
    def get_workforcemanagement_managementunit_week_schedule(self, management_unit_id: str, week_id: str, schedule_id: str, **kwargs) -> 'WeekScheduleResponse':
        """
        Deprecated.  Use the equivalent business unit resource instead. Get a week schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format. (required)
        :param str schedule_id: The ID of the schedule to fetch (required)
        :param str expand: Which fields, if any, to expand
        :param bool force_download_service: Force the result of this operation to be sent via download service.  For testing/app development purposes
        :return: WeekScheduleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_id', 'schedule_id', 'expand', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_week_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_week_schedule`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_managementunit_week_schedule`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `get_workforcemanagement_managementunit_week_schedule`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='WeekScheduleResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_workforcemanagement_managementunit_week_schedules is deprecated")
    def get_workforcemanagement_managementunit_week_schedules(self, management_unit_id: str, week_id: str, **kwargs) -> 'WeekScheduleListResponse':
        """
        Deprecated.  Use the equivalent business unit resource instead. Get the list of schedules in a week in management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format. (required)
        :param bool include_only_published: Return only published schedules
        :param str earliest_week_date: The start date of the earliest week to query in yyyy-MM-dd format
        :param str latest_week_date: The start date of the latest week to query in yyyy-MM-dd format
        :return: WeekScheduleListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_id', 'include_only_published', 'earliest_week_date', 'latest_week_date']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_week_schedules" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_week_schedules`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `get_workforcemanagement_managementunit_week_schedules`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

        query_params = {}
        if 'include_only_published' in params:
            query_params['includeOnlyPublished'] = params['include_only_published']
        if 'earliest_week_date' in params:
            query_params['earliestWeekDate'] = params['earliest_week_date']
        if 'latest_week_date' in params:
            query_params['latestWeekDate'] = params['latest_week_date']

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
                                            response_type='WeekScheduleListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_week_shifttrades(self, management_unit_id: str, week_date_id: date, **kwargs) -> 'WeekShiftTradeListResponse':
        """
        Gets all the shift trades for a given week
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param bool evaluate_matches: Whether to evaluate the matches for violations
        :param bool include_cross_week_shifts: Whether to include all shift trades with either the initiating shift or the receiving shift in the week
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: WeekShiftTradeListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'evaluate_matches', 'include_cross_week_shifts', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_week_shifttrades" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_week_shifttrades`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `get_workforcemanagement_managementunit_week_shifttrades`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

        query_params = {}
        if 'evaluate_matches' in params:
            query_params['evaluateMatches'] = params['evaluate_matches']
        if 'include_cross_week_shifts' in params:
            query_params['includeCrossWeekShifts'] = params['include_cross_week_shifts']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='WeekShiftTradeListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_workplan(self, management_unit_id: str, work_plan_id: str, **kwargs) -> 'WorkPlan':
        """
        Get a work plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_id: The ID of the work plan to fetch (required)
        :param list[str] include_only: limit response to the specified fields
        :return: WorkPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_id', 'include_only']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_workplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_workplan`")
        # verify the required parameter 'work_plan_id' is set
        if ('work_plan_id' not in params) or (params['work_plan_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_id` when calling `get_workforcemanagement_managementunit_workplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_id' in params:
            path_params['workPlanId'] = params['work_plan_id']

        query_params = {}
        if 'include_only' in params:
            query_params['includeOnly'] = params['include_only']

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
                                            response_type='WorkPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_workplanrotation(self, management_unit_id: str, work_plan_rotation_id: str, **kwargs) -> 'WorkPlanRotationResponse':
        """
        Get a work plan rotation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_rotation_id: The ID of the work plan rotation to fetch (required)
        :return: WorkPlanRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_rotation_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_workplanrotation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_workplanrotation`")
        # verify the required parameter 'work_plan_rotation_id' is set
        if ('work_plan_rotation_id' not in params) or (params['work_plan_rotation_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_rotation_id` when calling `get_workforcemanagement_managementunit_workplanrotation`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_rotation_id' in params:
            path_params['workPlanRotationId'] = params['work_plan_rotation_id']

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
                                            response_type='WorkPlanRotationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_workplanrotations(self, management_unit_id: str, **kwargs) -> 'WorkPlanRotationListResponse':
        """
        Get work plan rotations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_workplanrotations(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param list[str] expand: 
        :return: WorkPlanRotationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_workplanrotations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_workplanrotations`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WorkPlanRotationListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunit_workplans(self, management_unit_id: str, **kwargs) -> 'WorkPlanListResponse':
        """
        Get work plans
        \"expand=details\" is deprecated

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunit_workplans(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param list[str] expand: Include to access additional data on the work plans
        :param list[str] exclude: Exclude specific data on the work plans from the response
        :return: WorkPlanListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'expand', 'exclude']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunit_workplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `get_workforcemanagement_managementunit_workplans`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'exclude' in params:
            query_params['exclude'] = params['exclude']

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
                                            response_type='WorkPlanListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunits(self, **kwargs) -> 'ManagementUnitListing':
        """
        Get management units
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunits(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Deprecated, paging is not supported
        :param int page_number: Deprecated, paging is not supported
        :param str expand: Deprecated, expand settings on the single MU route
        :param str feature: If specified, the list of management units for which the user is authorized to use the requested feature will be returned
        :param str division_id: If specified, the list of management units belonging to the specified division will be returned
        :return: ManagementUnitListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'feature', 'division_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_managementunits" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/managementunits'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'feature' in params:
            query_params['feature'] = params['feature']
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
                                            response_type='ManagementUnitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_managementunits_divisionviews(self, **kwargs) -> 'ManagementUnitListing':
        """
        Get management units across divisions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_managementunits_divisionviews(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] division_id: The divisionIds to filter by. If omitted, will return all divisions
        :return: ManagementUnitListing
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
                    " to method get_workforcemanagement_managementunits_divisionviews" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/managementunits/divisionviews'.replace('{format}', 'json')
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
                                            response_type='ManagementUnitListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_notifications(self, **kwargs) -> 'NotificationsResponse':
        """
        Get a list of notifications for the current user
        Notifications are only initially sent if you have the relevant Notify and Edit permissions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_notifications(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: NotificationsResponse
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
                    " to method get_workforcemanagement_notifications" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/notifications'.replace('{format}', 'json')
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
                                            response_type='NotificationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_schedulingjob(self, job_id: str, **kwargs) -> 'SchedulingStatusResponse':
        """
        Get status of the scheduling job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_schedulingjob(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The id of the scheduling job (required)
        :return: SchedulingStatusResponse
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
                    " to method get_workforcemanagement_schedulingjob" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_schedulingjob`")


        resource_path = '/api/v2/workforcemanagement/schedulingjobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='SchedulingStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_shifttrades(self, **kwargs) -> 'ShiftTradeListResponse':
        """
        Gets all of my shift trades
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_shifttrades(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ShiftTradeListResponse
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
                    " to method get_workforcemanagement_shifttrades" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/shifttrades'.replace('{format}', 'json')
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
                                            response_type='ShiftTradeListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_shrinkage_job(self, job_id: str, **kwargs) -> 'WfmHistoricalShrinkageResponse':
        """
        Request to fetch the status of the historical shrinkage query
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_shrinkage_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: jobId (required)
        :return: WfmHistoricalShrinkageResponse
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
                    " to method get_workforcemanagement_shrinkage_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_shrinkage_job`")


        resource_path = '/api/v2/workforcemanagement/shrinkage/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='WfmHistoricalShrinkageResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_timeoffbalance_job(self, job_id: str, **kwargs) -> 'TimeOffBalanceJobResponse':
        """
        Query the results of time off types job
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_timeoffbalance_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: The ID of the job. (required)
        :return: TimeOffBalanceJobResponse
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
                    " to method get_workforcemanagement_timeoffbalance_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_workforcemanagement_timeoffbalance_job`")


        resource_path = '/api/v2/workforcemanagement/timeoffbalance/jobs/{jobId}'.replace('{format}', 'json')
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
                                            response_type='TimeOffBalanceJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_timeoffrequest(self, time_off_request_id: str, **kwargs) -> 'TimeOffRequestResponse':
        """
        Get a time off request for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_timeoffrequest(time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str time_off_request_id: The ID of the time off request (required)
        :return: TimeOffRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['time_off_request_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_timeoffrequest" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `get_workforcemanagement_timeoffrequest`")


        resource_path = '/api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId}'.replace('{format}', 'json')
        path_params = {}
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='TimeOffRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_timeoffrequest_waitlistpositions(self, time_off_request_id: str, **kwargs) -> 'WaitlistPositionListing':
        """
        Get the daily waitlist positions of a time off request for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_timeoffrequest_waitlistpositions(time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str time_off_request_id: The ID of the time off request (required)
        :return: WaitlistPositionListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['time_off_request_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_timeoffrequest_waitlistpositions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `get_workforcemanagement_timeoffrequest_waitlistpositions`")


        resource_path = '/api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId}/waitlistpositions'.replace('{format}', 'json')
        path_params = {}
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='WaitlistPositionListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_timeoffrequests(self, **kwargs) -> 'TimeOffRequestList':
        """
        Get a list of time off requests for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_timeoffrequests(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: TimeOffRequestList
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
                    " to method get_workforcemanagement_timeoffrequests" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/timeoffrequests'.replace('{format}', 'json')
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
                                            response_type='TimeOffRequestList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_user_workplanbidranks(self, user_id: str, **kwargs) -> 'WorkPlanBidRanks':
        """
        Get work plan bid ranks for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_user_workplanbidranks(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The userId to whom the work plan bid ranks apply. (required)
        :return: WorkPlanBidRanks
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
                    " to method get_workforcemanagement_user_workplanbidranks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_workforcemanagement_user_workplanbidranks`")


        resource_path = '/api/v2/workforcemanagement/users/{userId}/workplanbidranks'.replace('{format}', 'json')
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
                                            response_type='WorkPlanBidRanks',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_workplanbid_preferences(self, bid_id: str, **kwargs) -> 'AgentWorkPlanBiddingPreferenceResponse':
        """
        Gets an agent's work plan bidding preference
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_workplanbid_preferences(bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bid_id: The ID of the work plan bid (required)
        :return: AgentWorkPlanBiddingPreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bid_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_workplanbid_preferences" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_workplanbid_preferences`")


        resource_path = '/api/v2/workforcemanagement/workplanbids/{bidId}/preferences'.replace('{format}', 'json')
        path_params = {}
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='AgentWorkPlanBiddingPreferenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_workplanbid_workplans(self, bid_id: str, **kwargs) -> 'AgentWorkPlanListResponse':
        """
        Gets an agent's work plans for a bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_workplanbid_workplans(bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bid_id: The ID of the work plan bid (required)
        :return: AgentWorkPlanListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bid_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workforcemanagement_workplanbid_workplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `get_workforcemanagement_workplanbid_workplans`")


        resource_path = '/api/v2/workforcemanagement/workplanbids/{bidId}/workplans'.replace('{format}', 'json')
        path_params = {}
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='AgentWorkPlanListResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_workforcemanagement_workplanbids(self, **kwargs) -> 'AgentWorkPlanBids':
        """
        Gets the list of work plan bids that belong to an agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workforcemanagement_workplanbids(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AgentWorkPlanBids
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
                    " to method get_workforcemanagement_workplanbids" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/workplanbids'.replace('{format}', 'json')
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
                                            response_type='AgentWorkPlanBids',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_agent_adherence_explanation(self, agent_id: str, explanation_id: str, body: 'UpdateAdherenceExplanationStatusRequest', **kwargs) -> 'AdherenceExplanationAsyncResponse':
        """
        Update an adherence explanation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent to query (required)
        :param str explanation_id: The ID of the explanation to update (required)
        :param UpdateAdherenceExplanationStatusRequest body: The request body (required)
        :return: AdherenceExplanationAsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'explanation_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_agent_adherence_explanation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `patch_workforcemanagement_agent_adherence_explanation`")
        # verify the required parameter 'explanation_id' is set
        if ('explanation_id' not in params) or (params['explanation_id'] is None):
            raise ValueError("Missing the required parameter `explanation_id` when calling `patch_workforcemanagement_agent_adherence_explanation`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_agent_adherence_explanation`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/{explanationId}'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']
        if 'explanation_id' in params:
            path_params['explanationId'] = params['explanation_id']

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
                                            response_type='AdherenceExplanationAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_alternativeshifts_trade(self, trade_id: str, **kwargs) -> 'AlternativeShiftTradeResponse':
        """
        Update my alternative shifts trade by trade ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_alternativeshifts_trade(trade_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str trade_id: The ID of the alternative shift trade (required)
        :param AgentUpdateAlternativeShiftTradeRequest body: body
        :return: AlternativeShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trade_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_alternativeshifts_trade" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'trade_id' is set
        if ('trade_id' not in params) or (params['trade_id'] is None):
            raise ValueError("Missing the required parameter `trade_id` when calling `patch_workforcemanagement_alternativeshifts_trade`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades/{tradeId}'.replace('{format}', 'json')
        path_params = {}
        if 'trade_id' in params:
            path_params['tradeId'] = params['trade_id']

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
                                            response_type='AlternativeShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_alternativeshifts_trades_state_jobs(self, body: 'AdminBulkUpdateAlternativeShiftTradeStateRequest', **kwargs) -> 'AlternativeShiftAsyncResponse':
        """
        Bulk update alternative shift trade states
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_alternativeshifts_trades_state_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AdminBulkUpdateAlternativeShiftTradeStateRequest body: The request body (required)
        :return: AlternativeShiftAsyncResponse
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
                    " to method patch_workforcemanagement_alternativeshifts_trades_state_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_alternativeshifts_trades_state_jobs`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades/state/jobs'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit(self, business_unit_id: str, **kwargs) -> 'BusinessUnitResponse':
        """
        Update business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param UpdateBusinessUnitRequest body: body
        :return: BusinessUnitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BusinessUnitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_activitycode(self, business_unit_id: str, activity_code_id: str, **kwargs) -> 'BusinessUnitActivityCode':
        """
        Update an activity code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param str activity_code_id: The ID of the activity code to update (required)
        :param UpdateActivityCodeRequest body: body
        :return: BusinessUnitActivityCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_code_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_activitycode" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_activitycode`")
        # verify the required parameter 'activity_code_id' is set
        if ('activity_code_id' not in params) or (params['activity_code_id'] is None):
            raise ValueError("Missing the required parameter `activity_code_id` when calling `patch_workforcemanagement_businessunit_activitycode`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_code_id' in params:
            path_params['activityCodeId'] = params['activity_code_id']

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
                                            response_type='BusinessUnitActivityCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_activityplan(self, business_unit_id: str, activity_plan_id: str, body: 'UpdateActivityPlanRequest', **kwargs) -> 'ActivityPlanResponse':
        """
        Update an activity plan
        If a job associated with the activity plan is in 'Processing' state the activity plan cannot be updated

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str activity_plan_id: The ID of the activity plan to update (required)
        :param UpdateActivityPlanRequest body: body (required)
        :return: ActivityPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_plan_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_activityplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_activityplan`")
        # verify the required parameter 'activity_plan_id' is set
        if ('activity_plan_id' not in params) or (params['activity_plan_id'] is None):
            raise ValueError("Missing the required parameter `activity_plan_id` when calling `patch_workforcemanagement_businessunit_activityplan`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_businessunit_activityplan`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_plan_id' in params:
            path_params['activityPlanId'] = params['activity_plan_id']

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
                                            response_type='ActivityPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_alternativeshifts_settings(self, business_unit_id: str, **kwargs) -> 'AlternativeShiftBuSettingsResponse':
        """
        Update alternative shifts settings for a business unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param UpdateAlternativeShiftBuSettingsRequest body: body
        :return: AlternativeShiftBuSettingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_alternativeshifts_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_alternativeshifts_settings`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/settings'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='AlternativeShiftBuSettingsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_planninggroup(self, business_unit_id: str, planning_group_id: str, **kwargs) -> 'PlanningGroup':
        """
        Updates the planning group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str planning_group_id: The ID of a planning group to update (required)
        :param UpdatePlanningGroupRequest body: body
        :return: PlanningGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'planning_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_planninggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_planninggroup`")
        # verify the required parameter 'planning_group_id' is set
        if ('planning_group_id' not in params) or (params['planning_group_id'] is None):
            raise ValueError("Missing the required parameter `planning_group_id` when calling `patch_workforcemanagement_businessunit_planninggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'planning_group_id' in params:
            path_params['planningGroupId'] = params['planning_group_id']

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
                                            response_type='PlanningGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_scheduling_run(self, business_unit_id: str, run_id: str, **kwargs) -> None:
        """
        Mark a schedule run as applied
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str run_id: The ID of the schedule run (required)
        :param PatchBuScheduleRunRequest body: body
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'run_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_scheduling_run" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_scheduling_run`")
        # verify the required parameter 'run_id' is set
        if ('run_id' not in params) or (params['run_id'] is None):
            raise ValueError("Missing the required parameter `run_id` when calling `patch_workforcemanagement_businessunit_scheduling_run`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'run_id' in params:
            path_params['runId'] = params['run_id']

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

    def patch_workforcemanagement_businessunit_servicegoaltemplate(self, business_unit_id: str, service_goal_template_id: str, **kwargs) -> 'ServiceGoalTemplate':
        """
        Updates a service goal template
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param str service_goal_template_id: The ID of a service goal template to update (required)
        :param UpdateServiceGoalTemplate body: body
        :return: ServiceGoalTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'service_goal_template_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_servicegoaltemplate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_servicegoaltemplate`")
        # verify the required parameter 'service_goal_template_id' is set
        if ('service_goal_template_id' not in params) or (params['service_goal_template_id'] is None):
            raise ValueError("Missing the required parameter `service_goal_template_id` when calling `patch_workforcemanagement_businessunit_servicegoaltemplate`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'service_goal_template_id' in params:
            path_params['serviceGoalTemplateId'] = params['service_goal_template_id']

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
                                            response_type='ServiceGoalTemplate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_staffinggroup(self, business_unit_id: str, staffing_group_id: str, **kwargs) -> 'StaffingGroupResponse':
        """
        Updates a staffing group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str staffing_group_id: The ID of the staffing group to update (required)
        :param UpdateStaffingGroupRequest body: body
        :return: StaffingGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'staffing_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_staffinggroup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_staffinggroup`")
        # verify the required parameter 'staffing_group_id' is set
        if ('staffing_group_id' not in params) or (params['staffing_group_id'] is None):
            raise ValueError("Missing the required parameter `staffing_group_id` when calling `patch_workforcemanagement_businessunit_staffinggroup`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'staffing_group_id' in params:
            path_params['staffingGroupId'] = params['staffing_group_id']

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
                                            response_type='StaffingGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_timeoffplan(self, business_unit_id: str, time_off_plan_id: str, **kwargs) -> 'BuTimeOffPlanResponse':
        """
        Updates a time-off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_plan_id: The ID of the time-off plan to update (required)
        :param BuUpdateTimeOffPlanRequest body: body
        :return: BuTimeOffPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_plan_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `patch_workforcemanagement_businessunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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
                                            response_type='BuTimeOffPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_workplanbid(self, business_unit_id: str, bid_id: str, body: 'UpdateWorkPlanBid', **kwargs) -> 'WorkPlanBid':
        """
        Update work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The id of the workplanbid (required)
        :param UpdateWorkPlanBid body: The work plan bid to be updated (required)
        :return: WorkPlanBid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_workplanbid" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_workplanbid`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `patch_workforcemanagement_businessunit_workplanbid`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_businessunit_workplanbid`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='WorkPlanBid',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_workplanbid_group(self, business_unit_id: str, bid_id: str, bid_group_id: str, **kwargs) -> 'WorkPlanBidGroupResponse':
        """
        Update a bid group by bid group Id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param str bid_group_id: Work Plan Bid Group id (required)
        :param WorkPlanBidGroupUpdate body: body
        :return: WorkPlanBidGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'bid_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_workplanbid_group" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group`")
        # verify the required parameter 'bid_group_id' is set
        if ('bid_group_id' not in params) or (params['bid_group_id'] is None):
            raise ValueError("Missing the required parameter `bid_group_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']
        if 'bid_group_id' in params:
            path_params['bidGroupId'] = params['bid_group_id']

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
                                            response_type='WorkPlanBidGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_businessunit_workplanbid_group_preferences(self, business_unit_id: str, bid_id: str, bid_group_id: str, **kwargs) -> 'AdminAgentWorkPlanPreferenceResponse':
        """
        Overrides the assigned work plan for the specified agents
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param str bid_group_id: The ID of the work plan bid group (required)
        :param AgentsBidAssignedWorkPlanOverrideRequest body: body
        :return: AdminAgentWorkPlanPreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'bid_group_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_businessunit_workplanbid_group_preferences" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group_preferences`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group_preferences`")
        # verify the required parameter 'bid_group_id' is set
        if ('bid_group_id' not in params) or (params['bid_group_id'] is None):
            raise ValueError("Missing the required parameter `bid_group_id` when calling `patch_workforcemanagement_businessunit_workplanbid_group_preferences`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}/preferences'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']
        if 'bid_group_id' in params:
            path_params['bidGroupId'] = params['bid_group_id']

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
                                            response_type='AdminAgentWorkPlanPreferenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit(self, management_unit_id: str, **kwargs) -> 'ManagementUnit':
        """
        Update the requested management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param UpdateManagementUnitRequest body: body
        :return: ManagementUnit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='ManagementUnit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_agents(self, management_unit_id: str, **kwargs) -> None:
        """
        Update agent configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_agents(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param UpdateMuAgentsRequest body: body
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_agents" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_agents`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agents'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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

    def patch_workforcemanagement_managementunit_agents_workplans_bulk(self, management_unit_id: str, **kwargs) -> 'UpdateMuAgentWorkPlansBatchResponse':
        """
        Updates agent work plan configuration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_agents_workplans_bulk(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param UpdateMuAgentWorkPlansBatchRequest body: body
        :return: UpdateMuAgentWorkPlansBatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_agents_workplans_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_agents_workplans_bulk`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/workplans/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='UpdateMuAgentWorkPlansBatchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_timeofflimit(self, management_unit_id: str, time_off_limit_id: str, **kwargs) -> 'TimeOffLimit':
        """
        Updates a time off limit object.
        Updates time off limit object properties, but not daily values.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str time_off_limit_id: The id of time off limit object to update (required)
        :param UpdateTimeOffLimitRequest body: body
        :return: TimeOffLimit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_limit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_timeofflimit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_timeofflimit`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `patch_workforcemanagement_managementunit_timeofflimit`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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
                                            response_type='TimeOffLimit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_timeoffplan(self, management_unit_id: str, time_off_plan_id: str, **kwargs) -> 'TimeOffPlan':
        """
        Updates a time off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param str time_off_plan_id: The ID of the time off plan to update (required)
        :param UpdateTimeOffPlanRequest body: body
        :return: TimeOffPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_plan_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_timeoffplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_timeoffplan`")
        # verify the required parameter 'time_off_plan_id' is set
        if ('time_off_plan_id' not in params) or (params['time_off_plan_id'] is None):
            raise ValueError("Missing the required parameter `time_off_plan_id` when calling `patch_workforcemanagement_managementunit_timeoffplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_plan_id' in params:
            path_params['timeOffPlanId'] = params['time_off_plan_id']

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
                                            response_type='TimeOffPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus(self, management_unit_id: str, time_off_request_id: str, user_id: str, **kwargs) -> 'UserTimeOffIntegrationStatusResponse':
        """
        Set integration status for a time off request.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus(management_unit_id, time_off_request_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str time_off_request_id: The ID of the time off request. (required)
        :param str user_id: The ID of user to whom the time off request belongs. (required)
        :param SetTimeOffIntegrationStatusRequest body: body
        :return: UserTimeOffIntegrationStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_request_id', 'user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus`")
        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/{timeOffRequestId}/users/{userId}/integrationstatus'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']
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
                                            response_type='UserTimeOffIntegrationStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_user_timeoffrequest(self, management_unit_id: str, user_id: str, time_off_request_id: str, **kwargs) -> 'TimeOffRequestResponse':
        """
        Update a time off request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str user_id: The id of the user the requested time off request belongs to (required)
        :param str time_off_request_id: The id of the time off request to update (required)
        :param AdminTimeOffRequestPatch body: body
        :return: TimeOffRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'time_off_request_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_user_timeoffrequest" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_user_timeoffrequest`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_workforcemanagement_managementunit_user_timeoffrequest`")
        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `patch_workforcemanagement_managementunit_user_timeoffrequest`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='TimeOffRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_week_shifttrade(self, management_unit_id: str, week_date_id: date, trade_id: str, body: 'PatchShiftTradeRequest', **kwargs) -> 'ShiftTradeResponse':
        """
        Updates a shift trade. This route can only be called by the initiating agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_week_shifttrade(management_unit_id, week_date_id, trade_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str trade_id: The ID of the shift trade to update (required)
        :param PatchShiftTradeRequest body: body (required)
        :return: ShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'trade_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_week_shifttrade" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_week_shifttrade`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `patch_workforcemanagement_managementunit_week_shifttrade`")
        # verify the required parameter 'trade_id' is set
        if ('trade_id' not in params) or (params['trade_id'] is None):
            raise ValueError("Missing the required parameter `trade_id` when calling `patch_workforcemanagement_managementunit_week_shifttrade`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_managementunit_week_shifttrade`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/{tradeId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'trade_id' in params:
            path_params['tradeId'] = params['trade_id']

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
                                            response_type='ShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_workplan(self, management_unit_id: str, work_plan_id: str, **kwargs) -> 'WorkPlan':
        """
        Update a work plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_id: The ID of the work plan to update (required)
        :param str validation_mode: Allows to update work plan even if validation result is invalid
        :param WorkPlan body: body
        :return: WorkPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_id', 'validation_mode', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_workplan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_workplan`")
        # verify the required parameter 'work_plan_id' is set
        if ('work_plan_id' not in params) or (params['work_plan_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_id` when calling `patch_workforcemanagement_managementunit_workplan`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_id' in params:
            path_params['workPlanId'] = params['work_plan_id']

        query_params = {}
        if 'validation_mode' in params:
            query_params['validationMode'] = params['validation_mode']

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
                                            response_type='WorkPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_managementunit_workplanrotation(self, management_unit_id: str, work_plan_rotation_id: str, **kwargs) -> 'WorkPlanRotationResponse':
        """
        Update a work plan rotation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_rotation_id: The ID of the work plan rotation to update (required)
        :param UpdateWorkPlanRotationRequest body: body
        :return: WorkPlanRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_rotation_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_managementunit_workplanrotation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `patch_workforcemanagement_managementunit_workplanrotation`")
        # verify the required parameter 'work_plan_rotation_id' is set
        if ('work_plan_rotation_id' not in params) or (params['work_plan_rotation_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_rotation_id` when calling `patch_workforcemanagement_managementunit_workplanrotation`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId}'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_rotation_id' in params:
            path_params['workPlanRotationId'] = params['work_plan_rotation_id']

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
                                            response_type='WorkPlanRotationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_timeoffrequest(self, time_off_request_id: str, **kwargs) -> 'TimeOffRequestResponse':
        """
        Update a time off request for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_timeoffrequest(time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str time_off_request_id: The ID of the time off request (required)
        :param AgentTimeOffRequestPatch body: body
        :return: TimeOffRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['time_off_request_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_timeoffrequest" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `patch_workforcemanagement_timeoffrequest`")


        resource_path = '/api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId}'.replace('{format}', 'json')
        path_params = {}
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='TimeOffRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_user_workplanbidranks(self, user_id: str, **kwargs) -> 'WorkPlanBidRanks':
        """
        Update work plan bid ranks for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_user_workplanbidranks(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: The userId to whom the work plan bid ranks apply. (required)
        :param WorkPlanBidRanks body: body
        :return: WorkPlanBidRanks
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
                    " to method patch_workforcemanagement_user_workplanbidranks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_workforcemanagement_user_workplanbidranks`")


        resource_path = '/api/v2/workforcemanagement/users/{userId}/workplanbidranks'.replace('{format}', 'json')
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
                                            response_type='WorkPlanBidRanks',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_users_workplanbidranks_bulk(self, body: List['WorkPlanBidRanks'], **kwargs) -> 'EntityListing':
        """
        Update bulk work plan bid ranks on users. Max 50 users can be updated at a time.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_users_workplanbidranks_bulk(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[WorkPlanBidRanks] body: Users (required)
        :return: EntityListing
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
                    " to method patch_workforcemanagement_users_workplanbidranks_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_workforcemanagement_users_workplanbidranks_bulk`")


        resource_path = '/api/v2/workforcemanagement/users/workplanbidranks/bulk'.replace('{format}', 'json')
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
                                            response_type='EntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_workforcemanagement_workplanbid_preferences(self, bid_id: str, **kwargs) -> 'AgentWorkPlanBiddingPreferenceResponse':
        """
        Update an agent's work plan bidding preference
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_workforcemanagement_workplanbid_preferences(bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bid_id: The ID of the work plan bid (required)
        :param UpdateAgentWorkPlanBiddingPreference body: body
        :return: AgentWorkPlanBiddingPreferenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bid_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_workforcemanagement_workplanbid_preferences" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `patch_workforcemanagement_workplanbid_preferences`")


        resource_path = '/api/v2/workforcemanagement/workplanbids/{bidId}/preferences'.replace('{format}', 'json')
        path_params = {}
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='AgentWorkPlanBiddingPreferenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_adherence_explanations(self, body: 'AddAdherenceExplanationAgentRequest', **kwargs) -> 'AdherenceExplanationAsyncResponse':
        """
        Submit an adherence explanation for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_adherence_explanations(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AddAdherenceExplanationAgentRequest body: The request body (required)
        :return: AdherenceExplanationAsyncResponse
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
                    " to method post_workforcemanagement_adherence_explanations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_adherence_explanations`")


        resource_path = '/api/v2/workforcemanagement/adherence/explanations'.replace('{format}', 'json')
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
                                            response_type='AdherenceExplanationAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_adherence_explanations_query(self, body: 'AgentQueryAdherenceExplanationsRequest', **kwargs) -> 'QueryAdherenceExplanationsResponse':
        """
        Query adherence explanations for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_adherence_explanations_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentQueryAdherenceExplanationsRequest body: The request body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: QueryAdherenceExplanationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'force_async', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_adherence_explanations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_adherence_explanations_query`")


        resource_path = '/api/v2/workforcemanagement/adherence/explanations/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='QueryAdherenceExplanationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_workforcemanagement_adherence_historical is deprecated")
    def post_workforcemanagement_adherence_historical(self, **kwargs) -> 'WfmHistoricalAdherenceResponse':
        """
        Deprecated. Use bulk routes instead (/adherence/historical/bulk)
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_adherence_historical(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WfmHistoricalAdherenceQueryForUsers body: body
        :return: WfmHistoricalAdherenceResponse
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
                    " to method post_workforcemanagement_adherence_historical" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/adherence/historical'.replace('{format}', 'json')
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
                                            response_type='WfmHistoricalAdherenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_adherence_historical_bulk(self, **kwargs) -> 'WfmHistoricalAdherenceBulkResponse':
        """
        Request a historical adherence report in bulk
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_adherence_historical_bulk(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WfmHistoricalAdherenceBulkQuery body: body
        :return: WfmHistoricalAdherenceBulkResponse
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
                    " to method post_workforcemanagement_adherence_historical_bulk" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/adherence/historical/bulk'.replace('{format}', 'json')
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
                                            response_type='WfmHistoricalAdherenceBulkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agent_adherence_explanations(self, agent_id: str, body: 'AddAdherenceExplanationAdminRequest', **kwargs) -> 'AdherenceExplanationAsyncResponse':
        """
        Add an adherence explanation for the requested user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agent_adherence_explanations(agent_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent to query (required)
        :param AddAdherenceExplanationAdminRequest body: The request body (required)
        :return: AdherenceExplanationAsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_agent_adherence_explanations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `post_workforcemanagement_agent_adherence_explanations`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_agent_adherence_explanations`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/adherence/explanations'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='AdherenceExplanationAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agent_adherence_explanations_query(self, agent_id: str, body: 'AgentQueryAdherenceExplanationsRequest', **kwargs) -> 'AgentQueryAdherenceExplanationsResponse':
        """
        Query adherence explanations for the given agent across a specified range
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agent_adherence_explanations_query(agent_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent to query (required)
        :param AgentQueryAdherenceExplanationsRequest body: The request body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: AgentQueryAdherenceExplanationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'body', 'force_async', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_agent_adherence_explanations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `post_workforcemanagement_agent_adherence_explanations_query`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_agent_adherence_explanations_query`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/query'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='AgentQueryAdherenceExplanationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agents(self, **kwargs) -> 'MoveAgentsResponse':
        """
        Move agents in and out of management unit
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agents(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MoveAgentsRequest body: body
        :return: MoveAgentsResponse
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
                    " to method post_workforcemanagement_agents" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/agents'.replace('{format}', 'json')
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
                                            response_type='MoveAgentsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agents_integrations_hris_query(self, **kwargs) -> 'AgentsIntegrationsListing':
        """
        Query integrations for agents
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agents_integrations_hris_query(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param QueryAgentsIntegrationsRequest body: body
        :return: AgentsIntegrationsListing
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
                    " to method post_workforcemanagement_agents_integrations_hris_query" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/agents/integrations/hris/query'.replace('{format}', 'json')
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
                                            response_type='AgentsIntegrationsListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agents_me_possibleworkshifts(self, body: 'AgentPossibleWorkShiftsRequest', **kwargs) -> 'AgentPossibleWorkShiftsResponse':
        """
        Get agent possible work shifts for requested time frame
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agents_me_possibleworkshifts(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentPossibleWorkShiftsRequest body: body (required)
        :return: AgentPossibleWorkShiftsResponse
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
                    " to method post_workforcemanagement_agents_me_possibleworkshifts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_agents_me_possibleworkshifts`")


        resource_path = '/api/v2/workforcemanagement/agents/me/possibleworkshifts'.replace('{format}', 'json')
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
                                            response_type='AgentPossibleWorkShiftsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_agentschedules_mine(self, **kwargs) -> 'BuCurrentAgentScheduleSearchResponse':
        """
        Get published schedule for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_agentschedules_mine(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BuGetCurrentAgentScheduleRequest body: body
        :return: BuCurrentAgentScheduleSearchResponse
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
                    " to method post_workforcemanagement_agentschedules_mine" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/agentschedules/mine'.replace('{format}', 'json')
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
                                            response_type='BuCurrentAgentScheduleSearchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_alternativeshifts_offers_jobs(self, body: 'AlternativeShiftOffersRequest', **kwargs) -> 'AlternativeShiftAsyncResponse':
        """
        Request a list of alternative shift offers for a given schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_alternativeshifts_offers_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AlternativeShiftOffersRequest body: The request body (required)
        :return: AlternativeShiftAsyncResponse
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
                    " to method post_workforcemanagement_alternativeshifts_offers_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_alternativeshifts_offers_jobs`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/offers/jobs'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_alternativeshifts_offers_search_jobs(self, body: 'AlternativeShiftSearchOffersRequest', **kwargs) -> 'AlternativeShiftAsyncResponse':
        """
        Request a search of alternative shift offers for a given shift
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_alternativeshifts_offers_search_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AlternativeShiftSearchOffersRequest body: The request body (required)
        :return: AlternativeShiftAsyncResponse
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
                    " to method post_workforcemanagement_alternativeshifts_offers_search_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_alternativeshifts_offers_search_jobs`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/offers/search/jobs'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_alternativeshifts_trades(self, body: 'CreateAlternativeShiftTradeRequest', **kwargs) -> 'AlternativeShiftTradeResponse':
        """
        Create my alternative shift trade using an existing offer's jobId
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_alternativeshifts_trades(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAlternativeShiftTradeRequest body: The request body (required)
        :return: AlternativeShiftTradeResponse
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
                    " to method post_workforcemanagement_alternativeshifts_trades" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_alternativeshifts_trades`")


        resource_path = '/api/v2/workforcemanagement/alternativeshifts/trades'.replace('{format}', 'json')
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
                                            response_type='AlternativeShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_activitycodes(self, business_unit_id: str, **kwargs) -> 'BusinessUnitActivityCode':
        """
        Create a new activity code
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_activitycodes(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit, or 'mine' for the business unit of the logged-in user. (required)
        :param CreateActivityCodeRequest body: body
        :return: BusinessUnitActivityCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_activitycodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_activitycodes`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BusinessUnitActivityCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_activityplan_runs_jobs(self, business_unit_id: str, activity_plan_id: str, **kwargs) -> 'ActivityPlanJobResponse':
        """
        Run an activity plan manually
        Triggers a job running the activity plan. The activity plan cannot be updated until the job completes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_activityplan_runs_jobs(business_unit_id, activity_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str activity_plan_id: The ID of the activity plan to run (required)
        :return: ActivityPlanJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'activity_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_activityplan_runs_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_activityplan_runs_jobs`")
        # verify the required parameter 'activity_plan_id' is set
        if ('activity_plan_id' not in params) or (params['activity_plan_id'] is None):
            raise ValueError("Missing the required parameter `activity_plan_id` when calling `post_workforcemanagement_businessunit_activityplan_runs_jobs`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}/runs/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'activity_plan_id' in params:
            path_params['activityPlanId'] = params['activity_plan_id']

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
                                            response_type='ActivityPlanJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_activityplans(self, business_unit_id: str, body: 'CreateActivityPlanRequest', **kwargs) -> 'ActivityPlanResponse':
        """
        Create an activity plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_activityplans(business_unit_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param CreateActivityPlanRequest body: body (required)
        :return: ActivityPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_activityplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_activityplans`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_activityplans`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='ActivityPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_adherence_explanations_query(self, business_unit_id: str, body: 'BuQueryAdherenceExplanationsRequest', **kwargs) -> 'BuQueryAdherenceExplanationsResponse':
        """
        Query adherence explanations across an entire business unit for the requested period
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_adherence_explanations_query(business_unit_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param BuQueryAdherenceExplanationsRequest body: The request body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: BuQueryAdherenceExplanationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body', 'force_async', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_adherence_explanations_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_adherence_explanations_query`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_adherence_explanations_query`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/adherence/explanations/query'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuQueryAdherenceExplanationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_agentschedules_search(self, business_unit_id: str, **kwargs) -> 'BuAsyncAgentSchedulesSearchResponse':
        """
        Search published schedules
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_agentschedules_search(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :param BuSearchAgentSchedulesRequest body: body
        :return: BuAsyncAgentSchedulesSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'force_async', 'force_download_service', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_agentschedules_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_agentschedules_search`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/agentschedules/search'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuAsyncAgentSchedulesSearchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_alternativeshifts_trades_search(self, business_unit_id: str, body: 'SearchAlternativeShiftTradesRequest', **kwargs) -> 'BuListAlternativeShiftTradesResponse':
        """
        List alternative shifts trades for a given management unit or agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_alternativeshifts_trades_search(business_unit_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param SearchAlternativeShiftTradesRequest body: The request body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :return: BuListAlternativeShiftTradesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body', 'force_async']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_alternativeshifts_trades_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_alternativeshifts_trades_search`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_alternativeshifts_trades_search`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/search'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='BuListAlternativeShiftTradesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_intraday(self, business_unit_id: str, **kwargs) -> 'AsyncIntradayResponse':
        """
        Get intraday data for the given date for the requested planningGroupIds
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_intraday(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :param IntradayPlanningGroupRequest body: body
        :return: AsyncIntradayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'force_async', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_intraday" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_intraday`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/intraday'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='AsyncIntradayResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_planninggroups(self, business_unit_id: str, **kwargs) -> 'PlanningGroup':
        """
        Adds a new planning group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_planninggroups(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param CreatePlanningGroupRequest body: body
        :return: PlanningGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_planninggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_planninggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='PlanningGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_servicegoaltemplates(self, business_unit_id: str, **kwargs) -> 'ServiceGoalTemplate':
        """
        Adds a new service goal template
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit. (required)
        :param CreateServiceGoalTemplate body: body
        :return: ServiceGoalTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_servicegoaltemplates" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_servicegoaltemplates`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='ServiceGoalTemplate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_staffinggroups(self, business_unit_id: str, **kwargs) -> 'StaffingGroupResponse':
        """
        Creates a new staffing group
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_staffinggroups(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param CreateStaffingGroupRequest body: body
        :return: StaffingGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_staffinggroups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_staffinggroups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='StaffingGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_staffinggroups_query(self, business_unit_id: str, **kwargs) -> 'UserStaffingGroupListing':
        """
        Gets staffing group associations for a list of user IDs
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_staffinggroups_query(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param QueryUserStaffingGroupListRequest body: body
        :return: UserStaffingGroupListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_staffinggroups_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_staffinggroups_query`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/query'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='UserStaffingGroupListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_timeofflimits(self, business_unit_id: str, **kwargs) -> 'BuTimeOffLimitResponse':
        """
        Creates a new time-off limit object
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_timeofflimits(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param BuCreateTimeOffLimitRequest body: body
        :return: BuTimeOffLimitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_timeofflimits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_timeofflimits`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BuTimeOffLimitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_timeofflimits_values_query(self, business_unit_id: str, **kwargs) -> 'BuTimeOffLimitValuesResponse':
        """
        Retrieves time-off limit related values based on a given set of filters.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_timeofflimits_values_query(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param QueryTimeOffLimitValuesRequest body: body
        :return: BuTimeOffLimitValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_timeofflimits_values_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_timeofflimits_values_query`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/values/query'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BuTimeOffLimitValuesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_timeoffplans(self, business_unit_id: str, **kwargs) -> 'BuTimeOffPlanResponse':
        """
        Creates a new time-off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_timeoffplans(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param BuCreateTimeOffPlanRequest body: body
        :return: BuTimeOffPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_timeoffplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_timeoffplans`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='BuTimeOffPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_agentschedules_query(self, business_unit_id: str, week_id: date, schedule_id: str, body: 'BuQueryAgentSchedulesRequest', **kwargs) -> 'BuAsyncAgentSchedulesQueryResponse':
        """
        Loads agent schedule data from the schedule. Used in combination with the metadata route
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_agentschedules_query(business_unit_id, week_id, schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param BuQueryAgentSchedulesRequest body: body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: BuAsyncAgentSchedulesQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body', 'force_async', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_agentschedules_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_agentschedules_query`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_agentschedules_query`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_agentschedules_query`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedule_agentschedules_query`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/agentschedules/query'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuAsyncAgentSchedulesQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_copy(self, business_unit_id: str, week_id: date, schedule_id: str, body: 'BuCopyScheduleRequest', **kwargs) -> 'BuAsyncScheduleResponse':
        """
        Copy a schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_copy(business_unit_id, week_id, schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule to copy (required)
        :param BuCopyScheduleRequest body: body (required)
        :return: BuAsyncScheduleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_copy`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_copy`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_copy`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedule_copy`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BuAsyncScheduleResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations(self, business_unit_id: str, week_id: str, schedule_id: str, **kwargs) -> 'PerformancePredictionRecalculationResponse':
        """
        Request a daily recalculation of the performance prediction for the associated schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the performance prediction belongs (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format (required)
        :param str schedule_id: The ID of the schedule the performance prediction belongs to (required)
        :param WfmProcessUploadRequest body: body
        :return: PerformancePredictionRecalculationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PerformancePredictionRecalculationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl(self, business_unit_id: str, week_id: str, schedule_id: str, **kwargs) -> 'PerformancePredictionRecalculationUploadResponse':
        """
        Upload daily activity changes to be able to request a performance prediction recalculation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl(business_unit_id, week_id, schedule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the performance prediction belongs (required)
        :param str week_id: First day of schedule week in yyyy-MM-dd format (required)
        :param str schedule_id: The ID of the schedule the performance prediction belongs to (required)
        :param UploadUrlRequestBody body: body
        :return: PerformancePredictionRecalculationUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations/uploadurl'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PerformancePredictionRecalculationUploadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_reschedule(self, business_unit_id: str, week_id: date, schedule_id: str, body: 'BuRescheduleRequest', **kwargs) -> 'BuAsyncScheduleRunResponse':
        """
        Start a rescheduling run
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_reschedule(business_unit_id, week_id, schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param BuRescheduleRequest body: body (required)
        :return: BuAsyncScheduleRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_reschedule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_reschedule`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_reschedule`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_reschedule`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedule_reschedule`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/reschedule'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BuAsyncScheduleRunResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_update(self, business_unit_id: str, week_id: date, schedule_id: str, body: 'ProcessScheduleUpdateUploadRequest', **kwargs) -> 'BuAsyncScheduleResponse':
        """
        Starts processing a schedule update
        Call after uploading the schedule data to the url supplied by the /update/uploadurl route

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_update(business_unit_id, week_id, schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param ProcessScheduleUpdateUploadRequest body: body (required)
        :return: BuAsyncScheduleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_update" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_update`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_update`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedule_update`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/update'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BuAsyncScheduleResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedule_update_uploadurl(self, business_unit_id: str, week_id: date, schedule_id: str, body: 'UploadUrlRequestBody', **kwargs) -> 'UpdateScheduleUploadResponse':
        """
        Creates a signed upload URL for updating a schedule
        Once the upload is complete, call the /{scheduleId}/update route to start the schedule update process

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedule_update_uploadurl(business_unit_id, week_id, schedule_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str schedule_id: The ID of the schedule (required)
        :param UploadUrlRequestBody body: body (required)
        :return: UpdateScheduleUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'schedule_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedule_update_uploadurl" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedule_update_uploadurl`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedule_update_uploadurl`")
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params) or (params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `post_workforcemanagement_businessunit_week_schedule_update_uploadurl`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedule_update_uploadurl`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/update/uploadurl'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='UpdateScheduleUploadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedules(self, business_unit_id: str, week_id: date, body: 'BuCreateBlankScheduleRequest', **kwargs) -> 'BuScheduleMetadata':
        """
        Create a blank schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param BuCreateBlankScheduleRequest body: body (required)
        :return: BuScheduleMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedules" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedules`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedules`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedules`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

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
                                            response_type='BuScheduleMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedules_generate(self, business_unit_id: str, week_id: date, body: 'BuGenerateScheduleRequest', **kwargs) -> 'BuAsyncScheduleRunResponse':
        """
        Generate a schedule
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedules_generate(business_unit_id, week_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param BuGenerateScheduleRequest body: body (required)
        :return: BuAsyncScheduleRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedules_generate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedules_generate`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedules_generate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedules_generate`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/generate'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

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
                                            response_type='BuAsyncScheduleRunResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedules_import(self, business_unit_id: str, week_id: date, body: 'WfmProcessUploadRequest', **kwargs) -> 'ScheduleUploadProcessingResponse':
        """
        Starts processing a schedule import
        Call after uploading the schedule data to the url supplied by the /import/uploadurl route

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedules_import(business_unit_id, week_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param WfmProcessUploadRequest body:  (required)
        :return: ScheduleUploadProcessingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedules_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedules_import`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedules_import`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedules_import`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/import'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

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
                                            response_type='ScheduleUploadProcessingResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_schedules_import_uploadurl(self, business_unit_id: str, week_id: date, body: 'UploadUrlRequestBody', **kwargs) -> 'ImportScheduleUploadResponse':
        """
        Creates a signed upload URL for importing a schedule
        Once the upload is complete, call the /import route to start the schedule import process

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_schedules_import_uploadurl(business_unit_id, week_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param date week_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param UploadUrlRequestBody body: body (required)
        :return: ImportScheduleUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_schedules_import_uploadurl" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_schedules_import_uploadurl`")
        # verify the required parameter 'week_id' is set
        if ('week_id' not in params) or (params['week_id'] is None):
            raise ValueError("Missing the required parameter `week_id` when calling `post_workforcemanagement_businessunit_week_schedules_import_uploadurl`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_schedules_import_uploadurl`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/import/uploadurl'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_id' in params:
            path_params['weekId'] = params['week_id']

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
                                            response_type='ImportScheduleUploadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_shorttermforecast_copy(self, business_unit_id: str, week_date_id: date, forecast_id: str, body: 'CopyBuForecastRequest', **kwargs) -> 'AsyncForecastOperationResult':
        """
        Copy a short term forecast
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_shorttermforecast_copy(business_unit_id, week_date_id, forecast_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str forecast_id: The ID of the forecast to copy (required)
        :param CopyBuForecastRequest body: body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :return: AsyncForecastOperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'forecast_id', 'body', 'force_async']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_shorttermforecast_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecast_copy`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecast_copy`")
        # verify the required parameter 'forecast_id' is set
        if ('forecast_id' not in params) or (params['forecast_id'] is None):
            raise ValueError("Missing the required parameter `forecast_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecast_copy`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_shorttermforecast_copy`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'forecast_id' in params:
            path_params['forecastId'] = params['forecast_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='AsyncForecastOperationResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_shorttermforecasts_generate(self, business_unit_id: str, week_date_id: date, body: 'GenerateBuForecastRequest', **kwargs) -> 'AsyncForecastOperationResult':
        """
        Generate a short term forecast
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_shorttermforecasts_generate(business_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param GenerateBuForecastRequest body: body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :return: AsyncForecastOperationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'body', 'force_async']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_shorttermforecasts_generate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_generate`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_generate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_generate`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/generate'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='AsyncForecastOperationResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_shorttermforecasts_import(self, business_unit_id: str, week_date_id: date, body: 'WfmProcessUploadRequest', **kwargs) -> 'ImportForecastResponse':
        """
        Starts importing the uploaded short term forecast
        Call after uploading the forecast data to the url supplied by the /import/uploadurl route

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_shorttermforecasts_import(business_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param WfmProcessUploadRequest body: body (required)
        :return: ImportForecastResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_shorttermforecasts_import" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/import'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

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
                                            response_type='ImportForecastResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl(self, business_unit_id: str, week_date_id: date, body: 'UploadUrlRequestBody', **kwargs) -> 'ImportForecastUploadResponse':
        """
        Creates a signed upload URL for importing a short term forecast
        Once the upload is complete, call the /import route to start the short term forecast import process

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl(business_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit to which the forecast belongs (required)
        :param date week_date_id: First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param UploadUrlRequestBody body: body (required)
        :return: ImportForecastUploadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'week_date_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/import/uploadurl'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

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
                                            response_type='ImportForecastUploadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_workplanbid_copy(self, business_unit_id: str, bid_id: str, **kwargs) -> 'WorkPlanBid':
        """
        Copy a work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_workplanbid_copy(business_unit_id, bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The ID of the work plan bid to copy (required)
        :param CopyWorkPlanBid body: body
        :return: WorkPlanBid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_workplanbid_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_workplanbid_copy`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `post_workforcemanagement_businessunit_workplanbid_copy`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='WorkPlanBid',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_workplanbid_groups(self, business_unit_id: str, bid_id: str, **kwargs) -> 'WorkPlanBidGroupResponse':
        """
        Add a bid group in a given work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_workplanbid_groups(business_unit_id, bid_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str bid_id: The work plan bid id of the bid groups (required)
        :param WorkPlanBidGroupCreate body: body
        :return: WorkPlanBidGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'bid_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_workplanbid_groups" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_workplanbid_groups`")
        # verify the required parameter 'bid_id' is set
        if ('bid_id' not in params) or (params['bid_id'] is None):
            raise ValueError("Missing the required parameter `bid_id` when calling `post_workforcemanagement_businessunit_workplanbid_groups`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'bid_id' in params:
            path_params['bidId'] = params['bid_id']

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
                                            response_type='WorkPlanBidGroupResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunit_workplanbids(self, business_unit_id: str, **kwargs) -> 'WorkPlanBid':
        """
        Create a new work plan bid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunit_workplanbids(business_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param CreateWorkPlanBid body: The work plan bid to be created
        :return: WorkPlanBid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_businessunit_workplanbids" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `post_workforcemanagement_businessunit_workplanbids`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']

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
                                            response_type='WorkPlanBid',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_businessunits(self, **kwargs) -> 'BusinessUnitResponse':
        """
        Add a new business unit
        It may take a minute or two for a new business unit to be available for api operations

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_businessunits(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBusinessUnitRequest body: body
        :return: BusinessUnitResponse
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
                    " to method post_workforcemanagement_businessunits" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/businessunits'.replace('{format}', 'json')
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
                                            response_type='BusinessUnitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_calendar_url_ics(self, **kwargs) -> 'CalendarUrlResponse':
        """
        Create a newly generated calendar link for the current user; if the current user has previously generated one, the generated link will be returned
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_calendar_url_ics(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str language: A language tag (which is sometimes referred to as a \"locale identifier\") to use to localize default activity code names in the ics-formatted calendar
        :return: CalendarUrlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_calendar_url_ics" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/calendar/url/ics'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'language' in params:
            query_params['language'] = params['language']

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
                                            response_type='CalendarUrlResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_historicaldata_bulk_remove_jobs(self, **kwargs) -> 'HistoricalImportDeleteFilesJobResponse':
        """
        Delete the list of the historical data import entries
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_historicaldata_bulk_remove_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HistoricalImportDeleteFilesJobRequest body: body
        :return: HistoricalImportDeleteFilesJobResponse
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
                    " to method post_workforcemanagement_historicaldata_bulk_remove_jobs" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/bulk/remove/jobs'.replace('{format}', 'json')
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
                                            response_type='HistoricalImportDeleteFilesJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_workforcemanagement_historicaldata_deletejob is deprecated")
    def post_workforcemanagement_historicaldata_deletejob(self, **kwargs) -> 'HistoricalImportDeleteJobResponse':
        """
        Delete the entries of the historical data imports in the organization.
        Deprecated: Please use POST /workforcemanagement/historicaldata/bulk/remove/jobs instead.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_historicaldata_deletejob(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HistoricalImportDeleteJobResponse
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
                    " to method post_workforcemanagement_historicaldata_deletejob" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/deletejob'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HistoricalImportDeleteJobResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_historicaldata_validate(self, **kwargs) -> 'ValidationServiceAsyncResponse':
        """
        Trigger validation process for historical import
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_historicaldata_validate(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ValidationServiceRequest body: body
        :return: ValidationServiceAsyncResponse
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
                    " to method post_workforcemanagement_historicaldata_validate" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/historicaldata/validate'.replace('{format}', 'json')
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
                                            response_type='ValidationServiceAsyncResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_integrations_hri_timeofftypes_jobs(self, hris_integration_id: str, **kwargs) -> 'HrisTimeOffTypesResponse':
        """
        Get list of time off types configured in integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_integrations_hri_timeofftypes_jobs(hris_integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hris_integration_id: The ID of the HRIS integration for which time off types are queried. (required)
        :return: HrisTimeOffTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hris_integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_integrations_hri_timeofftypes_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hris_integration_id' is set
        if ('hris_integration_id' not in params) or (params['hris_integration_id'] is None):
            raise ValueError("Missing the required parameter `hris_integration_id` when calling `post_workforcemanagement_integrations_hri_timeofftypes_jobs`")


        resource_path = '/api/v2/workforcemanagement/integrations/hris/{hrisIntegrationId}/timeofftypes/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'hris_integration_id' in params:
            path_params['hrisIntegrationId'] = params['hris_integration_id']

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
                                            response_type='HrisTimeOffTypesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_agents_workplans_query(self, management_unit_id: str, **kwargs) -> 'AgentsWorkPlansResponse':
        """
        Get agents work plans configuration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_agents_workplans_query(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :param GetAgentsWorkPlansRequest body: body
        :return: AgentsWorkPlansResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'force_download_service', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_agents_workplans_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_agents_workplans_query`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/workplans/query'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='AgentsWorkPlansResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_agentschedules_search(self, management_unit_id: str, **kwargs) -> 'BuAsyncAgentSchedulesSearchResponse':
        """
        Query published schedules for given given time range for set of users
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_agentschedules_search(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :param BuSearchAgentSchedulesRequest body: body
        :return: BuAsyncAgentSchedulesSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'force_async', 'force_download_service', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_agentschedules_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_agentschedules_search`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/agentschedules/search'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='BuAsyncAgentSchedulesSearchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_historicaladherencequery(self, management_unit_id: str, **kwargs) -> 'WfmHistoricalAdherenceResponse':
        """
        Request a historical adherence report
        The maximum supported range for historical adherence queries is 31 days, or 7 days with includeExceptions = true

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_historicaladherencequery(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param WfmHistoricalAdherenceQuery body: body
        :return: WfmHistoricalAdherenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_historicaladherencequery" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_historicaladherencequery`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/historicaladherencequery'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WfmHistoricalAdherenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_move(self, management_unit_id: str, **kwargs) -> 'MoveManagementUnitResponse':
        """
        Move the requested management unit to a new business unit
        Returns status 200 if the management unit is already in the requested business unit

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_move(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param MoveManagementUnitRequest body: body
        :return: MoveManagementUnitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_move" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_move`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/move'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='MoveManagementUnitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_workforcemanagement_managementunit_schedules_search is deprecated")
    def post_workforcemanagement_managementunit_schedules_search(self, management_unit_id: str, **kwargs) -> 'UserScheduleContainer':
        """
        Query published schedules for given given time range for set of users
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_schedules_search(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param UserListScheduleRequestBody body: body
        :return: UserScheduleContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_schedules_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_schedules_search`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/schedules/search'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='UserScheduleContainer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_shrinkage_jobs(self, management_unit_id: str, **kwargs) -> 'WfmHistoricalShrinkageResponse':
        """
        Request a historical shrinkage report
        The maximum supported range for historical shrinkage queries is up to 32 days. Historical Shrinkage for a given date range can be queried in two modes - granular and aggregated. To see granular shrinkage information, provide granularity in the request body. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_shrinkage_jobs(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param WfmHistoricalShrinkageRequest body: body
        :return: WfmHistoricalShrinkageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_shrinkage_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_shrinkage_jobs`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/shrinkage/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WfmHistoricalShrinkageResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeofflimits(self, management_unit_id: str, **kwargs) -> 'TimeOffLimit':
        """
        Creates a new time off limit object under management unit.
        Only one limit object is allowed under management unit, so an attempt to create second object will fail.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeofflimits(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param CreateTimeOffLimitRequest body: body
        :return: TimeOffLimit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeofflimits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeofflimits`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='TimeOffLimit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeofflimits_values_query(self, management_unit_id: str, **kwargs) -> 'QueryTimeOffLimitValuesResponse':
        """
        Retrieves time off limit related values based on a given set of filters.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeofflimits_values_query(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param QueryTimeOffLimitValuesRequest body: body
        :return: QueryTimeOffLimitValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeofflimits_values_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeofflimits_values_query`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/values/query'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='QueryTimeOffLimitValuesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeoffplans(self, management_unit_id: str, **kwargs) -> 'TimeOffPlan':
        """
        Creates a new time off plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeoffplans(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param CreateTimeOffPlanRequest body: body
        :return: TimeOffPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeoffplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeoffplans`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='TimeOffPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeoffrequests(self, management_unit_id: str, **kwargs) -> 'TimeOffRequestList':
        """
        Create a new time off request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeoffrequests(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param CreateAdminTimeOffRequest body: body
        :return: TimeOffRequestList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeoffrequests" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeoffrequests`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='TimeOffRequestList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query(self, management_unit_id: str, **kwargs) -> 'UserTimeOffIntegrationStatusResponseListing':
        """
        Retrieves integration statuses for a list of time off requests
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param QueryTimeOffIntegrationStatusRequest body: body
        :return: UserTimeOffIntegrationStatusResponseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/integrationstatus/query'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='UserTimeOffIntegrationStatusResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeoffrequests_query(self, management_unit_id: str, **kwargs) -> 'TimeOffRequestListing':
        """
        Fetches time off requests matching the conditions specified in the request body
        Request body requires one of the following: User ID is specified, statuses == [Pending] or date range to be specified and less than or equal to 33 days.  All other fields are filters

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeoffrequests_query(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :param TimeOffRequestQueryBody body: body
        :return: TimeOffRequestListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'force_download_service', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeoffrequests_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeoffrequests_query`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/query'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='TimeOffRequestListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query(self, management_unit_id: str, **kwargs) -> 'WaitlistPositionListing':
        """
        Retrieves daily waitlist position for a list of time off requests
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param QueryWaitlistPositionsRequest body: body
        :return: WaitlistPositionListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/waitlistpositions/query'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WaitlistPositionListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_user_timeoffbalance_jobs(self, management_unit_id: str, user_id: str, body: 'TimeOffBalanceRequest', **kwargs) -> 'TimeOffBalancesResponse':
        """
        Query time off balances for a given user for specified activity code and dates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_user_timeoffbalance_jobs(management_unit_id, user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param str user_id: The ID of the user (required)
        :param TimeOffBalanceRequest body: The request body (required)
        :return: TimeOffBalancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_user_timeoffbalance_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_user_timeoffbalance_jobs`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_workforcemanagement_managementunit_user_timeoffbalance_jobs`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_managementunit_user_timeoffbalance_jobs`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffbalance/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
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
                                            response_type='TimeOffBalancesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs(self, management_unit_id: str, user_id: str, time_off_request_id: str, **kwargs) -> 'TimeOffBalancesResponse':
        """
        Query time off balances for dates spanned by a given time off request
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs(management_unit_id, user_id, time_off_request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str user_id: The userId to whom the time off request applies. (required)
        :param str time_off_request_id: The time off request id. (required)
        :return: TimeOffBalancesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'time_off_request_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs`")
        # verify the required parameter 'time_off_request_id' is set
        if ('time_off_request_id' not in params) or (params['time_off_request_id'] is None):
            raise ValueError("Missing the required parameter `time_off_request_id` when calling `post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}/timeoffbalance/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'time_off_request_id' in params:
            path_params['timeOffRequestId'] = params['time_off_request_id']

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
                                            response_type='TimeOffBalancesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_user_timeoffrequests_estimate(self, management_unit_id: str, user_id: str, **kwargs) -> 'EstimateAvailableTimeOffResponse':
        """
        Estimates available time off for an agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_user_timeoffrequests_estimate(management_unit_id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit (required)
        :param str user_id: The id of the user for whom the time off request estimate is requested (required)
        :param EstimateAvailableTimeOffRequest body: body
        :return: EstimateAvailableTimeOffResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'user_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_user_timeoffrequests_estimate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_user_timeoffrequests_estimate`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_workforcemanagement_managementunit_user_timeoffrequests_estimate`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/estimate'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
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
                                            response_type='EstimateAvailableTimeOffResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_week_shifttrade_match(self, management_unit_id: str, week_date_id: date, trade_id: str, body: 'MatchShiftTradeRequest', **kwargs) -> 'MatchShiftTradeResponse':
        """
        Matches a shift trade. This route can only be called by the receiving agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_week_shifttrade_match(management_unit_id, week_date_id, trade_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param str trade_id: The ID of the shift trade to update (required)
        :param MatchShiftTradeRequest body: body (required)
        :return: MatchShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'trade_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_week_shifttrade_match" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_week_shifttrade_match`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_managementunit_week_shifttrade_match`")
        # verify the required parameter 'trade_id' is set
        if ('trade_id' not in params) or (params['trade_id'] is None):
            raise ValueError("Missing the required parameter `trade_id` when calling `post_workforcemanagement_managementunit_week_shifttrade_match`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_managementunit_week_shifttrade_match`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/{tradeId}/match'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']
        if 'trade_id' in params:
            path_params['tradeId'] = params['trade_id']

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
                                            response_type='MatchShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_week_shifttrades(self, management_unit_id: str, week_date_id: date, body: 'AddShiftTradeRequest', **kwargs) -> 'ShiftTradeResponse':
        """
        Adds a shift trade
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param AddShiftTradeRequest body: body (required)
        :return: ShiftTradeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_week_shifttrades" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_week_shifttrades`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_managementunit_week_shifttrades`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_managementunit_week_shifttrades`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

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
                                            response_type='ShiftTradeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_week_shifttrades_search(self, management_unit_id: str, week_date_id: date, body: 'SearchShiftTradesRequest', **kwargs) -> 'SearchShiftTradesResponse':
        """
        Searches for potential shift trade matches for the current agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_week_shifttrades_search(management_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param SearchShiftTradesRequest body: body (required)
        :param bool force_download_service: Force the result of this operation to be sent via download service. For testing/app development purposes
        :return: SearchShiftTradesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'body', 'force_download_service']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_week_shifttrades_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_week_shifttrades_search`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_managementunit_week_shifttrades_search`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_managementunit_week_shifttrades_search`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/search'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

        query_params = {}
        if 'force_download_service' in params:
            query_params['forceDownloadService'] = params['force_download_service']

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
                                            response_type='SearchShiftTradesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_week_shifttrades_state_bulk(self, management_unit_id: str, week_date_id: date, body: 'BulkShiftTradeStateUpdateRequest', **kwargs) -> 'BulkUpdateShiftTradeStateResponse':
        """
        Updates the state of a batch of shift trades
        Admin functionality is not supported with \"mine\".

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_week_shifttrades_state_bulk(management_unit_id, week_date_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param date week_date_id: The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd (required)
        :param BulkShiftTradeStateUpdateRequest body: body (required)
        :param bool force_async: Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes
        :return: BulkUpdateShiftTradeStateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'week_date_id', 'body', 'force_async']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_week_shifttrades_state_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_week_shifttrades_state_bulk`")
        # verify the required parameter 'week_date_id' is set
        if ('week_date_id' not in params) or (params['week_date_id'] is None):
            raise ValueError("Missing the required parameter `week_date_id` when calling `post_workforcemanagement_managementunit_week_shifttrades_state_bulk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_managementunit_week_shifttrades_state_bulk`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/state/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'week_date_id' in params:
            path_params['weekDateId'] = params['week_date_id']

        query_params = {}
        if 'force_async' in params:
            query_params['forceAsync'] = params['force_async']

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
                                            response_type='BulkUpdateShiftTradeStateResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_workplan_copy(self, management_unit_id: str, work_plan_id: str, **kwargs) -> 'WorkPlan':
        """
        Create a copy of work plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_workplan_copy(management_unit_id, work_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_id: The ID of the work plan to create a copy (required)
        :param CopyWorkPlan body: body
        :return: WorkPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_workplan_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_workplan_copy`")
        # verify the required parameter 'work_plan_id' is set
        if ('work_plan_id' not in params) or (params['work_plan_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_id` when calling `post_workforcemanagement_managementunit_workplan_copy`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_id' in params:
            path_params['workPlanId'] = params['work_plan_id']

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
                                            response_type='WorkPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_workplan_validate(self, management_unit_id: str, work_plan_id: str, **kwargs) -> 'ValidateWorkPlanResponse':
        """
        Validate Work Plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_workplan_validate(management_unit_id, work_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_id: The ID of the work plan to validate. For new work plan, use the word 'new' for the ID. (required)
        :param list[str] expand: 
        :param WorkPlanValidationRequest body: body
        :return: ValidateWorkPlanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_id', 'expand', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_workplan_validate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_workplan_validate`")
        # verify the required parameter 'work_plan_id' is set
        if ('work_plan_id' not in params) or (params['work_plan_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_id` when calling `post_workforcemanagement_managementunit_workplan_validate`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}/validate'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_id' in params:
            path_params['workPlanId'] = params['work_plan_id']

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
                                            response_type='ValidateWorkPlanResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_workplanrotation_copy(self, management_unit_id: str, work_plan_rotation_id: str, **kwargs) -> 'WorkPlanRotationResponse':
        """
        Create a copy of work plan rotation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_workplanrotation_copy(management_unit_id, work_plan_rotation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str work_plan_rotation_id: The ID of the work plan rotation to create a copy (required)
        :param CopyWorkPlanRotationRequest body: body
        :return: WorkPlanRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'work_plan_rotation_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_workplanrotation_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_workplanrotation_copy`")
        # verify the required parameter 'work_plan_rotation_id' is set
        if ('work_plan_rotation_id' not in params) or (params['work_plan_rotation_id'] is None):
            raise ValueError("Missing the required parameter `work_plan_rotation_id` when calling `post_workforcemanagement_managementunit_workplanrotation_copy`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId}/copy'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'work_plan_rotation_id' in params:
            path_params['workPlanRotationId'] = params['work_plan_rotation_id']

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
                                            response_type='WorkPlanRotationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_workplanrotations(self, management_unit_id: str, **kwargs) -> 'WorkPlanRotationResponse':
        """
        Create a new work plan rotation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_workplanrotations(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param AddWorkPlanRotationRequest body: body
        :return: WorkPlanRotationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_workplanrotations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_workplanrotations`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

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
                                            response_type='WorkPlanRotationResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunit_workplans(self, management_unit_id: str, **kwargs) -> 'WorkPlan':
        """
        Create a new work plan
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunit_workplans(management_unit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit, or 'mine' for the management unit of the logged-in user. (required)
        :param str validation_mode: Allows to create work plan even if the validation result is invalid
        :param CreateWorkPlan body: body
        :return: WorkPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'validation_mode', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_managementunit_workplans" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `post_workforcemanagement_managementunit_workplans`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']

        query_params = {}
        if 'validation_mode' in params:
            query_params['validationMode'] = params['validation_mode']

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
                                            response_type='WorkPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_managementunits(self, **kwargs) -> 'ManagementUnit':
        """
        Add a management unit
        It may take a minute or two for a new management unit to be available for api operations

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_managementunits(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateManagementUnitApiRequest body: body
        :return: ManagementUnit
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
                    " to method post_workforcemanagement_managementunits" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/managementunits'.replace('{format}', 'json')
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
                                            response_type='ManagementUnit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_notifications_update(self, **kwargs) -> 'UpdateNotificationsResponse':
        """
        Mark a list of notifications as read or unread
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_notifications_update(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateNotificationsRequest body: body
        :return: UpdateNotificationsResponse
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
                    " to method post_workforcemanagement_notifications_update" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/notifications/update'.replace('{format}', 'json')
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
                                            response_type='UpdateNotificationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_workforcemanagement_schedules is deprecated")
    def post_workforcemanagement_schedules(self, **kwargs) -> 'UserScheduleContainer':
        """
        Get published schedule for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_schedules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CurrentUserScheduleRequestBody body: body
        :return: UserScheduleContainer
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
                    " to method post_workforcemanagement_schedules" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/schedules'.replace('{format}', 'json')
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
                                            response_type='UserScheduleContainer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_team_adherence_historical(self, team_id: str, **kwargs) -> 'WfmHistoricalAdherenceResponse':
        """
        Request a teams historical adherence report
        The maximum supported range for historical adherence queries is 31 days, or 7 days with includeExceptions = true

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_team_adherence_historical(team_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str team_id: The ID of the team (required)
        :param WfmHistoricalAdherenceQueryForTeams body: body
        :return: WfmHistoricalAdherenceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_team_adherence_historical" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'team_id' is set
        if ('team_id' not in params) or (params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `post_workforcemanagement_team_adherence_historical`")


        resource_path = '/api/v2/workforcemanagement/teams/{teamId}/adherence/historical'.replace('{format}', 'json')
        path_params = {}
        if 'team_id' in params:
            path_params['teamId'] = params['team_id']

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
                                            response_type='WfmHistoricalAdherenceResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_team_shrinkage_jobs(self, team_id: str, **kwargs) -> 'WfmHistoricalShrinkageResponse':
        """
        Request a historical shrinkage report
        The maximum supported range for historical shrinkage queries is up to 32 days

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_team_shrinkage_jobs(team_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str team_id: The ID of the team (required)
        :param WfmHistoricalShrinkageTeamsRequest body: body
        :return: WfmHistoricalShrinkageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workforcemanagement_team_shrinkage_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'team_id' is set
        if ('team_id' not in params) or (params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `post_workforcemanagement_team_shrinkage_jobs`")


        resource_path = '/api/v2/workforcemanagement/teams/{teamId}/shrinkage/jobs'.replace('{format}', 'json')
        path_params = {}
        if 'team_id' in params:
            path_params['teamId'] = params['team_id']

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
                                            response_type='WfmHistoricalShrinkageResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_timeoffbalance_jobs(self, body: 'TimeOffBalanceRequest', **kwargs) -> 'TimeOffBalancesResponse':
        """
        Query time off balances for the current user for specified activity code and dates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_timeoffbalance_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TimeOffBalanceRequest body: The request body (required)
        :return: TimeOffBalancesResponse
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
                    " to method post_workforcemanagement_timeoffbalance_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_workforcemanagement_timeoffbalance_jobs`")


        resource_path = '/api/v2/workforcemanagement/timeoffbalance/jobs'.replace('{format}', 'json')
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
                                            response_type='TimeOffBalancesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_timeofflimits_available_query(self, **kwargs) -> 'AvailableTimeOffResponse':
        """
        Queries available time off for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_timeofflimits_available_query(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AvailableTimeOffRequest body: body
        :return: AvailableTimeOffResponse
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
                    " to method post_workforcemanagement_timeofflimits_available_query" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/timeofflimits/available/query'.replace('{format}', 'json')
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
                                            response_type='AvailableTimeOffResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_timeoffrequests(self, **kwargs) -> 'TimeOffRequestResponse':
        """
        Create a time off request for the current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_timeoffrequests(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAgentTimeOffRequest body: body
        :return: TimeOffRequestResponse
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
                    " to method post_workforcemanagement_timeoffrequests" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/timeoffrequests'.replace('{format}', 'json')
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
                                            response_type='TimeOffRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_timeoffrequests_estimate(self, **kwargs) -> 'EstimateAvailableTimeOffResponse':
        """
        Estimates available time off for current user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_timeoffrequests_estimate(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EstimateAvailableTimeOffRequest body: body
        :return: EstimateAvailableTimeOffResponse
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
                    " to method post_workforcemanagement_timeoffrequests_estimate" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/timeoffrequests/estimate'.replace('{format}', 'json')
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
                                            response_type='EstimateAvailableTimeOffResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_workforcemanagement_timeoffrequests_integrationstatus_query(self, **kwargs) -> 'TimeOffIntegrationStatusResponseListing':
        """
        Retrieves integration statuses for a list of current user time off requests
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workforcemanagement_timeoffrequests_integrationstatus_query(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CurrentUserTimeOffIntegrationStatusRequest body: body
        :return: TimeOffIntegrationStatusResponseListing
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
                    " to method post_workforcemanagement_timeoffrequests_integrationstatus_query" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/workforcemanagement/timeoffrequests/integrationstatus/query'.replace('{format}', 'json')
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
                                            response_type='TimeOffIntegrationStatusResponseListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_workforcemanagement_agent_integrations_hris(self, agent_id: str, body: 'AgentIntegrationsRequest', **kwargs) -> 'AgentIntegrationsResponse':
        """
        Update integrations for agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_workforcemanagement_agent_integrations_hris(agent_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str agent_id: The ID of the agent (required)
        :param AgentIntegrationsRequest body: body (required)
        :return: AgentIntegrationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workforcemanagement_agent_integrations_hris" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `put_workforcemanagement_agent_integrations_hris`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_workforcemanagement_agent_integrations_hris`")


        resource_path = '/api/v2/workforcemanagement/agents/{agentId}/integrations/hris'.replace('{format}', 'json')
        path_params = {}
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='AgentIntegrationsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_workforcemanagement_businessunit_timeofflimit_values(self, business_unit_id: str, time_off_limit_id: str, **kwargs) -> 'BuTimeOffLimitResponse':
        """
        Sets daily values for a date range of time-off limit object
        Note that only limit daily values can be set through API, allocated and waitlisted values are read-only for time-off limit API

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_workforcemanagement_businessunit_timeofflimit_values(business_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_unit_id: The ID of the business unit (required)
        :param str time_off_limit_id: The ID of the time-off limit object to set values for (required)
        :param BuSetTimeOffLimitValuesRequest body: body
        :return: BuTimeOffLimitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'time_off_limit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workforcemanagement_businessunit_timeofflimit_values" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params) or (params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `put_workforcemanagement_businessunit_timeofflimit_values`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `put_workforcemanagement_businessunit_timeofflimit_values`")


        resource_path = '/api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId}/values'.replace('{format}', 'json')
        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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
                                            response_type='BuTimeOffLimitResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_workforcemanagement_managementunit_timeofflimit_values(self, management_unit_id: str, time_off_limit_id: str, **kwargs) -> 'TimeOffLimit':
        """
        Sets daily values for a date range of time off limit object
        Note that only limit daily values can be set through API, allocated and waitlisted values are read-only for time off limit API

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_workforcemanagement_managementunit_timeofflimit_values(management_unit_id, time_off_limit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str management_unit_id: The ID of the management unit. (required)
        :param str time_off_limit_id: The ID of the time off limit object to set values for (required)
        :param SetTimeOffLimitValuesRequest body: body
        :return: TimeOffLimit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['management_unit_id', 'time_off_limit_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workforcemanagement_managementunit_timeofflimit_values" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'management_unit_id' is set
        if ('management_unit_id' not in params) or (params['management_unit_id'] is None):
            raise ValueError("Missing the required parameter `management_unit_id` when calling `put_workforcemanagement_managementunit_timeofflimit_values`")
        # verify the required parameter 'time_off_limit_id' is set
        if ('time_off_limit_id' not in params) or (params['time_off_limit_id'] is None):
            raise ValueError("Missing the required parameter `time_off_limit_id` when calling `put_workforcemanagement_managementunit_timeofflimit_values`")


        resource_path = '/api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId}/values'.replace('{format}', 'json')
        path_params = {}
        if 'management_unit_id' in params:
            path_params['managementUnitId'] = params['management_unit_id']
        if 'time_off_limit_id' in params:
            path_params['timeOffLimitId'] = params['time_off_limit_id']

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
                                            response_type='TimeOffLimit',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
