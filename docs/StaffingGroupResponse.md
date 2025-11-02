# StaffingGroupResponse

## StaffingGroupResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the staffing group | |
| **users** | [list[UserReference]](UserReference) | The list of users that belong to the staffing group | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The ID of the management unit to which the staffing group users belong. If undefined the staffing group can include users from the entire business unit | [optional] |
| **planning_groups** | [list[PlanningGroupReference]](PlanningGroupReference) | The list of planning groups that are associated with the staffing group | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the staffing group | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_
