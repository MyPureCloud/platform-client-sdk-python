# ConversationCallEventTopicCallMediaParticipant

## ConversationCallEventTopicCallMediaParticipant

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
| **user** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **queue** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **team** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [ConversationCallEventTopicErrorBody](ConversationCallEventTopicErrorBody) |  | [optional] |
| **script** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **wrapup** | [ConversationCallEventTopicWrapup](ConversationCallEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [ConversationCallEventTopicConversationRoutingData](ConversationCallEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [ConversationCallEventTopicJourneyContext](ConversationCallEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [ConversationCallEventTopicQueueMediaSettings](ConversationCallEventTopicQueueMediaSettings) |  | [optional] |
| **muted** | bool |  | [optional] |
| **confined** | bool |  | [optional] |
| **recording** | bool |  | [optional] |
| **recording_state** | str |  | [optional] |
| **secure_pause** | bool |  | [optional] |
| **group** | [ConversationCallEventTopicUriReference](ConversationCallEventTopicUriReference) |  | [optional] |
| **ani** | str |  | [optional] |
| **dnis** | str |  | [optional] |
| **document_id** | str |  | [optional] |
| **monitored_participant_id** | str |  | [optional] |
| **coached_participant_id** | str |  | [optional] |
| **barged_participant_id** | str |  | [optional] |
| **barged_time** | datetime |  | [optional] |
| **consult_participant_id** | str |  | [optional] |
| **fax_status** | [ConversationCallEventTopicFaxStatus](ConversationCallEventTopicFaxStatus) |  | [optional] |



_PureCloudPlatformClientV2 219.1.0_
