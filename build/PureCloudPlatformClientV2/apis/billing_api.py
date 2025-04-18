# coding: utf-8

"""
BillingApi.py
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
from ..models import BillingUsageReport
from ..models import ErrorBody
from ..models import TrusteeBillingOverview

class BillingApi(object):
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

    def get_billing_reports_billableusage(self, start_date: datetime, end_date: datetime, **kwargs) -> 'BillingUsageReport':
        """
        Get a report of the billable license usages
        Report is of the billable usages (e.g. licenses and devices utilized) for a given period. If response's status is InProgress, wait a few seconds, then try the same request again.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_billing_reports_billableusage(start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_date: The period start date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (required)
        :param datetime end_date: The period end date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z (required)
        :return: BillingUsageReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_reports_billableusage" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_billing_reports_billableusage`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_billing_reports_billableusage`")


        resource_path = '/api/v2/billing/reports/billableusage'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'start_date' in params:
            query_params['startDate'] = params['start_date']
        if 'end_date' in params:
            query_params['endDate'] = params['end_date']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BillingUsageReport',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_billing_trusteebillingoverview_trustor_org_id(self, trustor_org_id: str, **kwargs) -> 'TrusteeBillingOverview':
        """
        Get the billing overview for an organization that is managed by a partner.
        Tax Disclaimer: Prices returned by this API do not include applicable taxes. It is the responsibility of the customer to pay all taxes that are appropriate in their jurisdiction. See the PureCloud API Documentation in the Developer Center for more information about this API: https://developer.mypurecloud.com/api/rest/v2/

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_billing_trusteebillingoverview_trustor_org_id(trustor_org_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str trustor_org_id: The organization ID of the trustor (customer) organization. (required)
        :param int billing_period_index: 0 for active period (overview data may change until period closes). 1 for prior completed billing period. 2 for two billing cycles prior, and so on.
        :return: TrusteeBillingOverview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trustor_org_id', 'billing_period_index']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_trusteebillingoverview_trustor_org_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'trustor_org_id' is set
        if ('trustor_org_id' not in params) or (params['trustor_org_id'] is None):
            raise ValueError("Missing the required parameter `trustor_org_id` when calling `get_billing_trusteebillingoverview_trustor_org_id`")


        resource_path = '/api/v2/billing/trusteebillingoverview/{trustorOrgId}'.replace('{format}', 'json')
        path_params = {}
        if 'trustor_org_id' in params:
            path_params['trustorOrgId'] = params['trustor_org_id']

        query_params = {}
        if 'billing_period_index' in params:
            query_params['billingPeriodIndex'] = params['billing_period_index']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TrusteeBillingOverview',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
