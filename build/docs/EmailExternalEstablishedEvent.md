# EmailExternalEstablishedEvent

## EmailExternalEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication. | |
| **display_name** | str | A name for the participant if it is available for this conversation. | [optional] |
| **include_message** | bool | Indicates that established communication has an initial email. If true, the initial messagesSent value will be initialized to 1. | [optional] |
| **initial_configuration** | [EmailInitialConfiguration](EmailInitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 218.0.0_
