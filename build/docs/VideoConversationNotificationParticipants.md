---
title: VideoConversationNotificationParticipants
---
## VideoConversationNotificationParticipants

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
| **queue** | [**VideoConversationNotificationUriReference**](VideoConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**VideoConversationNotificationErrorInfo**](VideoConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**VideoConversationNotificationUriReference**](VideoConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**VideoConversationNotificationUriReference**](VideoConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**VideoConversationNotificationUriReference**](VideoConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **audio_muted** | **bool** |  | [optional] |
| **video_muted** | **bool** |  | [optional] |
| **sharing_screen** | **bool** |  | [optional] |
| **peer_count** | **int** |  | [optional] |
| **context** | **str** |  | [optional] |
{: class="table table-striped"}


