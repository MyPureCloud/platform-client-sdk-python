---
title: Screenshare
---
## Screenshare

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **context** | **str** | The room id context (xmpp jid) for the conference session. | [optional] |
| **sharing** | **bool** | Indicates whether this participant is sharing their screen. | [optional] |
| **peer_count** | **int** | The number of peer participants from the perspective of the participant in the conference. | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_alerting_time** | **datetime** | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the screen share. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s call, divided into activity segments. | [optional] |
| **wrapup** | [**Wrapup**](Wrapup.html) | Call wrap up or disposition data. | [optional] |
| **after_call_work** | [**AfterCallWork**](AfterCallWork.html) | After-call work for the communication. | [optional] |
{: class="table table-striped"}


