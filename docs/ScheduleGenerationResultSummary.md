# ScheduleGenerationResultSummary

## ScheduleGenerationResultSummary

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **failed** | bool | Whether the schedule generation run failed | [optional] |
| **run_id** | str | The ID of the schedule generation run. Reference this when requesting support | [optional] |
| **message_count** | int | The number of schedule generation messages for this schedule generation run | [optional] |
| **message_severity_counts** | [list[SchedulerMessageSeverityCount]](SchedulerMessageSeverityCount) | The list of schedule generation message counts by severity for this schedule generation run | [optional] |



_PureCloudPlatformClientV2 233.0.0_
