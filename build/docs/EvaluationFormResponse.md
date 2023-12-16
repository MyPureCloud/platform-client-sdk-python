---
title: EvaluationFormResponse
---
## EvaluationFormResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The evaluation form name | |
| **modified_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **published** | **bool** |  | [optional] |
| **context_id** | **str** |  | [optional] |
| **question_groups** | [**list[EvaluationQuestionGroup]**](EvaluationQuestionGroup.html) | A list of question groups | [optional] |
| **weight_mode** | **str** | Mode for evaluation form weight | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


