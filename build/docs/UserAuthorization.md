---
title: UserAuthorization
---
## UserAuthorization

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **roles** | [**list[DomainRole]**](DomainRole.html) |  | [optional] |
| **unused_roles** | [**list[DomainRole]**](DomainRole.html) | A collection of the roles the user is not using | [optional] |
| **permissions** | **list[str]** | A collection of the permissions granted by all assigned roles | [optional] |
| **permission_policies** | [**list[ResourcePermissionPolicy]**](ResourcePermissionPolicy.html) | The policies configured for assigned permissions. | [optional] |
{: class="table table-striped"}


