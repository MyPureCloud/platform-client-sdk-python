---
title: CampaignSchedule
---
## CampaignSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **intervals** | [**list[ScheduleInterval]**](ScheduleInterval.html) | a list of start and end times | |
| **time_zone** | **str** | time zone identifier to be applied to the intervals; for example Africa/Abidjan | |
| **campaign** | [**UriReference**](UriReference.html) | identifier of the campaign to be scheduled | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


