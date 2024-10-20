# MessagingCommunicationDispositionAppliedEvent

## MessagingCommunicationDispositionAppliedEvent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **event_id** | str | A unique (V4 UUID) eventId for this event | |
| **event_date_time** | datetime | A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **conversation_id** | str | A unique Id (V4 UUID) identifying this conversation | |
| **communication_id** | str | A unique Id (V4 UUID) identifying this communication | |
| **code** | str | The wrapup-code (V4 UUID) used to disposition this interaction. If this value is not provided the disposition is considered skipped. | [optional] |
| **notes** | str | Text entered by the agent to describe the interaction or disposition. Ignored if the disposition is considered skipped. | [optional] |
| **tags** | list[str] | The list of tags selected by the agent to describe the interaction or disposition. Ignored if the disposition is considered skipped. | [optional] |



_PureCloudPlatformClientV2 214.0.0_
