# CreateWorkPlan

## CreateWorkPlan

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | Name of this work plan | |
| **enabled** | bool | Whether the work plan is enabled for scheduling | [optional] |
| **constrain_weekly_paid_time** | bool | Whether the weekly paid time constraint is enabled for this work plan | [optional] |
| **flexible_weekly_paid_time** | bool | Whether the weekly paid time constraint is flexible for this work plan | [optional] |
| **weekly_exact_paid_minutes** | int | Exact weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; false | [optional] |
| **weekly_minimum_paid_minutes** | int | Minimum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; true | [optional] |
| **weekly_maximum_paid_minutes** | int | Maximum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; true | [optional] |
| **constrain_paid_time_granularity** | bool | Whether paid time granularity should be constrained for this workplan | [optional] |
| **paid_time_granularity_minutes** | int | Granularity in minutes allowed for shift paid time in this work plan. Used if constrainPaidTimeGranularity &#x3D;&#x3D; true | [optional] |
| **constrain_minimum_time_between_shifts** | bool | Whether the minimum time between shifts constraint is enabled for this work plan | [optional] |
| **minimum_time_between_shifts_minutes** | int | Minimum time between shifts in minutes defined in this work plan. Used if constrainMinimumTimeBetweenShifts &#x3D;&#x3D; true | [optional] |
| **maximum_days** | int | Maximum number days in a week allowed to be scheduled for this work plan | [optional] |
| **minimum_consecutive_non_working_minutes_per_week** | int | Minimum amount of consecutive non working minutes per week that agents who are assigned this work plan are allowed to have off | [optional] |
| **constrain_maximum_consecutive_working_weekends** | bool | Whether to constrain the maximum consecutive working weekends | [optional] |
| **maximum_consecutive_working_weekends** | int | The maximum number of consecutive weekends that agents who are assigned to this work plan are allowed to work | [optional] |
| **minimum_working_days_per_week** | int | The minimum number of days that agents assigned to a work plan must work per week | [optional] |
| **constrain_maximum_consecutive_working_days** | bool | Whether to constrain the maximum consecutive working days | [optional] |
| **maximum_consecutive_working_days** | int | The maximum number of consecutive days that agents assigned to this work plan are allowed to work. Used if constrainMaximumConsecutiveWorkingDays &#x3D;&#x3D; true | [optional] |
| **minimum_shift_start_distance_minutes** | int | The time period in minutes for the duration between the start times of two consecutive working days | [optional] |
| **minimum_days_off_per_planning_period** | int | Minimum days off in the planning period | [optional] |
| **maximum_days_off_per_planning_period** | int | Maximum days off in the planning period | [optional] |
| **minimum_paid_minutes_per_planning_period** | int | Minimum paid minutes in the planning period | [optional] |
| **maximum_paid_minutes_per_planning_period** | int | Maximum paid minutes in the planning period | [optional] |
| **optional_days** | [SetWrapperDayOfWeek](SetWrapperDayOfWeek) | Optional days to schedule for this work plan | [optional] |
| **shift_start_variance_type** | str | This constraint ensures that an agent starts each workday within a user-defined time threshold | [optional] |
| **shift_start_variances** | [ListWrapperShiftStartVariance](ListWrapperShiftStartVariance) | Variance in minutes among start times of shifts in this work plan | [optional] |
| **shifts** | [list[CreateWorkPlanShift]](CreateWorkPlanShift) | Shifts in this work plan | [optional] |
| **agents** | [list[UserReference]](UserReference) | Agents in this work plan | [optional] |



_PureCloudPlatformClientV2 210.0.0_
