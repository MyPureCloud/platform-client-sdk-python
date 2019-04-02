---
title: Video
---
## Video

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **context** | **str** | The room id context (xmpp jid) for the conference session. | [optional] |
| **audio_muted** | **bool** | Indicates whether this participant has muted their outgoing audio. | [optional] |
| **video_muted** | **bool** | Indicates whether this participant has muted/paused their outgoing video. | [optional] |
| **sharing_screen** | **bool** | Indicates whether this participant is sharing their screen to the session. | [optional] |
| **peer_count** | **int** | The number of peer participants from the perspective of the participant in the conference. | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_alerting_time** | **datetime** | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the video. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **msids** | **list[str]** | List of media stream ids | [optional] |
| **pcSelf** | [**Address**](Address.html) | Address and name data for a call endpoint. | [optional] |
{: class="table table-striped"}


