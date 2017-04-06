---
title: Evaluation
---
## Evaluation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **conversation** | [**Conversation**](Conversation.html) |  | [optional] |
| **evaluation_form** | [**EvaluationForm**](EvaluationForm.html) | Evaluation form used for evaluation. | [optional] |
| **evaluator** | [**User**](User.html) |  | [optional] |
| **agent** | [**User**](User.html) |  | [optional] |
| **calibration** | [**Calibration**](Calibration.html) |  | [optional] |
| **status** | **str** |  | [optional] |
| **answers** | [**EvaluationScoringSet**](EvaluationScoringSet.html) |  | [optional] |
| **agent_has_read** | **bool** |  | [optional] |
| **release_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **assigned_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **changed_date** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **queue** | [**Queue**](Queue.html) |  | [optional] |
| **never_release** | **bool** | Signifies if the evaluation is never to be released. This cannot be set true if release date is also set. | [optional] |
| **resource_id** | **str** | Only used for email evaluations. Will be null for all other evaluations. | [optional] |
| **resource_type** | **str** | The type of resource. Only used for email evaluations. Will be null for evaluations on all other resources. | [optional] |
| **redacted** | **bool** | Is only true when the user making the request does not have sufficient permissions to see evaluation | [optional] |
| **is_scoring_index** | **bool** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


