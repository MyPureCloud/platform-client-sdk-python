# CommunicationEndedEvent

## CommunicationEndedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication | |
| **disconnect_type** | str | Indicates how this communication was ended. | |
| **destination_conversation_id** | str | The id (V4 UUID) of the conversation that the communication is being moved to when conversations are merged. | [optional] |



_PureCloudPlatformClientV2 234.0.0_
