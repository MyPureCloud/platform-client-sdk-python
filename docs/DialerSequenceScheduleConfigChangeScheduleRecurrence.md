# DialerSequenceScheduleConfigChangeScheduleRecurrence

## DialerSequenceScheduleConfigChangeScheduleRecurrence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | the recurrence id | [optional] |
| **start** | str | scheduled start time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end** | str | scheduled end time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **time_zone** | str | the timezone the recurrence will use | [optional] |
| **range** | [DialerSequenceScheduleConfigChangeRecurrenceRange](DialerSequenceScheduleConfigChangeRecurrenceRange) |  | [optional] |
| **pattern** | [DialerSequenceScheduleConfigChangeRecurrencePattern](DialerSequenceScheduleConfigChangeRecurrencePattern) |  | [optional] |
| **alterations** | [list[DialerSequenceScheduleConfigChangeAlteration]](DialerSequenceScheduleConfigChangeAlteration) | modifications to the original recurrence schedule | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 225.0.0_
