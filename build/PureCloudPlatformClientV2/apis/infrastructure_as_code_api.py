# coding: utf-8

"""
InfrastructureAsCodeApi.py
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

from typing import List
from typing import Dict
from typing import Any

from ..models import Empty
from ..models import AcceleratorInput
from ..models import ErrorBody
from ..models import InfrastructureascodeJob

class InfrastructureAsCodeApi(object):
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

    def get_infrastructureascode_job(self, job_id: str, **kwargs) -> 'InfrastructureascodeJob':
        """
        Get job status and results
        Get the execution status of a submitted job, optionally including results and error details.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_infrastructureascode_job(job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str job_id: Job ID (required)
        :param bool details: Include details of execution, including job results or error information
        :return: InfrastructureascodeJob
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'details']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_infrastructureascode_job" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_infrastructureascode_job`")


        resource_path = '/api/v2/infrastructureascode/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}
        if 'details' in params:
            query_params['details'] = params['details']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InfrastructureascodeJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_infrastructureascode_jobs(self, **kwargs) -> 'InfrastructureascodeJob':
        """
        Get job history
        Get a history of submitted jobs, optionally including error messages.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_infrastructureascode_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int max_results: Number of jobs to show
        :param bool include_errors: Include error messages
        :param str sort_by: Sort by
        :param str sort_order: Sort order
        :return: InfrastructureascodeJob
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['max_results', 'include_errors', 'sort_by', 'sort_order']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_infrastructureascode_jobs" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/infrastructureascode/jobs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'max_results' in params:
            query_params['maxResults'] = params['max_results']
        if 'include_errors' in params:
            query_params['includeErrors'] = params['include_errors']
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
                                            response_type='InfrastructureascodeJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_infrastructureascode_jobs(self, body: 'AcceleratorInput', **kwargs) -> 'InfrastructureascodeJob':
        """
        Create a Job
        Create and submit a job for remote execution or see job planning results.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_infrastructureascode_jobs(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AcceleratorInput body:  (required)
        :return: InfrastructureascodeJob
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
                    " to method post_infrastructureascode_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_infrastructureascode_jobs`")


        resource_path = '/api/v2/infrastructureascode/jobs'.replace('{format}', 'json')
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
                                            response_type='InfrastructureascodeJob',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response