# AgentWorkPlanShift

## AgentWorkPlanShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **days** | [SetWrapperDayOfWeek](SetWrapperDayOfWeek) | Days of the week applicable for this shift | |
| **flexible_start_time** | bool | Whether the start time of the shift is flexible | |
| **exact_start_time_minutes_from_midnight** | int | Exact start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime &#x3D;&#x3D; false | |
| **earliest_start_time_minutes_from_midnight** | int | Earliest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime &#x3D;&#x3D; true | |
| **latest_start_time_minutes_from_midnight** | int | Latest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime &#x3D;&#x3D; true | |
| **earliest_stop_time_minutes_from_midnight** | int | This is the earliest time a shift can end | |
| **constrain_latest_stop_time** | bool | Whether the latest stop time constraint for the shift is enabled | |
| **latest_stop_time_minutes_from_midnight** | int | Latest stop time of the shift defined as offset minutes from midnight. Used if constrainStopTime &#x3D;&#x3D; true | |
| **flexible_paid_time** | bool | Whether the paid time setting for the shift is flexible | |
| **exact_paid_time_minutes** | int | Exact paid time in minutes configured for the shift. Used if flexiblePaidTime &#x3D;&#x3D; false | |
| **minimum_paid_time_minutes** | int | Minimum paid time in minutes configured for the shift. Used if flexiblePaidTime &#x3D;&#x3D; true | |
| **maximum_paid_time_minutes** | int | Maximum paid time in minutes configured for the shift. Used if flexiblePaidTime &#x3D;&#x3D; true | |
| **activities** | [list[AgentWorkPlanActivity]](AgentWorkPlanActivity) | Activities configured for this shift | |



_PureCloudPlatformClientV2 219.1.0_
