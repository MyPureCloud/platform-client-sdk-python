# Participant

## Participant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this conversation. | [optional] |
| **start_time** | datetime | The timestamp when this participant joined the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_time** | datetime | The timestamp when this participant disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **connected_time** | datetime | The timestamp when this participant was connected to the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **name** | str | A human readable name identifying the participant. | [optional] |
| **user_uri** | str | If this participant represents a user, then this will be an URI that can be used to fetch the user. | [optional] |
| **user_id** | str | If this participant represents a user, then this will be the globally unique identifier for the user. | [optional] |
| **external_contact_id** | str | If this participant represents an external contact, then this will be the globally unique identifier for the external contact. | [optional] |
| **external_contact_initial_division_id** | str | If this participant represents an external contact, then this will be the initial division for the external contact. This value will not be updated if the external contact is reassigned. | [optional] |
| **external_organization_id** | str | If this participant represents an external org, then this will be the globally unique identifier for the external org. | [optional] |
| **queue_id** | str | If present, the queue id that the communication channel came in on. | [optional] |
| **group_id** | str | If present, group of users the participant represents. | [optional] |
| **team_id** | str | The team id that this participant is a member of when added to the conversation. | [optional] |
| **queue_name** | str | If present, the queue name that the communication channel came in on. | [optional] |
| **purpose** | str | A well known string that specifies the purpose of this participant. | [optional] |
| **participant_type** | str | A well known string that specifies the type of this participant. | [optional] |
| **consult_participant_id** | str | If this participant is part of a consult transfer, then this will be the participant id of the participant being transferred. | [optional] |
| **address** | str | The address for the this participant. For a phone call this will be the ANI. | [optional] |
| **ani** | str | The address for the this participant. For a phone call this will be the ANI. | [optional] |
| **ani_name** | str | The ani-based name for this participant. | [optional] |
| **dnis** | str | The address for the this participant. For a phone call this will be the ANI. | [optional] |
| **locale** | str | An ISO 639 language code specifying the locale for this participant | [optional] |
| **wrapup_required** | bool | True iff this participant is required to enter wrapup for this conversation. | [optional] |
| **wrapup_prompt** | str | This field controls how the UI prompts the agent for a wrapup. | [optional] |
| **wrapup_timeout_ms** | int | Specifies how long a timed ACW session will last. | [optional] |
| **wrapup_skipped** | bool | The UI sets this field when the agent chooses to skip entering a wrapup for this participant. | [optional] |
| **wrapup** | [Wrapup](Wrapup) | Call wrap up or disposition data. | [optional] |
| **media_roles** | list[str] | List of roles this participant&#39;s media has had on the conversation, ie monitor, coach, etc. | [optional] |
| **conversation_routing_data** | [ConversationRoutingData](ConversationRoutingData) | Information on how a communication should be routed to an agent. | [optional] |
| **alerting_timeout_ms** | int | Specifies how long the agent has to answer an interaction before being marked as not responding. | [optional] |
| **monitored_participant_id** | str | If this participant is a monitor, then this will be the id of the participant that is being monitored. | [optional] |
| **coached_participant_id** | str | If this participant is a coach, then this will be the id of the participant that is being coached. | [optional] |
| **attributes** | dict(str, str) | Additional participant attributes | [optional] |
| **calls** | [list[Call]](Call) |  | [optional] |
| **callbacks** | [list[Callback]](Callback) |  | [optional] |
| **chats** | [list[ConversationChat]](ConversationChat) |  | [optional] |
| **cobrowsesessions** | [list[Cobrowsesession]](Cobrowsesession) |  | [optional] |
| **emails** | [list[Email]](Email) |  | [optional] |
| **messages** | [list[Message]](Message) |  | [optional] |
| **screenshares** | [list[Screenshare]](Screenshare) |  | [optional] |
| **social_expressions** | [list[SocialExpression]](SocialExpression) |  | [optional] |
| **videos** | [list[Video]](Video) |  | [optional] |
| **evaluations** | [list[Evaluation]](Evaluation) |  | [optional] |
| **screen_recording_state** | str | The current screen recording state for this participant. | [optional] |
| **flagged_reason** | str | The reason specifying why participant flagged the conversation. | [optional] |
| **start_acw_time** | datetime | The timestamp when this participant started after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_acw_time** | datetime | The timestamp when this participant ended after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **internal_messages** | [list[InternalMessage]](InternalMessage) |  | [optional] |
| **barged_participant_id** | str | If this participant barged in a participant&#39;s call, then this will be the id of the targeted participant. | [optional] |



_PureCloudPlatformClientV2 229.0.0_
