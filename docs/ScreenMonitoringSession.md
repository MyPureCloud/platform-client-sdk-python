# ScreenMonitoringSession

## ScreenMonitoringSession

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **source_user** | [AddressableEntityRef](AddressableEntityRef) | The user who initiated the screen monitoring session | |
| **target_user** | [AddressableEntityRef](AddressableEntityRef) | The user being monitored (for agent-level monitoring) | [optional] |
| **conversation** | [AddressableEntityRef](AddressableEntityRef) | The conversation being monitored (for conversation-level monitoring) | [optional] |
| **participant_id** | str | The ID of the participant being monitored (for conversation-level monitoring) | [optional] |
| **monitoring_type** | str | The type of screen monitoring session | |
| **date_created** | datetime | The date and time when the screen monitoring session was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **screen_monitoring_id** | str | The unique identifier for this screen monitoring session | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 263.0.0_
