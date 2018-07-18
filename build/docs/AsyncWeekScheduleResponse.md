---
title: AsyncWeekScheduleResponse
---
## AsyncWeekScheduleResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | **str** | The status of the request | [optional] |
| **result** | [**WeekSchedule**](WeekSchedule.html) | Week schedule result. The value will be null if the data is sent through notification or if response is large. | [optional] |
| **operation_id** | **str** | The operation id to watch for on the notification topic if status == Processing | [optional] |
| **download_url** | **str** | The url to fetch the result for large responses. The value will be null if result contains the data | [optional] |
{: class="table table-striped"}


