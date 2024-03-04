---
title: BuSchedulingSettingsRequest
---
## BuSchedulingSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message_severities** | [**list[SchedulerMessageTypeSeverity]**](SchedulerMessageTypeSeverity.html) | Schedule generation message severity configuration | [optional] |
| **sync_time_off_properties** | [**SetWrapperSyncTimeOffProperty**](SetWrapperSyncTimeOffProperty.html) | Synchronize set of time off properties from scheduled activities to time off requests when the schedule is published. | [optional] |
| **service_goal_impact** | [**WfmServiceGoalImpactSettings**](WfmServiceGoalImpactSettings.html) | Configures the max percent increase and decrease of service goals for this business unit | [optional] |
| **allow_work_plan_per_minute_granularity** | **bool** | Indicates whether or not per minute granularity for scheduling will be enabled for this business unit. Defaults to false. | [optional] |
{: class="table table-striped"}


