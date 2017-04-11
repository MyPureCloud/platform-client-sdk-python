---
title: IntradayResponse
---
## IntradayResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | **datetime** | The start of the date range for which this data applies.  This is also the start reference point for the intervals represented in the various arrays. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end_date** | **datetime** | The end of the date range for which this data applies. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **interval_length_minutes** | **int** | The aggregation period in minutes, which determines the interval duration of the returned data | [optional] |
| **number_of_intervals** | **int** | The total number of time intervals represented by this data | [optional] |
| **metrics** | [**list[IntradayMetric]**](IntradayMetric.html) | The metrics to which this data corresponds | [optional] |
| **no_data_reason** | **str** | If not null, the reason there was no data for the request | [optional] |
| **queue_ids** | **list[str]** | The IDs of the queues this data corresponds to | [optional] |
| **intraday_data_groupings** | [**list[IntradayDataGroup]**](IntradayDataGroup.html) | Intraday data grouped by a single media type and set of queue IDs | [optional] |
{: class="table table-striped"}


