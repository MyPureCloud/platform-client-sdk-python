---
title: Trunk
---
## Trunk

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **trunk_type** | **str** | The type of this trunk. | [optional] |
| **edge** | [**UriReference**](UriReference.html) | The Edge using this trunk. | [optional] |
| **trunk_base** | [**UriReference**](UriReference.html) | The trunk base configuration used on this trunk. | [optional] |
| **trunk_metabase** | [**UriReference**](UriReference.html) | The metabase used to create this trunk. | [optional] |
| **edge_group** | [**UriReference**](UriReference.html) | The edge group associated with this trunk. | [optional] |
| **in_service** | **bool** | True if this trunk is in-service.  This comes from the trunk_enabled property of the referenced trunk base. | [optional] |
| **enabled** | **bool** | True if the Edge used by this trunk is in-service | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


