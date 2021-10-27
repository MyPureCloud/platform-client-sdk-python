---
title: ScheduleGenerationResult
---
## ScheduleGenerationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **failed** | **bool** | Whether the schedule generation run failed | [optional] |
| **run_id** | **str** | The ID of the schedule generation run. Reference this when requesting support | [optional] |
| **message_count** | **int** | The number of schedule generation messages for this schedule generation run | [optional] |
| **messages** | [**list[ScheduleGenerationMessage]**](ScheduleGenerationMessage.html) | User facing messages related to the schedule generation run | [optional] |
{: class="table table-striped"}


