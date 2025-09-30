# FlowActivityEntityData

## FlowActivityEntityData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **activity_date** | datetime | The time at which the activity was observed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **metric** | str | Activity metric | [optional] |
| **active_routing** | str | Active routing method | [optional] |
| **address_from** | str | The address that initiated an action | [optional] |
| **address_to** | str | The address receiving an action | [optional] |
| **ani** | str | Automatic Number Identification (caller&#39;s number) | [optional] |
| **conversation_id** | str | Unique identifier for the conversation | [optional] |
| **converted_from** | str | Session media type that was converted from in case of a media type conversion | [optional] |
| **converted_to** | str | Session media type that was converted to in case of a media type conversion | [optional] |
| **direction** | str | The direction of the communication | [optional] |
| **dnis** | str | Dialed number identification service (number dialed by the calling party) | [optional] |
| **flow_id** | str | The unique identifier of this flow | [optional] |
| **flow_type** | str | The type of this flow | [optional] |
| **media_type** | str | The session media type | [optional] |
| **participant_name** | str | A human readable name identifying the participant | [optional] |
| **queue_id** | str | Queue identifier | [optional] |
| **requested_language_id** | str | Unique identifier for the language requested for an interaction | [optional] |
| **requested_routing_skill_ids** | list[str] | Unique identifier(s) for skill(s) requested for an interaction | [optional] |
| **requested_routings** | list[str] | Routing type(s) for requested/attempted routing methods. | [optional] |
| **routing_priority** | int | Routing priority for the current interaction | [optional] |
| **session_id** | str | The unique identifier of this session | [optional] |
| **team_id** | str | The team ID the user is a member of | [optional] |
| **used_routing** | str | Complete routing method | [optional] |
| **user_id** | str | Unique identifier for the user | [optional] |
| **scored_agents** | [list[FlowActivityScoredAgent]](FlowActivityScoredAgent) | Scored agents | [optional] |



_PureCloudPlatformClientV2 239.0.0_
