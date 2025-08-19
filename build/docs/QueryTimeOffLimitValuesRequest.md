# QueryTimeOffLimitValuesRequest

## QueryTimeOffLimitValuesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_limit_id** | str | The time off limit object id to retrieve values for. Required if activityCodeId is not specified | [optional] |
| **activity_code_id** | str | The ID of the activity code by which to filter the affected limit objects. Required if timeOffLimitId is not specified | [optional] |
| **date_ranges** | [list[LocalDateRange]](LocalDateRange) | The list of the date ranges to return time off limit, allocated and waitlisted minutes. The valid number of date ranges is between 1 and 30. Maximum total number of days in all ranges in 366. | |



_PureCloudPlatformClientV2 235.1.0_
