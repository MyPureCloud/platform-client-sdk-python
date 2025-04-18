# coding: utf-8

"""
GeolocationApi.py
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
from ..models import Geolocation
from ..models import GeolocationSettings

class GeolocationApi(object):
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

    def get_geolocations_settings(self, **kwargs) -> 'GeolocationSettings':
        """
        Get a organization's GeolocationSettings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_geolocations_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: GeolocationSettings
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
                    " to method get_geolocations_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/geolocations/settings'.replace('{format}', 'json')
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
                                            response_type='GeolocationSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_user_geolocation(self, user_id: str, client_id: str, **kwargs) -> 'Geolocation':
        """
        Get a user's Geolocation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_geolocation(user_id, client_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: user Id (required)
        :param str client_id: client Id (required)
        :return: Geolocation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'client_id']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_geolocation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_geolocation`")
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `get_user_geolocation`")


        resource_path = '/api/v2/users/{userId}/geolocations/{clientId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

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
                                            response_type='Geolocation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_geolocations_settings(self, body: 'GeolocationSettings', **kwargs) -> 'GeolocationSettings':
        """
        Patch a organization's GeolocationSettings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_geolocations_settings(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param GeolocationSettings body: Geolocation settings (required)
        :return: GeolocationSettings
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
                    " to method patch_geolocations_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_geolocations_settings`")


        resource_path = '/api/v2/geolocations/settings'.replace('{format}', 'json')
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
                                            response_type='GeolocationSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_user_geolocation(self, user_id: str, client_id: str, body: 'Geolocation', **kwargs) -> 'Geolocation':
        """
        Patch a user's Geolocation
        The geolocation object can be patched one of three ways. Option 1: Set the 'primary' property to true. This will set the client as the user's primary geolocation source.  Option 2: Provide the 'latitude' and 'longitude' values.  This will enqueue an asynchronous update of the 'city', 'region', and 'country', generating a notification. A subsequent GET operation will include the new values for 'city', 'region' and 'country'.  Option 3:  Provide the 'city', 'region', 'country' values.  Option 1 can be combined with Option 2 or Option 3.  For example, update the client as primary and provide latitude and longitude values.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_user_geolocation(user_id, client_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: user Id (required)
        :param str client_id: client Id (required)
        :param Geolocation body: Geolocation (required)
        :return: Geolocation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'client_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_geolocation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `patch_user_geolocation`")
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `patch_user_geolocation`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_user_geolocation`")


        resource_path = '/api/v2/users/{userId}/geolocations/{clientId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='Geolocation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
