# QueueConversationCallEventTopicCallMediaParticipant

## QueueConversationCallEventTopicCallMediaParticipant

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
| **user** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **queue** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **team** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **attributes** | dict(str, str) |  | [optional] |
| **error_info** | [QueueConversationCallEventTopicErrorBody](QueueConversationCallEventTopicErrorBody) |  | [optional] |
| **script** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **wrapup_timeout_ms** | int |  | [optional] |
| **wrapup_skipped** | bool |  | [optional] |
| **alerting_timeout_ms** | int |  | [optional] |
| **provider** | str |  | [optional] |
| **external_contact** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **external_contact_initial_division_id** | str |  | [optional] |
| **external_organization** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **wrapup** | [QueueConversationCallEventTopicWrapup](QueueConversationCallEventTopicWrapup) |  | [optional] |
| **conversation_routing_data** | [QueueConversationCallEventTopicConversationRoutingData](QueueConversationCallEventTopicConversationRoutingData) |  | [optional] |
| **peer** | str |  | [optional] |
| **screen_recording_state** | str |  | [optional] |
| **flagged_reason** | str |  | [optional] |
| **journey_context** | [QueueConversationCallEventTopicJourneyContext](QueueConversationCallEventTopicJourneyContext) |  | [optional] |
| **start_acw_time** | datetime |  | [optional] |
| **end_acw_time** | datetime |  | [optional] |
| **resume_time** | datetime |  | [optional] |
| **park_time** | datetime |  | [optional] |
| **media_roles** | list[str] |  | [optional] |
| **queue_media_settings** | [QueueConversationCallEventTopicQueueMediaSettings](QueueConversationCallEventTopicQueueMediaSettings) |  | [optional] |
| **muted** | bool |  | [optional] |
| **confined** | bool |  | [optional] |
| **recording** | bool |  | [optional] |
| **recording_state** | str |  | [optional] |
| **secure_pause** | bool |  | [optional] |
| **group** | [QueueConversationCallEventTopicUriReference](QueueConversationCallEventTopicUriReference) |  | [optional] |
| **ani** | str |  | [optional] |
| **dnis** | str |  | [optional] |
| **document_id** | str |  | [optional] |
| **monitored_participant_id** | str |  | [optional] |
| **coached_participant_id** | str |  | [optional] |
| **barged_participant_id** | str |  | [optional] |
| **barged_time** | datetime |  | [optional] |
| **consult_participant_id** | str |  | [optional] |
| **fax_status** | [QueueConversationCallEventTopicFaxStatus](QueueConversationCallEventTopicFaxStatus) |  | [optional] |



_PureCloudPlatformClientV2 223.0.0_
