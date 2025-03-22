# ConversationCobrowseEventTopicCobrowseMediaParticipant

## ConversationCobrowseEventTopicCobrowseMediaParticipant

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
| **user** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **team** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationCobrowseEventTopicErrorBody](ConversationCobrowseEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationCobrowseEventTopicUriReference](ConversationCobrowseEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationCobrowseEventTopicWrapup](ConversationCobrowseEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationCobrowseEventTopicConversationRoutingData](ConversationCobrowseEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationCobrowseEventTopicJourneyContext](ConversationCobrowseEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationCobrowseEventTopicQueueMediaSettings](ConversationCobrowseEventTopicQueueMediaSettings) |  | [optional] |
| **cobrowse_session_id** | str |  | [optional] |
| **cobrowse_role** | str |  | [optional] |
| **viewer_url** | str |  | [optional] |
| **provider_event_time** | datetime |  | [optional] |
| **controlling** | list[str] |  | [optional] |



_PureCloudPlatformClientV2 224.0.0_
