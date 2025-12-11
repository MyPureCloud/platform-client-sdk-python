# DomainOrganizationRoleUpdate

## DomainOrganizationRoleUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | role id | [optional] |
| **name** | str | The name of the role | |
| **description** | str |  | [optional] |
| **default_role_id** | str |  | [optional] |
| **permissions** | list[str] |  | [optional] |
| **unused_permissions** | list[str] | A collection of the permissions the role is not using | [optional] |
| **permission_policies** | [list[DomainPermissionPolicy]](DomainPermissionPolicy) |  | [optional] |
| **user_count** | int |  | [optional] |
| **role_needs_update** | bool | Optional unless patch operation. | [optional] |
| **base_license** | str |  | [optional] |
| **addon_licenses** | list[str] |  | [optional] |
| **date_license_last_updated** | datetime | The time that this role licenses were most recently updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **base** | bool |  | [optional] |
| **default** | bool |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_
