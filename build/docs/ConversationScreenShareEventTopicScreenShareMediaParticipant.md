---
title: ConversationScreenShareEventTopicScreenShareMediaParticipant
---
## ConversationScreenShareEventTopicScreenShareMediaParticipant

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
| **user** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **team** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationScreenShareEventTopicErrorBody**](ConversationScreenShareEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationScreenShareEventTopicUriReference**](ConversationScreenShareEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationScreenShareEventTopicWrapup**](ConversationScreenShareEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**ConversationScreenShareEventTopicConversationRoutingData**](ConversationScreenShareEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationScreenShareEventTopicJourneyContext**](ConversationScreenShareEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **media_roles** | **list[str]** |  | [optional] |
| **context** | **str** |  | [optional] |
| **peer_count** | **int** |  | [optional] |
| **sharing** | **bool** |  | [optional] |
{: class="table table-striped"}


