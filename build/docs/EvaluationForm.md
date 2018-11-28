---
title: EvaluationForm
---
## EvaluationForm

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The evaluation form name | |
| **modified_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **published** | **bool** |  | [optional] |
| **context_id** | **str** |  | [optional] |
| **question_groups** | [**list[EvaluationQuestionGroup]**](EvaluationQuestionGroup.html) | A list of question groups | |
| **published_versions** | [**DomainEntityListingEvaluationForm**](DomainEntityListingEvaluationForm.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


