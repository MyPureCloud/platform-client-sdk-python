# EmailCampaignScheduleConfigChangeScheduleRecurrence

## EmailCampaignScheduleConfigChangeScheduleRecurrence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | the recurrence id | [optional] |
| **start** | str | scheduled start time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end** | str | scheduled end time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **time_zone** | str | the timezone the recurrence will use | [optional] |
| **range** | [EmailCampaignScheduleConfigChangeRecurrenceRange](EmailCampaignScheduleConfigChangeRecurrenceRange) |  | [optional] |
| **pattern** | [EmailCampaignScheduleConfigChangeRecurrencePattern](EmailCampaignScheduleConfigChangeRecurrencePattern) |  | [optional] |
| **alterations** | [list[EmailCampaignScheduleConfigChangeAlteration]](EmailCampaignScheduleConfigChangeAlteration) | modifications to the original recurrence schedule | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 254.0.0_
