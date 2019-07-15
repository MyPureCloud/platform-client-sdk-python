---
title: ConversationMessageEventTopicMessageMediaParticipant
---
## ConversationMessageEventTopicMessageMediaParticipant

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
| **user** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationMessageEventTopicErrorBody**](ConversationMessageEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationMessageEventTopicUriReference**](ConversationMessageEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationMessageEventTopicWrapup**](ConversationMessageEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**ConversationMessageEventTopicConversationRoutingData**](ConversationMessageEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationMessageEventTopicJourneyContext**](ConversationMessageEventTopicJourneyContext.html) |  | [optional] |
| **messages** | [**list[ConversationMessageEventTopicMessageDetails]**](ConversationMessageEventTopicMessageDetails.html) |  | [optional] |
| **type** | **str** |  | [optional] |
| **recipient_country** | **str** |  | [optional] |
| **recipient_type** | **str** |  | [optional] |
{: class="table table-striped"}


