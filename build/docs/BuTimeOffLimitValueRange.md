---
title: BuTimeOffLimitValueRange
---
## BuTimeOffLimitValueRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **time_off_limit** | [**BuTimeOffLimitReference**](BuTimeOffLimitReference.html) | The ID of the time-off limit | |
| **start_date** | **date** | Start date of the requested date range, in ISO-8601 format. The end date is determined by the size of interval lists | |
| **granularity** | **str** | Granularity choice for time-off limit | |
| **limit_minutes_per_interval** | **list[int]** | A list of time-off limit values in minutes per granularity interval | |
| **allocated_minutes_per_interval** | **list[int]** | A list of allocated time-off minutes per granularity interval | |
| **waitlisted_minutes_per_interval** | **list[int]** | A list of waitlisted time-off minutes per granularity interval | |
| **waitlisted_requests_per_interval** | **list[int]** | The current number of waitlisted time-off requests for every interval per granularity | |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the time-off limit | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


