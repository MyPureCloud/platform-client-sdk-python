# UserAuthorization

## UserAuthorization

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **roles** | [list[DomainRole]](DomainRole) |  | [optional] |
| **unused_roles** | [list[DomainRole]](DomainRole) | A collection of the roles the user is not using | [optional] |
| **permissions** | list[str] | A collection of the permissions granted by all assigned roles | [optional] |
| **permission_policies** | [list[ResourcePermissionPolicy]](ResourcePermissionPolicy) | The policies configured for assigned permissions. | [optional] |



_PureCloudPlatformClientV2 247.0.0_
