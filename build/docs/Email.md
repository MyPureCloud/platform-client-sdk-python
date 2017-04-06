---
title: Email
---
## Email

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **held** | **bool** | True if this call is held and the person on this side hears silence. | [optional] |
| **subject** | **str** | The subject for the initial email that started this conversation. | [optional] |
| **messages_sent** | **int** | The number of email messages sent by this participant. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s email, divided into activity segments. | [optional] |
| **direction** | **str** | The direction of the email | [optional] |
| **recording_id** | **str** | A globally unique identifier for the recording associated with this call. | [optional] |
| **error_info** | [**ErrorBody**](ErrorBody.html) |  | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | **datetime** | The timestamp the email was placed on hold in the cloud clock if the email is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the email. | [optional] |
{: class="table table-striped"}


