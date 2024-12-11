# Workspace

## Workspace

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The current name of the workspace. | |
| **type** | str |  | [optional] |
| **is_current_user_workspace** | bool |  | [optional] |
| **user** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **bucket** | str |  | [optional] |
| **date_created** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **summary** | [WorkspaceSummary](WorkspaceSummary) |  | [optional] |
| **acl** | list[str] |  | [optional] |
| **description** | str |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 218.0.0_
