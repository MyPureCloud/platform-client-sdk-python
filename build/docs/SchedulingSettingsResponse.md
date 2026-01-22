# SchedulingSettingsResponse

## SchedulingSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **max_occupancy_percent_for_deferred_work** | int | Max occupancy percent for deferred work | [optional] |
| **default_shrinkage_percent** | float | Default shrinkage percent for scheduling | [optional] |
| **shrinkage_overrides** | [ShrinkageOverrides](ShrinkageOverrides) | Shrinkage overrides for scheduling | [optional] |
| **planning_period** | [PlanningPeriodSettings](PlanningPeriodSettings) | Planning period settings for scheduling. Only one of planningPeriod or monthlyPlanningPeriod will be defined if applicable, but both can be null | [optional] |
| **monthly_planning_period** | [MonthlyPlanningPeriodSettings](MonthlyPlanningPeriodSettings) | Monthly planning period settings for scheduling. Only one of planningPeriod or monthlyPlanningPeriod will be defined if applicable, but both can be null | [optional] |
| **start_day_of_weekend** | str | Start day of weekend for scheduling | [optional] |



_PureCloudPlatformClientV2 249.0.0_
