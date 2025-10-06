# AvailableTopic

## AvailableTopic

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | str |  | [optional] |
| **id** | str |  | [optional] |
| **permission_details** | [list[PermissionDetails]](PermissionDetails) | Full detailed permissions required to subscribe to the topic | [optional] |
| **requires_permissions** | list[str] | Permissions required to subscribe to the topic | [optional] |
| **requires_division_permissions** | bool | True if the subscribing user must belong to the same division as the topic object ID | [optional] |
| **requires_any_validator** | bool | If multiple permissions are required for this topic, such as both requiresCurrentUser and requiresDivisionPermissions, then true here indicates that meeting any one condition will satisfy the requirements; false indicates all conditions must be met. | [optional] |
| **enforced** | bool | Whether or not the permissions on this topic are enforced | [optional] |
| **visibility** | str | Visibility of this topic (Public or Preview) | [optional] |
| **schema** | dict(str, object) |  | [optional] |
| **requires_current_user** | bool | True if the topic user ID is required to match the subscribing user ID | [optional] |
| **requires_current_user_or_permission** | bool | True if permissions are only required when the topic user ID does not match the subscribing user ID | [optional] |
| **transports** | list[str] | Transports that support events for the topic | [optional] |
| **public_api_template_uri_paths** | list[str] |  | [optional] |
| **topic_parameters** | list[str] | Parameters in the topic name that can be substituted, in the order they appear in the topic name | [optional] |



_PureCloudPlatformClientV2 240.0.0_
