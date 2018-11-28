---
title: AnalyticsConversation
---
## AnalyticsConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conversation_id** | **str** | Unique identifier for the conversation | [optional] |
| **conversation_start** | **datetime** | Date/time the conversation started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **conversation_end** | **datetime** | Date/time the conversation ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **media_stats_min_conversation_mos** | **float** | The lowest estimated average MOS among all the audio streams belonging to this conversation | [optional] |
| **media_stats_min_conversation_r_factor** | **float** | The lowest R-factor value among all of the audio streams belonging to this conversation | [optional] |
| **participants** | [**list[AnalyticsParticipant]**](AnalyticsParticipant.html) | Participants in the conversation | [optional] |
| **evaluations** | [**list[AnalyticsEvaluation]**](AnalyticsEvaluation.html) | Evaluations tied to this conversation | [optional] |
| **surveys** | [**list[AnalyticsSurvey]**](AnalyticsSurvey.html) | Surveys tied to this conversation | [optional] |
| **division_ids** | **list[str]** | Identifiers of divisions associated with this conversation | [optional] |
{: class="table table-striped"}


