---
title: DialerCampaignScheduleConfigChangeScheduleRecurrence
---
## DialerCampaignScheduleConfigChangeScheduleRecurrence

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | the recurrence id | [optional] |
| **start** | **str** | scheduled start time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end** | **str** | scheduled end time represented as an ISO-8601 string; for example, yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **time_zone** | **str** | the timezone the recurrence will use | [optional] |
| **range** | [**DialerCampaignScheduleConfigChangeRecurrenceRange**](DialerCampaignScheduleConfigChangeRecurrenceRange.html) |  | [optional] |
| **pattern** | [**DialerCampaignScheduleConfigChangeRecurrencePattern**](DialerCampaignScheduleConfigChangeRecurrencePattern.html) |  | [optional] |
| **alterations** | [**list[DialerCampaignScheduleConfigChangeAlteration]**](DialerCampaignScheduleConfigChangeAlteration.html) | modifications to the original recurrence schedule | [optional] |
| **additional_properties** | **dict(str, object)** |  | [optional] |
{: class="table table-striped"}


