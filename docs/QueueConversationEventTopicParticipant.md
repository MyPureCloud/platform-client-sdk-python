# QueueConversationEventTopicParticipant

## QueueConversationEventTopicParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this conversation. | [optional] |
| **connected_time** | datetime | The timestamp when this participant was connected to the conversation in the provider clock. | [optional] |
| **end_time** | datetime | The timestamp when this participant disconnected from the conversation in the provider clock. | [optional] |
| **user_id** | str | If this participant represents a user, then this will be the globally unique identifier for the user. | [optional] |
| **external_contact_id** | str | If this participant represents an external contact, then this will be the globally unique identifier for the external contact. | [optional] |
| **external_organization_id** | str | If this participant represents an external org, then this will be the globally unique identifier for the external org. | [optional] |
| **name** | str | A human readable name identifying the participant. | [optional] |
| **queue_id** | str | If present, the queue id that the communication channel came in on. | [optional] |
| **group_id** | str | If present, the group id that the participant represents. | [optional] |
| **team_id** | str | The team id that this participant is a member of when added to the conversation. | [optional] |
| **purpose** | str | A well known string that specifies the purpose or type of this participant. | [optional] |
| **consult_participant_id** | str | If this participant is part of a consult transfer, then this will be the participant id of the participant being transferred. | [optional] |
| **address** | str | The address for the this participant. For a phone call this will be the ANI. | [optional] |
| **wrapup_required** | bool | True iff this participant is required to enter wrapup for this conversation. | [optional] |
| **wrapup_expected** | bool | True when a participant is expected to enter a wrapup code once the call connects. | [optional] |
| **wrapup_prompt** | str | This field controls how the UI prompts the agent for a wrapup. | [optional] |
| **wrapup_timeout_ms** | int | Specifies how long a timed ACW session will last. | [optional] |
| **wrapup** | [QueueConversationEventTopicWrapup](QueueConversationEventTopicWrapup) |  | [optional] |
| **start_acw_time** | datetime | The timestamp when this participant started after-call work. | [optional] |
| **end_acw_time** | datetime | The timestamp when this participant ended after-call work. | [optional] |
| **conversation_routing_data** | [QueueConversationEventTopicConversationRoutingData](QueueConversationEventTopicConversationRoutingData) |  | [optional] |
| **alerting_timeout_ms** | int | Specifies how long the agent has to answer an interaction before being marked as not responding. | [optional] |
| **monitored_participant_id** | str | If this participant is a monitor, then this will be the id of the participant that is being monitored. | [optional] |
| **coached_participant_id** | str | If this participant is a coach, then this will be the id of the participant that is being coached. | [optional] |
| **barged_participant_id** | str | If this participant created a barge in conference, then this will be the id of the participant that is barged in. | [optional] |
| **media_roles** | list[str] | List of roles this participant&#39;s media has had on the conversation, ie monitor, coach, etc. | [optional] |
| **screen_recording_state** | str | The current screen recording state for this participant. | [optional] |
| **flagged_reason** | str | If this participant has flagged the conversation, the reason code given. | [optional] |
| **attributes** | dict(str, str) | Additional participant attributes | [optional] |
| **calls** | [list[QueueConversationEventTopicCall]](QueueConversationEventTopicCall) |  | [optional] |
| **callbacks** | [list[QueueConversationEventTopicCallback]](QueueConversationEventTopicCallback) |  | [optional] |
| **chats** | [list[QueueConversationEventTopicChat]](QueueConversationEventTopicChat) |  | [optional] |
| **cobrowsesessions** | [list[QueueConversationEventTopicCobrowse]](QueueConversationEventTopicCobrowse) |  | [optional] |
| **emails** | [list[QueueConversationEventTopicEmail]](QueueConversationEventTopicEmail) |  | [optional] |
| **messages** | [list[QueueConversationEventTopicMessage]](QueueConversationEventTopicMessage) |  | [optional] |
| **internal_messages** | [list[QueueConversationEventTopicInternalMessage]](QueueConversationEventTopicInternalMessage) |  | [optional] |
| **screenshares** | [list[QueueConversationEventTopicScreenshare]](QueueConversationEventTopicScreenshare) |  | [optional] |
| **social_expressions** | [list[QueueConversationEventTopicSocialExpression]](QueueConversationEventTopicSocialExpression) |  | [optional] |
| **videos** | [list[QueueConversationEventTopicVideo]](QueueConversationEventTopicVideo) |  | [optional] |
| **workflow** | [QueueConversationEventTopicWorkflow](QueueConversationEventTopicWorkflow) |  | [optional] |



_PureCloudPlatformClientV2 213.0.0_
