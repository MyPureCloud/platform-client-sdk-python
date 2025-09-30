# QueueConversationChatEventTopicChatMediaParticipant

## QueueConversationChatEventTopicChatMediaParticipant

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
| **user** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **queue** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **team** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [QueueConversationChatEventTopicErrorBody](QueueConversationChatEventTopicErrorBody) |  | [optional] |
| **script** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [QueueConversationChatEventTopicUriReference](QueueConversationChatEventTopicUriReference) |  | [optional] |
| **wrapup** | [QueueConversationChatEventTopicWrapup](QueueConversationChatEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [QueueConversationChatEventTopicConversationRoutingData](QueueConversationChatEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [QueueConversationChatEventTopicJourneyContext](QueueConversationChatEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [QueueConversationChatEventTopicQueueMediaSettings](QueueConversationChatEventTopicQueueMediaSettings) |  | [optional] |
| **room_id** | str |  | [optional] |
| **avatar_image_url** | str |  | [optional] |



_PureCloudPlatformClientV2 239.0.0_
