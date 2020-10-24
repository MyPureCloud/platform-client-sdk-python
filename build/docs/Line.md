---
title: Line
---
## Line

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **properties** | **dict(str, object)** |  | [optional] |
| **edge_group** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **template** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **site** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **line_base_settings** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **primary_edge** | [**Edge**](Edge.html) | The primary edge associated to the line. (Deprecated) | [optional] |
| **secondary_edge** | [**Edge**](Edge.html) | The secondary edge associated to the line. (Deprecated) | [optional] |
| **logged_in_user** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **default_for_user** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


