---
title: AsyncConversationQuery
---
## AsyncConversationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Specifies the date and time range of data being queried. Results will include conversations that both started on a day touched by the interval AND either started, ended, or any activity during the interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **conversation_filters** | [**list[ConversationDetailQueryFilter]**](ConversationDetailQueryFilter.html) | Filters that target conversation-level data | [optional] |
| **segment_filters** | [**list[SegmentDetailQueryFilter]**](SegmentDetailQueryFilter.html) | Filters that target individual segments within a conversation | [optional] |
| **evaluation_filters** | [**list[EvaluationDetailQueryFilter]**](EvaluationDetailQueryFilter.html) | Filters that target evaluations | [optional] |
| **media_endpoint_stat_filters** | [**list[MediaEndpointStatDetailQueryFilter]**](MediaEndpointStatDetailQueryFilter.html) | Filters that target mediaEndpointStats | [optional] |
| **survey_filters** | [**list[SurveyDetailQueryFilter]**](SurveyDetailQueryFilter.html) | Filters that target surveys | [optional] |
| **order** | **str** | Sort the result set in ascending/descending order. Default is ascending | [optional] |
| **order_by** | **str** | Specify which data element within the result set to use for sorting. The options  to use as a basis for sorting the results: conversationStart, segmentStart, and segmentEnd. If not specified, the default is conversationStart | [optional] |
| **limit** | **int** | Specify number of results to be returned | [optional] |
| **start_of_day_interval_matching** | **bool** | Add a filter to only include conversations that started after the beginning of the interval start date (UTC) | [optional] |
{: class="table table-striped"}


