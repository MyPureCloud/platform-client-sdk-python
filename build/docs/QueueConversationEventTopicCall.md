---
title: QueueConversationEventTopicCall
---
## QueueConversationEventTopicCall

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **recording** | **bool** |  | [optional] |
| **recording_state** | **str** |  | [optional] |
| **muted** | **bool** |  | [optional] |
| **confined** | **bool** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **error_info** | [**QueueConversationEventTopicErrorDetails**](QueueConversationEventTopicErrorDetails.html) |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **direction** | **str** |  | [optional] |
| **document_id** | **str** |  | [optional] |
| **pcSelf** | [**QueueConversationEventTopicAddress**](QueueConversationEventTopicAddress.html) |  | [optional] |
| **other** | [**QueueConversationEventTopicAddress**](QueueConversationEventTopicAddress.html) |  | [optional] |
| **provider** | **str** |  | [optional] |
| **script_id** | **str** |  | [optional] |
| **peer_id** | **str** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **disconnected_time** | **datetime** |  | [optional] |
| **disconnect_reasons** | [**list[QueueConversationEventTopicDisconnectReason]**](QueueConversationEventTopicDisconnectReason.html) |  | [optional] |
| **fax_status** | [**QueueConversationEventTopicFaxStatus**](QueueConversationEventTopicFaxStatus.html) |  | [optional] |
| **uui_data** | **str** |  | [optional] |
| **wrapup** | [**QueueConversationEventTopicWrapup**](QueueConversationEventTopicWrapup.html) |  | [optional] |
| **after_call_work** | [**QueueConversationEventTopicAfterCallWork**](QueueConversationEventTopicAfterCallWork.html) |  | [optional] |
| **after_call_work_required** | **bool** |  | [optional] |
| **agent_assistant_id** | **str** |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


