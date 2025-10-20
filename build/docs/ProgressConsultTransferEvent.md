# ProgressConsultTransferEvent

## ProgressConsultTransferEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **initiating_communication_id** | str | The id (V4 UUID) of the communication representing the participant that is initiating the transfer. | |
| **destination_communication_id** | str | The id (V4 UUID) of the communication that is being transferred to. | |
| **object_communication_id** | str | The id (V4 UUID) of the communication that is being transferred. | |



_PureCloudPlatformClientV2 241.0.0_
