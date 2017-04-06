---
title: Line
---
## Line

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
| **properties** | **dict(str, object)** |  | [optional] |
| **edge_group** | [**UriReference**](UriReference.html) |  | [optional] |
| **template** | [**UriReference**](UriReference.html) |  | [optional] |
| **site** | [**UriReference**](UriReference.html) |  | [optional] |
| **line_base_settings** | [**UriReference**](UriReference.html) |  | [optional] |
| **primary_edge** | [**Edge**](Edge.html) | The primary edge associated to the line. (Deprecated) | [optional] |
| **secondary_edge** | [**Edge**](Edge.html) | The secondary edge associated to the line. (Deprecated) | [optional] |
| **logged_in_user** | [**UriReference**](UriReference.html) |  | [optional] |
| **default_for_user** | [**UriReference**](UriReference.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


