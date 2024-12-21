# CoachingAppointmentAggregateRequest

## CoachingAppointmentAggregateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | str | Interval to aggregate across. End date is not inclusive. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **metrics** | list[str] | A list of metrics to aggregate.  If omitted, all metrics are returned. | [optional] |
| **group_by** | list[str] | An optional list of items by which to group the result data. | [optional] |
| **filter** | [QueryRequestFilter](QueryRequestFilter) | The filter applied to the data | |



_PureCloudPlatformClientV2 219.0.0_
