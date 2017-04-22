---
title: CallbackConversationNotificationParticipants
---
## CallbackConversationNotificationParticipants

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
| **user** | [**DependencyTrackingBuildNotificationNotificationUser**](DependencyTrackingBuildNotificationNotificationUser.html) |  | [optional] |
| **queue** | [**CallbackConversationNotificationUriReference**](CallbackConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**CallbackConversationNotificationErrorInfo**](CallbackConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**CallbackConversationNotificationUriReference**](CallbackConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**CallbackConversationNotificationUriReference**](CallbackConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**CallbackConversationNotificationUriReference**](CallbackConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **outbound_preview** | [**ConversationNotificationDialerPreview**](ConversationNotificationDialerPreview.html) |  | [optional] |
| **callback_numbers** | **list[str]** |  | [optional] |
| **callback_user_name** | **str** |  | [optional] |
| **skip_enabled** | **bool** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **callback_scheduled_time** | **datetime** |  | [optional] |
| **automated_callback_config_id** | **str** |  | [optional] |
{: class="table table-striped"}


