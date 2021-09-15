---
title: Annotation
---
## Annotation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **location** | **int** | Offset of annotation in milliseconds. | [optional] |
| **duration_ms** | **int** | Duration of annotation in milliseconds. | [optional] |
| **absolute_location** | **int** | Offset of annotation (milliseconds) from start of recording. | [optional] |
| **absolute_duration_ms** | **int** | Duration of annotation (milliseconds). | [optional] |
| **recording_location** | **int** | Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts | [optional] |
| **recording_duration_ms** | **int** | Duration of annotation (milliseconds), adjusted for any recording cuts. | [optional] |
| **user** | [**User**](User.html) | User that created this annotation (if any). | [optional] |
| **description** | **str** | Text of annotation. Maximum character limit is 500. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


