# RoutingEstablishedEvent

## RoutingEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication | |
| **phone_number** | str | Identifies the phone number used to reach this queue if it is different from the information that would be accessed by queueId. | [optional] |
| **queue_id** | str | The id (V4 UUID) of the queue that is routing this conversation. | |
| **ani** | str | The automatic number identification if it is available for this conversation. | [optional] |
| **dnis** | str | The dialed number identification if it is available for this conversation. | [optional] |
| **skill_ids** | list[str] | The unique identifiers (V4 UUID) for the skills that should be used to determine the destination for the conversation. | [optional] |
| **language_id** | str | The unique identifier (V4 UUID) for the language that should be used to determine the destination for the conversation. | [optional] |
| **initial_configuration** | [InitialConfiguration](InitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 243.0.0_
