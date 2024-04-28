---
title: ConversationsApi
---

## PureCloudPlatformClientV2.ConversationsApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_analytics_conversations_details_job**](ConversationsApi.html#delete_analytics_conversations_details_job) | Delete/cancel an async details job|
|[**delete_conversation_participant_code**](ConversationsApi.html#delete_conversation_participant_code) | Delete a code used to add a communication to this participant|
|[**delete_conversation_participant_flaggedreason**](ConversationsApi.html#delete_conversation_participant_flaggedreason) | Remove flagged reason from conversation participant.|
|[**delete_conversations_call_participant_consult**](ConversationsApi.html#delete_conversations_call_participant_consult) | Cancel the transfer|
|[**delete_conversations_email_messages_draft_attachment**](ConversationsApi.html#delete_conversations_email_messages_draft_attachment) | Delete attachment from draft|
|[**delete_conversations_messages_cachedmedia_cached_media_item_id**](ConversationsApi.html#delete_conversations_messages_cachedmedia_cached_media_item_id) | Remove a cached media item asychronously|
|[**delete_conversations_messaging_integrations_facebook_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_facebook_integration_id) | Delete a Facebook messaging integration|
|[**delete_conversations_messaging_integrations_instagram_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_instagram_integration_id) | Delete Instagram messaging integration|
|[**delete_conversations_messaging_integrations_line_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_line_integration_id) | Delete a LINE messenger integration (Deprecated)|
|[**delete_conversations_messaging_integrations_open_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_open_integration_id) | Delete an Open messaging integration|
|[**delete_conversations_messaging_integrations_twitter_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_twitter_integration_id) | Delete a Twitter messaging integration|
|[**delete_conversations_messaging_integrations_whatsapp_integration_id**](ConversationsApi.html#delete_conversations_messaging_integrations_whatsapp_integration_id) | Delete a WhatsApp messaging integration|
|[**delete_conversations_messaging_setting**](ConversationsApi.html#delete_conversations_messaging_setting) | Delete a messaging setting|
|[**delete_conversations_messaging_settings_default**](ConversationsApi.html#delete_conversations_messaging_settings_default) | Delete the organization&#39;s default setting, a global default will be applied to integrations without settings|
|[**delete_conversations_messaging_supportedcontent_supported_content_id**](ConversationsApi.html#delete_conversations_messaging_supportedcontent_supported_content_id) | Delete a supported content profile|
|[**get_analytics_conversation_details**](ConversationsApi.html#get_analytics_conversation_details) | Get a conversation by id|
|[**get_analytics_conversations_aggregates_job**](ConversationsApi.html#get_analytics_conversations_aggregates_job) | Get status for async query for conversation aggregates|
|[**get_analytics_conversations_aggregates_job_results**](ConversationsApi.html#get_analytics_conversations_aggregates_job_results) | Fetch a page of results for an async aggregates query|
|[**get_analytics_conversations_details**](ConversationsApi.html#get_analytics_conversations_details) | Gets multiple conversations by id|
|[**get_analytics_conversations_details_job**](ConversationsApi.html#get_analytics_conversations_details_job) | Get status for async query for conversation details|
|[**get_analytics_conversations_details_job_results**](ConversationsApi.html#get_analytics_conversations_details_job_results) | Fetch a page of results for an async details job|
|[**get_analytics_conversations_details_jobs_availability**](ConversationsApi.html#get_analytics_conversations_details_jobs_availability) | Lookup the datalake availability date and time|
|[**get_conversation**](ConversationsApi.html#get_conversation) | Get conversation|
|[**get_conversation_participant_secureivrsession**](ConversationsApi.html#get_conversation_participant_secureivrsession) | Fetch info on a secure session|
|[**get_conversation_participant_secureivrsessions**](ConversationsApi.html#get_conversation_participant_secureivrsessions) | Get a list of secure sessions for this participant.|
|[**get_conversation_participant_wrapup**](ConversationsApi.html#get_conversation_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversation_participant_wrapupcodes**](ConversationsApi.html#get_conversation_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversation_secureattributes**](ConversationsApi.html#get_conversation_secureattributes) | Get the secure attributes on a conversation.|
|[**get_conversations**](ConversationsApi.html#get_conversations) | Get active conversations for the logged in user|
|[**get_conversations_call**](ConversationsApi.html#get_conversations_call) | Get call conversation|
|[**get_conversations_call_participant_communication_wrapup**](ConversationsApi.html#get_conversations_call_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_call_participant_wrapup**](ConversationsApi.html#get_conversations_call_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_call_participant_wrapupcodes**](ConversationsApi.html#get_conversations_call_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_callback**](ConversationsApi.html#get_conversations_callback) | Get callback conversation|
|[**get_conversations_callback_participant_communication_wrapup**](ConversationsApi.html#get_conversations_callback_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_callback_participant_wrapup**](ConversationsApi.html#get_conversations_callback_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_callback_participant_wrapupcodes**](ConversationsApi.html#get_conversations_callback_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_callbacks**](ConversationsApi.html#get_conversations_callbacks) | Get active callback conversations for the logged in user|
|[**get_conversations_calls**](ConversationsApi.html#get_conversations_calls) | Get active call conversations for the logged in user|
|[**get_conversations_calls_history**](ConversationsApi.html#get_conversations_calls_history) | Get call history|
|[**get_conversations_calls_maximumconferenceparties**](ConversationsApi.html#get_conversations_calls_maximumconferenceparties) | Get the maximum number of participants that this user can have on a conference|
|[**get_conversations_chat**](ConversationsApi.html#get_conversations_chat) | Get chat conversation|
|[**get_conversations_chat_message**](ConversationsApi.html#get_conversations_chat_message) | Get a web chat conversation message|
|[**get_conversations_chat_messages**](ConversationsApi.html#get_conversations_chat_messages) | Get the messages of a chat conversation.|
|[**get_conversations_chat_participant_communication_wrapup**](ConversationsApi.html#get_conversations_chat_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_chat_participant_wrapup**](ConversationsApi.html#get_conversations_chat_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_chat_participant_wrapupcodes**](ConversationsApi.html#get_conversations_chat_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_chats**](ConversationsApi.html#get_conversations_chats) | Get active chat conversations for the logged in user|
|[**get_conversations_cobrowsesession**](ConversationsApi.html#get_conversations_cobrowsesession) | Get cobrowse conversation|
|[**get_conversations_cobrowsesession_participant_communication_wrapup**](ConversationsApi.html#get_conversations_cobrowsesession_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_cobrowsesession_participant_wrapup**](ConversationsApi.html#get_conversations_cobrowsesession_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_cobrowsesession_participant_wrapupcodes**](ConversationsApi.html#get_conversations_cobrowsesession_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_cobrowsesessions**](ConversationsApi.html#get_conversations_cobrowsesessions) | Get active cobrowse conversations for the logged in user|
|[**get_conversations_email**](ConversationsApi.html#get_conversations_email) | Get email conversation|
|[**get_conversations_email_message**](ConversationsApi.html#get_conversations_email_message) | Get conversation message|
|[**get_conversations_email_messages**](ConversationsApi.html#get_conversations_email_messages) | Get conversation messages|
|[**get_conversations_email_messages_draft**](ConversationsApi.html#get_conversations_email_messages_draft) | Get conversation draft reply|
|[**get_conversations_email_participant_communication_wrapup**](ConversationsApi.html#get_conversations_email_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_email_participant_wrapup**](ConversationsApi.html#get_conversations_email_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_email_participant_wrapupcodes**](ConversationsApi.html#get_conversations_email_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_email_settings**](ConversationsApi.html#get_conversations_email_settings) | Get emails settings for a given conversation|
|[**get_conversations_emails**](ConversationsApi.html#get_conversations_emails) | Get active email conversations for the logged in user|
|[**get_conversations_keyconfiguration**](ConversationsApi.html#get_conversations_keyconfiguration) | Get the encryption key configurations|
|[**get_conversations_keyconfigurations**](ConversationsApi.html#get_conversations_keyconfigurations) | Get a list of key configurations data|
|[**get_conversations_message**](ConversationsApi.html#get_conversations_message) | Get message conversation|
|[**get_conversations_message_communication_messages_media_media_id**](ConversationsApi.html#get_conversations_message_communication_messages_media_media_id) | Get media|
|[**get_conversations_message_details**](ConversationsApi.html#get_conversations_message_details) | Get message|
|[**get_conversations_message_message**](ConversationsApi.html#get_conversations_message_message) | Get conversation message|
|[**get_conversations_message_participant_communication_wrapup**](ConversationsApi.html#get_conversations_message_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_message_participant_wrapup**](ConversationsApi.html#get_conversations_message_participant_wrapup) | Get the wrap-up for this conversation participant. |
|[**get_conversations_message_participant_wrapupcodes**](ConversationsApi.html#get_conversations_message_participant_wrapupcodes) | Get list of wrapup codes for this conversation participant|
|[**get_conversations_messages**](ConversationsApi.html#get_conversations_messages) | Get active message conversations for the logged in user|
|[**get_conversations_messages_cachedmedia**](ConversationsApi.html#get_conversations_messages_cachedmedia) | Get a list of cached media items|
|[**get_conversations_messages_cachedmedia_cached_media_item_id**](ConversationsApi.html#get_conversations_messages_cachedmedia_cached_media_item_id) | Get a cached media item|
|[**get_conversations_messaging_facebook_app**](ConversationsApi.html#get_conversations_messaging_facebook_app) | Get Genesys Facebook App Id|
|[**get_conversations_messaging_facebook_permissions**](ConversationsApi.html#get_conversations_messaging_facebook_permissions) | Get a list of Facebook Permissions|
|[**get_conversations_messaging_integrations**](ConversationsApi.html#get_conversations_messaging_integrations) | Get a list of Integrations|
|[**get_conversations_messaging_integrations_facebook**](ConversationsApi.html#get_conversations_messaging_integrations_facebook) | Get a list of Facebook Integrations|
|[**get_conversations_messaging_integrations_facebook_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_facebook_integration_id) | Get a Facebook messaging integration|
|[**get_conversations_messaging_integrations_instagram**](ConversationsApi.html#get_conversations_messaging_integrations_instagram) | Get a list of Instagram Integrations|
|[**get_conversations_messaging_integrations_instagram_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_instagram_integration_id) | Get Instagram messaging integration|
|[**get_conversations_messaging_integrations_line**](ConversationsApi.html#get_conversations_messaging_integrations_line) | Get a list of LINE messenger Integrations (Deprecated)|
|[**get_conversations_messaging_integrations_line_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_line_integration_id) | Get a LINE messenger integration (Deprecated)|
|[**get_conversations_messaging_integrations_open**](ConversationsApi.html#get_conversations_messaging_integrations_open) | Get a list of Open messaging integrations|
|[**get_conversations_messaging_integrations_open_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_open_integration_id) | Get an Open messaging integration|
|[**get_conversations_messaging_integrations_twitter**](ConversationsApi.html#get_conversations_messaging_integrations_twitter) | Get a list of Twitter Integrations (Deprecated)|
|[**get_conversations_messaging_integrations_twitter_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_twitter_integration_id) | Get a Twitter messaging integration (Deprecated)|
|[**get_conversations_messaging_integrations_whatsapp**](ConversationsApi.html#get_conversations_messaging_integrations_whatsapp) | Get a list of WhatsApp Integrations|
|[**get_conversations_messaging_integrations_whatsapp_integration_id**](ConversationsApi.html#get_conversations_messaging_integrations_whatsapp_integration_id) | Get a WhatsApp messaging integration|
|[**get_conversations_messaging_setting**](ConversationsApi.html#get_conversations_messaging_setting) | Get a messaging setting|
|[**get_conversations_messaging_settings**](ConversationsApi.html#get_conversations_messaging_settings) | Get a list of messaging settings|
|[**get_conversations_messaging_settings_default**](ConversationsApi.html#get_conversations_messaging_settings_default) | Get the organization&#39;s default settings that will be used as the default when creating an integration.|
|[**get_conversations_messaging_sticker**](ConversationsApi.html#get_conversations_messaging_sticker) | Get a list of Messaging Stickers (Deprecated)|
|[**get_conversations_messaging_supportedcontent**](ConversationsApi.html#get_conversations_messaging_supportedcontent) | Get a list of Supported Content profiles|
|[**get_conversations_messaging_supportedcontent_default**](ConversationsApi.html#get_conversations_messaging_supportedcontent_default) | Get the organization&#39;s default supported content profile that will be used as the default when creating an integration.|
|[**get_conversations_messaging_supportedcontent_supported_content_id**](ConversationsApi.html#get_conversations_messaging_supportedcontent_supported_content_id) | Get a supported content profile|
|[**get_conversations_messaging_threadingtimeline**](ConversationsApi.html#get_conversations_messaging_threadingtimeline) | Get conversation threading window timeline for each messaging type|
|[**get_conversations_screenshare_participant_communication_wrapup**](ConversationsApi.html#get_conversations_screenshare_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_settings**](ConversationsApi.html#get_conversations_settings) | Get Settings|
|[**get_conversations_social_participant_communication_wrapup**](ConversationsApi.html#get_conversations_social_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_video_details**](ConversationsApi.html#get_conversations_video_details) | Get video conference details (e.g. the current number of active participants).|
|[**get_conversations_video_participant_communication_wrapup**](ConversationsApi.html#get_conversations_video_participant_communication_wrapup) | Get the wrap-up for this conversation communication. |
|[**get_conversations_videos_meeting**](ConversationsApi.html#get_conversations_videos_meeting) | Gets a record for a given meetingId|
|[**patch_conversation_participant**](ConversationsApi.html#patch_conversation_participant) | Update a participant.|
|[**patch_conversation_participant_attributes**](ConversationsApi.html#patch_conversation_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversation_secureattributes**](ConversationsApi.html#patch_conversation_secureattributes) | Update the secure attributes on a conversation.|
|[**patch_conversation_utilizationlabel**](ConversationsApi.html#patch_conversation_utilizationlabel) | Update the utilization label on a conversation. When there is no value provided, the system default label is applied|
|[**patch_conversations_aftercallwork_conversation_id_participant_communication**](ConversationsApi.html#patch_conversations_aftercallwork_conversation_id_participant_communication) | Update after-call work for this conversation communication.|
|[**patch_conversations_call**](ConversationsApi.html#patch_conversations_call) | Update a conversation by setting its recording state, merging in other conversations to create a conference, or disconnecting all of the participants|
|[**patch_conversations_call_participant**](ConversationsApi.html#patch_conversations_call_participant) | Update conversation participant|
|[**patch_conversations_call_participant_attributes**](ConversationsApi.html#patch_conversations_call_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_call_participant_communication**](ConversationsApi.html#patch_conversations_call_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_call_participant_consult**](ConversationsApi.html#patch_conversations_call_participant_consult) | Change who can speak|
|[**patch_conversations_callback**](ConversationsApi.html#patch_conversations_callback) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_callback_participant**](ConversationsApi.html#patch_conversations_callback_participant) | Update conversation participant|
|[**patch_conversations_callback_participant_attributes**](ConversationsApi.html#patch_conversations_callback_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_callback_participant_communication**](ConversationsApi.html#patch_conversations_callback_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_callbacks**](ConversationsApi.html#patch_conversations_callbacks) | Update a scheduled callback|
|[**patch_conversations_chat**](ConversationsApi.html#patch_conversations_chat) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_chat_participant**](ConversationsApi.html#patch_conversations_chat_participant) | Update conversation participant|
|[**patch_conversations_chat_participant_attributes**](ConversationsApi.html#patch_conversations_chat_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_chat_participant_communication**](ConversationsApi.html#patch_conversations_chat_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_cobrowsesession**](ConversationsApi.html#patch_conversations_cobrowsesession) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_cobrowsesession_participant**](ConversationsApi.html#patch_conversations_cobrowsesession_participant) | Update conversation participant|
|[**patch_conversations_cobrowsesession_participant_attributes**](ConversationsApi.html#patch_conversations_cobrowsesession_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_cobrowsesession_participant_communication**](ConversationsApi.html#patch_conversations_cobrowsesession_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_email**](ConversationsApi.html#patch_conversations_email) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_email_messages_draft**](ConversationsApi.html#patch_conversations_email_messages_draft) | Reset conversation draft to its initial state and/or auto-fill draft content|
|[**patch_conversations_email_participant**](ConversationsApi.html#patch_conversations_email_participant) | Update conversation participant|
|[**patch_conversations_email_participant_attributes**](ConversationsApi.html#patch_conversations_email_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_email_participant_communication**](ConversationsApi.html#patch_conversations_email_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_message**](ConversationsApi.html#patch_conversations_message) | Update a conversation by disconnecting all of the participants|
|[**patch_conversations_message_participant**](ConversationsApi.html#patch_conversations_message_participant) | Update conversation participant|
|[**patch_conversations_message_participant_attributes**](ConversationsApi.html#patch_conversations_message_participant_attributes) | Update the attributes on a conversation participant.|
|[**patch_conversations_message_participant_communication**](ConversationsApi.html#patch_conversations_message_participant_communication) | Update conversation participant&#39;s communication by disconnecting it.|
|[**patch_conversations_messaging_integrations_facebook_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_facebook_integration_id) | Update Facebook messaging integration|
|[**patch_conversations_messaging_integrations_instagram_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_instagram_integration_id) | Update Instagram messaging integration|
|[**patch_conversations_messaging_integrations_open_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_open_integration_id) | Update an Open messaging integration|
|[**patch_conversations_messaging_integrations_twitter_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_twitter_integration_id) | Update Twitter messaging integration|
|[**patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id) | Activate a WhatsApp messaging integration created using the WhatsApp embedded signup flow|
|[**patch_conversations_messaging_integrations_whatsapp_integration_id**](ConversationsApi.html#patch_conversations_messaging_integrations_whatsapp_integration_id) | Update a WhatsApp messaging integration|
|[**patch_conversations_messaging_setting**](ConversationsApi.html#patch_conversations_messaging_setting) | Update a messaging setting|
|[**patch_conversations_messaging_supportedcontent_supported_content_id**](ConversationsApi.html#patch_conversations_messaging_supportedcontent_supported_content_id) | Update a supported content profile|
|[**patch_conversations_settings**](ConversationsApi.html#patch_conversations_settings) | Update Settings|
|[**post_analytics_conversation_details_properties**](ConversationsApi.html#post_analytics_conversation_details_properties) | Index conversation properties|
|[**post_analytics_conversations_activity_query**](ConversationsApi.html#post_analytics_conversations_activity_query) | Query for conversation activity observations|
|[**post_analytics_conversations_aggregates_jobs**](ConversationsApi.html#post_analytics_conversations_aggregates_jobs) | Query for conversation aggregates asynchronously|
|[**post_analytics_conversations_aggregates_query**](ConversationsApi.html#post_analytics_conversations_aggregates_query) | Query for conversation aggregates|
|[**post_analytics_conversations_details_jobs**](ConversationsApi.html#post_analytics_conversations_details_jobs) | Query for conversation details asynchronously|
|[**post_analytics_conversations_details_query**](ConversationsApi.html#post_analytics_conversations_details_query) | Query for conversation details|
|[**post_conversation_assign**](ConversationsApi.html#post_conversation_assign) | Attempts to manually assign a specified conversation to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.|
|[**post_conversation_barge**](ConversationsApi.html#post_conversation_barge) | Barge a conversation creating a barged in conference of connected participants.|
|[**post_conversation_cobrowse**](ConversationsApi.html#post_conversation_cobrowse) | Creates a cobrowse session. Requires \&quot;conversation:cobrowse:add\&quot; (for web messaging) or \&quot;conversation:cobrowsevoice:add\&quot; permission.|
|[**post_conversation_disconnect**](ConversationsApi.html#post_conversation_disconnect) | Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resynchronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.|
|[**post_conversation_participant_callbacks**](ConversationsApi.html#post_conversation_participant_callbacks) | Create a new callback for the specified participant on the conversation.|
|[**post_conversation_participant_digits**](ConversationsApi.html#post_conversation_participant_digits) | Sends DTMF to the participant|
|[**post_conversation_participant_replace**](ConversationsApi.html#post_conversation_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversation_participant_replace_agent**](ConversationsApi.html#post_conversation_participant_replace_agent) | Replace this participant with the specified agent|
|[**post_conversation_participant_replace_external**](ConversationsApi.html#post_conversation_participant_replace_external) | Replace this participant with the an external contact|
|[**post_conversation_participant_replace_queue**](ConversationsApi.html#post_conversation_participant_replace_queue) | Replace this participant with the specified queue|
|[**post_conversation_participant_secureivrsessions**](ConversationsApi.html#post_conversation_participant_secureivrsessions) | Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.|
|[**post_conversation_summary_feedback**](ConversationsApi.html#post_conversation_summary_feedback) | Submit feedback for the summary.|
|[**post_conversations_call**](ConversationsApi.html#post_conversations_call) | Place a new call as part of a callback conversation.|
|[**post_conversations_call_participant_barge**](ConversationsApi.html#post_conversations_call_participant_barge) | Barge a given participant&#39;s call creating a barged in conference of connected participants.|
|[**post_conversations_call_participant_coach**](ConversationsApi.html#post_conversations_call_participant_coach) | Listen in on the conversation from the point of view of a given participant while speaking to just the given participant.|
|[**post_conversations_call_participant_communication_wrapup**](ConversationsApi.html#post_conversations_call_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_call_participant_consult**](ConversationsApi.html#post_conversations_call_participant_consult) | Initiate and update consult transfer|
|[**post_conversations_call_participant_consult_agent**](ConversationsApi.html#post_conversations_call_participant_consult_agent) | Initiate a consult transfer to an agent|
|[**post_conversations_call_participant_consult_external**](ConversationsApi.html#post_conversations_call_participant_consult_external) | Initiate a consult transfer to an external contact|
|[**post_conversations_call_participant_consult_queue**](ConversationsApi.html#post_conversations_call_participant_consult_queue) | Initiate a consult transfer to a queue|
|[**post_conversations_call_participant_monitor**](ConversationsApi.html#post_conversations_call_participant_monitor) | Listen in on the conversation from the point of view of a given participant.|
|[**post_conversations_call_participant_replace**](ConversationsApi.html#post_conversations_call_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_call_participants**](ConversationsApi.html#post_conversations_call_participants) | Add participants to a conversation|
|[**post_conversations_callback_participant_communication_wrapup**](ConversationsApi.html#post_conversations_callback_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_callback_participant_replace**](ConversationsApi.html#post_conversations_callback_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_callbacks**](ConversationsApi.html#post_conversations_callbacks) | Create a Callback|
|[**post_conversations_callbacks_bulk_disconnect**](ConversationsApi.html#post_conversations_callbacks_bulk_disconnect) | Disconnect multiple scheduled callbacks|
|[**post_conversations_callbacks_bulk_update**](ConversationsApi.html#post_conversations_callbacks_bulk_update) | Update multiple scheduled callbacks|
|[**post_conversations_calls**](ConversationsApi.html#post_conversations_calls) | Create a call conversation|
|[**post_conversations_chat_communication_messages**](ConversationsApi.html#post_conversations_chat_communication_messages) | Send a message on behalf of a communication in a chat conversation.|
|[**post_conversations_chat_communication_typing**](ConversationsApi.html#post_conversations_chat_communication_typing) | Send a typing-indicator on behalf of a communication in a chat conversation.|
|[**post_conversations_chat_participant_communication_wrapup**](ConversationsApi.html#post_conversations_chat_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_chat_participant_replace**](ConversationsApi.html#post_conversations_chat_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_chats**](ConversationsApi.html#post_conversations_chats) | Create a web chat conversation|
|[**post_conversations_cobrowsesession_participant_communication_wrapup**](ConversationsApi.html#post_conversations_cobrowsesession_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_cobrowsesession_participant_replace**](ConversationsApi.html#post_conversations_cobrowsesession_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_email_inboundmessages**](ConversationsApi.html#post_conversations_email_inboundmessages) | Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.|
|[**post_conversations_email_messages**](ConversationsApi.html#post_conversations_email_messages) | Send an email reply|
|[**post_conversations_email_messages_draft_attachments_copy**](ConversationsApi.html#post_conversations_email_messages_draft_attachments_copy) | Copy attachments from an email message to the current draft.|
|[**post_conversations_email_participant_communication_wrapup**](ConversationsApi.html#post_conversations_email_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_email_participant_replace**](ConversationsApi.html#post_conversations_email_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_emails**](ConversationsApi.html#post_conversations_emails) | Create an email conversation|
|[**post_conversations_emails_agentless**](ConversationsApi.html#post_conversations_emails_agentless) | Create an email conversation, per API|
|[**post_conversations_faxes**](ConversationsApi.html#post_conversations_faxes) | Create Fax Conversation|
|[**post_conversations_keyconfigurations**](ConversationsApi.html#post_conversations_keyconfigurations) | Setup configurations for encryption key creation|
|[**post_conversations_keyconfigurations_validate**](ConversationsApi.html#post_conversations_keyconfigurations_validate) | Validate encryption key configurations without saving it|
|[**post_conversations_message_communication_messages**](ConversationsApi.html#post_conversations_message_communication_messages) | Send message|
|[**post_conversations_message_communication_messages_media**](ConversationsApi.html#post_conversations_message_communication_messages_media) | Create media|
|[**post_conversations_message_communication_typing**](ConversationsApi.html#post_conversations_message_communication_typing) | Send message typing event|
|[**post_conversations_message_inbound_open_event**](ConversationsApi.html#post_conversations_message_inbound_open_event) | Send an inbound Open Event Message|
|[**post_conversations_message_inbound_open_message**](ConversationsApi.html#post_conversations_message_inbound_open_message) | Send inbound Open Message|
|[**post_conversations_message_inbound_open_receipt**](ConversationsApi.html#post_conversations_message_inbound_open_receipt) | Send an inbound Open Receipt Message|
|[**post_conversations_message_messages_bulk**](ConversationsApi.html#post_conversations_message_messages_bulk) | Get messages in batch|
|[**post_conversations_message_participant_communication_wrapup**](ConversationsApi.html#post_conversations_message_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_message_participant_monitor**](ConversationsApi.html#post_conversations_message_participant_monitor) | Listen in on the conversation from the point of view of a given participant.|
|[**post_conversations_message_participant_replace**](ConversationsApi.html#post_conversations_message_participant_replace) | Replace this participant with the specified user and/or address|
|[**post_conversations_messages**](ConversationsApi.html#post_conversations_messages) | Create an outbound messaging conversation.|
|[**post_conversations_messages_agentless**](ConversationsApi.html#post_conversations_messages_agentless) | Send an agentless outbound message|
|[**post_conversations_messages_inbound_open**](ConversationsApi.html#post_conversations_messages_inbound_open) | Send an inbound Open Message|
|[**post_conversations_messaging_integrations_facebook**](ConversationsApi.html#post_conversations_messaging_integrations_facebook) | Create a Facebook Integration|
|[**post_conversations_messaging_integrations_instagram**](ConversationsApi.html#post_conversations_messaging_integrations_instagram) | Create Instagram Integration|
|[**post_conversations_messaging_integrations_line**](ConversationsApi.html#post_conversations_messaging_integrations_line) | Create a LINE messenger Integration (Deprecated)|
|[**post_conversations_messaging_integrations_open**](ConversationsApi.html#post_conversations_messaging_integrations_open) | Create an Open messaging integration|
|[**post_conversations_messaging_integrations_twitter**](ConversationsApi.html#post_conversations_messaging_integrations_twitter) | Create a Twitter Integration|
|[**post_conversations_messaging_integrations_whatsapp**](ConversationsApi.html#post_conversations_messaging_integrations_whatsapp) | [This API is deprecated. Use POST /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup instead] Create a WhatsApp Integration|
|[**post_conversations_messaging_integrations_whatsapp_embeddedsignup**](ConversationsApi.html#post_conversations_messaging_integrations_whatsapp_embeddedsignup) | Create a WhatsApp Integration using the WhatsApp embedded signup flow|
|[**post_conversations_messaging_settings**](ConversationsApi.html#post_conversations_messaging_settings) | Create a messaging setting|
|[**post_conversations_messaging_supportedcontent**](ConversationsApi.html#post_conversations_messaging_supportedcontent) | Create a Supported Content profile|
|[**post_conversations_participants_attributes_search**](ConversationsApi.html#post_conversations_participants_attributes_search) | Search conversations|
|[**post_conversations_screenshare_participant_communication_wrapup**](ConversationsApi.html#post_conversations_screenshare_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_social_participant_communication_wrapup**](ConversationsApi.html#post_conversations_social_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_video_participant_communication_wrapup**](ConversationsApi.html#post_conversations_video_participant_communication_wrapup) | Apply wrap-up for this conversation communication|
|[**post_conversations_videos_meetings**](ConversationsApi.html#post_conversations_videos_meetings) | Generate a meetingId for a given conferenceId|
|[**put_conversation_participant_flaggedreason**](ConversationsApi.html#put_conversation_participant_flaggedreason) | Set flagged reason on conversation participant to indicate bad conversation quality.|
|[**put_conversation_secureattributes**](ConversationsApi.html#put_conversation_secureattributes) | Set the secure attributes on a conversation.|
|[**put_conversation_tags**](ConversationsApi.html#put_conversation_tags) | Update the tags on a conversation.|
|[**put_conversations_call_participant_communication_uuidata**](ConversationsApi.html#put_conversations_call_participant_communication_uuidata) | Set uuiData to be sent on future commands.|
|[**put_conversations_call_recordingstate**](ConversationsApi.html#put_conversations_call_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_callback_recordingstate**](ConversationsApi.html#put_conversations_callback_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_chat_recordingstate**](ConversationsApi.html#put_conversations_chat_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_cobrowsesession_recordingstate**](ConversationsApi.html#put_conversations_cobrowsesession_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_email_messages_draft**](ConversationsApi.html#put_conversations_email_messages_draft) | Update conversation draft reply|
|[**put_conversations_email_recordingstate**](ConversationsApi.html#put_conversations_email_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_keyconfiguration**](ConversationsApi.html#put_conversations_keyconfiguration) | Update the encryption key configurations|
|[**put_conversations_message_recordingstate**](ConversationsApi.html#put_conversations_message_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_messaging_integrations_line_integration_id**](ConversationsApi.html#put_conversations_messaging_integrations_line_integration_id) | Update a LINE messenger integration (Deprecated)|
|[**put_conversations_messaging_settings_default**](ConversationsApi.html#put_conversations_messaging_settings_default) | Set the organization&#39;s default setting that may be applied to to integrations without settings|
|[**put_conversations_messaging_supportedcontent_default**](ConversationsApi.html#put_conversations_messaging_supportedcontent_default) | Set the organization&#39;s default supported content profile that may be assigned to an integration when it is created.|
|[**put_conversations_messaging_threadingtimeline**](ConversationsApi.html#put_conversations_messaging_threadingtimeline) | Update conversation threading window timeline for each messaging type|
|[**put_conversations_screenshare_recordingstate**](ConversationsApi.html#put_conversations_screenshare_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_social_recordingstate**](ConversationsApi.html#put_conversations_social_recordingstate) | Update a conversation by setting its recording state|
|[**put_conversations_video_recordingstate**](ConversationsApi.html#put_conversations_video_recordingstate) | Update a conversation by setting its recording state|
{: class="table table-striped"}

<a name="delete_analytics_conversations_details_job"></a>

##  delete_analytics_conversations_details_job(job_id)



Delete/cancel an async details job

Wraps DELETE /api/v2/analytics/conversations/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Delete/cancel an async details job
    api_instance.delete_analytics_conversations_details_job(job_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_analytics_conversations_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversation_participant_code"></a>

##  delete_conversation_participant_code(conversation_id, participant_id, add_communication_code)



Delete a code used to add a communication to this participant

Wraps DELETE /api/v2/conversations/{conversationId}/participants/{participantId}/codes/{addCommunicationCode} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
add_communication_code = 'add_communication_code_example' # str | addCommunicationCode

try:
    # Delete a code used to add a communication to this participant
    api_instance.delete_conversation_participant_code(conversation_id, participant_id, add_communication_code)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversation_participant_code: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **add_communication_code** | **str**| addCommunicationCode |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversation_participant_flaggedreason"></a>

##  delete_conversation_participant_flaggedreason(conversation_id, participant_id)



Remove flagged reason from conversation participant.

Wraps DELETE /api/v2/conversations/{conversationId}/participants/{participantId}/flaggedreason 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Remove flagged reason from conversation participant.
    api_instance.delete_conversation_participant_flaggedreason(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversation_participant_flaggedreason: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_call_participant_consult"></a>

##  delete_conversations_call_participant_consult(conversation_id, participant_id)



Cancel the transfer

Wraps DELETE /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Cancel the transfer
    api_instance.delete_conversations_call_participant_consult(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_call_participant_consult: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_email_messages_draft_attachment"></a>

##  delete_conversations_email_messages_draft_attachment(conversation_id, attachment_id)



Delete attachment from draft

Wraps DELETE /api/v2/conversations/emails/{conversationId}/messages/draft/attachments/{attachmentId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
attachment_id = 'attachment_id_example' # str | attachmentId

try:
    # Delete attachment from draft
    api_instance.delete_conversations_email_messages_draft_attachment(conversation_id, attachment_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_email_messages_draft_attachment: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **attachment_id** | **str**| attachmentId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messages_cachedmedia_cached_media_item_id"></a>

##  delete_conversations_messages_cachedmedia_cached_media_item_id(cached_media_item_id)



Remove a cached media item asychronously

Wraps DELETE /api/v2/conversations/messages/cachedmedia/{cachedMediaItemId} 

Requires ANY permissions: 

* conversation:cachedMedia:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
cached_media_item_id = 'cached_media_item_id_example' # str | cachedMediaItemId

try:
    # Remove a cached media item asychronously
    api_instance.delete_conversations_messages_cachedmedia_cached_media_item_id(cached_media_item_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messages_cachedmedia_cached_media_item_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cached_media_item_id** | **str**| cachedMediaItemId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_facebook_integration_id"></a>

##  delete_conversations_messaging_integrations_facebook_integration_id(integration_id)



Delete a Facebook messaging integration

Wraps DELETE /api/v2/conversations/messaging/integrations/facebook/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a Facebook messaging integration
    api_instance.delete_conversations_messaging_integrations_facebook_integration_id(integration_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_facebook_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_instagram_integration_id"></a>

##  delete_conversations_messaging_integrations_instagram_integration_id(integration_id)



Delete Instagram messaging integration

Wraps DELETE /api/v2/conversations/messaging/integrations/instagram/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete Instagram messaging integration
    api_instance.delete_conversations_messaging_integrations_instagram_integration_id(integration_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_instagram_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_line_integration_id"></a>

##  delete_conversations_messaging_integrations_line_integration_id(integration_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a LINE messenger integration (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps DELETE /api/v2/conversations/messaging/integrations/line/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a LINE messenger integration (Deprecated)
    api_instance.delete_conversations_messaging_integrations_line_integration_id(integration_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_line_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_open_integration_id"></a>

##  delete_conversations_messaging_integrations_open_integration_id(integration_id)



Delete an Open messaging integration

See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

Wraps DELETE /api/v2/conversations/messaging/integrations/open/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete an Open messaging integration
    api_instance.delete_conversations_messaging_integrations_open_integration_id(integration_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_open_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_twitter_integration_id"></a>

##  delete_conversations_messaging_integrations_twitter_integration_id(integration_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Delete a Twitter messaging integration

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-x-formerly-twitter-third-party-messaging-channel/

Wraps DELETE /api/v2/conversations/messaging/integrations/twitter/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a Twitter messaging integration
    api_instance.delete_conversations_messaging_integrations_twitter_integration_id(integration_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_twitter_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_integrations_whatsapp_integration_id"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) delete_conversations_messaging_integrations_whatsapp_integration_id(integration_id)



Delete a WhatsApp messaging integration

Wraps DELETE /api/v2/conversations/messaging/integrations/whatsapp/{integrationId} 

Requires ALL permissions: 

* messaging:integration:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID

try:
    # Delete a WhatsApp messaging integration
    api_response = api_instance.delete_conversations_messaging_integrations_whatsapp_integration_id(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_integrations_whatsapp_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="delete_conversations_messaging_setting"></a>

##  delete_conversations_messaging_setting(message_setting_id)



Delete a messaging setting

Wraps DELETE /api/v2/conversations/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
message_setting_id = 'message_setting_id_example' # str | Message Setting ID

try:
    # Delete a messaging setting
    api_instance.delete_conversations_messaging_setting(message_setting_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Setting ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_conversations_messaging_settings_default"></a>

##  delete_conversations_messaging_settings_default()



Delete the organization's default setting, a global default will be applied to integrations without settings

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be assigned to it.

Wraps DELETE /api/v2/conversations/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Delete the organization's default setting, a global default will be applied to integrations without settings
    api_instance.delete_conversations_messaging_settings_default()
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_settings_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

void (empty response body)

<a name="delete_conversations_messaging_supportedcontent_supported_content_id"></a>

##  delete_conversations_messaging_supportedcontent_supported_content_id(supported_content_id)



Delete a supported content profile

Wraps DELETE /api/v2/conversations/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
supported_content_id = 'supported_content_id_example' # str | Supported Content ID

try:
    # Delete a supported content profile
    api_instance.delete_conversations_messaging_supportedcontent_supported_content_id(supported_content_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_conversations_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_analytics_conversation_details"></a>

## [**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes.html) get_analytics_conversation_details(conversation_id)



Get a conversation by id

Wraps GET /api/v2/analytics/conversations/{conversationId}/details 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get a conversation by id
    api_response = api_instance.get_analytics_conversation_details(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversation_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationWithoutAttributes**](AnalyticsConversationWithoutAttributes.html)

<a name="get_analytics_conversations_aggregates_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_conversations_aggregates_job(job_id)



Get status for async query for conversation aggregates

get_analytics_conversations_aggregates_job is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/conversations/aggregates/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for conversation aggregates
    api_response = api_instance.get_analytics_conversations_aggregates_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_aggregates_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_conversations_aggregates_job_results"></a>

## [**ConversationAsyncAggregateQueryResponse**](ConversationAsyncAggregateQueryResponse.html) get_analytics_conversations_aggregates_job_results(job_id, cursor=cursor)



Fetch a page of results for an async aggregates query

get_analytics_conversations_aggregates_job_results is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/analytics/conversations/aggregates/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Cursor token to retrieve next page (optional)

try:
    # Fetch a page of results for an async aggregates query
    api_response = api_instance.get_analytics_conversations_aggregates_job_results(job_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_aggregates_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Cursor token to retrieve next page | [optional]  |
{: class="table table-striped"}

### Return type

[**ConversationAsyncAggregateQueryResponse**](ConversationAsyncAggregateQueryResponse.html)

<a name="get_analytics_conversations_details"></a>

## [**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html) get_analytics_conversations_details(id=id)



Gets multiple conversations by id

Wraps GET /api/v2/analytics/conversations/details 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
id = ['id_example'] # list[str] | Comma-separated conversation ids (optional)

try:
    # Gets multiple conversations by id
    api_response = api_instance.get_analytics_conversations_details(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**list[str]**](str.html)| Comma-separated conversation ids | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html)

<a name="get_analytics_conversations_details_job"></a>

## [**AsyncQueryStatus**](AsyncQueryStatus.html) get_analytics_conversations_details_job(job_id)



Get status for async query for conversation details

Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId} 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
job_id = 'job_id_example' # str | jobId

try:
    # Get status for async query for conversation details
    api_response = api_instance.get_analytics_conversations_details_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_details_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryStatus**](AsyncQueryStatus.html)

<a name="get_analytics_conversations_details_job_results"></a>

## [**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse.html) get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)



Fetch a page of results for an async details job

Wraps GET /api/v2/analytics/conversations/details/jobs/{jobId}/results 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
job_id = 'job_id_example' # str | jobId
cursor = 'cursor_example' # str | Indicates where to resume query results (not required for first page) (optional)
page_size = 56 # int | The desired maximum number of results (optional)

try:
    # Fetch a page of results for an async details job
    api_response = api_instance.get_analytics_conversations_details_job_results(job_id, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_details_job_results: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |
| **cursor** | **str**| Indicates where to resume query results (not required for first page) | [optional]  |
| **page_size** | **int**| The desired maximum number of results | [optional]  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationAsyncQueryResponse**](AnalyticsConversationAsyncQueryResponse.html)

<a name="get_analytics_conversations_details_jobs_availability"></a>

## [**DataAvailabilityResponse**](DataAvailabilityResponse.html) get_analytics_conversations_details_jobs_availability()



Lookup the datalake availability date and time

Wraps GET /api/v2/analytics/conversations/details/jobs/availability 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Lookup the datalake availability date and time
    api_response = api_instance.get_analytics_conversations_details_jobs_availability()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_analytics_conversations_details_jobs_availability: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**DataAvailabilityResponse**](DataAvailabilityResponse.html)

<a name="get_conversation"></a>

## [**Conversation**](Conversation.html) get_conversation(conversation_id)



Get conversation

Wraps GET /api/v2/conversations/{conversationId} 

Requires ANY permissions: 

* conversation:communication:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Get conversation
    api_response = api_instance.get_conversation(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="get_conversation_participant_secureivrsession"></a>

## [**SecureSession**](SecureSession.html) get_conversation_participant_secureivrsession(conversation_id, participant_id, secure_session_id)



Fetch info on a secure session

Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions/{secureSessionId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
secure_session_id = 'secure_session_id_example' # str | secure IVR session ID

try:
    # Fetch info on a secure session
    api_response = api_instance.get_conversation_participant_secureivrsession(conversation_id, participant_id, secure_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation_participant_secureivrsession: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **secure_session_id** | **str**| secure IVR session ID |  |
{: class="table table-striped"}

### Return type

[**SecureSession**](SecureSession.html)

<a name="get_conversation_participant_secureivrsessions"></a>

## [**SecureSessionEntityListing**](SecureSessionEntityListing.html) get_conversation_participant_secureivrsessions(conversation_id, participant_id)



Get a list of secure sessions for this participant.

Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Get a list of secure sessions for this participant.
    api_response = api_instance.get_conversation_participant_secureivrsessions(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation_participant_secureivrsessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

[**SecureSessionEntityListing**](SecureSessionEntityListing.html)

<a name="get_conversation_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversation_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversation_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversation_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversation_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversation_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversation_secureattributes"></a>

## [**ConversationSecureAttributes**](ConversationSecureAttributes.html) get_conversation_secureattributes(conversation_id)



Get the secure attributes on a conversation.

Wraps GET /api/v2/conversations/{conversationId}/secureattributes 

Requires ANY permissions: 

* conversation:participant:attributesview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Get the secure attributes on a conversation.
    api_response = api_instance.get_conversation_secureattributes(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation_secureattributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

[**ConversationSecureAttributes**](ConversationSecureAttributes.html)

<a name="get_conversations"></a>

## [**ConversationEntityListing**](ConversationEntityListing.html) get_conversations(communication_type=communication_type)



Get active conversations for the logged in user

Wraps GET /api/v2/conversations 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
communication_type = 'communication_type_example' # str | Call or Chat communication filtering (optional)

try:
    # Get active conversations for the logged in user
    api_response = api_instance.get_conversations(communication_type=communication_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **communication_type** | **str**| Call or Chat communication filtering | [optional]  |
{: class="table table-striped"}

### Return type

[**ConversationEntityListing**](ConversationEntityListing.html)

<a name="get_conversations_call"></a>

## [**CallConversation**](CallConversation.html) get_conversations_call(conversation_id)



Get call conversation

Wraps GET /api/v2/conversations/calls/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get call conversation
    api_response = api_instance.get_conversations_call(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_call: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CallConversation**](CallConversation.html)

<a name="get_conversations_call_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_call_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_call_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_call_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_call_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_call_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_call_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_call_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/calls/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_call_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_call_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_callback"></a>

## [**CallbackConversation**](CallbackConversation.html) get_conversations_callback(conversation_id)



Get callback conversation

Wraps GET /api/v2/conversations/callbacks/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get callback conversation
    api_response = api_instance.get_conversations_callback(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_callback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CallbackConversation**](CallbackConversation.html)

<a name="get_conversations_callback_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_callback_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_callback_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_callback_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_callback_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_callback_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_callback_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_callback_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_callback_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_callback_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_callbacks"></a>

## [**CallbackConversationEntityListing**](CallbackConversationEntityListing.html) get_conversations_callbacks()



Get active callback conversations for the logged in user

Wraps GET /api/v2/conversations/callbacks 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active callback conversations for the logged in user
    api_response = api_instance.get_conversations_callbacks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_callbacks: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**CallbackConversationEntityListing**](CallbackConversationEntityListing.html)

<a name="get_conversations_calls"></a>

## [**CallConversationEntityListing**](CallConversationEntityListing.html) get_conversations_calls()



Get active call conversations for the logged in user

Wraps GET /api/v2/conversations/calls 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active call conversations for the logged in user
    api_response = api_instance.get_conversations_calls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_calls: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**CallConversationEntityListing**](CallConversationEntityListing.html)

<a name="get_conversations_calls_history"></a>

## [**CallHistoryConversationEntityListing**](CallHistoryConversationEntityListing.html) get_conversations_calls_history(page_size=page_size, page_number=page_number, interval=interval, expand=expand)



Get call history

Wraps GET /api/v2/conversations/calls/history 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size, maximum 50 (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
interval = 'interval_example' # str | Interval string; format is ISO-8601. Separate start and end times with forward slash '/' (optional)
expand = ['expand_example'] # list[str] | Which fields, if any, to expand. (optional)

try:
    # Get call history
    api_response = api_instance.get_conversations_calls_history(page_size=page_size, page_number=page_number, interval=interval, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_calls_history: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size, maximum 50 | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **interval** | **str**| Interval string; format is ISO-8601. Separate start and end times with forward slash &#39;/&#39; | [optional]  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand. | [optional] <br />**Values**: externalorganization, externalcontact, user, queue, group |
{: class="table table-striped"}

### Return type

[**CallHistoryConversationEntityListing**](CallHistoryConversationEntityListing.html)

<a name="get_conversations_calls_maximumconferenceparties"></a>

## [**MaxParticipants**](MaxParticipants.html) get_conversations_calls_maximumconferenceparties()



Get the maximum number of participants that this user can have on a conference

Wraps GET /api/v2/conversations/calls/maximumconferenceparties 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get the maximum number of participants that this user can have on a conference
    api_response = api_instance.get_conversations_calls_maximumconferenceparties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_calls_maximumconferenceparties: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**MaxParticipants**](MaxParticipants.html)

<a name="get_conversations_chat"></a>

## [**ChatConversation**](ChatConversation.html) get_conversations_chat(conversation_id)



Get chat conversation

Wraps GET /api/v2/conversations/chats/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get chat conversation
    api_response = api_instance.get_conversations_chat(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**ChatConversation**](ChatConversation.html)

<a name="get_conversations_chat_message"></a>

## [**WebChatMessage**](WebChatMessage.html) get_conversations_chat_message(conversation_id, message_id)



Get a web chat conversation message

The current user must be involved with the conversation to get its messages.

Wraps GET /api/v2/conversations/chats/{conversationId}/messages/{messageId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId

try:
    # Get a web chat conversation message
    api_response = api_instance.get_conversations_chat_message(conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**WebChatMessage**](WebChatMessage.html)

<a name="get_conversations_chat_messages"></a>

## [**WebChatMessageEntityList**](WebChatMessageEntityList.html) get_conversations_chat_messages(conversation_id, after=after, before=before, sort_order=sort_order, max_results=max_results)



Get the messages of a chat conversation.

The current user must be involved with the conversation to get its messages.

Wraps GET /api/v2/conversations/chats/{conversationId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
after = 'after_example' # str | If specified, get the messages chronologically after the id of this message (optional)
before = 'before_example' # str | If specified, get the messages chronologically before the id of this message (optional)
sort_order = ''ascending'' # str | Sort order (optional) (default to 'ascending')
max_results = 100 # int | Limit the returned number of messages, up to a maximum of 100 (optional) (default to 100)

try:
    # Get the messages of a chat conversation.
    api_response = api_instance.get_conversations_chat_messages(conversation_id, after=after, before=before, sort_order=sort_order, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **after** | **str**| If specified, get the messages chronologically after the id of this message | [optional]  |
| **before** | **str**| If specified, get the messages chronologically before the id of this message | [optional]  |
| **sort_order** | **str**| Sort order | [optional] [default to &#39;ascending&#39;]<br />**Values**: ascending, descending |
| **max_results** | **int**| Limit the returned number of messages, up to a maximum of 100 | [optional] [default to 100] |
{: class="table table-striped"}

### Return type

[**WebChatMessageEntityList**](WebChatMessageEntityList.html)

<a name="get_conversations_chat_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_chat_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_chat_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_chat_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_chat_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_chat_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/chats/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_chat_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chat_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_chats"></a>

## [**ChatConversationEntityListing**](ChatConversationEntityListing.html) get_conversations_chats()



Get active chat conversations for the logged in user

Wraps GET /api/v2/conversations/chats 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active chat conversations for the logged in user
    api_response = api_instance.get_conversations_chats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_chats: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ChatConversationEntityListing**](ChatConversationEntityListing.html)

<a name="get_conversations_cobrowsesession"></a>

## [**CobrowseConversation**](CobrowseConversation.html) get_conversations_cobrowsesession(conversation_id)



Get cobrowse conversation

Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get cobrowse conversation
    api_response = api_instance.get_conversations_cobrowsesession(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_cobrowsesession: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**CobrowseConversation**](CobrowseConversation.html)

<a name="get_conversations_cobrowsesession_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the wrap-up for this conversation communication. 

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_cobrowsesession_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_cobrowsesession_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_cobrowsesession_participant_wrapup(conversation_id, participant_id, provisional=provisional)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the wrap-up for this conversation participant. 

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_cobrowsesession_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_cobrowsesession_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_cobrowsesession_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_cobrowsesession_participant_wrapupcodes(conversation_id, participant_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get list of wrapup codes for this conversation participant

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps GET /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_cobrowsesession_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_cobrowsesession_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_cobrowsesessions"></a>

## [**CobrowseConversationEntityListing**](CobrowseConversationEntityListing.html) get_conversations_cobrowsesessions()



Get active cobrowse conversations for the logged in user

Wraps GET /api/v2/conversations/cobrowsesessions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active cobrowse conversations for the logged in user
    api_response = api_instance.get_conversations_cobrowsesessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_cobrowsesessions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**CobrowseConversationEntityListing**](CobrowseConversationEntityListing.html)

<a name="get_conversations_email"></a>

## [**EmailConversation**](EmailConversation.html) get_conversations_email(conversation_id)



Get email conversation

Wraps GET /api/v2/conversations/emails/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get email conversation
    api_response = api_instance.get_conversations_email(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="get_conversations_email_message"></a>

## [**EmailMessage**](EmailMessage.html) get_conversations_email_message(conversation_id, message_id)



Get conversation message

Wraps GET /api/v2/conversations/emails/{conversationId}/messages/{messageId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId

try:
    # Get conversation message
    api_response = api_instance.get_conversations_email_message(conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="get_conversations_email_messages"></a>

## [**EmailMessagePreviewListing**](EmailMessagePreviewListing.html) get_conversations_email_messages(conversation_id)



Get conversation messages

Wraps GET /api/v2/conversations/emails/{conversationId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get conversation messages
    api_response = api_instance.get_conversations_email_messages(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailMessagePreviewListing**](EmailMessagePreviewListing.html)

<a name="get_conversations_email_messages_draft"></a>

## [**EmailMessage**](EmailMessage.html) get_conversations_email_messages_draft(conversation_id)



Get conversation draft reply

Wraps GET /api/v2/conversations/emails/{conversationId}/messages/draft 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get conversation draft reply
    api_response = api_instance.get_conversations_email_messages_draft(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_messages_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="get_conversations_email_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_email_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_email_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_email_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_email_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_email_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/emails/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_email_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_email_settings"></a>

## [**EmailsSettings**](EmailsSettings.html) get_conversations_email_settings(conversation_id)



Get emails settings for a given conversation

Wraps GET /api/v2/conversations/emails/{conversationId}/settings 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get emails settings for a given conversation
    api_response = api_instance.get_conversations_email_settings(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_email_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**EmailsSettings**](EmailsSettings.html)

<a name="get_conversations_emails"></a>

## [**EmailConversationEntityListing**](EmailConversationEntityListing.html) get_conversations_emails()



Get active email conversations for the logged in user

Wraps GET /api/v2/conversations/emails 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active email conversations for the logged in user
    api_response = api_instance.get_conversations_emails()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_emails: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**EmailConversationEntityListing**](EmailConversationEntityListing.html)

<a name="get_conversations_keyconfiguration"></a>

## [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html) get_conversations_keyconfiguration(keyconfigurations_id)



Get the encryption key configurations

Wraps GET /api/v2/conversations/keyconfigurations/{keyconfigurationsId} 

Requires ANY permissions: 

* conversation:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
keyconfigurations_id = 'keyconfigurations_id_example' # str | Key Configurations Id

try:
    # Get the encryption key configurations
    api_response = api_instance.get_conversations_keyconfiguration(keyconfigurations_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_keyconfiguration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **keyconfigurations_id** | **str**| Key Configurations Id |  |
{: class="table table-striped"}

### Return type

[**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)

<a name="get_conversations_keyconfigurations"></a>

## [**ConversationEncryptionConfigurationListing**](ConversationEncryptionConfigurationListing.html) get_conversations_keyconfigurations()



Get a list of key configurations data

Wraps GET /api/v2/conversations/keyconfigurations 

Requires ANY permissions: 

* conversation:encryptionKey:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get a list of key configurations data
    api_response = api_instance.get_conversations_keyconfigurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_keyconfigurations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ConversationEncryptionConfigurationListing**](ConversationEncryptionConfigurationListing.html)

<a name="get_conversations_message"></a>

## [**MessageConversation**](MessageConversation.html) get_conversations_message(conversation_id)



Get message conversation

Wraps GET /api/v2/conversations/messages/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId

try:
    # Get message conversation
    api_response = api_instance.get_conversations_message(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
{: class="table table-striped"}

### Return type

[**MessageConversation**](MessageConversation.html)

<a name="get_conversations_message_communication_messages_media_media_id"></a>

## [**MessageMediaData**](MessageMediaData.html) get_conversations_message_communication_messages_media_media_id(conversation_id, communication_id, media_id)



Get media

See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

Wraps GET /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media/{mediaId} 

Requires ANY permissions: 

* conversation:message:view
* conversation:webmessaging:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
media_id = 'media_id_example' # str | mediaId

try:
    # Get media
    api_response = api_instance.get_conversations_message_communication_messages_media_media_id(conversation_id, communication_id, media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_communication_messages_media_media_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **media_id** | **str**| mediaId |  |
{: class="table table-striped"}

### Return type

[**MessageMediaData**](MessageMediaData.html)

<a name="get_conversations_message_details"></a>

## [**MessageData**](MessageData.html) get_conversations_message_details(message_id, use_normalized_message=use_normalized_message)



Get message

Wraps GET /api/v2/conversations/messages/{messageId}/details 

Requires ANY permissions: 

* conversation:message:view
* conversation:webmessaging:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
message_id = 'message_id_example' # str | messageId
use_normalized_message = False # bool | If true, response removes deprecated fields (textBody, media, stickers) (optional) (default to False)

try:
    # Get message
    api_response = api_instance.get_conversations_message_details(message_id, use_normalized_message=use_normalized_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_id** | **str**| messageId |  |
| **use_normalized_message** | **bool**| If true, response removes deprecated fields (textBody, media, stickers) | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**MessageData**](MessageData.html)

<a name="get_conversations_message_message"></a>

## [**MessageData**](MessageData.html) get_conversations_message_message(conversation_id, message_id, use_normalized_message=use_normalized_message)



Get conversation message

Wraps GET /api/v2/conversations/messages/{conversationId}/messages/{messageId} 

Requires ANY permissions: 

* conversation:message:view
* conversation:webmessaging:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
message_id = 'message_id_example' # str | messageId
use_normalized_message = False # bool | If true, response removes deprecated fields (textBody, media, stickers) (optional) (default to False)

try:
    # Get conversation message
    api_response = api_instance.get_conversations_message_message(conversation_id, message_id, use_normalized_message=use_normalized_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **message_id** | **str**| messageId |  |
| **use_normalized_message** | **bool**| If true, response removes deprecated fields (textBody, media, stickers) | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**MessageData**](MessageData.html)

<a name="get_conversations_message_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_message_participant_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_message_participant_wrapup(conversation_id, participant_id, provisional=provisional)



Get the wrap-up for this conversation participant. 

Wraps GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation participant. 
    api_response = api_instance.get_conversations_message_participant_wrapup(conversation_id, participant_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_participant_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_message_participant_wrapupcodes"></a>

## [**list[WrapupCode]**](WrapupCode.html) get_conversations_message_participant_wrapupcodes(conversation_id, participant_id)



Get list of wrapup codes for this conversation participant

Wraps GET /api/v2/conversations/messages/{conversationId}/participants/{participantId}/wrapupcodes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Get list of wrapup codes for this conversation participant
    api_response = api_instance.get_conversations_message_participant_wrapupcodes(conversation_id, participant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_message_participant_wrapupcodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

[**list[WrapupCode]**](WrapupCode.html)

<a name="get_conversations_messages"></a>

## [**MessageConversationEntityListing**](MessageConversationEntityListing.html) get_conversations_messages()



Get active message conversations for the logged in user

Wraps GET /api/v2/conversations/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get active message conversations for the logged in user
    api_response = api_instance.get_conversations_messages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messages: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**MessageConversationEntityListing**](MessageConversationEntityListing.html)

<a name="get_conversations_messages_cachedmedia"></a>

## [**CachedMediaItemEntityListing**](CachedMediaItemEntityListing.html) get_conversations_messages_cachedmedia(page_size=page_size, page_number=page_number, url=url)



Get a list of cached media items

Wraps GET /api/v2/conversations/messages/cachedmedia 

Requires ANY permissions: 

* conversation:cachedMedia:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
url = 'url_example' # str | URL to search for (optional)

try:
    # Get a list of cached media items
    api_response = api_instance.get_conversations_messages_cachedmedia(page_size=page_size, page_number=page_number, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messages_cachedmedia: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **url** | **str**| URL to search for | [optional]  |
{: class="table table-striped"}

### Return type

[**CachedMediaItemEntityListing**](CachedMediaItemEntityListing.html)

<a name="get_conversations_messages_cachedmedia_cached_media_item_id"></a>

## [**CachedMediaItem**](CachedMediaItem.html) get_conversations_messages_cachedmedia_cached_media_item_id(cached_media_item_id)



Get a cached media item

Wraps GET /api/v2/conversations/messages/cachedmedia/{cachedMediaItemId} 

Requires ANY permissions: 

* conversation:cachedMedia:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
cached_media_item_id = 'cached_media_item_id_example' # str | cachedMediaItemId

try:
    # Get a cached media item
    api_response = api_instance.get_conversations_messages_cachedmedia_cached_media_item_id(cached_media_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messages_cachedmedia_cached_media_item_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cached_media_item_id** | **str**| cachedMediaItemId |  |
{: class="table table-striped"}

### Return type

[**CachedMediaItem**](CachedMediaItem.html)

<a name="get_conversations_messaging_facebook_app"></a>

## [**FacebookAppCredentials**](FacebookAppCredentials.html) get_conversations_messaging_facebook_app()



Get Genesys Facebook App Id

Wraps GET /api/v2/conversations/messaging/facebook/app 

Requires ALL permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get Genesys Facebook App Id
    api_response = api_instance.get_conversations_messaging_facebook_app()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_facebook_app: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**FacebookAppCredentials**](FacebookAppCredentials.html)

<a name="get_conversations_messaging_facebook_permissions"></a>

## [**FacebookPermissionEntityListing**](FacebookPermissionEntityListing.html) get_conversations_messaging_facebook_permissions()



Get a list of Facebook Permissions

Wraps GET /api/v2/conversations/messaging/facebook/permissions 

Requires ANY permissions: 

* messaging:integration:add
* messaging:integration:edit
* messaging:conversationInstagramIntegration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get a list of Facebook Permissions
    api_response = api_instance.get_conversations_messaging_facebook_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_facebook_permissions: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**FacebookPermissionEntityListing**](FacebookPermissionEntityListing.html)

<a name="get_conversations_messaging_integrations"></a>

## [**MessagingIntegrationEntityListing**](MessagingIntegrationEntityListing.html) get_conversations_messaging_integrations(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)



Get a list of Integrations

Wraps GET /api/v2/conversations/messaging/integrations 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = ['expand_example'] # list[str] | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of Integrations
    api_response = api_instance.get_conversations_messaging_integrations(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | [**list[str]**](str.html)| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**MessagingIntegrationEntityListing**](MessagingIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_facebook"></a>

## [**FacebookIntegrationEntityListing**](FacebookIntegrationEntityListing.html) get_conversations_messaging_integrations_facebook(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)



Get a list of Facebook Integrations

Wraps GET /api/v2/conversations/messaging/integrations/facebook 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of Facebook Integrations
    api_response = api_instance.get_conversations_messaging_integrations_facebook(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_facebook: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**FacebookIntegrationEntityListing**](FacebookIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_facebook_integration_id"></a>

## [**FacebookIntegration**](FacebookIntegration.html) get_conversations_messaging_integrations_facebook_integration_id(integration_id, expand=expand)



Get a Facebook messaging integration

Wraps GET /api/v2/conversations/messaging/integrations/facebook/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get a Facebook messaging integration
    api_response = api_instance.get_conversations_messaging_integrations_facebook_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_facebook_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**FacebookIntegration**](FacebookIntegration.html)

<a name="get_conversations_messaging_integrations_instagram"></a>

## [**InstagramIntegrationEntityListing**](InstagramIntegrationEntityListing.html) get_conversations_messaging_integrations_instagram(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)



Get a list of Instagram Integrations

Wraps GET /api/v2/conversations/messaging/integrations/instagram 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of Instagram Integrations
    api_response = api_instance.get_conversations_messaging_integrations_instagram(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_instagram: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**InstagramIntegrationEntityListing**](InstagramIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_instagram_integration_id"></a>

## [**InstagramIntegration**](InstagramIntegration.html) get_conversations_messaging_integrations_instagram_integration_id(integration_id, expand=expand)



Get Instagram messaging integration

Wraps GET /api/v2/conversations/messaging/integrations/instagram/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get Instagram messaging integration
    api_response = api_instance.get_conversations_messaging_integrations_instagram_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_instagram_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**InstagramIntegration**](InstagramIntegration.html)

<a name="get_conversations_messaging_integrations_line"></a>

## [**LineIntegrationEntityListing**](LineIntegrationEntityListing.html) get_conversations_messaging_integrations_line(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a list of LINE messenger Integrations (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps GET /api/v2/conversations/messaging/integrations/line 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of LINE messenger Integrations (Deprecated)
    api_response = api_instance.get_conversations_messaging_integrations_line(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_line: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**LineIntegrationEntityListing**](LineIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_line_integration_id"></a>

## [**LineIntegration**](LineIntegration.html) get_conversations_messaging_integrations_line_integration_id(integration_id, expand=expand)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a LINE messenger integration (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps GET /api/v2/conversations/messaging/integrations/line/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get a LINE messenger integration (Deprecated)
    api_response = api_instance.get_conversations_messaging_integrations_line_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_line_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)

<a name="get_conversations_messaging_integrations_open"></a>

## [**OpenIntegrationEntityListing**](OpenIntegrationEntityListing.html) get_conversations_messaging_integrations_open(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)



Get a list of Open messaging integrations

See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

Wraps GET /api/v2/conversations/messaging/integrations/open 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of Open messaging integrations
    api_response = api_instance.get_conversations_messaging_integrations_open(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_open: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**OpenIntegrationEntityListing**](OpenIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_open_integration_id"></a>

## [**OpenIntegration**](OpenIntegration.html) get_conversations_messaging_integrations_open_integration_id(integration_id, expand=expand)



Get an Open messaging integration

See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

Wraps GET /api/v2/conversations/messaging/integrations/open/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get an Open messaging integration
    api_response = api_instance.get_conversations_messaging_integrations_open_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_open_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**OpenIntegration**](OpenIntegration.html)

<a name="get_conversations_messaging_integrations_twitter"></a>

## [**TwitterIntegrationEntityListing**](TwitterIntegrationEntityListing.html) get_conversations_messaging_integrations_twitter(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a list of Twitter Integrations (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-x-formerly-twitter-third-party-messaging-channel/

Wraps GET /api/v2/conversations/messaging/integrations/twitter 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of Twitter Integrations (Deprecated)
    api_response = api_instance.get_conversations_messaging_integrations_twitter(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_twitter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**TwitterIntegrationEntityListing**](TwitterIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_twitter_integration_id"></a>

## [**TwitterIntegration**](TwitterIntegration.html) get_conversations_messaging_integrations_twitter_integration_id(integration_id, expand=expand)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a Twitter messaging integration (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-x-formerly-twitter-third-party-messaging-channel/

Wraps GET /api/v2/conversations/messaging/integrations/twitter/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get a Twitter messaging integration (Deprecated)
    api_response = api_instance.get_conversations_messaging_integrations_twitter_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_twitter_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**TwitterIntegration**](TwitterIntegration.html)

<a name="get_conversations_messaging_integrations_whatsapp"></a>

## [**WhatsAppIntegrationEntityListing**](WhatsAppIntegrationEntityListing.html) get_conversations_messaging_integrations_whatsapp(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)



Get a list of WhatsApp Integrations

Wraps GET /api/v2/conversations/messaging/integrations/whatsapp 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
expand = 'expand_example' # str | Expand instructions for the return value. (optional)
supported_content_id = 'supported_content_id_example' # str | Filter integrations returned based on the supported content ID (optional)
messaging_setting_id = 'messaging_setting_id_example' # str | Filter integrations returned based on the setting ID (optional)

try:
    # Get a list of WhatsApp Integrations
    api_response = api_instance.get_conversations_messaging_integrations_whatsapp(page_size=page_size, page_number=page_number, expand=expand, supported_content_id=supported_content_id, messaging_setting_id=messaging_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_whatsapp: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
| **supported_content_id** | **str**| Filter integrations returned based on the supported content ID | [optional]  |
| **messaging_setting_id** | **str**| Filter integrations returned based on the setting ID | [optional]  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegrationEntityListing**](WhatsAppIntegrationEntityListing.html)

<a name="get_conversations_messaging_integrations_whatsapp_integration_id"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) get_conversations_messaging_integrations_whatsapp_integration_id(integration_id, expand=expand)



Get a WhatsApp messaging integration

Wraps GET /api/v2/conversations/messaging/integrations/whatsapp/{integrationId} 

Requires ALL permissions: 

* messaging:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
expand = 'expand_example' # str | Expand instructions for the return value. (optional)

try:
    # Get a WhatsApp messaging integration
    api_response = api_instance.get_conversations_messaging_integrations_whatsapp_integration_id(integration_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_integrations_whatsapp_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **expand** | **str**| Expand instructions for the return value. | [optional] <br />**Values**: supportedContent, messagingSetting |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="get_conversations_messaging_setting"></a>

## [**MessagingSetting**](MessagingSetting.html) get_conversations_messaging_setting(message_setting_id)



Get a messaging setting

Wraps GET /api/v2/conversations/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
message_setting_id = 'message_setting_id_example' # str | Message Setting ID

try:
    # Get a messaging setting
    api_response = api_instance.get_conversations_messaging_setting(message_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Setting ID |  |
{: class="table table-striped"}

### Return type

[**MessagingSetting**](MessagingSetting.html)

<a name="get_conversations_messaging_settings"></a>

## [**MessagingConfigListing**](MessagingConfigListing.html) get_conversations_messaging_settings(page_size=page_size, page_number=page_number)



Get a list of messaging settings

Wraps GET /api/v2/conversations/messaging/settings 

Requires ALL permissions: 

* messaging:setting:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of messaging settings
    api_response = api_instance.get_conversations_messaging_settings(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**MessagingConfigListing**](MessagingConfigListing.html)

<a name="get_conversations_messaging_settings_default"></a>

## [**MessagingSetting**](MessagingSetting.html) get_conversations_messaging_settings_default()



Get the organization's default settings that will be used as the default when creating an integration.

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be assigned to it.

Wraps GET /api/v2/conversations/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get the organization's default settings that will be used as the default when creating an integration.
    api_response = api_instance.get_conversations_messaging_settings_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_settings_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**MessagingSetting**](MessagingSetting.html)

<a name="get_conversations_messaging_sticker"></a>

## [**MessagingStickerEntityListing**](MessagingStickerEntityListing.html) get_conversations_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get a list of Messaging Stickers (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps GET /api/v2/conversations/messaging/stickers/{messengerType} 

Requires ALL permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
messenger_type = 'messenger_type_example' # str | Messenger Type
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Messaging Stickers (Deprecated)
    api_response = api_instance.get_conversations_messaging_sticker(messenger_type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_sticker: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **messenger_type** | **str**| Messenger Type | <br />**Values**: line |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**MessagingStickerEntityListing**](MessagingStickerEntityListing.html)

<a name="get_conversations_messaging_supportedcontent"></a>

## [**SupportedContentListing**](SupportedContentListing.html) get_conversations_messaging_supportedcontent(page_size=page_size, page_number=page_number)



Get a list of Supported Content profiles

Wraps GET /api/v2/conversations/messaging/supportedcontent 

Requires ALL permissions: 

* messaging:supportedContent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Get a list of Supported Content profiles
    api_response = api_instance.get_conversations_messaging_supportedcontent(page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_supportedcontent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **page_number** | **int**| Page number | [optional] [default to 1] |
{: class="table table-striped"}

### Return type

[**SupportedContentListing**](SupportedContentListing.html)

<a name="get_conversations_messaging_supportedcontent_default"></a>

## [**SupportedContent**](SupportedContent.html) get_conversations_messaging_supportedcontent_default()



Get the organization's default supported content profile that will be used as the default when creating an integration.

When an integration is created a supported content ID may be assigned to it. If the supported content ID is not supplied, the default supported content profile will be assigned to it.

Wraps GET /api/v2/conversations/messaging/supportedcontent/default 

Requires ALL permissions: 

* messaging:supportedContent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get the organization's default supported content profile that will be used as the default when creating an integration.
    api_response = api_instance.get_conversations_messaging_supportedcontent_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_supportedcontent_default: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**SupportedContent**](SupportedContent.html)

<a name="get_conversations_messaging_supportedcontent_supported_content_id"></a>

## [**SupportedContent**](SupportedContent.html) get_conversations_messaging_supportedcontent_supported_content_id(supported_content_id)



Get a supported content profile

Wraps GET /api/v2/conversations/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
supported_content_id = 'supported_content_id_example' # str | Supported Content ID

try:
    # Get a supported content profile
    api_response = api_instance.get_conversations_messaging_supportedcontent_supported_content_id(supported_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="get_conversations_messaging_threadingtimeline"></a>

## [**ConversationThreadingWindow**](ConversationThreadingWindow.html) get_conversations_messaging_threadingtimeline()



Get conversation threading window timeline for each messaging type

Conversation messaging threading timeline is a setting defined for each messenger type in your organization. This setting will dictate whether a new message is added to the most recent existing conversation, or creates a new Conversation. If the existing Conversation is still in a connected state the threading timeline setting will never play a role. After the conversation is disconnected, if an inbound message is received or an outbound message is sent after the setting for threading timeline expires, a new conversation is created.

Wraps GET /api/v2/conversations/messaging/threadingtimeline 

Requires ALL permissions: 

* conversation:threadingTimeline:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get conversation threading window timeline for each messaging type
    api_response = api_instance.get_conversations_messaging_threadingtimeline()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_messaging_threadingtimeline: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**ConversationThreadingWindow**](ConversationThreadingWindow.html)

<a name="get_conversations_screenshare_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Get the wrap-up for this conversation communication. 

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps GET /api/v2/conversations/screenshares/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_screenshare_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_settings"></a>

## [**Settings**](Settings.html) get_conversations_settings()



Get Settings

Wraps GET /api/v2/conversations/settings 

Requires ANY permissions: 

* conversation:settings:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()

try:
    # Get Settings
    api_response = api_instance.get_conversations_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.


### Return type

[**Settings**](Settings.html)

<a name="get_conversations_social_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/socials/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_social_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_video_details"></a>

## [**VideoConferenceDetails**](VideoConferenceDetails.html) get_conversations_video_details(conference_id)



Get video conference details (e.g. the current number of active participants).

get_conversations_video_details is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/conversations/videos/{conferenceId}/details 

Requires ANY permissions: 

* video:video:access

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conference_id = 'conference_id_example' # str | conferenceId

try:
    # Get video conference details (e.g. the current number of active participants).
    api_response = api_instance.get_conversations_video_details(conference_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_video_details: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conference_id** | **str**| conferenceId |  |
{: class="table table-striped"}

### Return type

[**VideoConferenceDetails**](VideoConferenceDetails.html)

<a name="get_conversations_video_participant_communication_wrapup"></a>

## [**AssignedWrapupCode**](AssignedWrapupCode.html) get_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)



Get the wrap-up for this conversation communication. 

Wraps GET /api/v2/conversations/videos/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
provisional = False # bool | Indicates if the wrap-up code is provisional. (optional) (default to False)

try:
    # Get the wrap-up for this conversation communication. 
    api_response = api_instance.get_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, provisional=provisional)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_video_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **provisional** | **bool**| Indicates if the wrap-up code is provisional. | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**AssignedWrapupCode**](AssignedWrapupCode.html)

<a name="get_conversations_videos_meeting"></a>

## [**MeetingIdRecord**](MeetingIdRecord.html) get_conversations_videos_meeting(meeting_id)



Gets a record for a given meetingId

get_conversations_videos_meeting is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/conversations/videos/meetings/{meetingId} 

Requires ANY permissions: 

* video:video:access

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
meeting_id = 'meeting_id_example' # str | meetingId

try:
    # Gets a record for a given meetingId
    api_response = api_instance.get_conversations_videos_meeting(meeting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_conversations_videos_meeting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **meeting_id** | **str**| meetingId |  |
{: class="table table-striped"}

### Return type

[**MeetingIdRecord**](MeetingIdRecord.html)

<a name="patch_conversation_participant"></a>

##  patch_conversation_participant(conversation_id, participant_id, body)



Update a participant.

Update conversation participant.

Wraps PATCH /api/v2/conversations/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update a participant.
    api_instance.patch_conversation_participant(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversation_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversation_participant_attributes"></a>

##  patch_conversation_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_instance.patch_conversation_participant_attributes(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversation_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversation_secureattributes"></a>

## str** patch_conversation_secureattributes(conversation_id, body)



Update the secure attributes on a conversation.

Wraps PATCH /api/v2/conversations/{conversationId}/secureattributes 

Requires ANY permissions: 

* conversation:participant:attributesedit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
body = PureCloudPlatformClientV2.ConversationSecureAttributes() # ConversationSecureAttributes | Conversation Secure Attributes

try:
    # Update the secure attributes on a conversation.
    api_response = api_instance.patch_conversation_secureattributes(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversation_secureattributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **body** | [**ConversationSecureAttributes**](ConversationSecureAttributes.html)| Conversation Secure Attributes |  |
{: class="table table-striped"}

### Return type

**str**

<a name="patch_conversation_utilizationlabel"></a>

## str** patch_conversation_utilizationlabel(conversation_id, body)



Update the utilization label on a conversation. When there is no value provided, the system default label is applied

patch_conversation_utilizationlabel is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps PATCH /api/v2/conversations/{conversationId}/utilizationlabel 

Requires ANY permissions: 

* conversation:utilizationLabel:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
body = PureCloudPlatformClientV2.ConversationUtilizationLabelUpdate() # ConversationUtilizationLabelUpdate | Conversation Utilization Label

try:
    # Update the utilization label on a conversation. When there is no value provided, the system default label is applied
    api_response = api_instance.patch_conversation_utilizationlabel(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversation_utilizationlabel: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **body** | [**ConversationUtilizationLabelUpdate**](ConversationUtilizationLabelUpdate.html)| Conversation Utilization Label |  |
{: class="table table-striped"}

### Return type

**str**

<a name="patch_conversations_aftercallwork_conversation_id_participant_communication"></a>

## [**AfterCallWorkUpdate**](AfterCallWorkUpdate.html) patch_conversations_aftercallwork_conversation_id_participant_communication(conversation_id, participant_id, communication_id, body)



Update after-call work for this conversation communication.

Wraps PATCH /api/v2/conversations/aftercallwork/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.AfterCallWorkUpdate() # AfterCallWorkUpdate | AfterCallWorkUpdate

try:
    # Update after-call work for this conversation communication.
    api_response = api_instance.patch_conversations_aftercallwork_conversation_id_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_aftercallwork_conversation_id_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**AfterCallWorkUpdate**](AfterCallWorkUpdate.html)| AfterCallWorkUpdate |  |
{: class="table table-striped"}

### Return type

[**AfterCallWorkUpdate**](AfterCallWorkUpdate.html)

<a name="patch_conversations_call"></a>

## [**Conversation**](Conversation.html) patch_conversations_call(conversation_id, body)



Update a conversation by setting its recording state, merging in other conversations to create a conference, or disconnecting all of the participants

Wraps PATCH /api/v2/conversations/calls/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by setting its recording state, merging in other conversations to create a conference, or disconnecting all of the participants
    api_response = api_instance.patch_conversations_call(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_call: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_call_participant"></a>

##  patch_conversations_call_participant(conversation_id, participant_id, body)



Update conversation participant

Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant request

try:
    # Update conversation participant
    api_instance.patch_conversations_call_participant(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_call_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_call_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_call_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_call_participant_attributes(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_call_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_call_participant_communication"></a>

## object** patch_conversations_call_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.

Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_call_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_call_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_call_participant_consult"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) patch_conversations_call_participant_consult(conversation_id, participant_id, body)



Change who can speak

Wraps PATCH /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransferUpdate() # ConsultTransferUpdate | new speak to

try:
    # Change who can speak
    api_response = api_instance.patch_conversations_call_participant_consult(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_call_participant_consult: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransferUpdate**](ConsultTransferUpdate.html)| new speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="patch_conversations_callback"></a>

## [**Conversation**](Conversation.html) patch_conversations_callback(conversation_id, body)



Update a conversation by disconnecting all of the participants

Wraps PATCH /api/v2/conversations/callbacks/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_callback(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_callback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_callback_participant"></a>

##  patch_conversations_callback_participant(conversation_id, participant_id, body)



Update conversation participant

Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant
    api_instance.patch_conversations_callback_participant(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_callback_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_callback_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_callback_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Attributes

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_callback_participant_attributes(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_callback_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Attributes |  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_callback_participant_communication"></a>

## object** patch_conversations_callback_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.

Wraps PATCH /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_callback_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_callback_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_callbacks"></a>

## [**PatchCallbackResponse**](PatchCallbackResponse.html) patch_conversations_callbacks(body)



Update a scheduled callback

Wraps PATCH /api/v2/conversations/callbacks 

Requires ANY permissions: 

* conversation:callback:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.PatchCallbackRequest() # PatchCallbackRequest | PatchCallbackRequest

try:
    # Update a scheduled callback
    api_response = api_instance.patch_conversations_callbacks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_callbacks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**PatchCallbackRequest**](PatchCallbackRequest.html)| PatchCallbackRequest |  |
{: class="table table-striped"}

### Return type

[**PatchCallbackResponse**](PatchCallbackResponse.html)

<a name="patch_conversations_chat"></a>

## [**Conversation**](Conversation.html) patch_conversations_chat(conversation_id, body)



Update a conversation by disconnecting all of the participants

Wraps PATCH /api/v2/conversations/chats/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_chat(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_chat: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_chat_participant"></a>

##  patch_conversations_chat_participant(conversation_id, participant_id, body)



Update conversation participant

Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update conversation participant
    api_instance.patch_conversations_chat_participant(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_chat_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_chat_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_chat_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_chat_participant_attributes(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_chat_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_chat_participant_communication"></a>

## object** patch_conversations_chat_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.

Wraps PATCH /api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_chat_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_chat_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_cobrowsesession"></a>

## [**Conversation**](Conversation.html) patch_conversations_cobrowsesession(conversation_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a conversation by disconnecting all of the participants

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_cobrowsesession(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_cobrowsesession: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_cobrowsesession_participant"></a>

##  patch_conversations_cobrowsesession_participant(conversation_id, participant_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update conversation participant

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest |  (optional)

try:
    # Update conversation participant
    api_instance.patch_conversations_cobrowsesession_participant(conversation_id, participant_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_cobrowsesession_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_cobrowsesession_participant_attributes(conversation_id, participant_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update the attributes on a conversation participant.

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes |  (optional)

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_cobrowsesession_participant_attributes(conversation_id, participant_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_cobrowsesession_participant_communication"></a>

## object** patch_conversations_cobrowsesession_participant_communication(conversation_id, participant_id, communication_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update conversation participant's communication by disconnecting it.

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps PATCH /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_cobrowsesession_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_cobrowsesession_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_email"></a>

## [**Conversation**](Conversation.html) patch_conversations_email(conversation_id, body)



Update a conversation by disconnecting all of the participants

Wraps PATCH /api/v2/conversations/emails/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_email(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_email: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_email_messages_draft"></a>

## [**EmailMessage**](EmailMessage.html) patch_conversations_email_messages_draft(conversation_id, auto_fill=auto_fill, discard=discard, body=body)



Reset conversation draft to its initial state and/or auto-fill draft content

Wraps PATCH /api/v2/conversations/emails/{conversationId}/messages/draft 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
auto_fill = True # bool | autoFill (optional)
discard = True # bool | discard (optional)
body = PureCloudPlatformClientV2.DraftManipulationRequest() # DraftManipulationRequest | Draft Manipulation Request (optional)

try:
    # Reset conversation draft to its initial state and/or auto-fill draft content
    api_response = api_instance.patch_conversations_email_messages_draft(conversation_id, auto_fill=auto_fill, discard=discard, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_email_messages_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **auto_fill** | **bool**| autoFill | [optional]  |
| **discard** | **bool**| discard | [optional]  |
| **body** | [**DraftManipulationRequest**](DraftManipulationRequest.html)| Draft Manipulation Request | [optional]  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="patch_conversations_email_participant"></a>

##  patch_conversations_email_participant(conversation_id, participant_id, body)



Update conversation participant

Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Update request

try:
    # Update conversation participant
    api_instance.patch_conversations_email_participant(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_email_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Update request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_email_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_email_participant_attributes(conversation_id, participant_id, body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes | Participant attributes

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_email_participant_attributes(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_email_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)| Participant attributes |  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_email_participant_communication"></a>

## object** patch_conversations_email_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.

Wraps PATCH /api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_email_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_email_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_message"></a>

## [**Conversation**](Conversation.html) patch_conversations_message(conversation_id, body)



Update a conversation by disconnecting all of the participants

Wraps PATCH /api/v2/conversations/messages/{conversationId} 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Update a conversation by disconnecting all of the participants
    api_response = api_instance.patch_conversations_message(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="patch_conversations_message_participant"></a>

##  patch_conversations_message_participant(conversation_id, participant_id, body=body)



Update conversation participant

Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId} 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest |  (optional)

try:
    # Update conversation participant
    api_instance.patch_conversations_message_participant(conversation_id, participant_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_message_participant: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="patch_conversations_message_participant_attributes"></a>

## [**ParticipantAttributes**](ParticipantAttributes.html) patch_conversations_message_participant_attributes(conversation_id, participant_id, body=body)



Update the attributes on a conversation participant.

Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/attributes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ParticipantAttributes() # ParticipantAttributes |  (optional)

try:
    # Update the attributes on a conversation participant.
    api_response = api_instance.patch_conversations_message_participant_attributes(conversation_id, participant_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_message_participant_attributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ParticipantAttributes**](ParticipantAttributes.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**ParticipantAttributes**](ParticipantAttributes.html)

<a name="patch_conversations_message_participant_communication"></a>

## object** patch_conversations_message_participant_communication(conversation_id, participant_id, communication_id, body)



Update conversation participant's communication by disconnecting it.

Wraps PATCH /api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MediaParticipantRequest() # MediaParticipantRequest | Participant

try:
    # Update conversation participant's communication by disconnecting it.
    api_response = api_instance.patch_conversations_message_participant_communication(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_message_participant_communication: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MediaParticipantRequest**](MediaParticipantRequest.html)| Participant |  |
{: class="table table-striped"}

### Return type

**object**

<a name="patch_conversations_messaging_integrations_facebook_integration_id"></a>

## [**FacebookIntegration**](FacebookIntegration.html) patch_conversations_messaging_integrations_facebook_integration_id(integration_id, body)



Update Facebook messaging integration

Wraps PATCH /api/v2/conversations/messaging/integrations/facebook/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.FacebookIntegrationUpdateRequest() # FacebookIntegrationUpdateRequest | FacebookIntegrationUpdateRequest

try:
    # Update Facebook messaging integration
    api_response = api_instance.patch_conversations_messaging_integrations_facebook_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_facebook_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**FacebookIntegrationUpdateRequest**](FacebookIntegrationUpdateRequest.html)| FacebookIntegrationUpdateRequest |  |
{: class="table table-striped"}

### Return type

[**FacebookIntegration**](FacebookIntegration.html)

<a name="patch_conversations_messaging_integrations_instagram_integration_id"></a>

## [**InstagramIntegration**](InstagramIntegration.html) patch_conversations_messaging_integrations_instagram_integration_id(integration_id, body)



Update Instagram messaging integration

Wraps PATCH /api/v2/conversations/messaging/integrations/instagram/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.InstagramIntegrationUpdateRequest() # InstagramIntegrationUpdateRequest | InstagramIntegrationUpdateRequest

try:
    # Update Instagram messaging integration
    api_response = api_instance.patch_conversations_messaging_integrations_instagram_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_instagram_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**InstagramIntegrationUpdateRequest**](InstagramIntegrationUpdateRequest.html)| InstagramIntegrationUpdateRequest |  |
{: class="table table-striped"}

### Return type

[**InstagramIntegration**](InstagramIntegration.html)

<a name="patch_conversations_messaging_integrations_open_integration_id"></a>

## [**OpenIntegration**](OpenIntegration.html) patch_conversations_messaging_integrations_open_integration_id(integration_id, body)



Update an Open messaging integration

See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

Wraps PATCH /api/v2/conversations/messaging/integrations/open/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.OpenIntegrationUpdateRequest() # OpenIntegrationUpdateRequest | OpenIntegrationUpdateRequest

try:
    # Update an Open messaging integration
    api_response = api_instance.patch_conversations_messaging_integrations_open_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_open_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**OpenIntegrationUpdateRequest**](OpenIntegrationUpdateRequest.html)| OpenIntegrationUpdateRequest |  |
{: class="table table-striped"}

### Return type

[**OpenIntegration**](OpenIntegration.html)

<a name="patch_conversations_messaging_integrations_twitter_integration_id"></a>

## [**TwitterIntegration**](TwitterIntegration.html) patch_conversations_messaging_integrations_twitter_integration_id(integration_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update Twitter messaging integration

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-x-formerly-twitter-third-party-messaging-channel/

Wraps PATCH /api/v2/conversations/messaging/integrations/twitter/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.TwitterIntegrationRequest() # TwitterIntegrationRequest | TwitterIntegrationRequest

try:
    # Update Twitter messaging integration
    api_response = api_instance.patch_conversations_messaging_integrations_twitter_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_twitter_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**TwitterIntegrationRequest**](TwitterIntegrationRequest.html)| TwitterIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**TwitterIntegration**](TwitterIntegration.html)

<a name="patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id(integration_id, body)



Activate a WhatsApp messaging integration created using the WhatsApp embedded signup flow

Please specify the phone number to associate with this WhatsApp integration from the list of available phone numbers returned to you in the POST call to create the integration. You can then run a GET on the integration to check if its status has been updated to Active

Wraps PATCH /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.WhatsAppEmbeddedSignupIntegrationActivationRequest() # WhatsAppEmbeddedSignupIntegrationActivationRequest | WhatsAppEmbeddedSignupIntegrationActivationRequest

try:
    # Activate a WhatsApp messaging integration created using the WhatsApp embedded signup flow
    api_response = api_instance.patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_whatsapp_embeddedsignup_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**WhatsAppEmbeddedSignupIntegrationActivationRequest**](WhatsAppEmbeddedSignupIntegrationActivationRequest.html)| WhatsAppEmbeddedSignupIntegrationActivationRequest |  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="patch_conversations_messaging_integrations_whatsapp_integration_id"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) patch_conversations_messaging_integrations_whatsapp_integration_id(integration_id, body)



Update a WhatsApp messaging integration

Wraps PATCH /api/v2/conversations/messaging/integrations/whatsapp/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.WhatsAppIntegrationUpdateRequest() # WhatsAppIntegrationUpdateRequest | WhatsAppIntegrationUpdateRequest

try:
    # Update a WhatsApp messaging integration
    api_response = api_instance.patch_conversations_messaging_integrations_whatsapp_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_integrations_whatsapp_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**WhatsAppIntegrationUpdateRequest**](WhatsAppIntegrationUpdateRequest.html)| WhatsAppIntegrationUpdateRequest |  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="patch_conversations_messaging_setting"></a>

## [**MessagingSetting**](MessagingSetting.html) patch_conversations_messaging_setting(message_setting_id, body)



Update a messaging setting

Wraps PATCH /api/v2/conversations/messaging/settings/{messageSettingId} 

Requires ALL permissions: 

* messaging:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
message_setting_id = 'message_setting_id_example' # str | Message Setting ID
body = PureCloudPlatformClientV2.MessagingSettingPatchRequest() # MessagingSettingPatchRequest | MessagingSetting

try:
    # Update a messaging setting
    api_response = api_instance.patch_conversations_messaging_setting(message_setting_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_setting: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **message_setting_id** | **str**| Message Setting ID |  |
| **body** | [**MessagingSettingPatchRequest**](MessagingSettingPatchRequest.html)| MessagingSetting |  |
{: class="table table-striped"}

### Return type

[**MessagingSetting**](MessagingSetting.html)

<a name="patch_conversations_messaging_supportedcontent_supported_content_id"></a>

## [**SupportedContent**](SupportedContent.html) patch_conversations_messaging_supportedcontent_supported_content_id(supported_content_id, body)



Update a supported content profile

Wraps PATCH /api/v2/conversations/messaging/supportedcontent/{supportedContentId} 

Requires ALL permissions: 

* messaging:supportedContent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
supported_content_id = 'supported_content_id_example' # str | Supported Content ID
body = PureCloudPlatformClientV2.SupportedContent() # SupportedContent | SupportedContent

try:
    # Update a supported content profile
    api_response = api_instance.patch_conversations_messaging_supportedcontent_supported_content_id(supported_content_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_messaging_supportedcontent_supported_content_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supported_content_id** | **str**| Supported Content ID |  |
| **body** | [**SupportedContent**](SupportedContent.html)| SupportedContent |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="patch_conversations_settings"></a>

##  patch_conversations_settings(body)



Update Settings

Wraps PATCH /api/v2/conversations/settings 

Requires ANY permissions: 

* conversation:settings:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.Settings() # Settings | Settings

try:
    # Update Settings
    api_instance.patch_conversations_settings(body)
except ApiException as e:
    print("Exception when calling ConversationsApi->patch_conversations_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**Settings**](Settings.html)| Settings |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_analytics_conversation_details_properties"></a>

## [**PropertyIndexRequest**](PropertyIndexRequest.html) post_analytics_conversation_details_properties(conversation_id, body)



Index conversation properties

Wraps POST /api/v2/analytics/conversations/{conversationId}/details/properties 

Requires ANY permissions: 

* analytics:conversationProperties:index

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.PropertyIndexRequest() # PropertyIndexRequest | request

try:
    # Index conversation properties
    api_response = api_instance.post_analytics_conversation_details_properties(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversation_details_properties: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**PropertyIndexRequest**](PropertyIndexRequest.html)| request |  |
{: class="table table-striped"}

### Return type

[**PropertyIndexRequest**](PropertyIndexRequest.html)

<a name="post_analytics_conversations_activity_query"></a>

## [**ConversationActivityResponse**](ConversationActivityResponse.html) post_analytics_conversations_activity_query(body, page_size=page_size, page_number=page_number)



Query for conversation activity observations

post_analytics_conversations_activity_query is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/conversations/activity/query 

Requires ANY permissions: 

* analytics:queueObservation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationActivityQuery() # ConversationActivityQuery | query
page_size = 56 # int | The desired page size (optional)
page_number = 56 # int | The desired page number (optional)

try:
    # Query for conversation activity observations
    api_response = api_instance.post_analytics_conversations_activity_query(body, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversations_activity_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationActivityQuery**](ConversationActivityQuery.html)| query |  |
| **page_size** | **int**| The desired page size | [optional]  |
| **page_number** | **int**| The desired page number | [optional]  |
{: class="table table-striped"}

### Return type

[**ConversationActivityResponse**](ConversationActivityResponse.html)

<a name="post_analytics_conversations_aggregates_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_conversations_aggregates_jobs(body)



Query for conversation aggregates asynchronously

post_analytics_conversations_aggregates_jobs is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/analytics/conversations/aggregates/jobs 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationAsyncAggregationQuery() # ConversationAsyncAggregationQuery | query

try:
    # Query for conversation aggregates asynchronously
    api_response = api_instance.post_analytics_conversations_aggregates_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversations_aggregates_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationAsyncAggregationQuery**](ConversationAsyncAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_conversations_aggregates_query"></a>

## [**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse.html) post_analytics_conversations_aggregates_query(body)



Query for conversation aggregates

Wraps POST /api/v2/analytics/conversations/aggregates/query 

Requires ANY permissions: 

* analytics:conversationAggregate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationAggregationQuery() # ConversationAggregationQuery | query

try:
    # Query for conversation aggregates
    api_response = api_instance.post_analytics_conversations_aggregates_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversations_aggregates_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationAggregationQuery**](ConversationAggregationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**ConversationAggregateQueryResponse**](ConversationAggregateQueryResponse.html)

<a name="post_analytics_conversations_details_jobs"></a>

## [**AsyncQueryResponse**](AsyncQueryResponse.html) post_analytics_conversations_details_jobs(body)



Query for conversation details asynchronously

Wraps POST /api/v2/analytics/conversations/details/jobs 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.AsyncConversationQuery() # AsyncConversationQuery | query

try:
    # Query for conversation details asynchronously
    api_response = api_instance.post_analytics_conversations_details_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversations_details_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AsyncConversationQuery**](AsyncConversationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AsyncQueryResponse**](AsyncQueryResponse.html)

<a name="post_analytics_conversations_details_query"></a>

## [**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html) post_analytics_conversations_details_query(body)



Query for conversation details

Wraps POST /api/v2/analytics/conversations/details/query 

Requires ANY permissions: 

* analytics:conversationDetail:view
* analytics:agentConversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationQuery() # ConversationQuery | query

try:
    # Query for conversation details
    api_response = api_instance.post_analytics_conversations_details_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_analytics_conversations_details_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationQuery**](ConversationQuery.html)| query |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationQueryResponse**](AnalyticsConversationQueryResponse.html)

<a name="post_conversation_assign"></a>

## str** post_conversation_assign(conversation_id, body)



Attempts to manually assign a specified conversation to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.

Wraps POST /api/v2/conversations/{conversationId}/assign 

Requires ANY permissions: 

* conversation:call:pull
* conversation:call:assign
* conversation:callback:pull
* conversation:callback:assign
* conversation:webchat:pull
* conversation:webchat:assign
* conversation:email:pull
* conversation:email:assign
* conversation:message:pull
* conversation:message:assign

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
body = PureCloudPlatformClientV2.ConversationUser() # ConversationUser | Targeted user

try:
    # Attempts to manually assign a specified conversation to a specified user.  Ignores bullseye ring, PAR score, skills, and languages.
    api_response = api_instance.post_conversation_assign(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_assign: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **body** | [**ConversationUser**](ConversationUser.html)| Targeted user |  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_conversation_barge"></a>

##  post_conversation_barge(conversation_id)



Barge a conversation creating a barged in conference of connected participants.

post_conversation_barge is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/conversations/{conversationId}/barge 

Requires ANY permissions: 

* conversation:call:barge

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Barge a conversation creating a barged in conference of connected participants.
    api_instance.post_conversation_barge(conversation_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_barge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_cobrowse"></a>

## [**CobrowseWebMessagingSession**](CobrowseWebMessagingSession.html) post_conversation_cobrowse(conversation_id)



Creates a cobrowse session. Requires \"conversation:cobrowse:add\" (for web messaging) or \"conversation:cobrowsevoice:add\" permission.

Wraps POST /api/v2/conversations/{conversationId}/cobrowse 

Requires ANY permissions: 

* conversation:cobrowse:add
* conversation:cobrowseVoice:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID

try:
    # Creates a cobrowse session. Requires \"conversation:cobrowse:add\" (for web messaging) or \"conversation:cobrowsevoice:add\" permission.
    api_response = api_instance.post_conversation_cobrowse(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_cobrowse: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
{: class="table table-striped"}

### Return type

[**CobrowseWebMessagingSession**](CobrowseWebMessagingSession.html)

<a name="post_conversation_disconnect"></a>

## str** post_conversation_disconnect(conversation_id)



Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resynchronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.

Wraps POST /api/v2/conversations/{conversationId}/disconnect 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID

try:
    # Performs a full conversation teardown. Issues disconnect requests for any connected media. Applies a system wrap-up code to any participants that are pending wrap-up. This is not intended to be the normal way of ending interactions but is available in the event of problems with the application to allow a resynchronization of state across all components. It is recommended that users submit a support case if they are relying on this endpoint systematically as there is likely something that needs investigation.
    api_response = api_instance.post_conversation_disconnect(conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_disconnect: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
{: class="table table-striped"}

### Return type

**str**

<a name="post_conversation_participant_callbacks"></a>

##  post_conversation_participant_callbacks(conversation_id, participant_id, body=body)



Create a new callback for the specified participant on the conversation.

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/callbacks 

Requires ALL permissions: 

* conversation:callback:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.CreateCallbackOnConversationCommand() # CreateCallbackOnConversationCommand |  (optional)

try:
    # Create a new callback for the specified participant on the conversation.
    api_instance.post_conversation_participant_callbacks(conversation_id, participant_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_callbacks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**CreateCallbackOnConversationCommand**](CreateCallbackOnConversationCommand.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_digits"></a>

##  post_conversation_participant_digits(conversation_id, participant_id, body=body)



Sends DTMF to the participant

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/digits 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.Digits() # Digits | Digits (optional)

try:
    # Sends DTMF to the participant
    api_instance.post_conversation_participant_digits(conversation_id, participant_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_digits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**Digits**](Digits.html)| Digits | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_replace"></a>

##  post_conversation_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversation_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_replace_agent"></a>

##  post_conversation_participant_replace_agent(conversation_id, participant_id, body)



Replace this participant with the specified agent

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/replace/agent 

Requires ANY permissions: 

* conversation:communication:blindTransfer
* conversation:communication:blindTransferAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.TransferToAgentRequest() # TransferToAgentRequest | Transfer request

try:
    # Replace this participant with the specified agent
    api_instance.post_conversation_participant_replace_agent(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_replace_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**TransferToAgentRequest**](TransferToAgentRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_replace_external"></a>

##  post_conversation_participant_replace_external(conversation_id, participant_id, body)



Replace this participant with the an external contact

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/replace/external 

Requires ANY permissions: 

* conversation:communication:blindTransfer
* conversation:communication:blindTransferExternal

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.TransferToExternalRequest() # TransferToExternalRequest | Transfer request

try:
    # Replace this participant with the an external contact
    api_instance.post_conversation_participant_replace_external(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_replace_external: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**TransferToExternalRequest**](TransferToExternalRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_replace_queue"></a>

##  post_conversation_participant_replace_queue(conversation_id, participant_id, body)



Replace this participant with the specified queue

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/replace/queue 

Requires ANY permissions: 

* conversation:communication:blindTransfer
* conversation:communication:blindTransferQueue

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.TransferToQueueRequest() # TransferToQueueRequest | Transfer request

try:
    # Replace this participant with the specified queue
    api_instance.post_conversation_participant_replace_queue(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_replace_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**TransferToQueueRequest**](TransferToQueueRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversation_participant_secureivrsessions"></a>

## [**SecureSession**](SecureSession.html) post_conversation_participant_secureivrsessions(conversation_id, participant_id, body=body)



Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.

Wraps POST /api/v2/conversations/{conversationId}/participants/{participantId}/secureivrsessions 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID
body = PureCloudPlatformClientV2.CreateSecureSession() # CreateSecureSession |  (optional)

try:
    # Create secure IVR session. Only a participant in the conversation can invoke a secure IVR.
    api_response = api_instance.post_conversation_participant_secureivrsessions(conversation_id, participant_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_participant_secureivrsessions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
| **body** | [**CreateSecureSession**](CreateSecureSession.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**SecureSession**](SecureSession.html)

<a name="post_conversation_summary_feedback"></a>

##  post_conversation_summary_feedback(conversation_id, summary_id, body=body)



Submit feedback for the summary.

Wraps POST /api/v2/conversations/{conversationId}/summaries/{summaryId}/feedback 

Requires ALL permissions: 

* conversation:summaryFeedback:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | Conversation ID
summary_id = 'summary_id_example' # str | Summary ID
body = PureCloudPlatformClientV2.FeedbackAddRequest() # FeedbackAddRequest |  (optional)

try:
    # Submit feedback for the summary.
    api_instance.post_conversation_summary_feedback(conversation_id, summary_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversation_summary_feedback: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| Conversation ID |  |
| **summary_id** | **str**| Summary ID |  |
| **body** | [**FeedbackAddRequest**](FeedbackAddRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call"></a>

## [**Conversation**](Conversation.html) post_conversations_call(conversation_id, body)



Place a new call as part of a callback conversation.

Wraps POST /api/v2/conversations/calls/{conversationId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.CallCommand() # CallCommand | Conversation

try:
    # Place a new call as part of a callback conversation.
    api_response = api_instance.post_conversations_call(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**CallCommand**](CallCommand.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="post_conversations_call_participant_barge"></a>

##  post_conversations_call_participant_barge(conversation_id, participant_id)



Barge a given participant's call creating a barged in conference of connected participants.

post_conversations_call_participant_barge is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/barge 

Requires ANY permissions: 

* conversation:call:barge

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Barge a given participant's call creating a barged in conference of connected participants.
    api_instance.post_conversations_call_participant_barge(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_barge: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participant_coach"></a>

##  post_conversations_call_participant_coach(conversation_id, participant_id)



Listen in on the conversation from the point of view of a given participant while speaking to just the given participant.

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/coach 

Requires ANY permissions: 

* conversation:call:coach

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Listen in on the conversation from the point of view of a given participant while speaking to just the given participant.
    api_instance.post_conversations_call_participant_coach(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_coach: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participant_communication_wrapup"></a>

##  post_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_call_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participant_consult"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) post_conversations_call_participant_consult(conversation_id, participant_id, body)



Initiate and update consult transfer

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult 

Requires ANY permissions: 

* conversation:communication:consultTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransfer() # ConsultTransfer | Destination address & initial speak to

try:
    # Initiate and update consult transfer
    api_response = api_instance.post_conversations_call_participant_consult(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_consult: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransfer**](ConsultTransfer.html)| Destination address &amp; initial speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="post_conversations_call_participant_consult_agent"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) post_conversations_call_participant_consult_agent(conversation_id, participant_id, body)



Initiate a consult transfer to an agent

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult/agent 

Requires ANY permissions: 

* conversation:communication:consultTransfer
* conversation:communication:consultTransferAgent

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransferToAgent() # ConsultTransferToAgent | Destination agent & initial speak to

try:
    # Initiate a consult transfer to an agent
    api_response = api_instance.post_conversations_call_participant_consult_agent(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_consult_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransferToAgent**](ConsultTransferToAgent.html)| Destination agent &amp; initial speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="post_conversations_call_participant_consult_external"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) post_conversations_call_participant_consult_external(conversation_id, participant_id, body)



Initiate a consult transfer to an external contact

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult/external 

Requires ANY permissions: 

* conversation:communication:consultTransfer
* conversation:communication:consultTransferExternal

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransferToExternal() # ConsultTransferToExternal | Destination address & initial speak to

try:
    # Initiate a consult transfer to an external contact
    api_response = api_instance.post_conversations_call_participant_consult_external(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_consult_external: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransferToExternal**](ConsultTransferToExternal.html)| Destination address &amp; initial speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="post_conversations_call_participant_consult_queue"></a>

## [**ConsultTransferResponse**](ConsultTransferResponse.html) post_conversations_call_participant_consult_queue(conversation_id, participant_id, body)



Initiate a consult transfer to a queue

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/consult/queue 

Requires ANY permissions: 

* conversation:communication:consultTransfer
* conversation:communication:consultTransferQueue

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.ConsultTransferToQueue() # ConsultTransferToQueue | Destination queue & initial speak to

try:
    # Initiate a consult transfer to a queue
    api_response = api_instance.post_conversations_call_participant_consult_queue(conversation_id, participant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_consult_queue: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**ConsultTransferToQueue**](ConsultTransferToQueue.html)| Destination queue &amp; initial speak to |  |
{: class="table table-striped"}

### Return type

[**ConsultTransferResponse**](ConsultTransferResponse.html)

<a name="post_conversations_call_participant_monitor"></a>

##  post_conversations_call_participant_monitor(conversation_id, participant_id)



Listen in on the conversation from the point of view of a given participant.

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/monitor 

Requires ANY permissions: 

* conversation:call:monitor

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Listen in on the conversation from the point of view of a given participant.
    api_instance.post_conversations_call_participant_monitor(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_monitor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participant_replace"></a>

##  post_conversations_call_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/calls/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_call_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_call_participants"></a>

## [**Conversation**](Conversation.html) post_conversations_call_participants(conversation_id, body)



Add participants to a conversation

Wraps POST /api/v2/conversations/calls/{conversationId}/participants 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.Conversation() # Conversation | Conversation

try:
    # Add participants to a conversation
    api_response = api_instance.post_conversations_call_participants(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_call_participants: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**Conversation**](Conversation.html)| Conversation |  |
{: class="table table-striped"}

### Return type

[**Conversation**](Conversation.html)

<a name="post_conversations_callback_participant_communication_wrapup"></a>

##  post_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_callback_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_callback_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_callback_participant_replace"></a>

##  post_conversations_callback_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/callbacks/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_callback_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_callback_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_callbacks"></a>

## [**CreateCallbackResponse**](CreateCallbackResponse.html) post_conversations_callbacks(body)



Create a Callback

Wraps POST /api/v2/conversations/callbacks 

Requires ALL permissions: 

* conversation:callback:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateCallbackCommand() # CreateCallbackCommand | Callback

try:
    # Create a Callback
    api_response = api_instance.post_conversations_callbacks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_callbacks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCallbackCommand**](CreateCallbackCommand.html)| Callback |  |
{: class="table table-striped"}

### Return type

[**CreateCallbackResponse**](CreateCallbackResponse.html)

<a name="post_conversations_callbacks_bulk_disconnect"></a>

##  post_conversations_callbacks_bulk_disconnect(body)



Disconnect multiple scheduled callbacks

Wraps POST /api/v2/conversations/callbacks/bulk/disconnect 

Requires ANY permissions: 

* conversation:communication:disconnect

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.BulkCallbackDisconnectRequest() # BulkCallbackDisconnectRequest | BulkCallbackDisconnectRequest

try:
    # Disconnect multiple scheduled callbacks
    api_instance.post_conversations_callbacks_bulk_disconnect(body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_callbacks_bulk_disconnect: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkCallbackDisconnectRequest**](BulkCallbackDisconnectRequest.html)| BulkCallbackDisconnectRequest |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_callbacks_bulk_update"></a>

## [**BulkCallbackPatchResponse**](BulkCallbackPatchResponse.html) post_conversations_callbacks_bulk_update(body)



Update multiple scheduled callbacks

Wraps POST /api/v2/conversations/callbacks/bulk/update 

Requires ANY permissions: 

* conversation:callback:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.BulkCallbackPatchRequest() # BulkCallbackPatchRequest | BulkCallbackPatchRequest

try:
    # Update multiple scheduled callbacks
    api_response = api_instance.post_conversations_callbacks_bulk_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_callbacks_bulk_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BulkCallbackPatchRequest**](BulkCallbackPatchRequest.html)| BulkCallbackPatchRequest |  |
{: class="table table-striped"}

### Return type

[**BulkCallbackPatchResponse**](BulkCallbackPatchResponse.html)

<a name="post_conversations_calls"></a>

## [**CreateCallResponse**](CreateCallResponse.html) post_conversations_calls(body)



Create a call conversation

Wraps POST /api/v2/conversations/calls 

Requires ANY permissions: 

* conversation:conference:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateCallRequest() # CreateCallRequest | Call request

try:
    # Create a call conversation
    api_response = api_instance.post_conversations_calls(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_calls: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCallRequest**](CreateCallRequest.html)| Call request |  |
{: class="table table-striped"}

### Return type

[**CreateCallResponse**](CreateCallResponse.html)

<a name="post_conversations_chat_communication_messages"></a>

## [**WebChatMessage**](WebChatMessage.html) post_conversations_chat_communication_messages(conversation_id, communication_id, body)



Send a message on behalf of a communication in a chat conversation.

Wraps POST /api/v2/conversations/chats/{conversationId}/communications/{communicationId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.CreateWebChatMessageRequest() # CreateWebChatMessageRequest | Message

try:
    # Send a message on behalf of a communication in a chat conversation.
    api_response = api_instance.post_conversations_chat_communication_messages(conversation_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_chat_communication_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**CreateWebChatMessageRequest**](CreateWebChatMessageRequest.html)| Message |  |
{: class="table table-striped"}

### Return type

[**WebChatMessage**](WebChatMessage.html)

<a name="post_conversations_chat_communication_typing"></a>

## [**WebChatTyping**](WebChatTyping.html) post_conversations_chat_communication_typing(conversation_id, communication_id)



Send a typing-indicator on behalf of a communication in a chat conversation.

Wraps POST /api/v2/conversations/chats/{conversationId}/communications/{communicationId}/typing 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId

try:
    # Send a typing-indicator on behalf of a communication in a chat conversation.
    api_response = api_instance.post_conversations_chat_communication_typing(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_chat_communication_typing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
{: class="table table-striped"}

### Return type

[**WebChatTyping**](WebChatTyping.html)

<a name="post_conversations_chat_participant_communication_wrapup"></a>

##  post_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/chats/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_chat_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_chat_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_chat_participant_replace"></a>

##  post_conversations_chat_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/chats/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_chat_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_chat_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_chats"></a>

## [**ChatConversation**](ChatConversation.html) post_conversations_chats(body)



Create a web chat conversation

Wraps POST /api/v2/conversations/chats 

Requires ALL permissions: 

* conversation:webchat:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateWebChatRequest() # CreateWebChatRequest | Create web chat request

try:
    # Create a web chat conversation
    api_response = api_instance.post_conversations_chats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_chats: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateWebChatRequest**](CreateWebChatRequest.html)| Create web chat request |  |
{: class="table table-striped"}

### Return type

[**ChatConversation**](ChatConversation.html)

<a name="post_conversations_cobrowsesession_participant_communication_wrapup"></a>

##  post_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Apply wrap-up for this conversation communication

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps POST /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_cobrowsesession_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_cobrowsesession_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_cobrowsesession_participant_replace"></a>

##  post_conversations_cobrowsesession_participant_replace(conversation_id, participant_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Replace this participant with the specified user and/or address

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps POST /api/v2/conversations/cobrowsesessions/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest |  (optional)

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_cobrowsesession_participant_replace(conversation_id, participant_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_cobrowsesession_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_email_inboundmessages"></a>

## [**EmailConversation**](EmailConversation.html) post_conversations_email_inboundmessages(conversation_id, body)



Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.

Wraps POST /api/v2/conversations/emails/{conversationId}/inboundmessages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.InboundMessageRequest() # InboundMessageRequest | Send external email reply

try:
    # Send an email to an external conversation. An external conversation is one where the provider is not PureCloud based. This endpoint allows the sender of the external email to reply or send a new message to the existing conversation. The new message will be treated as part of the existing conversation and chained to it.
    api_response = api_instance.post_conversations_email_inboundmessages(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_email_inboundmessages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**InboundMessageRequest**](InboundMessageRequest.html)| Send external email reply |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="post_conversations_email_messages"></a>

## [**EmailMessageReply**](EmailMessageReply.html) post_conversations_email_messages(conversation_id, body)



Send an email reply

Wraps POST /api/v2/conversations/emails/{conversationId}/messages 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.EmailMessage() # EmailMessage | Reply

try:
    # Send an email reply
    api_response = api_instance.post_conversations_email_messages(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_email_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**EmailMessage**](EmailMessage.html)| Reply |  |
{: class="table table-striped"}

### Return type

[**EmailMessageReply**](EmailMessageReply.html)

<a name="post_conversations_email_messages_draft_attachments_copy"></a>

## [**EmailMessage**](EmailMessage.html) post_conversations_email_messages_draft_attachments_copy(conversation_id, body)



Copy attachments from an email message to the current draft.

Wraps POST /api/v2/conversations/emails/{conversationId}/messages/draft/attachments/copy 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.CopyAttachmentsRequest() # CopyAttachmentsRequest | Copy Attachment Request

try:
    # Copy attachments from an email message to the current draft.
    api_response = api_instance.post_conversations_email_messages_draft_attachments_copy(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_email_messages_draft_attachments_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**CopyAttachmentsRequest**](CopyAttachmentsRequest.html)| Copy Attachment Request |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="post_conversations_email_participant_communication_wrapup"></a>

##  post_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/emails/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_email_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_email_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_email_participant_replace"></a>

##  post_conversations_email_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/emails/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_email_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_email_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_emails"></a>

## [**EmailConversation**](EmailConversation.html) post_conversations_emails(body)



Create an email conversation

If the direction of the request is INBOUND, this will create an external conversation with a third party provider. If the direction of the the request is OUTBOUND, this will create a conversation to send outbound emails on behalf of a queue.

Wraps POST /api/v2/conversations/emails 

Requires ANY permissions: 

* conversation:email:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateEmailRequest() # CreateEmailRequest | Create email request

try:
    # Create an email conversation
    api_response = api_instance.post_conversations_emails(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_emails: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateEmailRequest**](CreateEmailRequest.html)| Create email request |  |
{: class="table table-striped"}

### Return type

[**EmailConversation**](EmailConversation.html)

<a name="post_conversations_emails_agentless"></a>

## [**AgentlessEmailSendResponseDto**](AgentlessEmailSendResponseDto.html) post_conversations_emails_agentless(body)



Create an email conversation, per API

Wraps POST /api/v2/conversations/emails/agentless 

Requires ANY permissions: 

* conversation:email:create
* conversation:agentlessEmail:send

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.AgentlessEmailSendRequestDto() # AgentlessEmailSendRequestDto | Create agentless email request

try:
    # Create an email conversation, per API
    api_response = api_instance.post_conversations_emails_agentless(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_emails_agentless: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentlessEmailSendRequestDto**](AgentlessEmailSendRequestDto.html)| Create agentless email request |  |
{: class="table table-striped"}

### Return type

[**AgentlessEmailSendResponseDto**](AgentlessEmailSendResponseDto.html)

<a name="post_conversations_faxes"></a>

## [**FaxSendResponse**](FaxSendResponse.html) post_conversations_faxes(body)



Create Fax Conversation

Wraps POST /api/v2/conversations/faxes 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.FaxSendRequest() # FaxSendRequest | Fax

try:
    # Create Fax Conversation
    api_response = api_instance.post_conversations_faxes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_faxes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FaxSendRequest**](FaxSendRequest.html)| Fax |  |
{: class="table table-striped"}

### Return type

[**FaxSendResponse**](FaxSendResponse.html)

<a name="post_conversations_keyconfigurations"></a>

## [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html) post_conversations_keyconfigurations(body)



Setup configurations for encryption key creation

Wraps POST /api/v2/conversations/keyconfigurations 

Requires ANY permissions: 

* conversation:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationEncryptionConfiguration() # ConversationEncryptionConfiguration | Encryption Configuration

try:
    # Setup configurations for encryption key creation
    api_response = api_instance.post_conversations_keyconfigurations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_keyconfigurations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)| Encryption Configuration |  |
{: class="table table-striped"}

### Return type

[**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)

<a name="post_conversations_keyconfigurations_validate"></a>

## [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html) post_conversations_keyconfigurations_validate(body)



Validate encryption key configurations without saving it

Wraps POST /api/v2/conversations/keyconfigurations/validate 

Requires ANY permissions: 

* conversation:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationEncryptionConfiguration() # ConversationEncryptionConfiguration | Encryption Configuration

try:
    # Validate encryption key configurations without saving it
    api_response = api_instance.post_conversations_keyconfigurations_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_keyconfigurations_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)| Encryption Configuration |  |
{: class="table table-striped"}

### Return type

[**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)

<a name="post_conversations_message_communication_messages"></a>

## [**MessageData**](MessageData.html) post_conversations_message_communication_messages(conversation_id, communication_id, body, use_normalized_message=use_normalized_message)



Send message

Send message on existing conversation/communication. Only one message body field can be accepted, per request. Example: 1 textBody, 1 mediaId, 1 stickerId, or 1 messageTemplate.

Wraps POST /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages 

Requires ANY permissions: 

* conversation:message:create
* conversation:webmessaging:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.AdditionalMessage() # AdditionalMessage | Message
use_normalized_message = False # bool | If true, response removes deprecated fields (textBody, media, stickers) (optional) (default to False)

try:
    # Send message
    api_response = api_instance.post_conversations_message_communication_messages(conversation_id, communication_id, body, use_normalized_message=use_normalized_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_communication_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**AdditionalMessage**](AdditionalMessage.html)| Message |  |
| **use_normalized_message** | **bool**| If true, response removes deprecated fields (textBody, media, stickers) | [optional] [default to False] |
{: class="table table-striped"}

### Return type

[**MessageData**](MessageData.html)

<a name="post_conversations_message_communication_messages_media"></a>

## [**MessageMediaData**](MessageMediaData.html) post_conversations_message_communication_messages_media(conversation_id, communication_id)



Create media

See https://developer.genesys.cloud/api/rest/v2/conversations/messaging-media-upload for example usage.

Wraps POST /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/messages/media 

Requires ANY permissions: 

* conversation:message:create
* conversation:webmessaging:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId

try:
    # Create media
    api_response = api_instance.post_conversations_message_communication_messages_media(conversation_id, communication_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_communication_messages_media: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
{: class="table table-striped"}

### Return type

[**MessageMediaData**](MessageMediaData.html)

<a name="post_conversations_message_communication_typing"></a>

##  post_conversations_message_communication_typing(conversation_id, communication_id, body)



Send message typing event

Send message typing event for existing conversation/communication.

Wraps POST /api/v2/conversations/messages/{conversationId}/communications/{communicationId}/typing 

Requires ANY permissions: 

* conversation:message:create
* conversation:webmessaging:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.MessageTypingEventRequest() # MessageTypingEventRequest | MessageTypingEvent

try:
    # Send message typing event
    api_instance.post_conversations_message_communication_typing(conversation_id, communication_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_communication_typing: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**MessageTypingEventRequest**](MessageTypingEventRequest.html)| MessageTypingEvent |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_message_inbound_open_event"></a>

## [**OpenEventNormalizedMessage**](OpenEventNormalizedMessage.html) post_conversations_message_inbound_open_event(integration_id, body)



Send an inbound Open Event Message

Send an inbound event message to an Open Messaging integration. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will either generate a new Conversation, or be a part of an existing conversation. See https://developer.genesys.cloud/api/digital/openmessaging/ for example usage.

Wraps POST /api/v2/conversations/messages/{integrationId}/inbound/open/event 

Requires ALL permissions: 

* conversation:message:receive

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | integrationId
body = PureCloudPlatformClientV2.OpenInboundNormalizedEvent() # OpenInboundNormalizedEvent | NormalizedMessage

try:
    # Send an inbound Open Event Message
    api_response = api_instance.post_conversations_message_inbound_open_event(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_inbound_open_event: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| integrationId |  |
| **body** | [**OpenInboundNormalizedEvent**](OpenInboundNormalizedEvent.html)| NormalizedMessage |  |
{: class="table table-striped"}

### Return type

[**OpenEventNormalizedMessage**](OpenEventNormalizedMessage.html)

<a name="post_conversations_message_inbound_open_message"></a>

## [**OpenMessageNormalizedMessage**](OpenMessageNormalizedMessage.html) post_conversations_message_inbound_open_message(integration_id, body)



Send inbound Open Message

Send an inbound message to an Open Messaging integration. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will either generate a new Conversation, or be a part of an existing conversation. See https://developer.genesys.cloud/api/digital/openmessaging/ for example usage.

Wraps POST /api/v2/conversations/messages/{integrationId}/inbound/open/message 

Requires ALL permissions: 

* conversation:message:receive

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | integrationId
body = PureCloudPlatformClientV2.OpenInboundNormalizedMessage() # OpenInboundNormalizedMessage | NormalizedMessage

try:
    # Send inbound Open Message
    api_response = api_instance.post_conversations_message_inbound_open_message(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_inbound_open_message: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| integrationId |  |
| **body** | [**OpenInboundNormalizedMessage**](OpenInboundNormalizedMessage.html)| NormalizedMessage |  |
{: class="table table-striped"}

### Return type

[**OpenMessageNormalizedMessage**](OpenMessageNormalizedMessage.html)

<a name="post_conversations_message_inbound_open_receipt"></a>

## [**OpenReceiptNormalizedMessage**](OpenReceiptNormalizedMessage.html) post_conversations_message_inbound_open_receipt(integration_id, body)



Send an inbound Open Receipt Message

Send an inbound open Receipt to an Open Messaging integration. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will either generate a new Conversation, or be a part of an existing conversation. See https://developer.genesys.cloud/api/digital/openmessaging/ for example usage.

Wraps POST /api/v2/conversations/messages/{integrationId}/inbound/open/receipt 

Requires ALL permissions: 

* conversation:message:receive

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | integrationId
body = PureCloudPlatformClientV2.OpenInboundNormalizedReceipt() # OpenInboundNormalizedReceipt | NormalizedMessage

try:
    # Send an inbound Open Receipt Message
    api_response = api_instance.post_conversations_message_inbound_open_receipt(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_inbound_open_receipt: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| integrationId |  |
| **body** | [**OpenInboundNormalizedReceipt**](OpenInboundNormalizedReceipt.html)| NormalizedMessage |  |
{: class="table table-striped"}

### Return type

[**OpenReceiptNormalizedMessage**](OpenReceiptNormalizedMessage.html)

<a name="post_conversations_message_messages_bulk"></a>

## [**TextMessageListing**](TextMessageListing.html) post_conversations_message_messages_bulk(conversation_id, use_normalized_message=use_normalized_message, body=body)



Get messages in batch

The path parameter [conversationId] should contain the conversationId of the conversation being filtered. The body should contain the messageId(s) of messages being requested. For example: [\"a3069a33b-bbb1-4703-9d68-061d9e9db96e\", \"55bc6be3-078c-4a49-a4e6-1e05776ed7e8\"]

Wraps POST /api/v2/conversations/messages/{conversationId}/messages/bulk 

Requires ANY permissions: 

* conversation:message:view
* conversation:webmessaging:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | 
use_normalized_message = False # bool | If true, response removes deprecated fields (textBody, media, stickers) (optional) (default to False)
body = ['body_example'] # list[str] | messageIds (optional)

try:
    # Get messages in batch
    api_response = api_instance.post_conversations_message_messages_bulk(conversation_id, use_normalized_message=use_normalized_message, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_messages_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**|  |  |
| **use_normalized_message** | **bool**| If true, response removes deprecated fields (textBody, media, stickers) | [optional] [default to False] |
| **body** | [**list[str]**](str.html)| messageIds | [optional]  |
{: class="table table-striped"}

### Return type

[**TextMessageListing**](TextMessageListing.html)

<a name="post_conversations_message_participant_communication_wrapup"></a>

##  post_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/messages/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_message_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_message_participant_monitor"></a>

##  post_conversations_message_participant_monitor(conversation_id, participant_id)



Listen in on the conversation from the point of view of a given participant.

Wraps POST /api/v2/conversations/messages/{conversationId}/participants/{participantId}/monitor 

Requires ANY permissions: 

* conversation:message:monitor

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId

try:
    # Listen in on the conversation from the point of view of a given participant.
    api_instance.post_conversations_message_participant_monitor(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_participant_monitor: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_message_participant_replace"></a>

##  post_conversations_message_participant_replace(conversation_id, participant_id, body)



Replace this participant with the specified user and/or address

Wraps POST /api/v2/conversations/messages/{conversationId}/participants/{participantId}/replace 

Requires ANY permissions: 

* conversation:communication:blindTransfer

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
body = PureCloudPlatformClientV2.TransferRequest() # TransferRequest | Transfer request

try:
    # Replace this participant with the specified user and/or address
    api_instance.post_conversations_message_participant_replace(conversation_id, participant_id, body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_message_participant_replace: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **body** | [**TransferRequest**](TransferRequest.html)| Transfer request |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_messages"></a>

## [**MessageConversation**](MessageConversation.html) post_conversations_messages(body)



Create an outbound messaging conversation.

If there is an existing conversation between the remote address and the address associated with the queue specified in createOutboundRequest then the result of this request depends on the state of that conversation and the useExistingConversation field of createOutboundRequest. If the existing conversation is in alerting or connected state, then the request will fail. If the existing conversation is disconnected but still within the conversation window then the request will fail unless useExistingConversation is set to true.

Wraps POST /api/v2/conversations/messages 

Requires ALL permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.CreateOutboundMessagingConversationRequest() # CreateOutboundMessagingConversationRequest | Create outbound messaging conversation

try:
    # Create an outbound messaging conversation.
    api_response = api_instance.post_conversations_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messages: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateOutboundMessagingConversationRequest**](CreateOutboundMessagingConversationRequest.html)| Create outbound messaging conversation |  |
{: class="table table-striped"}

### Return type

[**MessageConversation**](MessageConversation.html)

<a name="post_conversations_messages_agentless"></a>

## [**SendAgentlessOutboundMessageResponse**](SendAgentlessOutboundMessageResponse.html) post_conversations_messages_agentless(body)



Send an agentless outbound message

Send an agentless (api participant) outbound message using a client credential grant. In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. If there is already a connected conversation between the 'fromAddress' and 'toAddress' specified, the 'useExistingActiveConversation' param can be used to barge in to the ongoing conversation.

Wraps POST /api/v2/conversations/messages/agentless 

Requires ALL permissions: 

* conversation:message:create

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.SendAgentlessOutboundMessageRequest() # SendAgentlessOutboundMessageRequest | Create agentless outbound messaging request

try:
    # Send an agentless outbound message
    api_response = api_instance.post_conversations_messages_agentless(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messages_agentless: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SendAgentlessOutboundMessageRequest**](SendAgentlessOutboundMessageRequest.html)| Create agentless outbound messaging request |  |
{: class="table table-striped"}

### Return type

[**SendAgentlessOutboundMessageResponse**](SendAgentlessOutboundMessageResponse.html)

<a name="post_conversations_messages_inbound_open"></a>

## [**OpenNormalizedMessage**](OpenNormalizedMessage.html) post_conversations_messages_inbound_open(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Send an inbound Open Message

[This API is deprecated. Instead, use 1. POST /api/v2/conversations/messages/{integrationId}/inbound/open/event, if you want to send an inbound Open Event Message 2. POST /api/v2/conversations/messages/{integrationId}/inbound/open/message, if you want to send an inbound Open Message 3. POST /api/v2/conversations/messages/{integrationId}/inbound/open/receipt, to send an inbound Open Receipt Message]  In order to call this endpoint you will need OAuth token generated using OAuth client credentials authorized with at least messaging scope. This will either generate a new Conversation, or be a part of an existing conversation. See https://developer.genesys.cloud/api/digital/openmessaging/ for example usage.

Wraps POST /api/v2/conversations/messages/inbound/open 

Requires ALL permissions: 

* conversation:message:receive

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.OpenNormalizedMessage() # OpenNormalizedMessage | NormalizedMessage

try:
    # Send an inbound Open Message
    api_response = api_instance.post_conversations_messages_inbound_open(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messages_inbound_open: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OpenNormalizedMessage**](OpenNormalizedMessage.html)| NormalizedMessage |  |
{: class="table table-striped"}

### Return type

[**OpenNormalizedMessage**](OpenNormalizedMessage.html)

<a name="post_conversations_messaging_integrations_facebook"></a>

## [**FacebookIntegration**](FacebookIntegration.html) post_conversations_messaging_integrations_facebook(body)



Create a Facebook Integration

Wraps POST /api/v2/conversations/messaging/integrations/facebook 

Requires ALL permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.FacebookIntegrationRequest() # FacebookIntegrationRequest | FacebookIntegrationRequest

try:
    # Create a Facebook Integration
    api_response = api_instance.post_conversations_messaging_integrations_facebook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_facebook: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**FacebookIntegrationRequest**](FacebookIntegrationRequest.html)| FacebookIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**FacebookIntegration**](FacebookIntegration.html)

<a name="post_conversations_messaging_integrations_instagram"></a>

## [**InstagramIntegration**](InstagramIntegration.html) post_conversations_messaging_integrations_instagram(body)



Create Instagram Integration

Wraps POST /api/v2/conversations/messaging/integrations/instagram 

Requires ALL permissions: 

* messaging:conversationInstagramIntegration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.InstagramIntegrationRequest() # InstagramIntegrationRequest | InstagramIntegrationRequest

try:
    # Create Instagram Integration
    api_response = api_instance.post_conversations_messaging_integrations_instagram(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_instagram: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**InstagramIntegrationRequest**](InstagramIntegrationRequest.html)| InstagramIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**InstagramIntegration**](InstagramIntegration.html)

<a name="post_conversations_messaging_integrations_line"></a>

## [**LineIntegration**](LineIntegration.html) post_conversations_messaging_integrations_line(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create a LINE messenger Integration (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps POST /api/v2/conversations/messaging/integrations/line 

Requires ALL permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.LineIntegrationRequest() # LineIntegrationRequest | LineIntegrationRequest

try:
    # Create a LINE messenger Integration (Deprecated)
    api_response = api_instance.post_conversations_messaging_integrations_line(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_line: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LineIntegrationRequest**](LineIntegrationRequest.html)| LineIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)

<a name="post_conversations_messaging_integrations_open"></a>

## [**OpenIntegration**](OpenIntegration.html) post_conversations_messaging_integrations_open(body)



Create an Open messaging integration

See https://developer.genesys.cloud/api/digital/openmessaging/ for more information.

Wraps POST /api/v2/conversations/messaging/integrations/open 

Requires ALL permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.OpenIntegrationRequest() # OpenIntegrationRequest | OpenIntegrationRequest

try:
    # Create an Open messaging integration
    api_response = api_instance.post_conversations_messaging_integrations_open(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_open: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**OpenIntegrationRequest**](OpenIntegrationRequest.html)| OpenIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**OpenIntegration**](OpenIntegration.html)

<a name="post_conversations_messaging_integrations_twitter"></a>

## [**TwitterIntegration**](TwitterIntegration.html) post_conversations_messaging_integrations_twitter(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Create a Twitter Integration

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-x-formerly-twitter-third-party-messaging-channel/

Wraps POST /api/v2/conversations/messaging/integrations/twitter 

Requires ALL permissions: 

* messaging:integration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.TwitterIntegrationRequest() # TwitterIntegrationRequest | TwitterIntegrationRequest

try:
    # Create a Twitter Integration
    api_response = api_instance.post_conversations_messaging_integrations_twitter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_twitter: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TwitterIntegrationRequest**](TwitterIntegrationRequest.html)| TwitterIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**TwitterIntegration**](TwitterIntegration.html)

<a name="post_conversations_messaging_integrations_whatsapp"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) post_conversations_messaging_integrations_whatsapp(body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

[This API is deprecated. Use POST /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup instead] Create a WhatsApp Integration

[This API is deprecated. Use POST /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup instead] You must be approved by WhatsApp to use this feature. Your approved e164-formatted phone number and valid WhatsApp certificate for your number are required. Your WhatsApp certificate must have valid base64 encoding. Please paste carefully and do not add any leading or trailing spaces. Do not alter any characters. An integration must be activated within 7 days of certificate generation. If you cannot complete the addition and activation of the number within 7 days, please obtain a new certificate before creating the integration. Integrations created with an invalid number or certificate may immediately incur additional integration fees. Please carefully enter your number and certificate as described.

Wraps POST /api/v2/conversations/messaging/integrations/whatsapp 

Requires ALL permissions: 

* messaging:whatsappIntegration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.WhatsAppIntegrationRequest() # WhatsAppIntegrationRequest | WhatsAppIntegrationRequest

try:
    # [This API is deprecated. Use POST /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup instead] Create a WhatsApp Integration
    api_response = api_instance.post_conversations_messaging_integrations_whatsapp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_whatsapp: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WhatsAppIntegrationRequest**](WhatsAppIntegrationRequest.html)| WhatsAppIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="post_conversations_messaging_integrations_whatsapp_embeddedsignup"></a>

## [**WhatsAppIntegration**](WhatsAppIntegration.html) post_conversations_messaging_integrations_whatsapp_embeddedsignup(body)



Create a WhatsApp Integration using the WhatsApp embedded signup flow

Use the access token returned from the embedded signup flow to obtain a list of available phone numbers that can be associated with the created integration. The returned WhatsApp integration will initially have a createStatus of Initiated until the list of available phone numbers can be obtained from the provider. Please run a GET on the created integration until it returns a createStatus of Completed, and the list of available phone numbers obtained from the provider. You can then specify one of the available phone numbers in the PATCH call on the integration to activate it.

Wraps POST /api/v2/conversations/messaging/integrations/whatsapp/embeddedsignup 

Requires ALL permissions: 

* messaging:whatsappIntegration:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.WhatsAppEmbeddedSignupIntegrationRequest() # WhatsAppEmbeddedSignupIntegrationRequest | WhatsAppEmbeddedSignupIntegrationRequest

try:
    # Create a WhatsApp Integration using the WhatsApp embedded signup flow
    api_response = api_instance.post_conversations_messaging_integrations_whatsapp_embeddedsignup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_integrations_whatsapp_embeddedsignup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WhatsAppEmbeddedSignupIntegrationRequest**](WhatsAppEmbeddedSignupIntegrationRequest.html)| WhatsAppEmbeddedSignupIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**WhatsAppIntegration**](WhatsAppIntegration.html)

<a name="post_conversations_messaging_settings"></a>

## [**MessagingSetting**](MessagingSetting.html) post_conversations_messaging_settings(body)



Create a messaging setting

Wraps POST /api/v2/conversations/messaging/settings 

Requires ALL permissions: 

* messaging:setting:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.MessagingSettingRequest() # MessagingSettingRequest | MessagingSetting

try:
    # Create a messaging setting
    api_response = api_instance.post_conversations_messaging_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MessagingSettingRequest**](MessagingSettingRequest.html)| MessagingSetting |  |
{: class="table table-striped"}

### Return type

[**MessagingSetting**](MessagingSetting.html)

<a name="post_conversations_messaging_supportedcontent"></a>

## [**SupportedContent**](SupportedContent.html) post_conversations_messaging_supportedcontent(body)



Create a Supported Content profile

Wraps POST /api/v2/conversations/messaging/supportedcontent 

Requires ANY permissions: 

* messaging:supportedContent:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.SupportedContent() # SupportedContent | SupportedContent

try:
    # Create a Supported Content profile
    api_response = api_instance.post_conversations_messaging_supportedcontent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_messaging_supportedcontent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SupportedContent**](SupportedContent.html)| SupportedContent |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="post_conversations_participants_attributes_search"></a>

## [**JsonCursorSearchResponse**](JsonCursorSearchResponse.html) post_conversations_participants_attributes_search(body)



Search conversations

Wraps POST /api/v2/conversations/participants/attributes/search 

Requires ANY permissions: 

* conversation:participant:attributesview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationParticipantSearchRequest() # ConversationParticipantSearchRequest | Search request options

try:
    # Search conversations
    api_response = api_instance.post_conversations_participants_attributes_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_participants_attributes_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationParticipantSearchRequest**](ConversationParticipantSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**JsonCursorSearchResponse**](JsonCursorSearchResponse.html)

<a name="post_conversations_screenshare_participant_communication_wrapup"></a>

##  post_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Apply wrap-up for this conversation communication

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps POST /api/v2/conversations/screenshares/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_screenshare_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_screenshare_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_social_participant_communication_wrapup"></a>

##  post_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/socials/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_social_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_social_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_video_participant_communication_wrapup"></a>

##  post_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)



Apply wrap-up for this conversation communication

Wraps POST /api/v2/conversations/videos/{conversationId}/participants/{participantId}/communications/{communicationId}/wrapup 

Requires ANY permissions: 

* conversation:participant:wrapup

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.WrapupInput() # WrapupInput | Wrap-up (optional)

try:
    # Apply wrap-up for this conversation communication
    api_instance.post_conversations_video_participant_communication_wrapup(conversation_id, participant_id, communication_id, body=body)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_video_participant_communication_wrapup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**WrapupInput**](WrapupInput.html)| Wrap-up | [optional]  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="post_conversations_videos_meetings"></a>

## [**MeetingIdRecord**](MeetingIdRecord.html) post_conversations_videos_meetings(body)



Generate a meetingId for a given conferenceId

post_conversations_videos_meetings is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps POST /api/v2/conversations/videos/meetings 

Requires ANY permissions: 

* video:video:access

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.GenerateMeetingIdRequest() # GenerateMeetingIdRequest | MeetingIdRequest

try:
    # Generate a meetingId for a given conferenceId
    api_response = api_instance.post_conversations_videos_meetings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->post_conversations_videos_meetings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GenerateMeetingIdRequest**](GenerateMeetingIdRequest.html)| MeetingIdRequest |  |
{: class="table table-striped"}

### Return type

[**MeetingIdRecord**](MeetingIdRecord.html)

<a name="put_conversation_participant_flaggedreason"></a>

##  put_conversation_participant_flaggedreason(conversation_id, participant_id)



Set flagged reason on conversation participant to indicate bad conversation quality.

Wraps PUT /api/v2/conversations/{conversationId}/participants/{participantId}/flaggedreason 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
participant_id = 'participant_id_example' # str | participant ID

try:
    # Set flagged reason on conversation participant to indicate bad conversation quality.
    api_instance.put_conversation_participant_flaggedreason(conversation_id, participant_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversation_participant_flaggedreason: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **participant_id** | **str**| participant ID |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="put_conversation_secureattributes"></a>

## str** put_conversation_secureattributes(conversation_id, body)



Set the secure attributes on a conversation.

Wraps PUT /api/v2/conversations/{conversationId}/secureattributes 

Requires ANY permissions: 

* conversation:participant:attributesedit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
body = PureCloudPlatformClientV2.ConversationSecureAttributes() # ConversationSecureAttributes | Conversation Secure Attributes

try:
    # Set the secure attributes on a conversation.
    api_response = api_instance.put_conversation_secureattributes(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversation_secureattributes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **body** | [**ConversationSecureAttributes**](ConversationSecureAttributes.html)| Conversation Secure Attributes |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversation_tags"></a>

## str** put_conversation_tags(conversation_id, body)



Update the tags on a conversation.

Wraps PUT /api/v2/conversations/{conversationId}/tags 

Requires ANY permissions: 

* conversation:externalTag:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversation ID
body = PureCloudPlatformClientV2.ConversationTagsUpdate() # ConversationTagsUpdate | Conversation Tags

try:
    # Update the tags on a conversation.
    api_response = api_instance.put_conversation_tags(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversation_tags: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversation ID |  |
| **body** | [**ConversationTagsUpdate**](ConversationTagsUpdate.html)| Conversation Tags |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_call_participant_communication_uuidata"></a>

## object** put_conversations_call_participant_communication_uuidata(conversation_id, participant_id, communication_id, body)



Set uuiData to be sent on future commands.

Wraps PUT /api/v2/conversations/calls/{conversationId}/participants/{participantId}/communications/{communicationId}/uuidata 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
participant_id = 'participant_id_example' # str | participantId
communication_id = 'communication_id_example' # str | communicationId
body = PureCloudPlatformClientV2.SetUuiDataRequest() # SetUuiDataRequest | UUIData Request

try:
    # Set uuiData to be sent on future commands.
    api_response = api_instance.put_conversations_call_participant_communication_uuidata(conversation_id, participant_id, communication_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_call_participant_communication_uuidata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **participant_id** | **str**| participantId |  |
| **communication_id** | **str**| communicationId |  |
| **body** | [**SetUuiDataRequest**](SetUuiDataRequest.html)| UUIData Request |  |
{: class="table table-striped"}

### Return type

**object**

<a name="put_conversations_call_recordingstate"></a>

## str** put_conversations_call_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/calls/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_call_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_call_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_callback_recordingstate"></a>

## str** put_conversations_callback_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/callbacks/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_callback_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_callback_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_chat_recordingstate"></a>

## str** put_conversations_chat_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/chats/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_chat_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_chat_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_cobrowsesession_recordingstate"></a>

## str** put_conversations_cobrowsesession_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/cobrowsesessions/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_cobrowsesession_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_cobrowsesession_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_email_messages_draft"></a>

## [**EmailMessage**](EmailMessage.html) put_conversations_email_messages_draft(conversation_id, body)



Update conversation draft reply

Wraps PUT /api/v2/conversations/emails/{conversationId}/messages/draft 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.EmailMessage() # EmailMessage | Draft

try:
    # Update conversation draft reply
    api_response = api_instance.put_conversations_email_messages_draft(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_email_messages_draft: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**EmailMessage**](EmailMessage.html)| Draft |  |
{: class="table table-striped"}

### Return type

[**EmailMessage**](EmailMessage.html)

<a name="put_conversations_email_recordingstate"></a>

## str** put_conversations_email_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/emails/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_email_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_email_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_keyconfiguration"></a>

## [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html) put_conversations_keyconfiguration(keyconfigurations_id, body)



Update the encryption key configurations

Wraps PUT /api/v2/conversations/keyconfigurations/{keyconfigurationsId} 

Requires ANY permissions: 

* conversation:encryptionKey:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
keyconfigurations_id = 'keyconfigurations_id_example' # str | Key Configurations Id
body = PureCloudPlatformClientV2.ConversationEncryptionConfiguration() # ConversationEncryptionConfiguration | Encryption key configuration metadata

try:
    # Update the encryption key configurations
    api_response = api_instance.put_conversations_keyconfiguration(keyconfigurations_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_keyconfiguration: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **keyconfigurations_id** | **str**| Key Configurations Id |  |
| **body** | [**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)| Encryption key configuration metadata |  |
{: class="table table-striped"}

### Return type

[**ConversationEncryptionConfiguration**](ConversationEncryptionConfiguration.html)

<a name="put_conversations_message_recordingstate"></a>

## str** put_conversations_message_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/messages/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_message_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_message_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_messaging_integrations_line_integration_id"></a>

## [**LineIntegration**](LineIntegration.html) put_conversations_messaging_integrations_line_integration_id(integration_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a LINE messenger integration (Deprecated)

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-native-line-third-party-messaging-channel/

Wraps PUT /api/v2/conversations/messaging/integrations/line/{integrationId} 

Requires ALL permissions: 

* messaging:integration:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
integration_id = 'integration_id_example' # str | Integration ID
body = PureCloudPlatformClientV2.LineIntegrationRequest() # LineIntegrationRequest | LineIntegrationRequest

try:
    # Update a LINE messenger integration (Deprecated)
    api_response = api_instance.put_conversations_messaging_integrations_line_integration_id(integration_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_messaging_integrations_line_integration_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str**| Integration ID |  |
| **body** | [**LineIntegrationRequest**](LineIntegrationRequest.html)| LineIntegrationRequest |  |
{: class="table table-striped"}

### Return type

[**LineIntegration**](LineIntegration.html)

<a name="put_conversations_messaging_settings_default"></a>

## [**MessagingSetting**](MessagingSetting.html) put_conversations_messaging_settings_default(body)



Set the organization's default setting that may be applied to to integrations without settings

When an integration is created a settings ID may be assigned to it. If the settings ID is not supplied, the default settings will be assigned to it.

Wraps PUT /api/v2/conversations/messaging/settings/default 

Requires ALL permissions: 

* messaging:setting:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.MessagingSettingDefaultRequest() # MessagingSettingDefaultRequest | MessagingSetting

try:
    # Set the organization's default setting that may be applied to to integrations without settings
    api_response = api_instance.put_conversations_messaging_settings_default(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_messaging_settings_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MessagingSettingDefaultRequest**](MessagingSettingDefaultRequest.html)| MessagingSetting |  |
{: class="table table-striped"}

### Return type

[**MessagingSetting**](MessagingSetting.html)

<a name="put_conversations_messaging_supportedcontent_default"></a>

## [**SupportedContent**](SupportedContent.html) put_conversations_messaging_supportedcontent_default(body)



Set the organization's default supported content profile that may be assigned to an integration when it is created.

When an integration is created a supported content ID may be assigned to it. If the supported content ID is not supplied, the default supported content profile will be assigned to it.

Wraps PUT /api/v2/conversations/messaging/supportedcontent/default 

Requires ALL permissions: 

* messaging:supportedContent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.SupportedContentReference() # SupportedContentReference | SupportedContent

try:
    # Set the organization's default supported content profile that may be assigned to an integration when it is created.
    api_response = api_instance.put_conversations_messaging_supportedcontent_default(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_messaging_supportedcontent_default: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SupportedContentReference**](SupportedContentReference.html)| SupportedContent |  |
{: class="table table-striped"}

### Return type

[**SupportedContent**](SupportedContent.html)

<a name="put_conversations_messaging_threadingtimeline"></a>

## [**ConversationThreadingWindow**](ConversationThreadingWindow.html) put_conversations_messaging_threadingtimeline(body)



Update conversation threading window timeline for each messaging type

PUT Conversation messaging threading timeline is intended to set the conversation threading settings for ALL messengerTypes. If you omit a messengerType in the request body then the setting for that messengerType will use the platform default value. The PUT replaces the existing setting(s) that were previously set for each messengerType.

Wraps PUT /api/v2/conversations/messaging/threadingtimeline 

Requires ALL permissions: 

* conversation:threadingTimeline:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
body = PureCloudPlatformClientV2.ConversationThreadingWindow() # ConversationThreadingWindow | ConversationThreadingWindowRequest

try:
    # Update conversation threading window timeline for each messaging type
    api_response = api_instance.put_conversations_messaging_threadingtimeline(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_messaging_threadingtimeline: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ConversationThreadingWindow**](ConversationThreadingWindow.html)| ConversationThreadingWindowRequest |  |
{: class="table table-striped"}

### Return type

[**ConversationThreadingWindow**](ConversationThreadingWindow.html)

<a name="put_conversations_screenshare_recordingstate"></a>

## str** put_conversations_screenshare_recordingstate(conversation_id, body)

<span style="background-color: #f0ad4e;display: inline-block;padding: 7px;font-weight: bold;line-height: 1;color: #ffffff;text-align: center;white-space: nowrap;vertical-align: baseline;border-radius: .25em;margin: 10px 0;">DEPRECATED</span>

Update a conversation by setting its recording state

This endpoint is deprecated. Please see the article https://help.mypurecloud.com/articles/deprecation-legacy-co-browse-and-screenshare/

Wraps PUT /api/v2/conversations/screenshares/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_screenshare_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_screenshare_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_social_recordingstate"></a>

## str** put_conversations_social_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/socials/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_social_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_social_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

<a name="put_conversations_video_recordingstate"></a>

## str** put_conversations_video_recordingstate(conversation_id, body)



Update a conversation by setting its recording state

Wraps PUT /api/v2/conversations/videos/{conversationId}/recordingstate 

Requires ANY permissions: 

* conversation:recording:pauseOthers

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.ConversationsApi()
conversation_id = 'conversation_id_example' # str | conversationId
body = PureCloudPlatformClientV2.SetRecordingState() # SetRecordingState | SetRecordingState

try:
    # Update a conversation by setting its recording state
    api_response = api_instance.put_conversations_video_recordingstate(conversation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->put_conversations_video_recordingstate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **conversation_id** | **str**| conversationId |  |
| **body** | [**SetRecordingState**](SetRecordingState.html)| SetRecordingState |  |
{: class="table table-striped"}

### Return type

**str**

