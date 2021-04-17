---
title: AnalyticsConversation
---
## AnalyticsConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conversation_end** | **datetime** | The end time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation_id** | **str** | Unique identifier for the conversation | [optional] |
| **conversation_start** | **datetime** | The start time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **division_ids** | **list[str]** | Identifier(s) of division(s) associated with a conversation | [optional] |
| **external_tag** | **str** | External tag for the conversation | [optional] |
| **media_stats_min_conversation_mos** | **float** | The lowest estimated average MOS among all the audio streams belonging to this conversation | [optional] |
| **media_stats_min_conversation_r_factor** | **float** | The lowest R-factor value among all of the audio streams belonging to this conversation | [optional] |
| **originating_direction** | **str** | The original direction of the conversation | [optional] |
| **evaluations** | [**list[AnalyticsEvaluation]**](AnalyticsEvaluation.html) | Evaluations associated with this conversation | [optional] |
| **surveys** | [**list[AnalyticsSurvey]**](AnalyticsSurvey.html) | Surveys associated with this conversation | [optional] |
| **resolutions** | [**list[AnalyticsResolution]**](AnalyticsResolution.html) | Resolutions associated with this conversation | [optional] |
| **participants** | [**list[AnalyticsParticipant]**](AnalyticsParticipant.html) | Participants in the conversation | [optional] |
{: class="table table-striped"}


