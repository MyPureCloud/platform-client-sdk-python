---
title: AnalyticsSurvey
---
## AnalyticsSurvey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **survey_id** | **str** | Unique identifier for the survey | [optional] |
| **survey_form_id** | **str** | Unique identifier for the survey form | [optional] |
| **survey_form_context_id** | **str** | Unique identifier for the survey form, regardless of version | [optional] |
| **event_time** | **datetime** | Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **user_id** | **str** | A unique identifier of the PureCloud user | [optional] |
| **queue_id** | **str** | Unique identifier for the queue the conversation was on | [optional] |
| **status** | **str** | Survey status | [optional] |
| **geto_survey_total_score** | **int** | Creation date of survey | [optional] |
| **survey_promoter_score** | **int** | NPS score of the survey | [optional] |
| **getsurvey_completed_date** | **datetime** | Completion date/time of the survey. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **media_types** | **list[str]** | Media types associated with the conversation | [optional] |
| **language_ids** | **list[str]** | Language IDs associated with the conversation | [optional] |
| **skill_ids** | **list[str]** | Skill IDs associated with the conversation | [optional] |
{: class="table table-striped"}


