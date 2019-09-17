---
title: UserRecording
---
## UserRecording

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **content_uri** | **str** |  | [optional] |
| **workspace** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **conversation** | [**Conversation**](Conversation.html) |  | [optional] |
| **content_length** | **int** |  | [optional] |
| **duration_milliseconds** | **int** |  | [optional] |
| **thumbnails** | [**list[DocumentThumbnail]**](DocumentThumbnail.html) |  | [optional] |
| **read** | **bool** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


