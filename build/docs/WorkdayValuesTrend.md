---
title: WorkdayValuesTrend
---
## WorkdayValuesTrend

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start_workday** | **date** | The start workday for the query range for the metric value trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | **date** | The end workday for the query range for the metric value trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **division** | [**Division**](Division.html) | The targeted division for the query | [optional] |
| **user** | [**UserReference**](UserReference.html) | The targeted user for the query | [optional] |
| **timezone** | **str** | The time zone used for aggregating metric values | [optional] |
| **results** | [**list[WorkdayValuesMetricItem]**](WorkdayValuesMetricItem.html) | The metric value trends | [optional] |
{: class="table table-striped"}


