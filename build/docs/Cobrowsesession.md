---
title: Cobrowsesession
---
## Cobrowsesession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **pcSelf** | [**Address**](Address.html) | Address and name data for a call endpoint. | [optional] |
| **cobrowse_session_id** | **str** | The co-browse session ID. | [optional] |
| **cobrowse_role** | **str** | This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer). | [optional] |
| **controlling** | **list[str]** | ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages). | [optional] |
| **viewer_url** | **str** | The URL that can be used to open co-browse session in web browser. | [optional] |
| **provider_event_time** | **datetime** | The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **start_alerting_time** | **datetime** | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the co-browse session. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s call, divided into activity segments. | [optional] |
{: class="table table-striped"}


