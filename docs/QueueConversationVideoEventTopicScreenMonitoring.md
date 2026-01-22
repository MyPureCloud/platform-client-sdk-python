# QueueConversationVideoEventTopicScreenMonitoring

## QueueConversationVideoEventTopicScreenMonitoring

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A globally unique identifier for this communication. | [optional] |
| **state** | str |  | [optional] |
| **initial_state** | str |  | [optional] |
| **provider** | str | The source provider. | [optional] |
| **disconnect_type** | str | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **connected_time** | datetime | The timestamp when this communication was connected in the cloud clock. | [optional] |
| **disconnected_time** | datetime | The timestamp when this communication disconnected from the conversation in the provider clock. | [optional] |
| **target_user_id** | str | The user ID for the participant who is being screen monitored. | [optional] |
| **screen_monitoring_id** | str | Screen Monitoring identifier unique to the sourceUserId-targetUserId pair. | [optional] |
| **monitoring_type** | str | The screen monitoring type. | [optional] |
| **count** | int | Number of Screen Monitoring sessions the targetUserId is involved in. | [optional] |



_PureCloudPlatformClientV2 249.0.0_
