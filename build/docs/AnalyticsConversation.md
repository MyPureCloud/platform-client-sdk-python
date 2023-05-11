---
title: AnalyticsConversation
---
## AnalyticsConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conference_start** | **datetime** | The start time of a conference call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation_end** | **datetime** | The end time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversation_id** | **str** | Unique identifier for the conversation | [optional] |
| **conversation_initiator** | **str** | Indicates the participant purpose of the participant initiating a message conversation | [optional] |
| **conversation_start** | **datetime** | The start time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **customer_participation** | **bool** | Indicates a messaging conversation in which the customer participated by sending at least one message | [optional] |
| **division_ids** | **list[str]** | Identifier(s) of division(s) associated with a conversation | [optional] |
| **external_tag** | **str** | External tag for the conversation | [optional] |
| **knowledge_base_ids** | **list[str]** | The unique identifier(s) of the knowledge base(s) used | [optional] |
| **media_stats_min_conversation_mos** | **float** | The lowest estimated average MOS among all the audio streams belonging to this conversation | [optional] |
| **media_stats_min_conversation_r_factor** | **float** | The lowest R-factor value among all of the audio streams belonging to this conversation | [optional] |
| **originating_direction** | **str** | The original direction of the conversation | [optional] |
| **self_served** | **bool** | Indicates whether all flow sessions were self serviced | [optional] |
| **evaluations** | [**list[AnalyticsEvaluation]**](AnalyticsEvaluation.html) | Evaluations associated with this conversation | [optional] |
| **surveys** | [**list[AnalyticsSurvey]**](AnalyticsSurvey.html) | Surveys associated with this conversation | [optional] |
| **resolutions** | [**list[AnalyticsResolution]**](AnalyticsResolution.html) | Resolutions associated with this conversation | [optional] |
| **participants** | [**list[AnalyticsParticipant]**](AnalyticsParticipant.html) | Participants in the conversation | [optional] |
{: class="table table-striped"}


