---
title: CallConversationNotificationCallMediaParticipant
---
## CallConversationNotificationCallMediaParticipant

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
| **queue** | [**CallConversationNotificationUriReference**](CallConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**CallConversationNotificationErrorInfo**](CallConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**CallConversationNotificationUriReference**](CallConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**CallConversationNotificationUriReference**](CallConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**CallConversationNotificationUriReference**](CallConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **muted** | **bool** |  | [optional] |
| **confined** | **bool** |  | [optional] |
| **recording** | **bool** |  | [optional] |
| **recording_state** | **str** |  | [optional] |
| **group** | [**CallConversationNotificationUriReference**](CallConversationNotificationUriReference.html) |  | [optional] |
| **ani** | **str** |  | [optional] |
| **dnis** | **str** |  | [optional] |
| **document_id** | **str** |  | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **consult_participant_id** | **str** |  | [optional] |
| **fax_status** | [**CallConversationNotificationFaxStatus**](CallConversationNotificationFaxStatus.html) |  | [optional] |
{: class="table table-striped"}


