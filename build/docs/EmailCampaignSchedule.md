---
title: EmailCampaignSchedule
---
## EmailCampaignSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | Required for updates, must match the version number of the most recent update | [optional] |
| **intervals** | [**list[ScheduleInterval]**](ScheduleInterval.html) | A list of intervals during which to run the associated Campaign. | |
| **time_zone** | **str** | The time zone for this email campaign schedule. | [optional] |
| **email_campaign** | [**DomainEntityRef**](DomainEntityRef.html) | The Campaign that this email campaign schedule is for. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


