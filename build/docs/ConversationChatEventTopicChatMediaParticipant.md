---
title: ConversationChatEventTopicChatMediaParticipant
---
## ConversationChatEventTopicChatMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **address** | **str** |  | [optional] |
| **start_time** | **datetime** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **end_time** | **datetime** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **purpose** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **initial_state** | **str** |  | [optional] |
| **direction** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **wrapup_required** | **bool** |  | [optional] |
| **wrapup_prompt** | **str** |  | [optional] |
| **user** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **team** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationChatEventTopicErrorBody**](ConversationChatEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationChatEventTopicUriReference**](ConversationChatEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationChatEventTopicWrapup**](ConversationChatEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**ConversationChatEventTopicConversationRoutingData**](ConversationChatEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationChatEventTopicJourneyContext**](ConversationChatEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **resume_time** | **datetime** |  | [optional] |
| **media_roles** | **list[str]** |  | [optional] |
| **queue_media_settings** | [**ConversationChatEventTopicQueueMediaSettings**](ConversationChatEventTopicQueueMediaSettings.html) |  | [optional] |
| **room_id** | **str** |  | [optional] |
| **avatar_image_url** | **str** |  | [optional] |
{: class="table table-striped"}


