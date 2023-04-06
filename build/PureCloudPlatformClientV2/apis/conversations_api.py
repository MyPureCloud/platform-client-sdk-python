# coding: utf-8

"""
ConversationsApi.py
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
from ..models import AdditionalMessage
from ..models import AfterCallWorkUpdate
from ..models import AgentlessEmailSendRequestDto
from ..models import AgentlessEmailSendResponseDto
from ..models import AnalyticsConversationAsyncQueryResponse
from ..models import AnalyticsConversationQueryResponse
from ..models import AnalyticsConversationWithoutAttributes
from ..models import AnalyticsConversationWithoutAttributesMultiGetResponse
from ..models import AssignedWrapupCode
from ..models import AsyncConversationQuery
from ..models import AsyncQueryResponse
from ..models import AsyncQueryStatus
from ..models import BulkCallbackDisconnectRequest
from ..models import BulkCallbackPatchRequest
from ..models import BulkCallbackPatchResponse
from ..models import CallCommand
from ..models import CallConversation
from ..models import CallConversationEntityListing
from ..models import CallHistoryConversationEntityListing
from ..models import CallbackConversation
from ..models import CallbackConversationEntityListing
from ..models import ChatConversation
from ..models import ChatConversationEntityListing
from ..models import CobrowseConversation
from ..models import CobrowseConversationEntityListing
from ..models import CobrowseWebMessagingSession
from ..models import ConsultTransfer
from ..models import ConsultTransferResponse
from ..models import ConsultTransferUpdate
from ..models import Conversation
from ..models import ConversationAggregateQueryResponse
from ..models import ConversationAggregationQuery
from ..models import ConversationEncryptionConfiguration
from ..models import ConversationEncryptionConfigurationListing
from ..models import ConversationEntityListing
from ..models import ConversationParticipantSearchRequest
from ..models import ConversationQuery
from ..models import ConversationSecureAttributes
from ..models import ConversationTagsUpdate
from ..models import ConversationThreadingWindow
from ..models import ConversationUser
from ..models import CopyAttachmentsRequest
from ..models import CreateCallRequest
from ..models import CreateCallResponse
from ..models import CreateCallbackCommand
from ..models import CreateCallbackOnConversationCommand
from ..models import CreateCallbackResponse
from ..models import CreateEmailRequest
from ..models import CreateOutboundMessagingConversationRequest
from ..models import CreateSecureSession
from ..models import CreateWebChatMessageRequest
from ..models import CreateWebChatRequest
from ..models import DataAvailabilityResponse
from ..models import Digits
from ..models import EmailConversation
from ..models import EmailConversationEntityListing
from ..models import EmailMessage
from ..models import EmailMessageListing
from ..models import EmailMessageReply
from ..models import EmailsSettings
from ..models import ErrorBody
from ..models import FacebookAppCredentials
from ..models import FacebookIntegration
from ..models import FacebookIntegrationEntityListing
from ..models import FacebookIntegrationRequest
from ..models import FacebookIntegrationUpdateRequest
from ..models import FaxSendRequest
from ..models import FaxSendResponse
from ..models import InboundMessageRequest
from ..models import JsonCursorSearchResponse
from ..models import LineIntegration
from ..models import LineIntegrationEntityListing
from ..models import LineIntegrationRequest
from ..models import MaxParticipants
from ..models import MediaParticipantRequest
from ..models import MessageConversation
from ..models import MessageConversationEntityListing
from ..models import MessageData
from ..models import MessageMediaData
from ..models import MessageTypingEventRequest
from ..models import MessagingIntegrationEntityListing
from ..models import MessagingStickerEntityListing
from ..models import OpenIntegration
from ..models import OpenIntegrationEntityListing
from ..models import OpenIntegrationRequest
from ..models import OpenIntegrationUpdateRequest
from ..models import OpenNormalizedMessage
from ..models import ParticipantAttributes
from ..models import PatchCallbackRequest
from ..models import PatchCallbackResponse
from ..models import PropertyIndexRequest
from ..models import SecureSession
from ..models import SecureSessionEntityListing
from ..models import SendAgentlessOutboundMessageRequest
from ..models import SendAgentlessOutboundMessageResponse
from ..models import SetRecordingState
from ..models import SetUuiDataRequest
from ..models import Settings
from ..models import SupportedContent
from ..models import SupportedContentListing
from ..models import SupportedContentReference
from ..models import TextMessageListing
from ..models import TransferRequest
from ..models import TwitterIntegration
from ..models import TwitterIntegrationEntityListing
from ..models import TwitterIntegrationRequest
from ..models import WebChatMessage
from ..models import WebChatMessageEntityList
from ..models import WebChatTyping
from ..models import WhatsAppIntegration
from ..models import WhatsAppIntegrationEntityListing
from ..models import WhatsAppIntegrationRequest
from ..models import WhatsAppIntegrationUpdateRequest
from ..models import WrapupCode
from ..models import WrapupInput

class ConversationsApi(object):
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

    def delete_conversation_participant_code(self, conversation_id: str, participant_id: str, add_communication_code: str, **kwargs) -> None:
        """
        Delete a code used to add a communication to this participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversation_participant_code(conversation_id, participant_id, add_communication_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param str add_communication_code: addCommunicationCode (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'add_communication_code']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversation_participant_code" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `delete_conversation_participant_code`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `delete_conversation_participant_code`")
        # verify the required parameter 'add_communication_code' is set
        if ('add_communication_code' not in params) or (params['add_communication_code'] is None):
            raise ValueError("Missing the required parameter `add_communication_code` when calling `delete_conversation_participant_code`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/codes/{addCommunicationCode}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'add_communication_code' in params:
            path_params['addCommunicationCode'] = params['add_communication_code']

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

    def delete_conversation_participant_flaggedreason(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Remove flagged reason from conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversation_participant_flaggedreason(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversation_participant_flaggedreason" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `delete_conversation_participant_flaggedreason`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `delete_conversation_participant_flaggedreason`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/flaggedreason'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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

    def delete_conversations_call_participant_consult(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Cancel the transfer
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_call_participant_consult(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_call_participant_consult" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `delete_conversations_call_participant_consult`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `delete_conversations_call_participant_consult`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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

    def delete_conversations_email_messages_draft_attachment(self, conversation_id: str, attachment_id: str, **kwargs) -> None:
        """
        Delete attachment from draft
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_email_messages_draft_attachment(conversation_id, attachment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str attachment_id: attachmentId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'attachment_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_email_messages_draft_attachment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `delete_conversations_email_messages_draft_attachment`")
        # verify the required parameter 'attachment_id' is set
        if ('attachment_id' not in params) or (params['attachment_id'] is None):
            raise ValueError("Missing the required parameter `attachment_id` when calling `delete_conversations_email_messages_draft_attachment`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages/draft/attachments/{attachmentId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'attachment_id' in params:
            path_params['attachmentId'] = params['attachment_id']

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

    def delete_conversations_messaging_integrations_facebook_integration_id(self, integration_id: str, **kwargs) -> None:
        """
        Delete a Facebook messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_integrations_facebook_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_integrations_facebook_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_conversations_messaging_integrations_facebook_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/facebook/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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

    def delete_conversations_messaging_integrations_line_integration_id(self, integration_id: str, **kwargs) -> None:
        """
        Delete a LINE messenger integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_integrations_line_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_integrations_line_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_conversations_messaging_integrations_line_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/line/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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

    def delete_conversations_messaging_integrations_open_integration_id(self, integration_id: str, **kwargs) -> None:
        """
        Delete an Open messaging integration
        See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_integrations_open_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_integrations_open_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_conversations_messaging_integrations_open_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/open/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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

    def delete_conversations_messaging_integrations_twitter_integration_id(self, integration_id: str, **kwargs) -> None:
        """
        Delete a Twitter messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_integrations_twitter_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_integrations_twitter_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_conversations_messaging_integrations_twitter_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/twitter/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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

    def delete_conversations_messaging_integrations_whatsapp_integration_id(self, integration_id: str, **kwargs) -> 'WhatsAppIntegration':
        """
        Delete a WhatsApp messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_integrations_whatsapp_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :return: WhatsAppIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_integrations_whatsapp_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_conversations_messaging_integrations_whatsapp_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/whatsapp/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='WhatsAppIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_conversations_messaging_supportedcontent_supported_content_id(self, supported_content_id: str, **kwargs) -> None:
        """
        Delete a supported content profile
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_conversations_messaging_supportedcontent_supported_content_id(supported_content_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supported_content_id: Supported Content ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supported_content_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_conversations_messaging_supportedcontent_supported_content_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'supported_content_id' is set
        if ('supported_content_id' not in params) or (params['supported_content_id'] is None):
            raise ValueError("Missing the required parameter `supported_content_id` when calling `delete_conversations_messaging_supportedcontent_supported_content_id`")


        resource_path = '/api/v2/conversations/messaging/supportedcontent/{supportedContentId}'.replace('{format}', 'json')
        path_params = {}
        if 'supported_content_id' in params:
            path_params['supportedContentId'] = params['supported_content_id']

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

    def get_conversation(self, conversation_id: str, **kwargs) -> 'Conversation':
        """
        Get conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :return: Conversation
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
                    " to method get_conversation" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation`")


        resource_path = '/api/v2/conversations/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversation_participant_secureivrsession(self, conversation_id: str, participant_id: str, secure_session_id: str, **kwargs) -> 'SecureSession':
        """
        Fetch info on a secure session
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_participant_secureivrsession(conversation_id, participant_id, secure_session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param str secure_session_id: secure IVR session ID (required)
        :return: SecureSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'secure_session_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversation_participant_secureivrsession" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_participant_secureivrsession`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversation_participant_secureivrsession`")
        # verify the required parameter 'secure_session_id' is set
        if ('secure_session_id' not in params) or (params['secure_session_id'] is None):
            raise ValueError("Missing the required parameter `secure_session_id` when calling `get_conversation_participant_secureivrsession`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions/{secureSessionId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'secure_session_id' in params:
            path_params['secureSessionId'] = params['secure_session_id']

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
                                            response_type='SecureSession',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversation_participant_secureivrsessions(self, conversation_id: str, participant_id: str, **kwargs) -> 'SecureSessionEntityListing':
        """
        Get a list of secure sessions for this participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_participant_secureivrsessions(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :return: SecureSessionEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversation_participant_secureivrsessions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_participant_secureivrsessions`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversation_participant_secureivrsessions`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='SecureSessionEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversation_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversation_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversation_participant_wrapup`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversation_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversation_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversation_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversation_secureattributes(self, conversation_id: str, **kwargs) -> 'ConversationSecureAttributes':
        """
        Get the secure attributes on a conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversation_secureattributes(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :return: ConversationSecureAttributes
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
                    " to method get_conversation_secureattributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversation_secureattributes`")


        resource_path = '/api/v2/conversations/{conversationId}/secureattributes'.replace('{format}', 'json')
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
                                            response_type='ConversationSecureAttributes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations(self, **kwargs) -> 'ConversationEntityListing':
        """
        Get active conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str communication_type: Call or Chat communication filtering
        :return: ConversationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['communication_type']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'communication_type' in params:
            query_params['communicationType'] = params['communication_type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_call(self, conversation_id: str, **kwargs) -> 'CallConversation':
        """
        Get call conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_call(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: CallConversation
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
                    " to method get_conversations_call" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_call`")


        resource_path = '/api/v2/conversations/calls/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='CallConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_call_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_call_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_call_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_call_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_call_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_call_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_call_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_call_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_call_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_call_participant_wrapup`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_call_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_call_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_call_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_call_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_call_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_callback(self, conversation_id: str, **kwargs) -> 'CallbackConversation':
        """
        Get callback conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_callback(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: CallbackConversation
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
                    " to method get_conversations_callback" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_callback`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='CallbackConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_callback_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_callback_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_callback_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_callback_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_callback_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_callback_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_callback_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_callback_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_callback_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_callback_participant_wrapup`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_callback_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_callback_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_callback_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_callback_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_callback_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_callbacks(self, **kwargs) -> 'CallbackConversationEntityListing':
        """
        Get active callback conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_callbacks(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CallbackConversationEntityListing
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
                    " to method get_conversations_callbacks" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/callbacks'.replace('{format}', 'json')
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
                                            response_type='CallbackConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_calls(self, **kwargs) -> 'CallConversationEntityListing':
        """
        Get active call conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_calls(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CallConversationEntityListing
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
                    " to method get_conversations_calls" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/calls'.replace('{format}', 'json')
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
                                            response_type='CallConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_calls_history(self, **kwargs) -> 'CallHistoryConversationEntityListing':
        """
        Get call history
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_calls_history(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size, maximum 50
        :param int page_number: Page number
        :param str interval: Interval string; format is ISO-8601. Separate start and end times with forward slash '/'
        :param list[str] expand: Which fields, if any, to expand.
        :return: CallHistoryConversationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'interval', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_calls_history" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/calls/history'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'interval' in params:
            query_params['interval'] = params['interval']
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
                                            response_type='CallHistoryConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_calls_maximumconferenceparties(self, **kwargs) -> 'MaxParticipants':
        """
        Get the maximum number of participants that this user can have on a conference
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_calls_maximumconferenceparties(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MaxParticipants
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
                    " to method get_conversations_calls_maximumconferenceparties" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/calls/maximumconferenceparties'.replace('{format}', 'json')
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
                                            response_type='MaxParticipants',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat(self, conversation_id: str, **kwargs) -> 'ChatConversation':
        """
        Get chat conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: ChatConversation
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
                    " to method get_conversations_chat" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat`")


        resource_path = '/api/v2/conversations/chats/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='ChatConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat_message(self, conversation_id: str, message_id: str, **kwargs) -> 'WebChatMessage':
        """
        Get a web chat conversation message
        The current user must be involved with the conversation to get its messages.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat_message(conversation_id, message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str message_id: messageId (required)
        :return: WebChatMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'message_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_chat_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat_message`")
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_conversations_chat_message`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/messages/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

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
                                            response_type='WebChatMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat_messages(self, conversation_id: str, **kwargs) -> 'WebChatMessageEntityList':
        """
        Get the messages of a chat conversation.
        The current user must be involved with the conversation to get its messages.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat_messages(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str after: If specified, get the messages chronologically after the id of this message
        :param str before: If specified, get the messages chronologically before the id of this message
        :param str sort_order: Sort order
        :param int max_results: Limit the returned number of messages, up to a maximum of 100
        :return: WebChatMessageEntityList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'after', 'before', 'sort_order', 'max_results']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_chat_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat_messages`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/messages'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']

        query_params = {}
        if 'after' in params:
            query_params['after'] = params['after']
        if 'before' in params:
            query_params['before'] = params['before']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'max_results' in params:
            query_params['maxResults'] = params['max_results']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='WebChatMessageEntityList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_chat_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_chat_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_chat_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_chat_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_chat_participant_wrapup`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chat_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chat_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_chat_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_chat_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_chat_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_chats(self, **kwargs) -> 'ChatConversationEntityListing':
        """
        Get active chat conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_chats(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ChatConversationEntityListing
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
                    " to method get_conversations_chats" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/chats'.replace('{format}', 'json')
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
                                            response_type='ChatConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_cobrowsesession(self, conversation_id: str, **kwargs) -> 'CobrowseConversation':
        """
        Get cobrowse conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_cobrowsesession(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: CobrowseConversation
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
                    " to method get_conversations_cobrowsesession" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_cobrowsesession`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='CobrowseConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_cobrowsesession_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_cobrowsesession_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_cobrowsesession_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_cobrowsesession_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_cobrowsesession_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_cobrowsesession_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_cobrowsesession_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_cobrowsesession_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_cobrowsesession_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_cobrowsesession_participant_wrapup`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_cobrowsesession_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_cobrowsesession_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_cobrowsesession_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_cobrowsesession_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_cobrowsesession_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_cobrowsesessions(self, **kwargs) -> 'CobrowseConversationEntityListing':
        """
        Get active cobrowse conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_cobrowsesessions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CobrowseConversationEntityListing
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
                    " to method get_conversations_cobrowsesessions" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/cobrowsesessions'.replace('{format}', 'json')
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
                                            response_type='CobrowseConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email(self, conversation_id: str, **kwargs) -> 'EmailConversation':
        """
        Get email conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: EmailConversation
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
                    " to method get_conversations_email" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email`")


        resource_path = '/api/v2/conversations/emails/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='EmailConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_message(self, conversation_id: str, message_id: str, **kwargs) -> 'EmailMessage':
        """
        Get conversation message
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_message(conversation_id, message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str message_id: messageId (required)
        :return: EmailMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'message_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_email_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_message`")
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_conversations_email_message`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

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
                                            response_type='EmailMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_messages(self, conversation_id: str, **kwargs) -> 'EmailMessageListing':
        """
        Get conversation messages
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_messages(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: EmailMessageListing
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
                    " to method get_conversations_email_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_messages`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages'.replace('{format}', 'json')
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
                                            response_type='EmailMessageListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_messages_draft(self, conversation_id: str, **kwargs) -> 'EmailMessage':
        """
        Get conversation draft reply
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_messages_draft(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: EmailMessage
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
                    " to method get_conversations_email_messages_draft" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_messages_draft`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages/draft'.replace('{format}', 'json')
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
                                            response_type='EmailMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_email_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_email_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_email_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_email_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_email_participant_wrapup`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_email_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_email_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_email_settings(self, conversation_id: str, **kwargs) -> 'EmailsSettings':
        """
        Get emails settings for a given conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_email_settings(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: EmailsSettings
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
                    " to method get_conversations_email_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_email_settings`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/settings'.replace('{format}', 'json')
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
                                            response_type='EmailsSettings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_emails(self, **kwargs) -> 'EmailConversationEntityListing':
        """
        Get active email conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_emails(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: EmailConversationEntityListing
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
                    " to method get_conversations_emails" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/emails'.replace('{format}', 'json')
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
                                            response_type='EmailConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_keyconfiguration(self, keyconfigurations_id: str, **kwargs) -> 'ConversationEncryptionConfiguration':
        """
        Get the encryption key configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_keyconfiguration(keyconfigurations_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str keyconfigurations_id: Key Configurations Id (required)
        :return: ConversationEncryptionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyconfigurations_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_keyconfiguration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'keyconfigurations_id' is set
        if ('keyconfigurations_id' not in params) or (params['keyconfigurations_id'] is None):
            raise ValueError("Missing the required parameter `keyconfigurations_id` when calling `get_conversations_keyconfiguration`")


        resource_path = '/api/v2/conversations/keyconfigurations/{keyconfigurationsId}'.replace('{format}', 'json')
        path_params = {}
        if 'keyconfigurations_id' in params:
            path_params['keyconfigurationsId'] = params['keyconfigurations_id']

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
                                            response_type='ConversationEncryptionConfiguration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_keyconfigurations(self, **kwargs) -> 'ConversationEncryptionConfigurationListing':
        """
        Get a list of key configurations data
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_keyconfigurations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ConversationEncryptionConfigurationListing
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
                    " to method get_conversations_keyconfigurations" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/keyconfigurations'.replace('{format}', 'json')
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
                                            response_type='ConversationEncryptionConfigurationListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message(self, conversation_id: str, **kwargs) -> 'MessageConversation':
        """
        Get message conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :return: MessageConversation
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
                    " to method get_conversations_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message`")


        resource_path = '/api/v2/conversations/messages/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='MessageConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_communication_messages_media_media_id(self, conversation_id: str, communication_id: str, media_id: str, **kwargs) -> 'MessageMediaData':
        """
        Get media
        See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_communication_messages_media_media_id(conversation_id, communication_id, media_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :param str media_id: mediaId (required)
        :return: MessageMediaData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id', 'media_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_communication_messages_media_media_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message_communication_messages_media_media_id`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_message_communication_messages_media_media_id`")
        # verify the required parameter 'media_id' is set
        if ('media_id' not in params) or (params['media_id'] is None):
            raise ValueError("Missing the required parameter `media_id` when calling `get_conversations_message_communication_messages_media_media_id`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media/{mediaId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']
        if 'media_id' in params:
            path_params['mediaId'] = params['media_id']

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
                                            response_type='MessageMediaData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_details(self, message_id: str, **kwargs) -> 'MessageData':
        """
        Get message
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_details(message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_id: messageId (required)
        :param bool use_normalized_message: If true, response removes deprecated fields (textBody, media, stickers)
        :return: MessageData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'use_normalized_message']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_details" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_conversations_message_details`")


        resource_path = '/api/v2/conversations/messages/{messageId}/details'.replace('{format}', 'json')
        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

        query_params = {}
        if 'use_normalized_message' in params:
            query_params['useNormalizedMessage'] = params['use_normalized_message']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MessageData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_message(self, conversation_id: str, message_id: str, **kwargs) -> 'MessageData':
        """
        Get conversation message
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_message(conversation_id, message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str message_id: messageId (required)
        :param bool use_normalized_message: If true, response removes deprecated fields (textBody, media, stickers)
        :return: MessageData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'message_id', 'use_normalized_message']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message_message`")
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_conversations_message_message`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/messages/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

        query_params = {}
        if 'use_normalized_message' in params:
            query_params['useNormalizedMessage'] = params['use_normalized_message']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MessageData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_message_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_message_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_participant_wrapup(self, conversation_id: str, participant_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation participant. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_participant_wrapup(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_participant_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message_participant_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_message_participant_wrapup`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_message_participant_wrapupcodes(self, conversation_id: str, participant_id: str, **kwargs) -> List['WrapupCode']:
        """
        Get list of wrapup codes for this conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_message_participant_wrapupcodes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id:  conversationId (required)
        :param str participant_id: participantId (required)
        :return: list[WrapupCode]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_message_participant_wrapupcodes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_message_participant_wrapupcodes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_message_participant_wrapupcodes`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapupcodes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type='list[WrapupCode]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messages(self, **kwargs) -> 'MessageConversationEntityListing':
        """
        Get active message conversations for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messages(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: MessageConversationEntityListing
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
                    " to method get_conversations_messages" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messages'.replace('{format}', 'json')
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
                                            response_type='MessageConversationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_facebook_app(self, **kwargs) -> 'FacebookAppCredentials':
        """
        Get Genesys Facebook App Id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_facebook_app(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FacebookAppCredentials
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
                    " to method get_conversations_messaging_facebook_app" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/facebook/app'.replace('{format}', 'json')
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
                                            response_type='FacebookAppCredentials',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations(self, **kwargs) -> 'MessagingIntegrationEntityListing':
        """
        Get a list of Integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param list[str] expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: MessagingIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MessagingIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_facebook(self, **kwargs) -> 'FacebookIntegrationEntityListing':
        """
        Get a list of Facebook Integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_facebook(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: FacebookIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_facebook" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations/facebook'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FacebookIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_facebook_integration_id(self, integration_id: str, **kwargs) -> 'FacebookIntegration':
        """
        Get a Facebook messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_facebook_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param str expand: Expand instructions for the return value.
        :return: FacebookIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_facebook_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_conversations_messaging_integrations_facebook_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/facebook/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='FacebookIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_line(self, **kwargs) -> 'LineIntegrationEntityListing':
        """
        Get a list of LINE messenger Integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_line(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: LineIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_line" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations/line'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LineIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_line_integration_id(self, integration_id: str, **kwargs) -> 'LineIntegration':
        """
        Get a LINE messenger integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_line_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param str expand: Expand instructions for the return value.
        :return: LineIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_line_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_conversations_messaging_integrations_line_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/line/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='LineIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_open(self, **kwargs) -> 'OpenIntegrationEntityListing':
        """
        Get a list of Open messaging integrations
        See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_open(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: OpenIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_open" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations/open'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OpenIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_open_integration_id(self, integration_id: str, **kwargs) -> 'OpenIntegration':
        """
        Get an Open messaging integration
        See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_open_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param str expand: Expand instructions for the return value.
        :return: OpenIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_open_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_conversations_messaging_integrations_open_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/open/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='OpenIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_twitter(self, **kwargs) -> 'TwitterIntegrationEntityListing':
        """
        Get a list of Twitter Integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_twitter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: TwitterIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_twitter" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations/twitter'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TwitterIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_twitter_integration_id(self, integration_id: str, **kwargs) -> 'TwitterIntegration':
        """
        Get a Twitter messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_twitter_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param str expand: Expand instructions for the return value.
        :return: TwitterIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_twitter_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_conversations_messaging_integrations_twitter_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/twitter/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='TwitterIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_whatsapp(self, **kwargs) -> 'WhatsAppIntegrationEntityListing':
        """
        Get a list of WhatsApp Integrations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_whatsapp(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :param str expand: Expand instructions for the return value.
        :param str supported_content_id: Filter integrations returned based on the supported content ID
        :param str messaging_setting_id: Filter integrations returned based on the setting ID
        :return: WhatsAppIntegrationEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'expand', 'supported_content_id', 'messaging_setting_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_whatsapp" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/integrations/whatsapp'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'supported_content_id' in params:
            query_params['supportedContent.id'] = params['supported_content_id']
        if 'messaging_setting_id' in params:
            query_params['messagingSetting.id'] = params['messaging_setting_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='WhatsAppIntegrationEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_integrations_whatsapp_integration_id(self, integration_id: str, **kwargs) -> 'WhatsAppIntegration':
        """
        Get a WhatsApp messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_integrations_whatsapp_integration_id(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param str expand: Expand instructions for the return value.
        :return: WhatsAppIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'expand']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_integrations_whatsapp_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_conversations_messaging_integrations_whatsapp_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/whatsapp/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

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
                                            response_type='WhatsAppIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_sticker(self, messenger_type: str, **kwargs) -> 'MessagingStickerEntityListing':
        """
        Get a list of Messaging Stickers
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_sticker(messenger_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str messenger_type: Messenger Type (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: MessagingStickerEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messenger_type', 'page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_sticker" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'messenger_type' is set
        if ('messenger_type' not in params) or (params['messenger_type'] is None):
            raise ValueError("Missing the required parameter `messenger_type` when calling `get_conversations_messaging_sticker`")


        resource_path = '/api/v2/conversations/messaging/stickers/{messengerType}'.replace('{format}', 'json')
        path_params = {}
        if 'messenger_type' in params:
            path_params['messengerType'] = params['messenger_type']

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
                                            response_type='MessagingStickerEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_supportedcontent(self, **kwargs) -> 'SupportedContentListing':
        """
        Get a list of Supported Content profiles
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_supportedcontent(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: SupportedContentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_supportedcontent" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/supportedcontent'.replace('{format}', 'json')
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
                                            response_type='SupportedContentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_supportedcontent_default(self, **kwargs) -> 'SupportedContent':
        """
        Get the organization's default supported content profile that will be used as the default when creating an integration.
        When an integration is created a supported content ID may be assigned to it. If the supported content ID is not supplied, the default supported content profile will be assigned to it.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_supportedcontent_default(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: SupportedContent
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
                    " to method get_conversations_messaging_supportedcontent_default" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/supportedcontent/default'.replace('{format}', 'json')
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
                                            response_type='SupportedContent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_supportedcontent_supported_content_id(self, supported_content_id: str, **kwargs) -> 'SupportedContent':
        """
        Get a supported content profile
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_supportedcontent_supported_content_id(supported_content_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supported_content_id: Supported Content ID (required)
        :return: SupportedContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supported_content_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_messaging_supportedcontent_supported_content_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'supported_content_id' is set
        if ('supported_content_id' not in params) or (params['supported_content_id'] is None):
            raise ValueError("Missing the required parameter `supported_content_id` when calling `get_conversations_messaging_supportedcontent_supported_content_id`")


        resource_path = '/api/v2/conversations/messaging/supportedcontent/{supportedContentId}'.replace('{format}', 'json')
        path_params = {}
        if 'supported_content_id' in params:
            path_params['supportedContentId'] = params['supported_content_id']

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
                                            response_type='SupportedContent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_messaging_threadingtimeline(self, **kwargs) -> 'ConversationThreadingWindow':
        """
        Get conversation threading window timeline for each messaging type
        Conversation messaging threading timeline is a setting defined for each messenger type in your organization. This setting will dictate whether a new message is added to the most recent existing conversation, or creates a new Conversation. If the existing Conversation is still in a connected state the threading timeline setting will never play a role. After the conversation is disconnected, if an inbound message is received or an outbound message is sent after the setting for threading timeline expires, a new conversation is created.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_messaging_threadingtimeline(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ConversationThreadingWindow
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
                    " to method get_conversations_messaging_threadingtimeline" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/messaging/threadingtimeline'.replace('{format}', 'json')
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
                                            response_type='ConversationThreadingWindow',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_screenshare_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_screenshare_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_screenshare_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_screenshare_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_screenshare_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/screenshares/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_settings(self, **kwargs) -> 'Settings':
        """
        Get Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Settings
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
                    " to method get_conversations_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/conversations/settings'.replace('{format}', 'json')
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
                                            response_type='Settings',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_social_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_social_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_social_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_social_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_social_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/socials/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_conversations_video_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> 'AssignedWrapupCode':
        """
        Get the wrap-up for this conversation communication. 
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param bool provisional: Indicates if the wrap-up code is provisional.
        :return: AssignedWrapupCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'provisional']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_conversations_video_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_conversations_video_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `get_conversations_video_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `get_conversations_video_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/videos/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'provisional' in params:
            query_params['provisional'] = params['provisional']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignedWrapupCode',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversation_participant(self, conversation_id: str, participant_id: str, body: 'MediaParticipantRequest', **kwargs) -> None:
        """
        Update a participant.
        Update conversation participant.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversation_participant(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param MediaParticipantRequest body: Update request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversation_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversation_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversation_participant`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversation_participant`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversation_participant_attributes(self, conversation_id: str, participant_id: str, body: 'ParticipantAttributes', **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversation_participant_attributes(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param ParticipantAttributes body: Participant attributes (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversation_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversation_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversation_participant_attributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversation_participant_attributes`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversation_secureattributes(self, conversation_id: str, body: 'ConversationSecureAttributes', **kwargs) -> str:
        """
        Update the secure attributes on a conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversation_secureattributes(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param ConversationSecureAttributes body: Conversation Secure Attributes (required)
        :return: str
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
                    " to method patch_conversation_secureattributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversation_secureattributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversation_secureattributes`")


        resource_path = '/api/v2/conversations/{conversationId}/secureattributes'.replace('{format}', 'json')
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_aftercallwork_conversation_id_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'AfterCallWorkUpdate', **kwargs) -> 'AfterCallWorkUpdate':
        """
        Update after-call work for this conversation communication.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_aftercallwork_conversation_id_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param AfterCallWorkUpdate body: AfterCallWorkUpdate (required)
        :return: AfterCallWorkUpdate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_aftercallwork_conversation_id_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_aftercallwork_conversation_id_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_aftercallwork_conversation_id_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_aftercallwork_conversation_id_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_aftercallwork_conversation_id_participant_communication`")


        resource_path = '/api/v2/conversations/aftercallwork/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='AfterCallWorkUpdate',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_call(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by setting its recording state, merging in other conversations to create a conference, or disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_call(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_call" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_call`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_call`")


        resource_path = '/api/v2/conversations/calls/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_call_participant(self, conversation_id: str, participant_id: str, body: 'MediaParticipantRequest', **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_call_participant(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: Participant request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_call_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_call_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_call_participant`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_call_participant`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_call_participant_attributes(self, conversation_id: str, participant_id: str, body: 'ParticipantAttributes', **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_call_participant_attributes(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: Participant attributes (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_call_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_call_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_call_participant_attributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_call_participant_attributes`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_call_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_call_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_call_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_call_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_call_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_call_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_call_participant_communication`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_call_participant_consult(self, conversation_id: str, participant_id: str, body: 'ConsultTransferUpdate', **kwargs) -> 'ConsultTransferResponse':
        """
        Change who can speak
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_call_participant_consult(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ConsultTransferUpdate body: new speak to (required)
        :return: ConsultTransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_call_participant_consult" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_call_participant_consult`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_call_participant_consult`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_call_participant_consult`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='ConsultTransferResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_callback(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_callback(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_callback" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_callback`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_callback`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_callback_participant(self, conversation_id: str, participant_id: str, body: 'MediaParticipantRequest', **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_callback_participant(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_callback_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_callback_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_callback_participant`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_callback_participant`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_callback_participant_attributes(self, conversation_id: str, participant_id: str, body: 'ParticipantAttributes', **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_callback_participant_attributes(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: Attributes (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_callback_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_callback_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_callback_participant_attributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_callback_participant_attributes`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_callback_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_callback_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_callback_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_callback_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_callback_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_callback_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_callback_participant_communication`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_callbacks(self, body: 'PatchCallbackRequest', **kwargs) -> 'PatchCallbackResponse':
        """
        Update a scheduled callback
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_callbacks(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PatchCallbackRequest body: PatchCallbackRequest (required)
        :return: PatchCallbackResponse
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
                    " to method patch_conversations_callbacks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_callbacks`")


        resource_path = '/api/v2/conversations/callbacks'.replace('{format}', 'json')
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
                                            response_type='PatchCallbackResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_chat(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_chat(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_chat" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_chat`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_chat`")


        resource_path = '/api/v2/conversations/chats/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_chat_participant(self, conversation_id: str, participant_id: str, body: 'MediaParticipantRequest', **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_chat_participant(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: Update request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_chat_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_chat_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_chat_participant`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_chat_participant`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_chat_participant_attributes(self, conversation_id: str, participant_id: str, body: 'ParticipantAttributes', **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_chat_participant_attributes(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: Participant attributes (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_chat_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_chat_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_chat_participant_attributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_chat_participant_attributes`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_chat_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_chat_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_chat_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_chat_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_chat_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_chat_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_chat_participant_communication`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_cobrowsesession(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_cobrowsesession(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_cobrowsesession" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_cobrowsesession`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_cobrowsesession`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_cobrowsesession_participant(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_cobrowsesession_participant(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_cobrowsesession_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_cobrowsesession_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_cobrowsesession_participant`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_cobrowsesession_participant_attributes(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_cobrowsesession_participant_attributes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_cobrowsesession_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_cobrowsesession_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_cobrowsesession_participant_attributes`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_cobrowsesession_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_cobrowsesession_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_cobrowsesession_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_cobrowsesession_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_cobrowsesession_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_cobrowsesession_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_cobrowsesession_participant_communication`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_email(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_email(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_email" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_email`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_email`")


        resource_path = '/api/v2/conversations/emails/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_email_participant(self, conversation_id: str, participant_id: str, body: 'MediaParticipantRequest', **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_email_participant(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: Update request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_email_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_email_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_email_participant`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_email_participant`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_email_participant_attributes(self, conversation_id: str, participant_id: str, body: 'ParticipantAttributes', **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_email_participant_attributes(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: Participant attributes (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_email_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_email_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_email_participant_attributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_email_participant_attributes`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_email_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_email_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_email_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_email_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_email_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_email_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_email_participant_communication`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_message(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Update a conversation by disconnecting all of the participants
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_message(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method patch_conversations_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_message`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_message`")


        resource_path = '/api/v2/conversations/messages/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_message_participant(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Update conversation participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_message_participant(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id:  conversationId (required)
        :param str participant_id: participantId (required)
        :param MediaParticipantRequest body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_message_participant" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_message_participant`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_message_participant`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_message_participant_attributes(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Update the attributes on a conversation participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_message_participant_attributes(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id:  conversationId (required)
        :param str participant_id: participantId (required)
        :param ParticipantAttributes body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_message_participant_attributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_message_participant_attributes`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_message_participant_attributes`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/attributes'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def patch_conversations_message_participant_communication(self, conversation_id: str, participant_id: str, communication_id: str, body: 'MediaParticipantRequest', **kwargs) -> object:
        """
        Update conversation participant's communication by disconnecting it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_message_participant_communication(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id:  conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param MediaParticipantRequest body: Participant (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_message_participant_communication" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `patch_conversations_message_participant_communication`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `patch_conversations_message_participant_communication`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `patch_conversations_message_participant_communication`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_message_participant_communication`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_messaging_integrations_facebook_integration_id(self, integration_id: str, body: 'FacebookIntegrationUpdateRequest', **kwargs) -> 'FacebookIntegration':
        """
        Update Facebook messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_messaging_integrations_facebook_integration_id(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param FacebookIntegrationUpdateRequest body: FacebookIntegrationUpdateRequest (required)
        :return: FacebookIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_messaging_integrations_facebook_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `patch_conversations_messaging_integrations_facebook_integration_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_messaging_integrations_facebook_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/facebook/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='FacebookIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_messaging_integrations_open_integration_id(self, integration_id: str, body: 'OpenIntegrationUpdateRequest', **kwargs) -> 'OpenIntegration':
        """
        Update an Open messaging integration
        See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_messaging_integrations_open_integration_id(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param OpenIntegrationUpdateRequest body: OpenIntegrationUpdateRequest (required)
        :return: OpenIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_messaging_integrations_open_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `patch_conversations_messaging_integrations_open_integration_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_messaging_integrations_open_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/open/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='OpenIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_messaging_integrations_twitter_integration_id(self, integration_id: str, body: 'TwitterIntegrationRequest', **kwargs) -> 'TwitterIntegration':
        """
        Update Twitter messaging integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_messaging_integrations_twitter_integration_id(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param TwitterIntegrationRequest body: TwitterIntegrationRequest (required)
        :return: TwitterIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_messaging_integrations_twitter_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `patch_conversations_messaging_integrations_twitter_integration_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_messaging_integrations_twitter_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/twitter/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='TwitterIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_messaging_integrations_whatsapp_integration_id(self, integration_id: str, body: 'WhatsAppIntegrationUpdateRequest', **kwargs) -> 'WhatsAppIntegration':
        """
        Update or activate a WhatsApp messaging integration
        The following steps are required in order to fully activate a WhatsApp Integration: Initially, you will need to get an activation code by sending: an action set to Activate, and an authenticationMethod choosing from Sms or Voice. Finally, once you have been informed of an activation code on selected authenticationMethod, you will need to confirm the code by sending: an action set to Confirm, and the confirmationCode you have received from Whatsapp.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_messaging_integrations_whatsapp_integration_id(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param WhatsAppIntegrationUpdateRequest body: WhatsAppIntegrationUpdateRequest (required)
        :return: WhatsAppIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_messaging_integrations_whatsapp_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `patch_conversations_messaging_integrations_whatsapp_integration_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_messaging_integrations_whatsapp_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/whatsapp/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='WhatsAppIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_messaging_supportedcontent_supported_content_id(self, supported_content_id: str, body: 'SupportedContent', **kwargs) -> 'SupportedContent':
        """
        Update a supported content profile
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_messaging_supportedcontent_supported_content_id(supported_content_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supported_content_id: Supported Content ID (required)
        :param SupportedContent body: SupportedContent (required)
        :return: SupportedContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supported_content_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_conversations_messaging_supportedcontent_supported_content_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'supported_content_id' is set
        if ('supported_content_id' not in params) or (params['supported_content_id'] is None):
            raise ValueError("Missing the required parameter `supported_content_id` when calling `patch_conversations_messaging_supportedcontent_supported_content_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_messaging_supportedcontent_supported_content_id`")


        resource_path = '/api/v2/conversations/messaging/supportedcontent/{supportedContentId}'.replace('{format}', 'json')
        path_params = {}
        if 'supported_content_id' in params:
            path_params['supportedContentId'] = params['supported_content_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='SupportedContent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_conversations_settings(self, body: 'Settings', **kwargs) -> None:
        """
        Update Settings
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_conversations_settings(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Settings body: Settings (required)
        :return: None
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
                    " to method patch_conversations_settings" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_conversations_settings`")


        resource_path = '/api/v2/conversations/settings'.replace('{format}', 'json')
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

    def post_conversation_assign(self, conversation_id: str, body: 'ConversationUser', **kwargs) -> str:
        """
        Attempts to manually assign a specified conversation to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_assign(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param ConversationUser body: Targeted user (required)
        :return: str
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
                    " to method post_conversation_assign" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_assign`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversation_assign`")


        resource_path = '/api/v2/conversations/{conversationId}/assign'.replace('{format}', 'json')
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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversation_cobrowse(self, conversation_id: str, **kwargs) -> 'CobrowseWebMessagingSession':
        """
        Creates a cobrowse session. Requires \"conversation:cobrowse:add\" (for web messaging) or \"conversation:cobrowsevoice:add\" permission.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_cobrowse(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: Conversation ID (required)
        :return: CobrowseWebMessagingSession
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
                    " to method post_conversation_cobrowse" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_cobrowse`")


        resource_path = '/api/v2/conversations/{conversationId}/cobrowse'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CobrowseWebMessagingSession',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversation_disconnect(self, conversation_id: str, **kwargs) -> str:
        """
        Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resynchronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_disconnect(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :return: str
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
                    " to method post_conversation_disconnect" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_disconnect`")


        resource_path = '/api/v2/conversations/{conversationId}/disconnect'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'POST',
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

    def post_conversation_participant_callbacks(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Create a new callback for the specified participant on the conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_participant_callbacks(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param CreateCallbackOnConversationCommand body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversation_participant_callbacks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_participant_callbacks`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversation_participant_callbacks`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/callbacks'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversation_participant_digits(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Sends DTMF to the participant
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_participant_digits(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param Digits body: Digits
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversation_participant_digits" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_participant_digits`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversation_participant_digits`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/digits'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversation_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversation_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversation_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversation_participant_replace`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversation_participant_secureivrsessions(self, conversation_id: str, participant_id: str, **kwargs) -> 'SecureSession':
        """
        Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversation_participant_secureivrsessions(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :param CreateSecureSession body: 
        :return: SecureSession
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversation_participant_secureivrsessions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversation_participant_secureivrsessions`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversation_participant_secureivrsessions`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='SecureSession',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_call(self, conversation_id: str, body: 'CallCommand', **kwargs) -> 'Conversation':
        """
        Place a new call as part of a callback conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param CallCommand body: Conversation (required)
        :return: Conversation
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
                    " to method post_conversations_call" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_call`")


        resource_path = '/api/v2/conversations/calls/{conversationId}'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_call_participant_coach(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Listen in on the conversation from the point of view of a given participant while speaking to just the given participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participant_coach(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_call_participant_coach" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participant_coach`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_call_participant_coach`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/coach'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_call_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_call_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_call_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_call_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_call_participant_consult(self, conversation_id: str, participant_id: str, body: 'ConsultTransfer', **kwargs) -> 'ConsultTransferResponse':
        """
        Initiate and update consult transfer
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participant_consult(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param ConsultTransfer body: Destination address & initial speak to (required)
        :return: ConsultTransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_call_participant_consult" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participant_consult`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_call_participant_consult`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_call_participant_consult`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='ConsultTransferResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_call_participant_monitor(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Listen in on the conversation from the point of view of a given participant.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participant_monitor(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_call_participant_monitor" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participant_monitor`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_call_participant_monitor`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/monitor'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_call_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_call_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_call_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_call_participant_replace`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_call_participants(self, conversation_id: str, body: 'Conversation', **kwargs) -> 'Conversation':
        """
        Add participants to a conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_call_participants(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param Conversation body: Conversation (required)
        :return: Conversation
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
                    " to method post_conversations_call_participants" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_call_participants`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_call_participants`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants'.replace('{format}', 'json')
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
                                            response_type='Conversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_callback_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_callback_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_callback_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_callback_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_callback_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_callback_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_callback_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_callback_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_callback_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_callback_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_callback_participant_replace`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_callbacks(self, body: 'CreateCallbackCommand', **kwargs) -> 'CreateCallbackResponse':
        """
        Create a Callback
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_callbacks(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateCallbackCommand body: Callback (required)
        :return: CreateCallbackResponse
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
                    " to method post_conversations_callbacks" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_callbacks`")


        resource_path = '/api/v2/conversations/callbacks'.replace('{format}', 'json')
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
                                            response_type='CreateCallbackResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_callbacks_bulk_disconnect(self, body: 'BulkCallbackDisconnectRequest', **kwargs) -> None:
        """
        Disconnect multiple scheduled callbacks
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_callbacks_bulk_disconnect(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BulkCallbackDisconnectRequest body: BulkCallbackDisconnectRequest (required)
        :return: None
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
                    " to method post_conversations_callbacks_bulk_disconnect" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_callbacks_bulk_disconnect`")


        resource_path = '/api/v2/conversations/callbacks/bulk/disconnect'.replace('{format}', 'json')
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

    def post_conversations_callbacks_bulk_update(self, body: 'BulkCallbackPatchRequest', **kwargs) -> 'BulkCallbackPatchResponse':
        """
        Update multiple scheduled callbacks
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_callbacks_bulk_update(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BulkCallbackPatchRequest body: BulkCallbackPatchRequest (required)
        :return: BulkCallbackPatchResponse
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
                    " to method post_conversations_callbacks_bulk_update" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_callbacks_bulk_update`")


        resource_path = '/api/v2/conversations/callbacks/bulk/update'.replace('{format}', 'json')
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
                                            response_type='BulkCallbackPatchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_calls(self, body: 'CreateCallRequest', **kwargs) -> 'CreateCallResponse':
        """
        Create a call conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_calls(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateCallRequest body: Call request (required)
        :return: CreateCallResponse
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
                    " to method post_conversations_calls" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_calls`")


        resource_path = '/api/v2/conversations/calls'.replace('{format}', 'json')
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
                                            response_type='CreateCallResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_chat_communication_messages(self, conversation_id: str, communication_id: str, body: 'CreateWebChatMessageRequest', **kwargs) -> 'WebChatMessage':
        """
        Send a message on behalf of a communication in a chat conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_chat_communication_messages(conversation_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :param CreateWebChatMessageRequest body: Message (required)
        :return: WebChatMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_chat_communication_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_chat_communication_messages`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_chat_communication_messages`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_chat_communication_messages`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/communications/{communicationId}/messages'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='WebChatMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_chat_communication_typing(self, conversation_id: str, communication_id: str, **kwargs) -> 'WebChatTyping':
        """
        Send a typing-indicator on behalf of a communication in a chat conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_chat_communication_typing(conversation_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :return: WebChatTyping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_chat_communication_typing" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_chat_communication_typing`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_chat_communication_typing`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/communications/{communicationId}/typing'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

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
                                            response_type='WebChatTyping',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_chat_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_chat_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_chat_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_chat_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_chat_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_chat_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_chat_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_chat_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_chat_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_chat_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_chat_participant_replace`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_chats(self, body: 'CreateWebChatRequest', **kwargs) -> 'ChatConversation':
        """
        Create a web chat conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_chats(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateWebChatRequest body: Create web chat request (required)
        :return: ChatConversation
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
                    " to method post_conversations_chats" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_chats`")


        resource_path = '/api/v2/conversations/chats'.replace('{format}', 'json')
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
                                            response_type='ChatConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_cobrowsesession_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_cobrowsesession_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_cobrowsesession_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_cobrowsesession_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_cobrowsesession_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_cobrowsesession_participant_replace(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_cobrowsesession_participant_replace(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_cobrowsesession_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_cobrowsesession_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_cobrowsesession_participant_replace`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_email_inboundmessages(self, conversation_id: str, body: 'InboundMessageRequest', **kwargs) -> 'EmailConversation':
        """
        Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_email_inboundmessages(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param InboundMessageRequest body: Send external email reply (required)
        :return: EmailConversation
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
                    " to method post_conversations_email_inboundmessages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_email_inboundmessages`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_email_inboundmessages`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/inboundmessages'.replace('{format}', 'json')
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
                                            response_type='EmailConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_email_messages(self, conversation_id: str, body: 'EmailMessage', **kwargs) -> 'EmailMessageReply':
        """
        Send an email reply
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_email_messages(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param EmailMessage body: Reply (required)
        :return: EmailMessageReply
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
                    " to method post_conversations_email_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_email_messages`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_email_messages`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages'.replace('{format}', 'json')
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
                                            response_type='EmailMessageReply',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_email_messages_draft_attachments_copy(self, conversation_id: str, body: 'CopyAttachmentsRequest', **kwargs) -> 'EmailMessage':
        """
        Copy attachments from an email message to the current draft.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_email_messages_draft_attachments_copy(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param CopyAttachmentsRequest body: Copy Attachment Request (required)
        :return: EmailMessage
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
                    " to method post_conversations_email_messages_draft_attachments_copy" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_email_messages_draft_attachments_copy`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_email_messages_draft_attachments_copy`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages/draft/attachments/copy'.replace('{format}', 'json')
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
                                            response_type='EmailMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_email_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_email_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_email_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_email_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_email_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_email_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_email_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_email_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_email_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_email_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_email_participant_replace`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_emails(self, body: 'CreateEmailRequest', **kwargs) -> 'EmailConversation':
        """
        Create an email conversation
        If the direction of the request is INBOUND, this will create an external conversation with a third party provider. If the direction of the the request is OUTBOUND, this will create a conversation to send outbound emails on behalf of a queue.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_emails(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateEmailRequest body: Create email request (required)
        :return: EmailConversation
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
                    " to method post_conversations_emails" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_emails`")


        resource_path = '/api/v2/conversations/emails'.replace('{format}', 'json')
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
                                            response_type='EmailConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_emails_agentless(self, body: 'AgentlessEmailSendRequestDto', **kwargs) -> 'AgentlessEmailSendResponseDto':
        """
        Create an email conversation, per API
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_emails_agentless(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AgentlessEmailSendRequestDto body: Create agentless email request (required)
        :return: AgentlessEmailSendResponseDto
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
                    " to method post_conversations_emails_agentless" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_emails_agentless`")


        resource_path = '/api/v2/conversations/emails/agentless'.replace('{format}', 'json')
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
                                            response_type='AgentlessEmailSendResponseDto',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_faxes(self, body: 'FaxSendRequest', **kwargs) -> 'FaxSendResponse':
        """
        Create Fax Conversation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_faxes(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FaxSendRequest body: Fax (required)
        :return: FaxSendResponse
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
                    " to method post_conversations_faxes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_faxes`")


        resource_path = '/api/v2/conversations/faxes'.replace('{format}', 'json')
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
                                            response_type='FaxSendResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_keyconfigurations(self, body: 'ConversationEncryptionConfiguration', **kwargs) -> 'ConversationEncryptionConfiguration':
        """
        Setup configurations for encryption key creation
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_keyconfigurations(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationEncryptionConfiguration body: Encryption Configuration (required)
        :return: ConversationEncryptionConfiguration
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
                    " to method post_conversations_keyconfigurations" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_keyconfigurations`")


        resource_path = '/api/v2/conversations/keyconfigurations'.replace('{format}', 'json')
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
                                            response_type='ConversationEncryptionConfiguration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_keyconfigurations_validate(self, body: 'ConversationEncryptionConfiguration', **kwargs) -> 'ConversationEncryptionConfiguration':
        """
        Validate encryption key configurations without saving it
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_keyconfigurations_validate(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationEncryptionConfiguration body: Encryption Configuration (required)
        :return: ConversationEncryptionConfiguration
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
                    " to method post_conversations_keyconfigurations_validate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_keyconfigurations_validate`")


        resource_path = '/api/v2/conversations/keyconfigurations/validate'.replace('{format}', 'json')
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
                                            response_type='ConversationEncryptionConfiguration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_message_communication_messages(self, conversation_id: str, communication_id: str, body: 'AdditionalMessage', **kwargs) -> 'MessageData':
        """
        Send message
        Send message on existing conversation/communication. Only one message body field can be accepted, per request. Example: 1 textBody, 1 mediaId, 1 stickerId, or 1 messageTemplate.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_communication_messages(conversation_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :param AdditionalMessage body: Message (required)
        :param bool use_normalized_message: If true, response removes deprecated fields (textBody, media, stickers)
        :return: MessageData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id', 'body', 'use_normalized_message']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_communication_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_communication_messages`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_message_communication_messages`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_message_communication_messages`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}
        if 'use_normalized_message' in params:
            query_params['useNormalizedMessage'] = params['use_normalized_message']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='MessageData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_message_communication_messages_media(self, conversation_id: str, communication_id: str, **kwargs) -> 'MessageMediaData':
        """
        Create media
        See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_communication_messages_media(conversation_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :return: MessageMediaData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_communication_messages_media" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_communication_messages_media`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_message_communication_messages_media`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

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
                                            response_type='MessageMediaData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_message_communication_typing(self, conversation_id: str, communication_id: str, body: 'MessageTypingEventRequest', **kwargs) -> None:
        """
        Send message typing event
        Send message typing event for existing conversation/communication.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_communication_typing(conversation_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str communication_id: communicationId (required)
        :param MessageTypingEventRequest body: MessageTypingEvent (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_communication_typing" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_communication_typing`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_message_communication_typing`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_message_communication_typing`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/communications/{communicationId}/typing'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_message_messages_bulk(self, conversation_id: str, **kwargs) -> 'TextMessageListing':
        """
        Get messages in batch
        The path parameter [conversationId] should contain the conversationId of the conversation being filtered. The body should contain the messageId(s) of messages being requested. For example: [\"a3069a33b-bbb1-4703-9d68-061d9e9db96e\", \"55bc6be3-078c-4a49-a4e6-1e05776ed7e8\"]

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_messages_bulk(conversation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id:  (required)
        :param bool use_normalized_message: If true, response removes deprecated fields (textBody, media, stickers)
        :param list[str] body: messageIds
        :return: TextMessageListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'use_normalized_message', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_messages_bulk" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_messages_bulk`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/messages/bulk'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']

        query_params = {}
        if 'use_normalized_message' in params:
            query_params['useNormalizedMessage'] = params['use_normalized_message']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='TextMessageListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_message_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_message_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_message_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_message_participant_replace(self, conversation_id: str, participant_id: str, body: 'TransferRequest', **kwargs) -> None:
        """
        Replace this participant with the specified user and/or address
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_message_participant_replace(conversation_id, participant_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param TransferRequest body: Transfer request (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_message_participant_replace" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_message_participant_replace`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_message_participant_replace`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_message_participant_replace`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/participants/{participantId}/replace'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_messages(self, body: 'CreateOutboundMessagingConversationRequest', **kwargs) -> 'MessageConversation':
        """
        Create an outbound messaging conversation.
        If there is an existing conversation between the remote address and the address associated with the queue specified in createOutboundRequest then the result of this request depends on the state of that conversation and the useExistingConversation field of createOutboundRequest. If the existing conversation is in alerting or connected state, then the request will fail. If the existing conversation is disconnected but still within the conversation window then the request will fail unless useExistingConversation is set to true.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messages(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateOutboundMessagingConversationRequest body: Create outbound messaging conversation (required)
        :return: MessageConversation
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
                    " to method post_conversations_messages" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messages`")


        resource_path = '/api/v2/conversations/messages'.replace('{format}', 'json')
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
                                            response_type='MessageConversation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messages_agentless(self, body: 'SendAgentlessOutboundMessageRequest', **kwargs) -> 'SendAgentlessOutboundMessageResponse':
        """
        Send an agentless outbound message
        Send an agentless (api participant) outbound message using a client credential grant. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will generate a new Conversation, if there is an existing active Conversation between the fromAddress and toAddress already, then this POST will fail.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messages_agentless(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SendAgentlessOutboundMessageRequest body: Create agentless outbound messaging request (required)
        :return: SendAgentlessOutboundMessageResponse
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
                    " to method post_conversations_messages_agentless" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messages_agentless`")


        resource_path = '/api/v2/conversations/messages/agentless'.replace('{format}', 'json')
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
                                            response_type='SendAgentlessOutboundMessageResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messages_inbound_open(self, body: 'OpenNormalizedMessage', **kwargs) -> 'OpenNormalizedMessage':
        """
        Send an inbound Open Message
        Send an inbound message to an Open Messaging integration. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will either generate a new Conversation, or be a part of an existing conversation. See https://developer.genesys.cloud/api/digital/openmessaging/ for example usage.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messages_inbound_open(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OpenNormalizedMessage body: NormalizedMessage (required)
        :return: OpenNormalizedMessage
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
                    " to method post_conversations_messages_inbound_open" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messages_inbound_open`")


        resource_path = '/api/v2/conversations/messages/inbound/open'.replace('{format}', 'json')
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
                                            response_type='OpenNormalizedMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_integrations_facebook(self, body: 'FacebookIntegrationRequest', **kwargs) -> 'FacebookIntegration':
        """
        Create a Facebook Integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_integrations_facebook(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FacebookIntegrationRequest body: FacebookIntegrationRequest (required)
        :return: FacebookIntegration
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
                    " to method post_conversations_messaging_integrations_facebook" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_integrations_facebook`")


        resource_path = '/api/v2/conversations/messaging/integrations/facebook'.replace('{format}', 'json')
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
                                            response_type='FacebookIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_integrations_line(self, body: 'LineIntegrationRequest', **kwargs) -> 'LineIntegration':
        """
        Create a LINE messenger Integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_integrations_line(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param LineIntegrationRequest body: LineIntegrationRequest (required)
        :return: LineIntegration
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
                    " to method post_conversations_messaging_integrations_line" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_integrations_line`")


        resource_path = '/api/v2/conversations/messaging/integrations/line'.replace('{format}', 'json')
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
                                            response_type='LineIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_integrations_open(self, body: 'OpenIntegrationRequest', **kwargs) -> 'OpenIntegration':
        """
        Create an Open messaging integration
        See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_integrations_open(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OpenIntegrationRequest body: OpenIntegrationRequest (required)
        :return: OpenIntegration
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
                    " to method post_conversations_messaging_integrations_open" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_integrations_open`")


        resource_path = '/api/v2/conversations/messaging/integrations/open'.replace('{format}', 'json')
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
                                            response_type='OpenIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_integrations_twitter(self, body: 'TwitterIntegrationRequest', **kwargs) -> 'TwitterIntegration':
        """
        Create a Twitter Integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_integrations_twitter(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TwitterIntegrationRequest body: TwitterIntegrationRequest (required)
        :return: TwitterIntegration
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
                    " to method post_conversations_messaging_integrations_twitter" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_integrations_twitter`")


        resource_path = '/api/v2/conversations/messaging/integrations/twitter'.replace('{format}', 'json')
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
                                            response_type='TwitterIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_integrations_whatsapp(self, body: 'WhatsAppIntegrationRequest', **kwargs) -> 'WhatsAppIntegration':
        """
        Create a WhatsApp Integration
        You must be approved by WhatsApp to use this feature. Your approved e164-formatted phone number and valid WhatsApp certificate for your number are required. Your WhatsApp certificate must have valid base64 encoding. Please paste carefully and do not add any leading or trailing spaces. Do not alter any characters. An integration must be activated within 7 days of certificate generation. If you cannot complete the addition and activation of the number within 7 days, please obtain a new certificate before creating the integration. Integrations created with an invalid number or certificate may immediately incur additional integration fees. Please carefully enter your number and certificate as described.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_integrations_whatsapp(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WhatsAppIntegrationRequest body: WhatsAppIntegrationRequest (required)
        :return: WhatsAppIntegration
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
                    " to method post_conversations_messaging_integrations_whatsapp" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_integrations_whatsapp`")


        resource_path = '/api/v2/conversations/messaging/integrations/whatsapp'.replace('{format}', 'json')
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
                                            response_type='WhatsAppIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_messaging_supportedcontent(self, body: 'SupportedContent', **kwargs) -> 'SupportedContent':
        """
        Create a Supported Content profile
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_messaging_supportedcontent(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SupportedContent body: SupportedContent (required)
        :return: SupportedContent
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
                    " to method post_conversations_messaging_supportedcontent" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_messaging_supportedcontent`")


        resource_path = '/api/v2/conversations/messaging/supportedcontent'.replace('{format}', 'json')
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
                                            response_type='SupportedContent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_participants_attributes_search(self, body: 'ConversationParticipantSearchRequest', **kwargs) -> 'JsonCursorSearchResponse':
        """
        Search conversations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_participants_attributes_search(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationParticipantSearchRequest body: Search request options (required)
        :return: JsonCursorSearchResponse
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
                    " to method post_conversations_participants_attributes_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_conversations_participants_attributes_search`")


        resource_path = '/api/v2/conversations/participants/attributes/search'.replace('{format}', 'json')
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
                                            response_type='JsonCursorSearchResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_conversations_screenshare_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_screenshare_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_screenshare_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_screenshare_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_screenshare_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/screenshares/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_social_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_social_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_social_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_social_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_social_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/socials/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def post_conversations_video_participant_communication_wrapup(self, conversation_id: str, participant_id: str, communication_id: str, **kwargs) -> None:
        """
        Apply wrap-up for this conversation communication
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param WrapupInput body: Wrap-up
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_conversations_video_participant_communication_wrapup" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `post_conversations_video_participant_communication_wrapup`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `post_conversations_video_participant_communication_wrapup`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `post_conversations_video_participant_communication_wrapup`")


        resource_path = '/api/v2/conversations/videos/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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

    def put_conversation_participant_flaggedreason(self, conversation_id: str, participant_id: str, **kwargs) -> None:
        """
        Set flagged reason on conversation participant to indicate bad conversation quality.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversation_participant_flaggedreason(conversation_id, participant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param str participant_id: participant ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_conversation_participant_flaggedreason" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversation_participant_flaggedreason`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `put_conversation_participant_flaggedreason`")


        resource_path = '/api/v2/conversations/{conversationId}/participants/{participantId}/flaggedreason'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversation_secureattributes(self, conversation_id: str, body: 'ConversationSecureAttributes', **kwargs) -> str:
        """
        Set the secure attributes on a conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversation_secureattributes(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param ConversationSecureAttributes body: Conversation Secure Attributes (required)
        :return: str
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
                    " to method put_conversation_secureattributes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversation_secureattributes`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversation_secureattributes`")


        resource_path = '/api/v2/conversations/{conversationId}/secureattributes'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversation_tags(self, conversation_id: str, body: 'ConversationTagsUpdate', **kwargs) -> str:
        """
        Update the tags on a conversation.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversation_tags(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversation ID (required)
        :param ConversationTagsUpdate body: Conversation Tags (required)
        :return: str
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
                    " to method put_conversation_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversation_tags`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversation_tags`")


        resource_path = '/api/v2/conversations/{conversationId}/tags'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_call_participant_communication_uuidata(self, conversation_id: str, participant_id: str, communication_id: str, body: 'SetUuiDataRequest', **kwargs) -> object:
        """
        Set uuiData to be sent on future commands.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_call_participant_communication_uuidata(conversation_id, participant_id, communication_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param str participant_id: participantId (required)
        :param str communication_id: communicationId (required)
        :param SetUuiDataRequest body: UUIData Request (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversation_id', 'participant_id', 'communication_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_conversations_call_participant_communication_uuidata" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_call_participant_communication_uuidata`")
        # verify the required parameter 'participant_id' is set
        if ('participant_id' not in params) or (params['participant_id'] is None):
            raise ValueError("Missing the required parameter `participant_id` when calling `put_conversations_call_participant_communication_uuidata`")
        # verify the required parameter 'communication_id' is set
        if ('communication_id' not in params) or (params['communication_id'] is None):
            raise ValueError("Missing the required parameter `communication_id` when calling `put_conversations_call_participant_communication_uuidata`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_call_participant_communication_uuidata`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/uuidata'.replace('{format}', 'json')
        path_params = {}
        if 'conversation_id' in params:
            path_params['conversationId'] = params['conversation_id']
        if 'participant_id' in params:
            path_params['participantId'] = params['participant_id']
        if 'communication_id' in params:
            path_params['communicationId'] = params['communication_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_call_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_call_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_call_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_call_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_call_recordingstate`")


        resource_path = '/api/v2/conversations/calls/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_callback_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_callback_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_callback_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_callback_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_callback_recordingstate`")


        resource_path = '/api/v2/conversations/callbacks/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_chat_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_chat_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_chat_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_chat_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_chat_recordingstate`")


        resource_path = '/api/v2/conversations/chats/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_cobrowsesession_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_cobrowsesession_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_cobrowsesession_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_cobrowsesession_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_cobrowsesession_recordingstate`")


        resource_path = '/api/v2/conversations/cobrowsesessions/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_email_messages_draft(self, conversation_id: str, body: 'EmailMessage', **kwargs) -> 'EmailMessage':
        """
        Update conversation draft reply
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_email_messages_draft(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param EmailMessage body: Draft (required)
        :return: EmailMessage
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
                    " to method put_conversations_email_messages_draft" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_email_messages_draft`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_email_messages_draft`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/messages/draft'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EmailMessage',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_email_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_email_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_email_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_email_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_email_recordingstate`")


        resource_path = '/api/v2/conversations/emails/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_keyconfiguration(self, keyconfigurations_id: str, body: 'ConversationEncryptionConfiguration', **kwargs) -> 'ConversationEncryptionConfiguration':
        """
        Update the encryption key configurations
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_keyconfiguration(keyconfigurations_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str keyconfigurations_id: Key Configurations Id (required)
        :param ConversationEncryptionConfiguration body: Encryption key configuration metadata (required)
        :return: ConversationEncryptionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyconfigurations_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_conversations_keyconfiguration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'keyconfigurations_id' is set
        if ('keyconfigurations_id' not in params) or (params['keyconfigurations_id'] is None):
            raise ValueError("Missing the required parameter `keyconfigurations_id` when calling `put_conversations_keyconfiguration`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_keyconfiguration`")


        resource_path = '/api/v2/conversations/keyconfigurations/{keyconfigurationsId}'.replace('{format}', 'json')
        path_params = {}
        if 'keyconfigurations_id' in params:
            path_params['keyconfigurationsId'] = params['keyconfigurations_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='ConversationEncryptionConfiguration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_message_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_message_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_message_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_message_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_message_recordingstate`")


        resource_path = '/api/v2/conversations/messages/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_messaging_integrations_line_integration_id(self, integration_id: str, body: 'LineIntegrationRequest', **kwargs) -> 'LineIntegration':
        """
        Update a LINE messenger integration
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_messaging_integrations_line_integration_id(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str integration_id: Integration ID (required)
        :param LineIntegrationRequest body: LineIntegrationRequest (required)
        :return: LineIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_conversations_messaging_integrations_line_integration_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `put_conversations_messaging_integrations_line_integration_id`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_messaging_integrations_line_integration_id`")


        resource_path = '/api/v2/conversations/messaging/integrations/line/{integrationId}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
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
                                            response_type='LineIntegration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_messaging_supportedcontent_default(self, body: 'SupportedContentReference', **kwargs) -> 'SupportedContent':
        """
        Set the organization's default supported content profile that may be assigned to an integration when it is created.
        When an integration is created a supported content ID may be assigned to it. If the supported content ID is not supplied, the default supported content profile will be assigned to it.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_messaging_supportedcontent_default(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SupportedContentReference body: SupportedContent (required)
        :return: SupportedContent
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
                    " to method put_conversations_messaging_supportedcontent_default" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_messaging_supportedcontent_default`")


        resource_path = '/api/v2/conversations/messaging/supportedcontent/default'.replace('{format}', 'json')
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
                                            response_type='SupportedContent',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_messaging_threadingtimeline(self, body: 'ConversationThreadingWindow', **kwargs) -> 'ConversationThreadingWindow':
        """
        Update conversation threading window timeline for each messaging type
        PUT Conversation messaging threading timeline is intended to set the conversation threading settings for ALL messengerTypes. If you omit a messengerType in the request body then the setting for that messengerType will use the platform default value. The PUT replaces the existing setting(s) that were previously set for each messengerType.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_messaging_threadingtimeline(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ConversationThreadingWindow body: ConversationThreadingWindowRequest (required)
        :return: ConversationThreadingWindow
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
                    " to method put_conversations_messaging_threadingtimeline" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_messaging_threadingtimeline`")


        resource_path = '/api/v2/conversations/messaging/threadingtimeline'.replace('{format}', 'json')
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
                                            response_type='ConversationThreadingWindow',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_conversations_screenshare_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_screenshare_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_screenshare_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_screenshare_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_screenshare_recordingstate`")


        resource_path = '/api/v2/conversations/screenshares/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_social_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_social_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_social_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_social_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_social_recordingstate`")


        resource_path = '/api/v2/conversations/socials/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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

    def put_conversations_video_recordingstate(self, conversation_id: str, body: 'SetRecordingState', **kwargs) -> str:
        """
        Update a conversation by setting its recording state
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_conversations_video_recordingstate(conversation_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversation_id: conversationId (required)
        :param SetRecordingState body: SetRecordingState (required)
        :return: str
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
                    " to method put_conversations_video_recordingstate" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params) or (params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `put_conversations_video_recordingstate`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_conversations_video_recordingstate`")


        resource_path = '/api/v2/conversations/videos/{conversationId}/recordingstate'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
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
