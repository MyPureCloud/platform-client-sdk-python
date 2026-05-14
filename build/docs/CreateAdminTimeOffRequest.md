# CreateAdminTimeOffRequest

## CreateAdminTimeOffRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The status of this time off request | |
| **users** | [list[UserReference]](UserReference) | A set of IDs for users to associate with this time off request | |
| **activity_code_id** | str | The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category | |
| **notes** | str | Notes about the time off request | [optional] |
| **full_day_management_unit_dates** | list[str] | A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit&#39;s configured time zone | [optional] |
| **partial_day_start_date_times** | list[datetime] | A set of start date-times in ISO-8601 format for partial day requests | [optional] |
| **daily_duration_minutes** | int | Daily duration in minutes applied to all days of this time off request. Ignored if durationMinutes is specified. At least one of dailyDurationMinutes or durationMinutes is required | [optional] |
| **duration_minutes** | list[int] | Duration in minutes for each day of this time off request. Must match the size of fullDayManagementUnitDates or partialDayStartDateTimes. At least one of dailyDurationMinutes or durationMinutes is required | [optional] |
| **payable_minutes** | list[int] | Payable minutes for each day of this time off request, representing scheduled paid time displaced by this request. Defaults to dailyDurationMinutes if not specified | [optional] |
| **paid** | bool | Whether this is a paid time off request. Defaults to the activity code&#39;s paid value if not specified | [optional] |



_PureCloudPlatformClientV2 257.1.0_
