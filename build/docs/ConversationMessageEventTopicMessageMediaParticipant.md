# ConversationMessageEventTopicMessageMediaParticipant

## ConversationMessageEventTopicMessageMediaParticipant

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
| **user** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **team** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationMessageEventTopicErrorBody](ConversationMessageEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationMessageEventTopicUriReference](ConversationMessageEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationMessageEventTopicWrapup](ConversationMessageEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationMessageEventTopicConversationRoutingData](ConversationMessageEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationMessageEventTopicJourneyContext](ConversationMessageEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationMessageEventTopicQueueMediaSettings](ConversationMessageEventTopicQueueMediaSettings) |  | [optional] |
| **messages** | [list[ConversationMessageEventTopicMessageDetails]](ConversationMessageEventTopicMessageDetails) |  | [optional] |
| **type** | str |  | [optional] |
| **recipient_country** | str |  | [optional] |
| **recipient_type** | str |  | [optional] |
| **byo_sms_integration_id** | str |  | [optional] |
| **monitored_participant_id** | str |  | [optional] |



_PureCloudPlatformClientV2 234.0.0_
