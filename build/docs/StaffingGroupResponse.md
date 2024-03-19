---
title: StaffingGroupResponse
---
## StaffingGroupResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the staffing group | |
| **users** | [**list[UserReference]**](UserReference.html) | The list of users that belong to the staffing group | [optional] |
| **management_unit** | [**ManagementUnitReference**](ManagementUnitReference.html) | The ID of the management unit to which the staffing group users belong. If undefined the staffing group can include users from the entire business unit | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the staffing group | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


