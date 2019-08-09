---
title: AsyncConversationQuery
---
## AsyncConversationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Specifies the date and time range of data being queried. Results will include conversations that both started on a day touched by the interval AND either started, ended, or any activity during the interval. Conversations that started before the earliest day of the interval will not be searched. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **conversation_filters** | [**list[AnalyticsQueryFilter]**](AnalyticsQueryFilter.html) | Filters that target conversation-level data | [optional] |
| **evaluation_filters** | [**list[AnalyticsQueryFilter]**](AnalyticsQueryFilter.html) | Filters that target quality management evaluation-level data | [optional] |
| **survey_filters** | [**list[AnalyticsQueryFilter]**](AnalyticsQueryFilter.html) | Filters that target quality management survey-level data | [optional] |
| **media_endpoint_stat_filters** | [**list[AnalyticsQueryFilter]**](AnalyticsQueryFilter.html) | Filters that target call quality of service data | [optional] |
| **segment_filters** | [**list[AnalyticsQueryFilter]**](AnalyticsQueryFilter.html) | Filters that target individual segments within a conversation | [optional] |
| **order** | **str** | Sort the result set in ascending/descending order. Default is ascending | [optional] |
| **order_by** | **str** | Specify which data element within the result set to use for sorting. The options  to use as a basis for sorting the results: conversationStart, segmentStart, and segmentEnd. If not specified, the default is conversationStart | [optional] |
| **limit** | **int** | Specify number of results to be returned | [optional] |
{: class="table table-striped"}

