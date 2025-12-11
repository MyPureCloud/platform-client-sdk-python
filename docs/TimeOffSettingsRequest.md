# TimeOffSettingsRequest

## TimeOffSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **submission_range_enforced** | bool | Whether to enforce a submission range for agent time off requests | [optional] |
| **submission_range_type** | str | The type of the submission range | [optional] |
| **submission_earliest_days_from_now** | int | The earliest number of days from now for which an agent can submit a time off request.  Use negative numbers to indicate days in the past | [optional] |
| **submission_latest_days_from_now** | int | The latest number of days from now for which an agent can submit a time off request | [optional] |
| **submission_latest_date** | [ValueWrapperLocalDate](ValueWrapperLocalDate) | The latest date for the time off request submission interpreted in the business unit time zone in yyyy-MM-dd format | [optional] |



_PureCloudPlatformClientV2 246.0.0_
