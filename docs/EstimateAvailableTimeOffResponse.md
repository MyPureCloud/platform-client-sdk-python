# EstimateAvailableTimeOffResponse

## EstimateAvailableTimeOffResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **full_day_dates** | [list[EstimateAvailableFullDayTimeOffResponse]](EstimateAvailableFullDayTimeOffResponse) | Full day dates. partialDayDates must be empty if this field is populated | [optional] |
| **partial_day_dates** | [list[EstimateAvailablePartialDayTimeOffResponse]](EstimateAvailablePartialDayTimeOffResponse) | Partial day dates. fullDayDates must be empty if this field is populated | [optional] |
| **user** | [UserReference](UserReference) | The user to whom the time off request belongs | |
| **activity_code_id** | str | The ID of the activity code associated with the time off request. Activity code must be of the TimeOff category | |
| **paid** | bool | Whether this estimate is for a paid time off request | |



_PureCloudPlatformClientV2 230.0.0_
