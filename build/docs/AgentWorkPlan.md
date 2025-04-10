# AgentWorkPlan

## AgentWorkPlan

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **constrain_weekly_paid_time** | bool | Whether the weekly paid time constraint is enabled for this work plan | |
| **flexible_weekly_paid_time** | bool | Whether the weekly paid time constraint is flexible for this work plan | |
| **weekly_exact_paid_minutes** | int | Exact weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; false | |
| **weekly_minimum_paid_minutes** | int | Minimum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; true | |
| **weekly_maximum_paid_minutes** | int | Maximum weekly paid time in minutes for this work plan. Used if flexibleWeeklyPaidTime &#x3D;&#x3D; true | |
| **optional_days** | [SetWrapperDayOfWeek](SetWrapperDayOfWeek) | Optional days to schedule for this work plan | [optional] |
| **shifts** | [list[AgentWorkPlanShift]](AgentWorkPlanShift) | Shifts in this work plan | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 225.0.0_
