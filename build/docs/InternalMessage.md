# InternalMessage

## InternalMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | str | The connection state of this communication. | [optional] |
| **initial_state** | str | The initial connection state of this communication. | [optional] |
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s internal message, divided into activity segments. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **provider** | str | The source provider for the message. | [optional] |
| **peer_id** | str | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **target_user_id** | str | The user ID for the participant on receiving side of the internal message conversation. | [optional] |
| **source_user_id** | str | The user ID for the participant on sending side of the internal message conversation. | [optional] |
| **to_address** | [Address](Address) | Address for the participant on receiving side of the internal message communication. | [optional] |
| **from_address** | [Address](Address) | Address for the participant on the sending side of the internal message communication. | [optional] |
| **messages** | [list[InternalMessageDetails]](InternalMessageDetails) | The messages sent on this communication channel. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
