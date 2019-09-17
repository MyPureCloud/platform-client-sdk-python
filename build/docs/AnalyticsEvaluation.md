---
title: AnalyticsEvaluation
---
## AnalyticsEvaluation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **evaluation_id** | **str** | Unique identifier for the evaluation | [optional] |
| **evaluator_id** | **str** | A unique identifier of the PureCloud user who evaluated the interaction | [optional] |
| **user_id** | **str** | Unique identifier for the user being evaluated | [optional] |
| **event_time** | **datetime** | Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **queue_id** | **str** | Unique identifier for the queue the conversation was on | [optional] |
| **form_id** | **str** | Unique identifier for the form used to evaluate the conversation/agent | [optional] |
| **context_id** | **str** | A unique identifier for an evaluation form, regardless of version | [optional] |
| **form_name** | **str** | Name of the evaluation form | [optional] |
| **calibration_id** | **str** | The calibration id used for the purpose of training evaluators | [optional] |
| **o_total_score** | **int** |  | [optional] |
| **o_total_critical_score** | **int** |  | [optional] |
{: class="table table-striped"}


