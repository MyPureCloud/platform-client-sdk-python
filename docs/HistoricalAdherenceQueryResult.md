# HistoricalAdherenceQueryResult

## HistoricalAdherenceQueryResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | str | The ID of the user for whom the adherence is queried | [optional] |
| **management_unit_id** | str | The ID of the management unit of the user for whom the adherence is queried | [optional] |
| **start_date** | datetime | Beginning of the date range that was queried, in ISO-8601 format | [optional] |
| **end_date** | datetime | End of the date range that was queried, in ISO-8601 format. If it was not set, end date will be set to the queried time | [optional] |
| **adherence_percentage** | float | Adherence percentage for this user, in the scale of 0 - 100 | [optional] |
| **conformance_percentage** | float | Conformance percentage for this user, in the scale of 0 - 100. Conformance percentage can be greater than 100 when the actual on-queue time is greater than the scheduled on-queue time for the same period. | [optional] |
| **impact** | str | The impact of the current adherence state for this user | [optional] |
| **exception_info** | [list[HistoricalAdherenceExceptionInfo]](HistoricalAdherenceExceptionInfo) | List of adherence exceptions for this user | [optional] |
| **day_metrics** | [list[HistoricalAdherenceDayMetrics]](HistoricalAdherenceDayMetrics) | Adherence and conformance metrics for days in query range | [optional] |
| **actuals_end_date** | datetime | The end date of the actual activities in ISO-8601 format. | [optional] |
| **actuals** | [list[HistoricalAdherenceActuals]](HistoricalAdherenceActuals) | List of actual activity with offset for this user | [optional] |



_PureCloudPlatformClientV2 232.0.0_
