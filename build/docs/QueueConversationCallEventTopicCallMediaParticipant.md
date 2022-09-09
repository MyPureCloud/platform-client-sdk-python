---
title: QueueConversationCallEventTopicCallMediaParticipant
---
## QueueConversationCallEventTopicCallMediaParticipant

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
| **user** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **queue** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **team** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**QueueConversationCallEventTopicErrorBody**](QueueConversationCallEventTopicErrorBody.html) |  | [optional] |
| **script** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**QueueConversationCallEventTopicWrapup**](QueueConversationCallEventTopicWrapup.html) |  | [optional] |
| **conversation_routing_data** | [**QueueConversationCallEventTopicConversationRoutingData**](QueueConversationCallEventTopicConversationRoutingData.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**QueueConversationCallEventTopicJourneyContext**](QueueConversationCallEventTopicJourneyContext.html) |  | [optional] |
| **start_acw_time** | **datetime** |  | [optional] |
| **end_acw_time** | **datetime** |  | [optional] |
| **muted** | **bool** |  | [optional] |
| **confined** | **bool** |  | [optional] |
| **recording** | **bool** |  | [optional] |
| **recording_state** | **str** |  | [optional] |
| **group** | [**QueueConversationCallEventTopicUriReference**](QueueConversationCallEventTopicUriReference.html) |  | [optional] |
| **ani** | **str** |  | [optional] |
| **dnis** | **str** |  | [optional] |
| **document_id** | **str** |  | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **coached_participant_id** | **str** |  | [optional] |
| **barged_participant_id** | **str** |  | [optional] |
| **barged_time** | **datetime** |  | [optional] |
| **consult_participant_id** | **str** |  | [optional] |
| **fax_status** | [**QueueConversationCallEventTopicFaxStatus**](QueueConversationCallEventTopicFaxStatus.html) |  | [optional] |
{: class="table table-striped"}


