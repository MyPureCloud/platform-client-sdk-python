# coding: utf-8

"""
WidgetsApi.py
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
from ..models import ErrorBody
from ..models import WidgetDeployment
from ..models import WidgetDeploymentEntityListing

class WidgetsApi(object):
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

    @deprecated("delete_widgets_deployment is deprecated")
    def delete_widgets_deployment(self, deployment_id: str, **kwargs) -> None:
        """
        Delete a Widget deployment
        This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_widgets_deployment(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Widget Config Id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_widgets_deployment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `delete_widgets_deployment`")


        resource_path = '/api/v2/widgets/deployments/{deploymentId}'.replace('{format}', 'json')
        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

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

    @deprecated("get_widgets_deployment is deprecated")
    def get_widgets_deployment(self, deployment_id: str, **kwargs) -> 'WidgetDeployment':
        """
        Get a Widget deployment
        This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_widgets_deployment(deployment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Widget Config Id (required)
        :return: WidgetDeployment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widgets_deployment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `get_widgets_deployment`")


        resource_path = '/api/v2/widgets/deployments/{deploymentId}'.replace('{format}', 'json')
        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

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
                                            response_type='WidgetDeployment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("get_widgets_deployments is deprecated")
    def get_widgets_deployments(self, **kwargs) -> 'WidgetDeploymentEntityListing':
        """
        List Widget deployments
        This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_widgets_deployments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: WidgetDeploymentEntityListing
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
                    " to method get_widgets_deployments" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/widgets/deployments'.replace('{format}', 'json')
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
                                            response_type='WidgetDeploymentEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("post_widgets_deployments is deprecated")
    def post_widgets_deployments(self, body: 'WidgetDeployment', **kwargs) -> 'WidgetDeployment':
        """
        Create Widget deployment
        This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_widgets_deployments(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WidgetDeployment body: Deployment (required)
        :return: WidgetDeployment
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
                    " to method post_widgets_deployments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_widgets_deployments`")


        resource_path = '/api/v2/widgets/deployments'.replace('{format}', 'json')
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
                                            response_type='WidgetDeployment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    @deprecated("put_widgets_deployment is deprecated")
    def put_widgets_deployment(self, deployment_id: str, body: 'WidgetDeployment', **kwargs) -> 'WidgetDeployment':
        """
        Update a Widget deployment
        This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-removal-of-acd-web-chat-version-2/. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_widgets_deployment(deployment_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str deployment_id: Widget Config Id (required)
        :param WidgetDeployment body: Deployment (required)
        :return: WidgetDeployment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['deployment_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_widgets_deployment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'deployment_id' is set
        if ('deployment_id' not in params) or (params['deployment_id'] is None):
            raise ValueError("Missing the required parameter `deployment_id` when calling `put_widgets_deployment`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_widgets_deployment`")


        resource_path = '/api/v2/widgets/deployments/{deploymentId}'.replace('{format}', 'json')
        path_params = {}
        if 'deployment_id' in params:
            path_params['deploymentId'] = params['deployment_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='WidgetDeployment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
