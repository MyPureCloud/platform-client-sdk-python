# UserPresenceEvent

## UserPresenceEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **user_id** | str | The User ID of the user associated with this UserPresence | |
| **source_id** | str | The id (V4 UUID) of the presence source being updated | |
| **presence_definition_id** | str | The id (UUID) of the presence definition that the user presence is associated with | [optional] |
| **message** | str | The message associated with the presence | [optional] |



_PureCloudPlatformClientV2 210.0.0_
