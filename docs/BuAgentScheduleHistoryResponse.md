# BuAgentScheduleHistoryResponse

## BuAgentScheduleHistoryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **prior_published_schedules** | [list[BuScheduleReference]](BuScheduleReference) | The list of previously published schedules | [optional] |
| **base_published_schedule** | [BuAgentScheduleHistoryChange](BuAgentScheduleHistoryChange) | The originally published agent schedules | [optional] |
| **dropped_changes** | [list[BuAgentScheduleHistoryDroppedChange]](BuAgentScheduleHistoryDroppedChange) | The changes dropped from the schedule history. This will happen if the schedule history is too large | [optional] |
| **changes** | [list[BuAgentScheduleHistoryChange]](BuAgentScheduleHistoryChange) | The list of changes for the schedule history | [optional] |



_PureCloudPlatformClientV2 233.0.0_
