# BuTimeOffLimitResponse

## BuTimeOffLimitResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **staffing_group** | [StaffingGroupReference](StaffingGroupReference) | The staffing group to which this time-off limit is associated. If managementUnit is set, then the staffing group belongs to that management unit.Otherwise, if managementUnit is not set, it is a business unit level staffing group.At least one of managementUnit and staffingGroup must be set | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this time-off limit is associated. If staffingGroup is set, then the limit is associated with that staffing group, which belongs to this management unit.At least one of managementUnit and staffingGroup must be set | [optional] |
| **granularity** | str | Granularity choice for time off limit | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time-off limit | |
| **full_day_time_off_start_time** | str | The start time of full day time off requests associated with this limit interval in HH:mm format. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 265.0.0_
