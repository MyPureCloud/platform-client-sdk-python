# EventLog

## EventLog

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **error_entity** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **related_entity** | [DomainEntityRef](DomainEntityRef) |  | [optional] |
| **timestamp** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **level** | str |  | [optional] |
| **category** | str |  | [optional] |
| **correlation_id** | str |  | [optional] |
| **event_message** | [EventMessage](EventMessage) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_
