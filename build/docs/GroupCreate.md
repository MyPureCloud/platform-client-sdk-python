# GroupCreate

## GroupCreate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The group name. | |
| **description** | str |  | [optional] |
| **date_modified** | datetime | Last modified date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **member_count** | int | Number of members. | [optional] |
| **state** | str | Active, inactive, or deleted state. | [optional] |
| **version** | int | Current version for this resource. | [optional] |
| **type** | str | Type of group. | |
| **images** | [list[Image]](Image) |  | [optional] |
| **addresses** | [list[GroupContact]](GroupContact) |  | [optional] |
| **rules_visible** | bool | Are membership rules visible to the person requesting to view the group | |
| **visibility** | str | Who can view this group | |
| **roles_enabled** | bool | Allow roles to be assigned to this group | [optional] |
| **include_owners** | bool | Allow owners to be included as members of the group | [optional] |
| **calls_enabled** | bool | Allow calls to be placed to this group. | [optional] |
| **owner_ids** | list[str] | Owners of the group | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 219.0.0_
