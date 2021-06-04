---
title: WorkPlanShift
---
## WorkPlanShift

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | Name of the shift | |
| **days** | [**SetWrapperDayOfWeek**](SetWrapperDayOfWeek.html) | Days of the week applicable for this shift | [optional] |
| **flexible_start_time** | **bool** | Whether the start time of the shift is flexible | [optional] |
| **exact_start_time_minutes_from_midnight** | **int** | Exact start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == false | [optional] |
| **earliest_start_time_minutes_from_midnight** | **int** | Earliest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true | [optional] |
| **latest_start_time_minutes_from_midnight** | **int** | Latest start time of the shift defined as offset minutes from midnight. Used if flexibleStartTime == true | [optional] |
| **constrain_stop_time** | **bool** | Whether the latest stop time constraint for the shift is enabled.  Deprecated, use constrainLatestStopTime instead | [optional] |
| **constrain_latest_stop_time** | **bool** | Whether the latest stop time constraint for the shift is enabled | [optional] |
| **latest_stop_time_minutes_from_midnight** | **int** | Latest stop time of the shift defined as offset minutes from midnight. Used if constrainStopTime == true | [optional] |
| **constrain_earliest_stop_time** | **bool** | Whether the earliest stop time constraint for the shift is enabled | [optional] |
| **earliest_stop_time_minutes_from_midnight** | **int** | This is the earliest time a shift can end | [optional] |
| **start_increment_minutes** | **int** | Increment in offset minutes that would contribute to different possible start times for the shift. Used if flexibleStartTime == true | [optional] |
| **flexible_paid_time** | **bool** | Whether the paid time setting for the shift is flexible | [optional] |
| **exact_paid_time_minutes** | **int** | Exact paid time in minutes configured for the shift. Used if flexiblePaidTime == false | [optional] |
| **minimum_paid_time_minutes** | **int** | Minimum paid time in minutes configured for the shift. Used if flexiblePaidTime == true | [optional] |
| **maximum_paid_time_minutes** | **int** | Maximum paid time in minutes configured for the shift. Used if flexiblePaidTime == true | [optional] |
| **constrain_contiguous_work_time** | **bool** | Whether the contiguous time constraint for the shift is enabled | [optional] |
| **minimum_contiguous_work_time_minutes** | **int** | Minimum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true | [optional] |
| **maximum_contiguous_work_time_minutes** | **int** | Maximum contiguous time in minutes configured for the shift. Used if constrainContiguousWorkTime == true | [optional] |
| **activities** | [**list[WorkPlanActivity]**](WorkPlanActivity.html) | Activities configured for this shift | [optional] |
| **id** | **str** | ID of the shift. This is required only for the case of updating an existing shift | [optional] |
| **delete** | **bool** | If marked true for updating an existing shift, the shift will be permanently deleted | [optional] |
| **validation_id** | **str** | ID of shift in the context of work plan validation | [optional] |
{: class="table table-striped"}


