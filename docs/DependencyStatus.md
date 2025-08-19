# DependencyStatus

## DependencyStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **user** | [User](User) | User that initiated the build. | [optional] |
| **client** | [DomainEntityRef](DomainEntityRef) | OAuth client that initiated the build. | [optional] |
| **build_id** | str |  | [optional] |
| **date_started** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | datetime | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | str |  | [optional] |
| **failed_objects** | [list[FailedObject]](FailedObject) |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
