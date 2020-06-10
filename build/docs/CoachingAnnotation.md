---
title: CoachingAnnotation
---
## CoachingAnnotation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | The user who created the annotation. | [optional] |
| **date_created** | **datetime** | The date/time the annotation was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The last user to modify the annotation. | [optional] |
| **date_modified** | **datetime** | The date/time the annotation was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **text** | **str** | The text of the annotation. | |
| **is_deleted** | **bool** | Flag indicating whether the annotation is deleted. | [optional] |
| **access_type** | **str** | Determines the permissions required to view this item. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


