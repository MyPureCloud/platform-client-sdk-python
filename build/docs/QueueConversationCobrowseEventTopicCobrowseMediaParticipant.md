# QueueConversationCobrowseEventTopicCobrowseMediaParticipant

## QueueConversationCobrowseEventTopicCobrowseMediaParticipant

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
| **user** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **queue** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **team** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [QueueConversationCobrowseEventTopicErrorBody](QueueConversationCobrowseEventTopicErrorBody) |  | [optional] |
| **script** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [QueueConversationCobrowseEventTopicUriReference](QueueConversationCobrowseEventTopicUriReference) |  | [optional] |
| **wrapup** | [QueueConversationCobrowseEventTopicWrapup](QueueConversationCobrowseEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [QueueConversationCobrowseEventTopicConversationRoutingData](QueueConversationCobrowseEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [QueueConversationCobrowseEventTopicJourneyContext](QueueConversationCobrowseEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [QueueConversationCobrowseEventTopicQueueMediaSettings](QueueConversationCobrowseEventTopicQueueMediaSettings) |  | [optional] |
| **cobrowse_session_id** | str |  | [optional] |
| **cobrowse_role** | str |  | [optional] |
| **viewer_url** | str |  | [optional] |
| **provider_event_time** | datetime |  | [optional] |
| **controlling** | list[str] |  | [optional] |



_PureCloudPlatformClientV2 227.1.0_
