# ConversationScreenShareEventTopicScreenShareMediaParticipant

## ConversationScreenShareEventTopicScreenShareMediaParticipant

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
| **user** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **team** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationScreenShareEventTopicErrorBody](ConversationScreenShareEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationScreenShareEventTopicUriReference](ConversationScreenShareEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationScreenShareEventTopicWrapup](ConversationScreenShareEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationScreenShareEventTopicConversationRoutingData](ConversationScreenShareEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationScreenShareEventTopicJourneyContext](ConversationScreenShareEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationScreenShareEventTopicQueueMediaSettings](ConversationScreenShareEventTopicQueueMediaSettings) |  | [optional] |
| **context** | str |  | [optional] |
| **peer_count** | int |  | [optional] |
| **sharing** | bool |  | [optional] |



_PureCloudPlatformClientV2 222.0.0_
