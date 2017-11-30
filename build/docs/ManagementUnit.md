---
title: ManagementUnit
---
## ManagementUnit

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **start_day_of_week** | **str** | Start day of week for scheduling and forecasting purposes | [optional] |
| **time_zone** | **str** | The time zone for the management unit in standard Olson Format (See https://en.wikipedia.org/wiki/Tz_database) | [optional] |
| **settings** | [**ManagementUnitSettings**](ManagementUnitSettings.html) | The configuration settings for this management unit | [optional] |
| **version** | **int** | The version of the underlying entity | |
| **date_modified** | **datetime** | The date and time at which this entity was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | [**User**](User.html) | The user who last modified this entity | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


