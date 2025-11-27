# BuTimeOffLimitResponse

## BuTimeOffLimitResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **staffing_group** | [StaffingGroupReference](StaffingGroupReference) | The staffing group to which this time-off limit is associated. If managementUnit is set, then the staffing group belongs to that management unit.Otherwise, if managementUnit is not set, it is a business unit level staffing group.At least one of managementUnit and staffingGroup must be set | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this time-off limit is associated. If staffingGroup is set, then the limit is associated with that staffing group, which belongs to this management unit.At least one of managementUnit and staffingGroup must be set | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time-off limit | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 245.0.0_
