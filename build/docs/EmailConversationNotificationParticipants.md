---
title: EmailConversationNotificationParticipants
---
## EmailConversationNotificationParticipants

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
| **user** | [**DocumentDataV2NotificationCreatedBy**](DocumentDataV2NotificationCreatedBy.html) |  | [optional] |
| **queue** | [**EmailConversationNotificationUriReference**](EmailConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**EmailConversationNotificationErrorInfo**](EmailConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**EmailConversationNotificationUriReference**](EmailConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**EmailConversationNotificationUriReference**](EmailConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**EmailConversationNotificationUriReference**](EmailConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **subject** | **str** |  | [optional] |
| **messages_sent** | **int** |  | [optional] |
| **auto_generated** | **bool** |  | [optional] |
| **message_id** | **str** |  | [optional] |
{: class="table table-striped"}


