---
title: ConversationVideoEventTopicVideoMediaParticipant
---
## ConversationVideoEventTopicVideoMediaParticipant

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
| **user** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **team** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationVideoEventTopicErrorBody**](ConversationVideoEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationVideoEventTopicUriReference**](ConversationVideoEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationVideoEventTopicWrapup**](ConversationVideoEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**ConversationVideoEventTopicConversationRoutingData**](ConversationVideoEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationVideoEventTopicJourneyContext**](ConversationVideoEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **audio_muted** | **bool** |  | [optional] |
| **video_muted** | **bool** |  | [optional] |
| **sharing_screen** | **bool** |  | [optional] |
| **peer_count** | **int** |  | [optional] |
| **context** | **str** |  | [optional] |
| **msids** | **list[str]** |  | [optional] |
{: class="table table-striped"}


