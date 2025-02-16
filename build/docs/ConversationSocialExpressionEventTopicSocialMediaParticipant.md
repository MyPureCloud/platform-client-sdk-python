# ConversationSocialExpressionEventTopicSocialMediaParticipant

## ConversationSocialExpressionEventTopicSocialMediaParticipant

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
| **user** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **team** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationSocialExpressionEventTopicErrorBody](ConversationSocialExpressionEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationSocialExpressionEventTopicUriReference](ConversationSocialExpressionEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationSocialExpressionEventTopicWrapup](ConversationSocialExpressionEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationSocialExpressionEventTopicConversationRoutingData](ConversationSocialExpressionEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationSocialExpressionEventTopicJourneyContext](ConversationSocialExpressionEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationSocialExpressionEventTopicQueueMediaSettings](ConversationSocialExpressionEventTopicQueueMediaSettings) |  | [optional] |
| **social_media_id** | str |  | [optional] |
| **social_media_hub** | str |  | [optional] |
| **social_user_name** | str |  | [optional] |
| **preview_text** | str |  | [optional] |



_PureCloudPlatformClientV2 222.0.0_
