# AdminTimeOffRequestPatch

## AdminTimeOffRequestPatch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | str | The status of this time off request | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category | [optional] |
| **paid** | bool | Whether this is a paid time off request | [optional] |
| **notes** | str | Notes about the time off request | [optional] |
| **full_day_management_unit_dates** | list[str] | A set of dates in yyyy-MM-dd format. Should be interpreted in the management unit&#39;s configured time zone | [optional] |
| **full_day_earliest_start_offset_minutes** | [ListWrapperInteger](ListWrapperInteger) | Earliest start offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | [optional] |
| **full_day_latest_end_offset_minutes** | [ListWrapperInteger](ListWrapperInteger) | Latest end offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | [optional] |
| **partial_day_start_date_times** | list[datetime] | A set of start date-times in ISO-8601 format for partial day requests | [optional] |
| **daily_duration_minutes** | int | The daily duration of this time off request in minutes | [optional] |
| **duration_minutes** | list[int] | Daily durations for each day of this time off request in minutes | [optional] |
| **payable_minutes** | list[int] | Payable minutes for each day of this time off request | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time off request | |



_PureCloudPlatformClientV2 261.0.0_
