---
title: PatchSegment
---
## PatchSegment

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **is_active** | **bool** | Whether or not the segment is active. | [optional] |
| **display_name** | **str** | The display name of the segment. | |
| **version** | **int** | The version of the segment. | [optional] |
| **description** | **str** | A description of the segment. | [optional] |
| **color** | **str** | The hexadecimal color value of the segment. | [optional] |
| **should_display_to_agent** | **bool** | Whether or not the segment should be displayed to agent/supervisor users. | [optional] |
| **context** | [**Context**](Context.html) | The context of the segment. | [optional] |
| **journey** | [**Journey**](Journey.html) | The pattern of rules defining the segment. | [optional] |
| **assignment_expiration_days** | **int** | Time, in days, from when the segment is assigned until it is automatically unassigned. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the segment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | **datetime** | Timestamp indicating when the the segment was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


