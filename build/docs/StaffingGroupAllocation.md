# StaffingGroupAllocation

## StaffingGroupAllocation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **staffing_group_id** | str | The staffing group to which the result allocation belongs | |
| **shrinkage_percentages** | list[float] | The weekly projected shrinkage percentage of staffing group, in the scale of 0 - 100 | |
| **attrition_percentages** | list[float] | The weekly projected attrition percentage of the staffing group, in the scale of 0 - 100 | |
| **new_hires_full_time_equivalent_count** | list[float] | The weekly projected full time equivalent agents of new hire agents added to the staffing group | [optional] |
| **starting_weekly_full_time_equivalent_count** | float | The weekly count of full time equivalent agents that can be used for the first week of the capacity plan | |
| **planning_group_ids** | list[str] | The IDs of the planning groups associated with this staffing group | [optional] |



_PureCloudPlatformClientV2 241.0.0_
