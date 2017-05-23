---
title: ManagementUnit
---
## ManagementUnit

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **start_day_of_week** | **str** | Start day of week for workforce management planning purposes | [optional] |
| **timezone** | **str** | The time zone for the management unit in standard Olson Format (See https://en.wikipedia.org/wiki/Tz_database) | [optional] |
| **version** | **int** | The version of the underlying ManagementUnit object. Useful for handling eventual consistency issues.  User must submit the current version they of the ManagementUnit in any write requests | |
| **date_modified** | **datetime** | The date and time at which this management unit was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


