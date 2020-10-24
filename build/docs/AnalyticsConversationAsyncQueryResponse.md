---
title: AnalyticsConversationAsyncQueryResponse
---
## AnalyticsConversationAsyncQueryResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **cursor** | **str** | Optional cursor to indicate where to resume the results | [optional] |
| **data_availability_date** | **datetime** | Data available up to at least this datetime. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **conversations** | [**list[AnalyticsConversation]**](AnalyticsConversation.html) |  | [optional] |
{: class="table table-striped"}


