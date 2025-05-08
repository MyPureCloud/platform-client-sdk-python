# TimeOffBalanceResponse

## TimeOffBalanceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **activity_code_id** | str | The ID for activity code associated with time off balance | |
| **hris_time_off_type_id** | str | The ID of the time off type configured in HRIS integration | |
| **hris_time_off_type_secondary_id** | str | The secondary ID of the time off type configured in HRIS integration | [optional] |
| **start_date** | date | The Start date of the requested date range. The end date is determined by the size of interval list. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **balance_minutes_per_day** | list[int] | The list of available time off balance values in minutes for each day | [optional] |



_PureCloudPlatformClientV2 227.1.0_
