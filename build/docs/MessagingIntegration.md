---
title: MessagingIntegration
---
## MessagingIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A unique Integration Id | |
| **name** | **str** | The name of the Integration | |
| **status** | **str** | The status of the Integration | [optional] |
| **messenger_type** | **str** | The type of Messaging Integration | |
| **recipient** | [**UriReference**](UriReference.html) | The recipient associated to the Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | **datetime** | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **created_by** | [**UriReference**](UriReference.html) | User reference that created this Integration | [optional] |
| **modified_by** | [**UriReference**](UriReference.html) | User reference that last modified this Integration | [optional] |
| **version** | **int** | Version number required for updates. | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


