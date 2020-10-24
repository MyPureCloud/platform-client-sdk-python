---
title: DependencyStatus
---
## DependencyStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **user** | [**User**](User.html) | User that initiated the build. | [optional] |
| **client** | [**DomainEntityRef**](DomainEntityRef.html) | OAuth client that initiated the build. | [optional] |
| **build_id** | **str** |  | [optional] |
| **date_started** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_completed** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | **str** |  | [optional] |
| **failed_objects** | [**list[FailedObject]**](FailedObject.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


