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
| **participants** | [**list[AnalyticsParticipant]**](AnalyticsParticipant.html) | Participants in the conversation | [optional] |
| **evaluations** | [**list[AnalyticsEvaluation]**](AnalyticsEvaluation.html) | Evaluations tied to this conersation | [optional] |
{: class="table table-striped"}


