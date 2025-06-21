# GroupUpdate

## GroupUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The group name. | [optional] |
| **description** | str |  | [optional] |
| **state** | str | State of the group. | [optional] |
| **version** | int | Current version for this resource. | |
| **images** | [list[Image]](Image) |  | [optional] |
| **addresses** | [list[GroupContact]](GroupContact) |  | [optional] |
| **rules_visible** | bool | Are membership rules visible to the person requesting to view the group | [optional] |
| **visibility** | str | Who can view this group | [optional] |
| **roles_enabled** | bool | Allow roles to be assigned to this group | [optional] |
| **include_owners** | bool | Allow owners to be included as members of the group | [optional] |
| **calls_enabled** | bool | Allow calls to be placed to this group. | [optional] |
| **owner_ids** | list[str] | Owners of the group | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 231.0.0_
