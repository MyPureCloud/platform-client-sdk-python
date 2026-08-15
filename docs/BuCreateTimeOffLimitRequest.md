# BuCreateTimeOffLimitRequest

## BuCreateTimeOffLimitRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **staffing_group_id** | str | The ID of the staffing group to which this time-off limit is associated. It can be either management unit or business unit level staffing group. One of managementUnitId or staffingGroupId must be set. This must not be set if managementUnitId has value | [optional] |
| **management_unit_id** | str | The ID of the management unit to which this time-off limit is associated. One of managementUnitId or staffingGroupId must be set. This must not be set if staffingGroupId has value | [optional] |
| **granularity** | str | Granularity choice for time off limit | [optional] |
| **full_day_time_off_start_time** | str | The start time of full day time off requests associated with this limit interval in HH:mm format.Setting this value is allowed only for time-off limit with fifteen minutes granularity | [optional] |



_PureCloudPlatformClientV2 264.0.0_
