---
title: Endpoint
---
## Endpoint

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | Name | |
| **description** | **str** | The resource&#39;s description. | [optional] |
| **version** | **int** | The current version of the resource. | [optional] |
| **date_created** | **datetime** | The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** | The ID of the user that last modified the resource. | [optional] |
| **created_by** | **str** | The ID of the user that created the resource. | [optional] |
| **state** | **str** | Indicates if the resource is active, inactive, or deleted. | [optional] |
| **modified_by_app** | **str** | The application that last modified the resource. | [optional] |
| **created_by_app** | **str** | The application that created the resource. | [optional] |
| **count** | **int** |  | [optional] |
| **properties** | **dict(str, object)** |  | [optional] |
| **schema** | [**UriReference**](UriReference.html) | Schema | |
| **enabled** | **bool** |  | [optional] |
| **site** | [**UriReference**](UriReference.html) |  | [optional] |
| **dids** | **list[str]** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


