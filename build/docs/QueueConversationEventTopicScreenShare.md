# QueueConversationEventTopicScreenShare

## QueueConversationEventTopicScreenShare

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **pcSelf** | [QueueConversationEventTopicAddress](QueueConversationEventTopicAddress) | Address and name data for a call endpoint. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **context** | str | The room id context (xmpp jid) for the conference session. | [optional] |
| **sharing** | bool | Indicates whether this participant is sharing their screen to the session. | [optional] |
| **provider** | str | The source provider of the screen share. | [optional] |
| **script_id** | str | The UUID of the script to use. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **peer_count** | int | The number of peer participants from the perspective of the participant in the conference. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **wrapup** | [QueueConversationEventTopicWrapup](QueueConversationEventTopicWrapup) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [QueueConversationEventTopicAfterCallWork](QueueConversationEventTopicAfterCallWork) | A communication&#39;s after-call work data. | [optional] |
| **after_call_work_required** | bool | Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested. | [optional] |
| **queue_media_settings** | [QueueConversationEventTopicQueueMediaSettings](QueueConversationEventTopicQueueMediaSettings) | Represents the queue setting for this media. | [optional] |



_PureCloudPlatformClientV2 244.0.0_
