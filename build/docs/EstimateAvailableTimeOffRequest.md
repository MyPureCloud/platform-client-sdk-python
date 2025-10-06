# EstimateAvailableTimeOffRequest

## EstimateAvailableTimeOffRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **full_day_dates** | [list[EstimateAvailableFullDayTimeOffRequest]](EstimateAvailableFullDayTimeOffRequest) | Full day dates. partialDayDates must be empty if this field is populated | [optional] |
| **partial_day_dates** | [list[EstimateAvailablePartialDayTimeOffRequest]](EstimateAvailablePartialDayTimeOffRequest) | Partial day dates. fullDayDates must be empty if this field is populated | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the time off request. Activity code must be of the TimeOff category | |
| **paid** | bool | Whether this estimate is for a paid time off request | |



_PureCloudPlatformClientV2 240.0.0_
