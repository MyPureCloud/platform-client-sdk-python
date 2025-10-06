# UserTransferEvent

## UserTransferEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **transfer_type** | str | Indicates the desired type of transfer. | |
| **command_id** | str | The id (V4 UUID) used by the external platform to refer to the transfer in subsequent Transfer events. | |
| **initiating_communication_id** | str | The id (V4 UUID) of the communication representing the participant that is initiating the transfer. | |
| **target_communication_id** | str | The id (V4 UUID) of the communication that is being transferred away from. In many cases this will be the same as the &#x60;initiatingCommunicationId&#x60;. | |
| **object_communication_id** | str | The id (V4 UUID) of the communication that is being transferred. | |
| **destination_user_id** | str | The id (V4 UUID) of the desired destination user that the object communication should be transferred to. | |



_PureCloudPlatformClientV2 240.0.0_
