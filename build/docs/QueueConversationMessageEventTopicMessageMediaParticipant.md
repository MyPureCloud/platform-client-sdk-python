---
title: QueueConversationMessageEventTopicMessageMediaParticipant
---
## QueueConversationMessageEventTopicMessageMediaParticipant

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
| **user** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **queue** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **team** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**QueueConversationMessageEventTopicErrorBody**](QueueConversationMessageEventTopicErrorBody.html) |  | [optional] |
| **script** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**QueueConversationMessageEventTopicUriReference**](QueueConversationMessageEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**QueueConversationMessageEventTopicWrapup**](QueueConversationMessageEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**QueueConversationMessageEventTopicConversationRoutingData**](QueueConversationMessageEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**QueueConversationMessageEventTopicJourneyContext**](QueueConversationMessageEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **messages** | [**list[QueueConversationMessageEventTopicMessageDetails]**](QueueConversationMessageEventTopicMessageDetails.html) |  | [optional] |
| **type** | **str** |  | [optional] |
| **recipient_country** | **str** |  | [optional] |
| **recipient_type** | **str** |  | [optional] |
{: class="table table-striped"}


