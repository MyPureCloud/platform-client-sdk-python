---
title: ConversationCallbackEventTopicCallbackMediaParticipant
---
## ConversationCallbackEventTopicCallbackMediaParticipant

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
| **direction** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **wrapup_required** | **bool** |  | [optional] |
| **wrapup_prompt** | **str** |  | [optional] |
| **user** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **team** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationCallbackEventTopicErrorBody**](ConversationCallbackEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationCallbackEventTopicUriReference**](ConversationCallbackEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationCallbackEventTopicWrapup**](ConversationCallbackEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**ConversationCallbackEventTopicConversationRoutingData**](ConversationCallbackEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationCallbackEventTopicJourneyContext**](ConversationCallbackEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **outbound_preview** | [**ConversationCallbackEventTopicDialerPreview**](ConversationCallbackEventTopicDialerPreview.html) |  | [optional] |
| **voicemail** | [**ConversationCallbackEventTopicVoicemail**](ConversationCallbackEventTopicVoicemail.html) |  | [optional] |
| **callback_numbers** | **list[str]** |  | [optional] |
| **callback_user_name** | **str** |  | [optional] |
| **skip_enabled** | **bool** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **callback_scheduled_time** | **datetime** |  | [optional] |
| **automated_callback_config_id** | **str** |  | [optional] |
{: class="table table-striped"}


