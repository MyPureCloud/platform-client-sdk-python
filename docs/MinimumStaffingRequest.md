# MinimumStaffingRequest

## MinimumStaffingRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **enabled** | bool | Whether the setting is turned on or off | [optional] |
| **minimum_value** | float | Default minimum staff value to be applied to all planning groups | [optional] |
| **planning_group_overrides** | [ListWrapperPlanningGroupMinimumsRequest](ListWrapperPlanningGroupMinimumsRequest) | List of planning groups with their minimum staff value overrides and the days to which the overrides apply. Setting the enclosed list to empty will clear out all existing overrides | [optional] |
| **applicable_intervals** | str | The intervals to which the minimum staff values will apply | [optional] |



_PureCloudPlatformClientV2 257.1.0_
