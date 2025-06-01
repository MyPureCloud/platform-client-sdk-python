# MessagingUserEstablishedEvent

## MessagingUserEstablishedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication. | |
| **user_id** | str | A unique Id (V4 UUID) identifying the user this communication belongs to. | |
| **queue_id** | str | A unique Id (V4 UUID) identifying the queue that the user is messaging on behalf of. Applies to outbound messages only. | [optional] |
| **after_call_work_required** | bool | Indicates whether or not this user will be required to complete after call work. | [optional] |
| **initial_configuration** | [MessagingInitialConfiguration](MessagingInitialConfiguration) | Metadata about this communication. | |
| **source_configuration** | [SourceConfiguration](SourceConfiguration) | Metadata about the source of this communication&#39;s interaction. | |



_PureCloudPlatformClientV2 230.0.0_
