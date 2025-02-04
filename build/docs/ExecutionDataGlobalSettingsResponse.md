# ExecutionDataGlobalSettingsResponse

## ExecutionDataGlobalSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **enabled** | bool | whether or not the setting is enabled. | [optional] |
| **modified_by** | [UserReference](UserReference) | User that last changed the setting. | [optional] |
| **modified_by_client** | [DomainEntityRef](DomainEntityRef) | OAuth client that last changed the setting. | [optional] |
| **date_modified** | datetime | The time this setting was set. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
