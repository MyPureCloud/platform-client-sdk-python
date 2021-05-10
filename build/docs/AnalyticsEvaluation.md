---
title: AnalyticsEvaluation
---
## AnalyticsEvaluation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **calibration_id** | **str** | The calibration ID used for the purpose of training evaluators | [optional] |
| **context_id** | **str** | A unique identifier for an evaluation form, regardless of version | [optional] |
| **deleted** | **bool** | Whether the evaluation has been deleted | [optional] |
| **evaluation_id** | **str** | Unique identifier for the evaluation | [optional] |
| **evaluator_id** | **str** | A unique identifier of the user who evaluated the interaction | [optional] |
| **event_time** | **datetime** | Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **form_id** | **str** | ID of the evaluation form used | [optional] |
| **form_name** | **str** | Name of the evaluation form used | [optional] |
| **queue_id** | **str** | The ID of the associated queue | [optional] |
| **rescored** | **bool** | Whether the evaluation has been rescored at least once | [optional] |
| **user_id** | **str** | ID of the agent the evaluation was performed against | [optional] |
| **geto_total_critical_score** | **int** | Total critical score of the evaluation | [optional] |
| **geto_total_score** | **int** | Total score of the evaluation | [optional] |
{: class="table table-striped"}


