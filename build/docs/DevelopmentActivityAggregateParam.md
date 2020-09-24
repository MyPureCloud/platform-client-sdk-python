---
title: DevelopmentActivityAggregateParam
---
## DevelopmentActivityAggregateParam

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Specifies the range of due dates to be used for filtering. Milliseconds will be truncated. A maximum of 365 days can be specified in the range. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **metrics** | **list[str]** | The list of metrics to be returned. If omitted, all metrics are returned. | [optional] |
| **group_by** | **list[str]** | Specifies if the aggregated data is combined into a single set of metrics (groupBy is empty or not specified), or contains an element per attendeeId (groupBy is \&quot;attendeeId\&quot;) | [optional] |
| **filter** | [**DevelopmentActivityAggregateQueryRequestFilter**](DevelopmentActivityAggregateQueryRequestFilter.html) | The filter applied to the data. This is ANDed with the interval parameter. | |
{: class="table table-striped"}


