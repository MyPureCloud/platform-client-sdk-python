---
title: BuGenerateScheduleRequest
---
## BuGenerateScheduleRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** | The description for the schedule | |
| **short_term_forecast** | [**BuShortTermForecastReference**](BuShortTermForecastReference.html) | The forecast to use when generating the schedule.  Note that the forecast must fully encompass the schedule&#39;s start week + week count | [optional] |
| **week_count** | **int** | The number of weeks in the schedule. One extra day is added at the end | |
| **options** | [**SchedulingOptionsRequest**](SchedulingOptionsRequest.html) | Additional scheduling options | [optional] |
{: class="table table-striped"}


