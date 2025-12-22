# SchedulingSettingsRequest

## SchedulingSettingsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **max_occupancy_percent_for_deferred_work** | int | Max occupancy percent for deferred work | [optional] |
| **default_shrinkage_percent** | float | Default shrinkage percent for scheduling | [optional] |
| **shrinkage_overrides** | [ShrinkageOverrides](ShrinkageOverrides) | Shrinkage overrides for scheduling | [optional] |
| **planning_period** | [ValueWrapperPlanningPeriodSettings](ValueWrapperPlanningPeriodSettings) | Planning period settings for scheduling. Only one of planningPeriod or monthlyPlanningPeriod may be defined | [optional] |
| **monthly_planning_period** | [ValueWrapperMonthlyPlanningPeriodSettings](ValueWrapperMonthlyPlanningPeriodSettings) | Monthly planning period setting for scheduling. Only one of planningPeriod or monthlyPlanningPeriod may be defined | [optional] |
| **start_day_of_weekend** | str | Start day of weekend for scheduling | [optional] |



_PureCloudPlatformClientV2 246.1.0_
