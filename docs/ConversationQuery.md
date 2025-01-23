# ConversationQuery

## ConversationQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conversation_filters** | [list[ConversationDetailQueryFilter]](ConversationDetailQueryFilter) | Filters that target conversation-level data | [optional] |
| **segment_filters** | [list[SegmentDetailQueryFilter]](SegmentDetailQueryFilter) | Filters that target individual segments within a conversation | [optional] |
| **evaluation_filters** | [list[EvaluationDetailQueryFilter]](EvaluationDetailQueryFilter) | Filters that target evaluations | [optional] |
| **survey_filters** | [list[SurveyDetailQueryFilter]](SurveyDetailQueryFilter) | Filters that target surveys | [optional] |
| **resolution_filters** | [list[ResolutionDetailQueryFilter]](ResolutionDetailQueryFilter) | Filters that target resolutions | [optional] |
| **order** | str | Sort the result set in ascending/descending order. Default is ascending | [optional] |
| **order_by** | str | Specify which data element within the result set to use for sorting. The options  to use as a basis for sorting the results: conversationStart, segmentStart, and segmentEnd. If not specified, the default is conversationStart | [optional] |
| **interval** | str | Specifies the date and time range of data being queried. Results will only include conversations that started on a day touched by the interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **aggregations** | [list[AnalyticsQueryAggregation]](AnalyticsQueryAggregation) | Include faceted search and aggregate roll-ups describing your search results. This does not function as a filter, but rather, summary data about the data matching your filters | [optional] |
| **paging** | [PagingSpec](PagingSpec) | Page size and number to control iterating through large result sets. Default page size is 25 | [optional] |



_PureCloudPlatformClientV2 220.0.0_
