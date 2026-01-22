# UserEstablishedEvent

## UserEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication | |
| **phone_number** | str | Identifies the phone number used to reach this user if it is different from the information that would be accessed by userId. | [optional] |
| **user_id** | str | The userId (V4 UUID) for the user this communication belongs to. | |
| **station_id** | str | A Station ID (V4 UUID) that identifies the station being used if the user is using a station and the stationId is known. | [optional] |
| **ani** | str | The automatic number identification if it is available for this conversation. | [optional] |
| **dnis** | str | The dialed number identification if it is available for this conversation. | [optional] |
| **after_call_work_required** | bool | Indicates whether or not this user will be required to complete after call work. | [optional] |
| **queue_id** | str | The id (V4 UUID) of the queue that the user is calling on behalf of. Applies to outbound calls only. | [optional] |
| **initial_configuration** | [InitialConfiguration](InitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 249.0.0_
