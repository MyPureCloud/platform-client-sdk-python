---
title: ConversationEventTopicCall
---
## ConversationEventTopicCall

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
| **error_info** | [**ConversationEventTopicErrorDetails**](ConversationEventTopicErrorDetails.html) |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **direction** | **str** |  | [optional] |
| **document_id** | **str** |  | [optional] |
| **pcSelf** | [**ConversationEventTopicAddress**](ConversationEventTopicAddress.html) |  | [optional] |
| **other** | [**ConversationEventTopicAddress**](ConversationEventTopicAddress.html) |  | [optional] |
| **provider** | **str** |  | [optional] |
| **script_id** | **str** |  | [optional] |
| **peer_id** | **str** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **disconnected_time** | **datetime** |  | [optional] |
| **disconnect_reasons** | [**list[ConversationEventTopicDisconnectReason]**](ConversationEventTopicDisconnectReason.html) |  | [optional] |
| **fax_status** | [**ConversationEventTopicFaxStatus**](ConversationEventTopicFaxStatus.html) |  | [optional] |
| **uui_data** | **str** |  | [optional] |
| **wrapup** | [**ConversationEventTopicWrapup**](ConversationEventTopicWrapup.html) |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


