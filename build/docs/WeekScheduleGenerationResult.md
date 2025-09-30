# WeekScheduleGenerationResult

## WeekScheduleGenerationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **failed** | bool | Whether the schedule generation failed | [optional] |
| **run_id** | str | ID of the schedule run | [optional] |
| **agent_warnings** | [list[ScheduleGenerationWarning]](ScheduleGenerationWarning) | Warning messages from the schedule run. This will be available only when requesting information for a single week schedule | [optional] |
| **agent_warning_count** | int | Count of warning messages from the schedule run. This will be available only when requesting multiple week schedules | [optional] |



_PureCloudPlatformClientV2 239.0.0_
