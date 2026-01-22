# CreateCapacityPlanStaffingGroupMetricChangeRequest

## CreateCapacityPlanStaffingGroupMetricChangeRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **number_of_weeks** | int | The number of weeks to which the metric change applies | |
| **week_start_number** | int | The start number of the week (starting from 1) to which the metric change applies, related to numberOfWeeks | |
| **value** | float | The value of the metric | |
| **metric** | str | The metric which is going to be modified for the selected staffing groups | |
| **notes** | str | Notes about the staffing groups metric changes | [optional] |
| **staffing_group_ids** | list[str] | The IDs of the staffing groups affected by the metric change | |
| **version** | int | The version of the capacity plan | |



_PureCloudPlatformClientV2 249.0.0_
