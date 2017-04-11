---
title: Call
---
## Call

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **direction** | **str** | The direction of the call | [optional] |
| **recording** | **bool** | True if this call is being recorded. | [optional] |
| **recording_state** | **str** | State of recording on this call. | [optional] |
| **muted** | **bool** | True if this call is muted so that remote participants can&#39;t hear any audio from this end. | [optional] |
| **confined** | **bool** | True if this call is held and the person on this side hears hold music. | [optional] |
| **held** | **bool** | True if this call is held and the person on this side hears silence. | [optional] |
| **recording_id** | **str** | A globally unique identifier for the recording associated with this call. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s call, divided into activity segments. | [optional] |
| **error_info** | [**ErrorBody**](ErrorBody.html) |  | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | **datetime** | The timestamp the call was placed on hold in the cloud clock if the call is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **document_id** | **str** | If call is an outbound fax of a document from content management, then this is the id in content management. | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnect_reasons** | [**list[DisconnectReason]**](DisconnectReason.html) | List of reasons that this call was disconnected. This will be set once the call disconnects. | [optional] |
| **fax_status** | [**FaxStatus**](FaxStatus.html) | Extra information on fax transmission. | [optional] |
| **provider** | **str** | The source provider for the call. | [optional] |
| **script_id** | **str** | The UUID of the script to use. | [optional] |
{: class="table table-striped"}


