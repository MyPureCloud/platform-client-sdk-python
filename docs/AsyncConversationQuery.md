# AsyncConversationQuery

## AsyncConversationQuery

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
| **interval** | str | Specifies the date and time range of data being queried. Results will include all conversations that had activity during the interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **limit** | int | Specify number of results to be returned | [optional] |
| **start_of_day_interval_matching** | bool | Add a filter to only include conversations that started after the beginning of the interval start date (UTC) | [optional] |



_PureCloudPlatformClientV2 219.0.0_
