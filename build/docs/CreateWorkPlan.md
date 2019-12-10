---
title: CreateWorkPlan
---
## CreateWorkPlan

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | Name of this work plan | |
| **enabled** | **bool** | Whether the work plan is enabled for scheduling | [optional] |
| **constrain_weekly_paid_time** | **bool** | Whether the weekly paid time constraint is enabled for this work plan | [optional] |
| **flexible_weekly_paid_time** | **bool** | Whether the weekly paid time constraint is flexible for this work plan | [optional] |
| **weekly_exact_paid_minutes** | **int** | Exact weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == false | [optional] |
| **weekly_minimum_paid_minutes** | **int** | Minimum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true | [optional] |
| **weekly_maximum_paid_minutes** | **int** | Maximum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime == true | [optional] |
| **constrain_paid_time_granularity** | **bool** | Whether paid time granularity should be constrained for this workplan | [optional] |
| **paid_time_granularity_minutes** | **int** | Granularity in minutes allowed for shift paid time in this work plan. Used if constrainPaidTimeGranularity == true | [optional] |
| **constrain_minimum_time_between_shifts** | **bool** | Whether the minimum time between shifts constraint is enabled for this work plan | [optional] |
| **minimum_time_between_shifts_minutes** | **int** | Minimum time between shifts in minutes defined in this work plan. Used if constrainMinimumTimeBetweenShifts == true | [optional] |
| **maximum_days** | **int** | Maximum number days in a week allowed to be scheduled for this work plan | [optional] |
| **minimum_working_days_per_week** | **int** | The minimum number of days that agents assigned to a work plan must work per week | [optional] |
| **optional_days** | [**SetWrapperDayOfWeek**](SetWrapperDayOfWeek.html) | Optional days to schedule for this work plan | [optional] |
| **shift_start_variances** | [**ListWrapperShiftStartVariance**](ListWrapperShiftStartVariance.html) | Variance in minutes among start times of shifts in this work plan | [optional] |
| **shifts** | [**list[CreateWorkPlanShift]**](CreateWorkPlanShift.html) | Shifts in this work plan | [optional] |
| **agents** | [**list[UserReference]**](UserReference.html) | Agents in this work plan | [optional] |
{: class="table table-striped"}


