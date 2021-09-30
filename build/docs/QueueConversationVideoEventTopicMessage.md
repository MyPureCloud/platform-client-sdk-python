---
title: QueueConversationVideoEventTopicMessage
---
## QueueConversationVideoEventTopicMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **error_info** | [**QueueConversationVideoEventTopicErrorDetails**](QueueConversationVideoEventTopicErrorDetails.html) |  | [optional] |
| **provider** | **str** |  | [optional] |
| **script_id** | **str** |  | [optional] |
| **peer_id** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **disconnected_time** | **datetime** |  | [optional] |
| **to_address** | [**QueueConversationVideoEventTopicAddress**](QueueConversationVideoEventTopicAddress.html) |  | [optional] |
| **from_address** | [**QueueConversationVideoEventTopicAddress**](QueueConversationVideoEventTopicAddress.html) |  | [optional] |
| **messages** | [**list[QueueConversationVideoEventTopicMessageDetails]**](QueueConversationVideoEventTopicMessageDetails.html) |  | [optional] |
| **messages_transcript_uri** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **recipient_country** | **str** |  | [optional] |
| **recipient_type** | **str** |  | [optional] |
| **journey_context** | [**QueueConversationVideoEventTopicJourneyContext**](QueueConversationVideoEventTopicJourneyContext.html) |  | [optional] |
| **wrapup** | [**QueueConversationVideoEventTopicWrapup**](QueueConversationVideoEventTopicWrapup.html) |  | [optional] |
| **after_call_work** | [**QueueConversationVideoEventTopicAfterCallWork**](QueueConversationVideoEventTopicAfterCallWork.html) |  | [optional] |
| **after_call_work_required** | **bool** |  | [optional] |
| **agent_assistant_id** | **str** |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


