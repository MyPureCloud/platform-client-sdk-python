---
title: Message
---
## Message

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **held** | **bool** | True if this call is held and the person on this side hears silence. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s message, divided into activity segments. | [optional] |
| **direction** | **str** | The direction of the message. | [optional] |
| **recording_id** | **str** | A globally unique identifier for the recording associated with this message. | [optional] |
| **error_info** | [**ErrorBody**](ErrorBody.html) |  | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | **datetime** | The timestamp the message was placed on hold in the cloud clock if the message is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the message. | [optional] |
| **script_id** | **str** | The UUID of the script to use. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **to_address** | [**Address**](Address.html) | Address and name data for a call endpoint. | [optional] |
| **from_address** | [**Address**](Address.html) | Address and name data for a call endpoint. | [optional] |
| **messages** | [**list[MessageDetails]**](MessageDetails.html) | The messages sent on this communication channel. | [optional] |
{: class="table table-striped"}


