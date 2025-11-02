# FlowSettingsResponse

## FlowSettingsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **type** | str | The Flow Type | [optional] |
| **modified_by** | [UserReference](UserReference) | User that last changed the log level setting. | [optional] |
| **modified_by_client** | [DomainEntityRef](DomainEntityRef) | OAuth client that last changed the log level setting. | [optional] |
| **date_modified** | datetime | The time this log level was set. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **log_level_characteristics** | [FlowLogLevel](FlowLogLevel) | The log level set for this flow | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_
