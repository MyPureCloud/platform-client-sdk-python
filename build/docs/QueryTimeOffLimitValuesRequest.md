---
title: QueryTimeOffLimitValuesRequest
---
## QueryTimeOffLimitValuesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_limit_id** | **str** | The time off limit object id to retrieve values for. Required if activityCodeId is not specified | [optional] |
| **activity_code_id** | **str** | The activity code id to filter the affected limit objects by. Required if timeOffLimitId is not specified | [optional] |
| **date_ranges** | [**list[LocalDateRange]**](LocalDateRange.html) | The list of the date ranges to return time off limit, allocated and waitlisted minutes. | |
{: class="table table-striped"}


