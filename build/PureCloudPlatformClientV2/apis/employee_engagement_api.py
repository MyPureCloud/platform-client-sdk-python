# coding: utf-8

"""
EmployeeEngagementApi.py
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
from ..models import CelebrationStateParam
from ..models import CreateRecognition
from ..models import ErrorBody
from ..models import GetCelebrationListing
from ..models import Recognition
from ..models import RecognitionBase

class EmployeeEngagementApi(object):
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

    def delete_employeeengagement_celebration(self, celebration_id: str, **kwargs) -> None:
        """
        Deletes a celebration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_employeeengagement_celebration(celebration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str celebration_id: The ID of the celebration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['celebration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_employeeengagement_celebration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'celebration_id' is set
        if ('celebration_id' not in params) or (params['celebration_id'] is None):
            raise ValueError("Missing the required parameter `celebration_id` when calling `delete_employeeengagement_celebration`")


        resource_path = '/api/v2/employeeengagement/celebrations/{celebrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'celebration_id' in params:
            path_params['celebrationId'] = params['celebration_id']

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

    def get_employeeengagement_celebrations(self, **kwargs) -> 'GetCelebrationListing':
        """
        Get all celebrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_employeeengagement_celebrations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: 
        :param int page_size: 
        :return: GetCelebrationListing
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
                    " to method get_employeeengagement_celebrations" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/employeeengagement/celebrations'.replace('{format}', 'json')
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
                                            response_type='GetCelebrationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_employeeengagement_recognition(self, recognition_id: str, **kwargs) -> 'Recognition':
        """
        Gets a single recognition
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_employeeengagement_recognition(recognition_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recognition_id: The Recognition ID (required)
        :return: Recognition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recognition_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_employeeengagement_recognition" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'recognition_id' is set
        if ('recognition_id' not in params) or (params['recognition_id'] is None):
            raise ValueError("Missing the required parameter `recognition_id` when calling `get_employeeengagement_recognition`")


        resource_path = '/api/v2/employeeengagement/recognitions/{recognitionId}'.replace('{format}', 'json')
        path_params = {}
        if 'recognition_id' in params:
            path_params['recognitionId'] = params['recognition_id']

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
                                            response_type='Recognition',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_employeeengagement_celebration(self, celebration_id: str, body: 'CelebrationStateParam', **kwargs) -> None:
        """
        Set a state for a celebration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_employeeengagement_celebration(celebration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str celebration_id: The ID of the celebration (required)
        :param CelebrationStateParam body: Patch Celebration state (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['celebration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_employeeengagement_celebration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'celebration_id' is set
        if ('celebration_id' not in params) or (params['celebration_id'] is None):
            raise ValueError("Missing the required parameter `celebration_id` when calling `patch_employeeengagement_celebration`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_employeeengagement_celebration`")


        resource_path = '/api/v2/employeeengagement/celebrations/{celebrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'celebration_id' in params:
            path_params['celebrationId'] = params['celebration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_employeeengagement_recognitions(self, body: 'CreateRecognition', **kwargs) -> 'RecognitionBase':
        """
        Creates a recognition
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_employeeengagement_recognitions(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecognition body: Create Recognition (required)
        :return: RecognitionBase
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
                    " to method post_employeeengagement_recognitions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_employeeengagement_recognitions`")


        resource_path = '/api/v2/employeeengagement/recognitions'.replace('{format}', 'json')
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
                                            response_type='RecognitionBase',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response