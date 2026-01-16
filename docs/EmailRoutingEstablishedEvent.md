# EmailRoutingEstablishedEvent

## EmailRoutingEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication. | |
| **queue_id** | str | The id of the queue that is routing this conversation. | |
| **skill_ids** | list[str] | The unique identifiers for the skills that should be used to determine the destination for the conversation. | [optional] |
| **language_id** | str | The unique identifier for the language that should be used to determine the destination for the conversation. | [optional] |
| **label** | str | An optional label that categorizes the conversation. Max-utilization settings can be configured at a per-label level. | [optional] |
| **initial_configuration** | [EmailInitialConfiguration](EmailInitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 248.0.0_
