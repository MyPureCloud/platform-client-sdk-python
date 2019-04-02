---
title: ObservationMetricData
---
## ObservationMetricData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metric** | **str** |  | [optional] |
| **qualifier** | **str** |  | [optional] |
| **stats** | [**StatisticalSummary**](StatisticalSummary.html) |  | [optional] |
| **truncated** | **bool** | Flag for a truncated list of observations. If truncated, the first half of the list of observations will contain the oldest observations and the second half the newest observations. | [optional] |
| **observations** | [**list[ObservationValue]**](ObservationValue.html) | List of observations sorted by timestamp in ascending order. This list may be truncated. | [optional] |
{: class="table table-striped"}


