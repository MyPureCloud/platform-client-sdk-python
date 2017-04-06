---
title: Site
---
## Site

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
| **primary_sites** | [**list[UriReference]**](UriReference.html) |  | [optional] |
| **secondary_sites** | [**list[UriReference]**](UriReference.html) |  | [optional] |
| **primary_edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **secondary_edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **addresses** | [**list[Contact]**](Contact.html) |  | [optional] |
| **edges** | [**list[Edge]**](Edge.html) |  | [optional] |
| **edge_auto_update_config** | [**EdgeAutoUpdateConfig**](EdgeAutoUpdateConfig.html) | Recurrance rule, time zone, and start/end settings for automatic edge updates for this site | [optional] |
| **location** | [**LocationDefinition**](LocationDefinition.html) | Location | |
| **managed** | **bool** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


