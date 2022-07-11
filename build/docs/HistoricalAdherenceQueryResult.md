---
title: HistoricalAdherenceQueryResult
---
## HistoricalAdherenceQueryResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | **str** | The ID of the user for whom the adherence is queried | [optional] |
| **start_date** | **datetime** | Beginning of the date range that was queried, in ISO-8601 format | [optional] |
| **end_date** | **datetime** | End of the date range that was queried, in ISO-8601 format. If it was not set, end date will be set to the queried time | [optional] |
| **adherence_percentage** | **float** | Adherence percentage for this user, in the scale of 0 - 100 | [optional] |
| **conformance_percentage** | **float** | Conformance percentage for this user, in the scale of 0 - 100. Conformance percentage can be greater than 100 when the actual on queue time is greater than the scheduled on queue time for the same period. | [optional] |
| **impact** | **str** | The impact of the current adherence state for this user | [optional] |
| **exception_info** | [**list[HistoricalAdherenceExceptionInfo]**](HistoricalAdherenceExceptionInfo.html) | List of adherence exceptions for this user | [optional] |
| **day_metrics** | [**list[HistoricalAdherenceDayMetrics]**](HistoricalAdherenceDayMetrics.html) | Adherence and conformance metrics for days in query range | [optional] |
| **actuals** | [**list[HistoricalAdherenceActuals]**](HistoricalAdherenceActuals.html) | List of actual activity with offset for this user | [optional] |
| **actuals_ends_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


