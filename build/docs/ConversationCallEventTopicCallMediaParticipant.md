---
title: ConversationCallEventTopicCallMediaParticipant
---
## ConversationCallEventTopicCallMediaParticipant

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
| **user** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationCallEventTopicErrorBody**](ConversationCallEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationCallEventTopicWrapup**](ConversationCallEventTopicWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**ConversationCallEventTopicJourneyContext**](ConversationCallEventTopicJourneyContext.html) |  | [optional] |
| **muted** | **bool** |  | [optional] |
| **confined** | **bool** |  | [optional] |
| **recording** | **bool** |  | [optional] |
| **recording_state** | **str** |  | [optional] |
| **group** | [**ConversationCallEventTopicUriReference**](ConversationCallEventTopicUriReference.html) |  | [optional] |
| **ani** | **str** |  | [optional] |
| **dnis** | **str** |  | [optional] |
| **document_id** | **str** |  | [optional] |
| **monitored_participant_id** | **str** |  | [optional] |
| **consult_participant_id** | **str** |  | [optional] |
| **fax_status** | [**ConversationCallEventTopicFaxStatus**](ConversationCallEventTopicFaxStatus.html) |  | [optional] |
{: class="table table-striped"}


