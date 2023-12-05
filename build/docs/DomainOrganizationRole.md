---
title: DomainOrganizationRole
---
## DomainOrganizationRole

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | role id | [optional] |
| **name** | **str** |  | [optional] |
| **description** | **str** |  | [optional] |
| **default_role_id** | **str** |  | [optional] |
| **permissions** | **list[str]** |  | [optional] |
| **unused_permissions** | **list[str]** | A collection of the permissions the role is not using | [optional] |
| **permission_policies** | [**list[DomainPermissionPolicy]**](DomainPermissionPolicy.html) |  | [optional] |
| **user_count** | **int** |  | [optional] |
| **role_needs_update** | **bool** | Optional unless patch operation. | [optional] |
| **default** | **bool** |  | [optional] |
| **base** | **bool** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


