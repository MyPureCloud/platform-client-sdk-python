---
title: DomainOrganizationRoleUpdate
---
## DomainOrganizationRoleUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the role | |
| **description** | **str** |  | [optional] |
| **default_role_id** | **str** |  | [optional] |
| **permissions** | **list[str]** |  | [optional] |
| **permission_policies** | [**list[DomainPermissionPolicy]**](DomainPermissionPolicy.html) |  | [optional] |
| **user_count** | **int** |  | [optional] |
| **role_needs_update** | **bool** | Optional unless patch operation. | [optional] |
| **default** | **bool** |  | [optional] |
| **base** | **bool** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


