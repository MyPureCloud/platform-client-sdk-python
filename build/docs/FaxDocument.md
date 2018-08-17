---
title: FaxDocument
---
## FaxDocument

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **content_uri** | **str** |  | [optional] |
| **workspace** | [**UriReference**](UriReference.html) |  | [optional] |
| **created_by** | [**UriReference**](UriReference.html) |  | [optional] |
| **content_type** | **str** |  | [optional] |
| **content_length** | **int** |  | [optional] |
| **filename** | **str** |  | [optional] |
| **read** | **bool** |  | [optional] |
| **page_count** | **int** |  | [optional] |
| **caller_address** | **str** |  | [optional] |
| **receiver_address** | **str** |  | [optional] |
| **thumbnails** | [**list[DocumentThumbnail]**](DocumentThumbnail.html) |  | [optional] |
| **download_sharing_uri** | **str** |  | [optional] |
| **sharing_uri** | **str** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


