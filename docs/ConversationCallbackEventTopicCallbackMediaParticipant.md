# ConversationCallbackEventTopicCallbackMediaParticipant

## ConversationCallbackEventTopicCallbackMediaParticipant

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
| **user** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **team** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationCallbackEventTopicErrorBody](ConversationCallbackEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationCallbackEventTopicUriReference](ConversationCallbackEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationCallbackEventTopicWrapup](ConversationCallbackEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationCallbackEventTopicConversationRoutingData](ConversationCallbackEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationCallbackEventTopicJourneyContext](ConversationCallbackEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationCallbackEventTopicQueueMediaSettings](ConversationCallbackEventTopicQueueMediaSettings) |  | [optional] |
| **outbound_preview** | [ConversationCallbackEventTopicDialerPreview](ConversationCallbackEventTopicDialerPreview) |  | [optional] |
| **voicemail** | [ConversationCallbackEventTopicVoicemail](ConversationCallbackEventTopicVoicemail) |  | [optional] |
| **callback_numbers** | list[str] |  | [optional] |
| **callback_user_name** | str |  | [optional] |
| **skip_enabled** | bool |  | [optional] |
| **external_campaign** | bool |  | [optional] |
| **timeout_seconds** | int |  | [optional] |
| **callback_scheduled_time** | datetime |  | [optional] |
| **automated_callback_config_id** | str |  | [optional] |



_PureCloudPlatformClientV2 219.0.0_
