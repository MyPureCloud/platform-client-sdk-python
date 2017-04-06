---
title: PhoneBase
---
## PhoneBase

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
| **phone_meta_base** | [**UriReference**](UriReference.html) | A phone metabase is essentially a database for storing phone configuration settings, which simplifies the configuration process. | |
| **lines** | [**list[LineBase]**](LineBase.html) | The list of linebases associated with the phone base. | |
| **properties** | **dict(str, object)** |  | [optional] |
| **capabilities** | [**PhoneCapabilities**](PhoneCapabilities.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


