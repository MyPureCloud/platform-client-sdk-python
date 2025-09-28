# ScheduleGenerationResult

## ScheduleGenerationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **failed** | bool | Whether the schedule generation run failed | [optional] |
| **run_id** | str | The ID of the schedule generation run. Reference this when requesting support | [optional] |
| **message_count** | int | The number of schedule generation messages for this schedule generation run | [optional] |
| **messages** | [list[ScheduleGenerationMessage]](ScheduleGenerationMessage) | User facing messages related to the schedule generation run | [optional] |
| **message_severities** | [list[SchedulerMessageTypeSeverity]](SchedulerMessageTypeSeverity) | The list of messages by severity in this schedule generation run | [optional] |



_PureCloudPlatformClientV2 238.0.0_
