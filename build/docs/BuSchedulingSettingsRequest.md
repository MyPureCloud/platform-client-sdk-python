# BuSchedulingSettingsRequest

## BuSchedulingSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_severities** | [list[SchedulerMessageTypeSeverity]](SchedulerMessageTypeSeverity) | Schedule generation message severity configuration | [optional] |
| **sync_time_off_properties** | [SetWrapperSyncTimeOffProperty](SetWrapperSyncTimeOffProperty) | Synchronize set of time off properties from scheduled activities to time off requests when the schedule is published. | [optional] |
| **service_goal_impact** | [WfmServiceGoalImpactSettings](WfmServiceGoalImpactSettings) | Configures the max percent increase and decrease of service goals for this business unit | [optional] |
| **allow_work_plan_per_minute_granularity** | bool | Indicates whether or not per minute granularity for scheduling will be enabled for this business unit. Defaults to false. | [optional] |
| **activity_smoothing_type** | str | The activity smoothing type for schedule generation in this business unit | [optional] |
| **induce_schedule_variability** | bool | Indicates whether to provide variability in schedule generation | [optional] |



_PureCloudPlatformClientV2 226.0.0_
