# WaitlistPosition

## WaitlistPosition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_request** | [TimeOffRequestReference](TimeOffRequestReference) | The time off request for this wait list position | [optional] |
| **time_off_limit** | [TimeOffLimitReference](TimeOffLimitReference) | The time off limit for which time off request is waitlisted | [optional] |
| **date** | date | The date to which this wait list position applies, as defined by the time zone of the business unit. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **waitlist_position** | int | The time off request&#39;s position in the waitlist on the date. 1 means time off is the first in the waitlist | [optional] |



_PureCloudPlatformClientV2 214.0.0_
