# QueueConversationMessageEventTopicMessageMediaParticipant

## QueueConversationMessageEventTopicMessageMediaParticipant

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
| **user** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **queue** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **team** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [QueueConversationMessageEventTopicErrorBody](QueueConversationMessageEventTopicErrorBody) |  | [optional] |
| **script** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [QueueConversationMessageEventTopicUriReference](QueueConversationMessageEventTopicUriReference) |  | [optional] |
| **wrapup** | [QueueConversationMessageEventTopicWrapup](QueueConversationMessageEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [QueueConversationMessageEventTopicConversationRoutingData](QueueConversationMessageEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [QueueConversationMessageEventTopicJourneyContext](QueueConversationMessageEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [QueueConversationMessageEventTopicQueueMediaSettings](QueueConversationMessageEventTopicQueueMediaSettings) |  | [optional] |
| **messages** | [list[QueueConversationMessageEventTopicMessageDetails]](QueueConversationMessageEventTopicMessageDetails) |  | [optional] |
| **type** | str |  | [optional] |
| **recipient_country** | str |  | [optional] |
| **recipient_type** | str |  | [optional] |
| **byo_sms_integration_id** | str |  | [optional] |
| **engagement_source** | str |  | [optional] |
| **monitored_participant_id** | str |  | [optional] |



_PureCloudPlatformClientV2 240.0.0_
