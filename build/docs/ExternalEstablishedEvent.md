# ExternalEstablishedEvent

## ExternalEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication | |
| **ani** | str | The automatic number identification if it is available for this conversation. | [optional] |
| **ani_name** | str | The automatic number identification name if it is available for this conversation. | [optional] |
| **dnis** | str | The dialed number identification if it is available for this conversation. | [optional] |
| **dnis_name** | str | The dialed number identification name if it is available for this conversation. | [optional] |
| **initial_configuration** | [InitialConfiguration](InitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 227.1.0_
