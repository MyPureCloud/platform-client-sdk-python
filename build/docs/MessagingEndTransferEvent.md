# MessagingEndTransferEvent

## MessagingEndTransferEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **command_id** | str | The id (V4 UUID) used to identify the transfer already started by the external platform. | |
| **final_state** | str | Indicates whether the transfer completed successfully, was cancelled, or failed for some reason. | |
| **object_communication_id** | str | The id (V4 UUID) of the communication that was being transferred. | |



_PureCloudPlatformClientV2 221.0.0_
