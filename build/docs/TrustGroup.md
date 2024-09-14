# TrustGroup

## TrustGroup

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
| **images** | [list[UserImage]](UserImage) |  | [optional] |
| **addresses** | [list[GroupContact]](GroupContact) |  | [optional] |
| **rules_visible** | bool | Are membership rules visible to the person requesting to view the group | |
| **visibility** | str | Who can view this group | |
| **roles_enabled** | bool | Allow roles to be assigned to this group | [optional] |
| **owners** | [list[User]](User) | Owners of the group | [optional] |
| **date_created** | datetime | The date on which the trusted group was added. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [OrgUser](OrgUser) | The user that added trusted group. | [optional] |



_PureCloudPlatformClientV2 211.1.0_
