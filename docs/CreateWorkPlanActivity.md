# CreateWorkPlanActivity

## CreateWorkPlanActivity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **activity_code_id** | str | ID of the activity code associated with this activity | [optional] |
| **description** | str | Description of the activity | [optional] |
| **length_minutes** | int | Length of the activity in minutes | [optional] |
| **start_time_is_relative_to_shift_start** | bool | Whether the start time of the activity is relative to the start time of the shift it belongs to | [optional] |
| **flexible_start_time** | bool | Whether the start time of the activity is flexible | [optional] |
| **earliest_start_time_minutes** | int | Earliest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart &#x3D;&#x3D; true else its based on midnight. Used if flexibleStartTime &#x3D;&#x3D; true | [optional] |
| **latest_start_time_minutes** | int | Latest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart &#x3D;&#x3D; true else its based on midnight. Used if flexibleStartTime &#x3D;&#x3D; true | [optional] |
| **exact_start_time_minutes** | int | Exact activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart &#x3D;&#x3D; true else its based on midnight. Used if flexibleStartTime &#x3D;&#x3D; false | [optional] |
| **start_time_increment_minutes** | int | Increment in offset minutes that would contribute to different possible start times for the activity | [optional] |
| **counts_as_paid_time** | bool | Whether the activity is paid | [optional] |
| **counts_as_contiguous_work_time** | bool | Whether the activity duration is counted towards contiguous work time | [optional] |
| **minimum_length_from_shift_start_minutes** | int | The minimum duration between shift start and shift item (e.g., break or meal) start in minutes | [optional] |
| **minimum_length_from_shift_end_minutes** | int | The minimum duration between shift item (e.g., break or meal) end and shift end in minutes | [optional] |



_PureCloudPlatformClientV2 210.0.0_
