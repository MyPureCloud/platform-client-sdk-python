# BuTimeOffLimitValues

## BuTimeOffLimitValues

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | date | Start date of the requested date range, in ISO-8601 format. The end date is determined by the size of interval lists | |
| **values_per_day** | [TimeOffLimitValues](TimeOffLimitValues) | Time-off limit values specified in per day granularity. Set only if granularity is &#39;Daily&#39; | [optional] |
| **values_per_fifteen_minutes** | [TimeOffLimitValues](TimeOffLimitValues) | Time-off limit values specified in per fifteen minutes granularity. Set only if granularity is &#39;FifteenMinutes&#39; | [optional] |



_PureCloudPlatformClientV2 266.0.0_
