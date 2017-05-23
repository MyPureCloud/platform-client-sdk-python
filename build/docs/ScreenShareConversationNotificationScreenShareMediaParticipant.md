---
title: ScreenShareConversationNotificationScreenShareMediaParticipant
---
## ScreenShareConversationNotificationScreenShareMediaParticipant

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
| **queue** | [**ScreenShareConversationNotificationUriReference**](ScreenShareConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ScreenShareConversationNotificationErrorInfo**](ScreenShareConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**ScreenShareConversationNotificationUriReference**](ScreenShareConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ScreenShareConversationNotificationUriReference**](ScreenShareConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**ScreenShareConversationNotificationUriReference**](ScreenShareConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **context** | **str** |  | [optional] |
| **peer_count** | **int** |  | [optional] |
| **sharing** | **bool** |  | [optional] |
{: class="table table-striped"}


