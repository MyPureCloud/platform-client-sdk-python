# QueueConversationEmailEventTopicEmailMediaParticipant

## QueueConversationEmailEventTopicEmailMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str |  | [optional] |
| **name** | str |  | [optional] |
| **address** | str |  | [optional] |
| **start_time** | datetime |  | [optional] |
| **connected_time** | datetime |  | [optional] |
| **end_time** | datetime |  | [optional] |
| **start_hold_time** | datetime |  | [optional] |
| **purpose** | str |  | [optional] |
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **direction** | str |  | [optional] |
| **disconnect_type** | str |  | [optional] |
| **held** | bool |  | [optional] |
| **wrapup_required** | bool |  | [optional] |
| **wrapup_prompt** | str |  | [optional] |
| **user** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **queue** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **team** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [QueueConversationEmailEventTopicErrorBody](QueueConversationEmailEventTopicErrorBody) |  | [optional] |
| **script** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **external_organization** | [QueueConversationEmailEventTopicUriReference](QueueConversationEmailEventTopicUriReference) |  | [optional] |
| **wrapup** | [QueueConversationEmailEventTopicWrapup](QueueConversationEmailEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [QueueConversationEmailEventTopicConversationRoutingData](QueueConversationEmailEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [QueueConversationEmailEventTopicJourneyContext](QueueConversationEmailEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [QueueConversationEmailEventTopicQueueMediaSettings](QueueConversationEmailEventTopicQueueMediaSettings) |  | [optional] |
| **subject** | str |  | [optional] |
| **messages_sent** | int |  | [optional] |
| **auto_generated** | bool |  | [optional] |
| **message_id** | str |  | [optional] |
| **draft_attachments** | [list[QueueConversationEmailEventTopicAttachment]](QueueConversationEmailEventTopicAttachment) |  | [optional] |
| **spam** | bool |  | [optional] |



_PureCloudPlatformClientV2 210.0.0_
