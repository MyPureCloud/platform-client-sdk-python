# ConversationEventTopicInternalMessage

## ConversationEventTopicInternalMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **provider** | str | The source provider of the message. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **target_user_id** | str | The user ID for the participant on receiving side of the internal message conversation. | [optional] |
| **source_user_id** | str | The user ID for the participant on sending side of the internal message conversation. | [optional] |
| **to_address** | [ConversationEventTopicAddress](ConversationEventTopicAddress) | Address and name data for a call endpoint. | [optional] |
| **from_address** | [ConversationEventTopicAddress](ConversationEventTopicAddress) | Address and name data for a call endpoint. | [optional] |
| **messages** | [list[ConversationEventTopicInternalMessageDetails]](ConversationEventTopicInternalMessageDetails) | The messages sent on this communication channel. | [optional] |



_PureCloudPlatformClientV2 220.0.0_
