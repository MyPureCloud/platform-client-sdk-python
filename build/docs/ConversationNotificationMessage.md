---
title: ConversationNotificationMessage
---
## ConversationNotificationMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **script_id** | **str** |  | [optional] |
| **peer_id** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **disconnected_time** | **datetime** |  | [optional] |
| **to_address** | [**ConversationNotificationAddress**](ConversationNotificationAddress.html) |  | [optional] |
| **from_address** | [**ConversationNotificationAddress**](ConversationNotificationAddress.html) |  | [optional] |
| **messages** | [**list[ConversationNotificationMessages]**](ConversationNotificationMessages.html) |  | [optional] |
| **messages_transcript_uri** | **str** |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


