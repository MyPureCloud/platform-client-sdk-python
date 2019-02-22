---
title: AsyncWeekScheduleResponse
---
## AsyncWeekScheduleResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **result** | [**WeekSchedule**](WeekSchedule.html) | Week schedule result. The value will be null if the data is sent through notification or if response is large. | [optional] |
| **download_url** | **str** | The url to fetch the result for large responses. The value is null if result contains the data | [optional] |
| **status** | **str** | The status of the request | [optional] |
| **operation_id** | **str** | The operation id to watch for on the notification topic if status == Processing | [optional] |
{: class="table table-striped"}


