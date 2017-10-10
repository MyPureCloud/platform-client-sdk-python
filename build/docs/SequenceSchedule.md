---
title: SequenceSchedule
---
## SequenceSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **intervals** | [**list[ScheduleInterval]**](ScheduleInterval.html) | A list of intervals during which to run the associated CampaignSequence. | |
| **time_zone** | **str** | The time zone for this SequenceSchedule. For example, Africa/Abidjan. | |
| **sequence** | [**UriReference**](UriReference.html) | The CampaignSequence that this SequenceSchedule is for. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


