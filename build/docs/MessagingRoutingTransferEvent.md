# MessagingRoutingTransferEvent

## MessagingRoutingTransferEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **transfer_type** | str | Indicates the desired type of transfer. | |
| **command_id** | str | The id (V4 UUID) used by the external platform to refer to the transfer in subsequent *Transfer events. | |
| **initiating_communication_id** | str | Indicates the desired type of transfer. | |
| **target_communication_id** | str | The id (V4 UUID) of the communication that is being transferred away from. In many cases this will be the same as the &#x60;initiatingCommunicationId&#x60;. | |
| **object_communication_id** | str | The id (V4 UUID) of the communication that is being transferred. | |
| **destination_queue_id** | str | The id (V4 UUID) of the desired destination queue that the object communication should be transferred to. | |
| **language_id** | str | The unique identifier (V4 UUID) for the language that should be used to determine the destination for the conversation. | [optional] |
| **skill_ids** | list[str] | The unique identifiers (V4 UUID) for the skills that should be used to determine the destination for the conversation. | [optional] |



_PureCloudPlatformClientV2 221.0.0_
