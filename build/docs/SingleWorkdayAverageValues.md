---
title: SingleWorkdayAverageValues
---
## SingleWorkdayAverageValues

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_workday** | **date** | The targeted workday for average value query. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **division** | [**Division**](Division.html) | The targeted division for the metrics | [optional] |
| **user** | [**UserReference**](UserReference.html) | The targeted user for the metrics | [optional] |
| **timezone** | **str** | The time zone used for aggregating metric values | [optional] |
| **results** | [**list[WorkdayValuesMetricItem]**](WorkdayValuesMetricItem.html) | The metric value averages | [optional] |
{: class="table table-striped"}


