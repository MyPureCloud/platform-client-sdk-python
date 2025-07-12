# ConversationVideoEventTopicVideoMediaParticipant

## ConversationVideoEventTopicVideoMediaParticipant

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
| **user** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **team** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationVideoEventTopicErrorBody](ConversationVideoEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationVideoEventTopicUriReference](ConversationVideoEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationVideoEventTopicWrapup](ConversationVideoEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationVideoEventTopicConversationRoutingData](ConversationVideoEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationVideoEventTopicJourneyContext](ConversationVideoEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationVideoEventTopicQueueMediaSettings](ConversationVideoEventTopicQueueMediaSettings) |  | [optional] |
| **audio_muted** | bool |  | [optional] |
| **video_muted** | bool |  | [optional] |
| **sharing_screen** | bool |  | [optional] |
| **peer_count** | int |  | [optional] |
| **context** | str |  | [optional] |
| **msids** | list[str] |  | [optional] |



_PureCloudPlatformClientV2 233.0.0_
