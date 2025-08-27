# V2QueueObservationObservation

## V2QueueObservationObservation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **observation_date** | datetime | The timestamp when the observation started | [optional] |
| **conversation_id** | str | Unique identifier of the conversation to which this observation belongs | [optional] |
| **session_id** | str | Unique identifier of the user session associated with this observation | [optional] |
| **requested_routing_skill_ids** | list[str] | Unique identifiers for skills requested for an interaction | [optional] |
| **requested_language_id** | str | Unique identifier for the language requested for an interaction | [optional] |
| **routing_priority** | int | Routing priority for the current interaction | [optional] |
| **participant_name** | str | A human readable name identifying the participant | [optional] |
| **user_id** | str | Unique identifier for the user | [optional] |
| **direction** | str | The direction of the communication | [optional] |
| **converted_from** | str | Session media type that was converted from in case of a media type conversion | [optional] |
| **converted_to** | str | Session media type that was converted to in case of a media type conversion | [optional] |
| **address_from** | str | The address that initiated an action | [optional] |
| **address_to** | str | The address receiving an action | [optional] |
| **ani** | str | Automatic Number Identification (caller&#39;s number) | [optional] |
| **dnis** | str | Dialed number identification service (number dialed by the calling party) | [optional] |
| **team_id** | str | The team Id the user is a member of | [optional] |
| **scored_agents** | [list[V2QueueObservationScoredAgent]](V2QueueObservationScoredAgent) | Scored agents for this conversation | [optional] |
| **requested_routings** | list[str] | All routing types for requested/attempted routing methods. | [optional] |
| **used_routing** | str | Complete routing method | [optional] |



_PureCloudPlatformClientV2 236.0.0_
