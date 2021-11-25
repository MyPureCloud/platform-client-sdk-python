---
title: Outcome
---
## Outcome

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **is_active** | **bool** | Whether or not the outcome is active. | [optional] |
| **display_name** | **str** | The display name of the outcome. | |
| **version** | **int** | The version of the outcome. | [optional] |
| **description** | **str** | A description of the outcome. | [optional] |
| **is_positive** | **bool** | Whether or not the outcome is positive. | [optional] |
| **context** | [**Context**](Context.html) | The context of the outcome. | [optional] |
| **journey** | [**Journey**](Journey.html) | The pattern of rules defining the filter of the outcome. | [optional] |
| **associated_value_field** | [**AssociatedValueField**](AssociatedValueField.html) | The field from the event indicating the associated value. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **created_date** | **datetime** | Timestamp indicating when the outcome was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_date** | **datetime** | Timestamp indicating when the outcome was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
{: class="table table-striped"}


