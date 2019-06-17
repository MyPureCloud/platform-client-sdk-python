---
title: QueueConversationEmailEventTopicEmailMediaParticipant
---
## QueueConversationEmailEventTopicEmailMediaParticipant

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
| **user** | [**QueueConversationEmailEventTopicUriReference**](QueueConversationEmailEventTopicUriReference.html) |  | [optional] |
| **queue** | [**QueueConversationEmailEventTopicUriReference**](QueueConversationEmailEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**QueueConversationEmailEventTopicErrorBody**](QueueConversationEmailEventTopicErrorBody.html) |  | [optional] |
| **script** | [**QueueConversationEmailEventTopicUriReference**](QueueConversationEmailEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**QueueConversationEmailEventTopicUriReference**](QueueConversationEmailEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**QueueConversationEmailEventTopicUriReference**](QueueConversationEmailEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**QueueConversationEmailEventTopicWrapup**](QueueConversationEmailEventTopicWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **journey_context** | [**QueueConversationEmailEventTopicJourneyContext**](QueueConversationEmailEventTopicJourneyContext.html) |  | [optional] |
| **subject** | **str** |  | [optional] |
| **messages_sent** | **int** |  | [optional] |
| **auto_generated** | **bool** |  | [optional] |
| **message_id** | **str** |  | [optional] |
| **draft_attachments** | [**list[QueueConversationEmailEventTopicAttachment]**](QueueConversationEmailEventTopicAttachment.html) |  | [optional] |
| **spam** | **bool** |  | [optional] |
{: class="table table-striped"}


