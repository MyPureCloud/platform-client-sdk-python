---
title: Trunk
---
## Trunk

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** |  | [optional] |
| **created_by** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **modified_by_app** | **str** |  | [optional] |
| **created_by_app** | **str** |  | [optional] |
| **trunk_type** | **str** | The type of this trunk. | [optional] |
| **edge** | [**UriReference**](UriReference.html) | The Edge using this trunk. | [optional] |
| **trunk_base** | [**UriReference**](UriReference.html) | The trunk base configuration used on this trunk. | [optional] |
| **trunk_metabase** | [**UriReference**](UriReference.html) | The metabase used to create this trunk. | [optional] |
| **edge_group** | [**UriReference**](UriReference.html) | The edge group associated with this trunk. | [optional] |
| **in_service** | **bool** | True if this trunk is in-service.  This comes from the trunk_enabled property of the referenced trunk base. | [optional] |
| **enabled** | **bool** | True if the Edge used by this trunk is in-service | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


