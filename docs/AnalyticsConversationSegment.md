# AnalyticsConversationSegment

## AnalyticsConversationSegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **audio_muted** | bool | Flag indicating if audio is muted or not (true/false) | [optional] |
| **conference** | bool | Indicates whether the segment was a conference | [optional] |
| **destination_conversation_id** | str | The unique identifier of a new conversation when a conversation is ended for a conference | [optional] |
| **destination_session_id** | str | The unique identifier of a new session when a session is ended for a conference | [optional] |
| **disconnect_type** | str | The session disconnect type | [optional] |
| **error_code** | str | A code corresponding to the error that occurred | [optional] |
| **group_id** | str | Unique identifier for a Genesys Cloud group | [optional] |
| **q850_response_codes** | list[int] | Q.850 response code(s) | [optional] |
| **queue_id** | str | Queue identifier | [optional] |
| **requested_language_id** | str | Unique identifier for the language requested for an interaction | [optional] |
| **requested_routing_skill_ids** | list[str] | Unique identifier(s) for skill(s) requested for an interaction | [optional] |
| **requested_routing_user_ids** | list[str] | Unique identifier(s) for agent(s) requested for an interaction | [optional] |
| **segment_end** | datetime | The end time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **segment_start** | datetime | The start time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **segment_type** | str | The activity that takes place in the segment, such as hold or interact | [optional] |
| **sip_response_codes** | list[int] | SIP response code(s) | [optional] |
| **source_conversation_id** | str | The unique identifier of the previous conversation when a new conversation is created for a conference | [optional] |
| **source_session_id** | str | The unique identifier of the previous session when a new session is created for a conference | [optional] |
| **subject** | str | The subject for the initial email that started this conversation | [optional] |
| **video_muted** | bool | Flag indicating if video is muted/paused or not (true/false) | [optional] |
| **wrap_up_code** | str | Wrap up code | [optional] |
| **wrap_up_note** | str | Note entered by an agent during after-call work | [optional] |
| **wrap_up_tags** | list[str] | Tag(s) assigned during after-call work | [optional] |
| **scored_agents** | [list[AnalyticsScoredAgent]](AnalyticsScoredAgent) | Scored agents | [optional] |
| **properties** | [list[AnalyticsProperty]](AnalyticsProperty) | Additional segment properties | [optional] |



_PureCloudPlatformClientV2 228.0.0_
