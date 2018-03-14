---
title: Document
---
## Document

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **change_number** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_uploaded** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **content_uri** | **str** |  | [optional] |
| **workspace** | [**UriReference**](UriReference.html) |  | [optional] |
| **created_by** | [**UriReference**](UriReference.html) |  | [optional] |
| **uploaded_by** | [**UriReference**](UriReference.html) |  | [optional] |
| **content_type** | **str** |  | [optional] |
| **content_length** | **int** |  | [optional] |
| **system_type** | **str** |  | [optional] |
| **filename** | **str** |  | [optional] |
| **page_count** | **int** |  | [optional] |
| **read** | **bool** |  | [optional] |
| **caller_address** | **str** |  | [optional] |
| **receiver_address** | **str** |  | [optional] |
| **tags** | **list[str]** |  | [optional] |
| **tag_values** | [**list[TagValue]**](TagValue.html) |  | [optional] |
| **attributes** | [**list[DocumentAttribute]**](DocumentAttribute.html) |  | [optional] |
| **thumbnails** | [**list[DocumentThumbnail]**](DocumentThumbnail.html) |  | [optional] |
| **upload_status** | [**UriReference**](UriReference.html) |  | [optional] |
| **upload_destination_uri** | **str** |  | [optional] |
| **upload_method** | **str** |  | [optional] |
| **lock_info** | [**LockInfo**](LockInfo.html) |  | [optional] |
| **acl** | **list[str]** | A list of permitted action rights for the user making the request | [optional] |
| **sharing_status** | **str** |  | [optional] |
| **download_sharing_uri** | **str** |  | [optional] |
| **sharing_uri** | **str** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


