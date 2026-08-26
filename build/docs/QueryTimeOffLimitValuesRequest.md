# QueryTimeOffLimitValuesRequest

## QueryTimeOffLimitValuesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_limit_id** | str | Deprecated. The time off limit object id to retrieve values for. Required if activityCodeId is not specified | [optional] |
| **activity_code_id** | str | Deprecated. The ID of the activity code by which to filter the affected limit objects. Required if timeOffLimitId is not specified | [optional] |
| **date_ranges** | [list[LocalDateRange]](LocalDateRange) | Deprecated. The list of the date ranges to return time off limit, allocated and waitlisted minutes. The valid number of date ranges is between 1 and 30. Maximum total number of days in all ranges in 366. | |



_PureCloudPlatformClientV2 265.0.0_
