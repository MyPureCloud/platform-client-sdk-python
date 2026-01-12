# ScreenMonitoring

## ScreenMonitoring

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **initial_state** | str | The initial connection state of this communication. | [optional] |
| **state** | str | The connection state of this communication. | [optional] |
| **segments** | [list[Segment]](Segment) | The time line of the participant&#39;s Screen Monitoring media, divided into activity segments. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **provider** | str | The source provider of Screen Monitoring media. | [optional] |
| **target_user** | [AddressableEntityRef](AddressableEntityRef) | The user participant who is being screen monitored. | [optional] |
| **screen_monitoring** | [AddressableEntityRef](AddressableEntityRef) | Screen Monitoring identifier unique to the sourceUserId-targetUserId pair. | [optional] |
| **monitoring_type** | str | The screen monitoring type. | [optional] |
| **count** | int | Number of Screen Monitoring sessions the targetUserId is involved in. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 247.0.0_
