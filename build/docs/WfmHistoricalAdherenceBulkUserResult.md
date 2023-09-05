---
title: WfmHistoricalAdherenceBulkUserResult
---
## WfmHistoricalAdherenceBulkUserResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_id** | **str** | The ID of the user for whom the adherence is queried | [optional] |
| **adherence_percentage** | **float** | Adherence percentage for this user, in the scale of 0 - 100 | [optional] |
| **conformance_percentage** | **float** | Conformance percentage for this user, in the scale of 0 - 100. Conformance percentage can be greater than 100 when the actual on queue time is greater than the scheduled on queue time for the same period. | [optional] |
| **impact** | **str** | The impact of the current adherence state for this user | [optional] |
| **exception_info** | [**list[HistoricalAdherenceExceptionInfo]**](HistoricalAdherenceExceptionInfo.html) | List of adherence exceptions for this user | [optional] |
| **actuals** | [**list[HistoricalAdherenceActuals]**](HistoricalAdherenceActuals.html) | List of adherence actuals for this user | [optional] |
| **day_metrics** | [**list[WfmHistoricalAdherenceBulkUserDayMetrics]**](WfmHistoricalAdherenceBulkUserDayMetrics.html) | Adherence and conformance metrics for days in query range | [optional] |
{: class="table table-striped"}


