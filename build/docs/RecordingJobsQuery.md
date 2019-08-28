---
title: RecordingJobsQuery
---
## RecordingJobsQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | **str** | Operation to perform bulk task | |
| **action_date** | **datetime** | The date when the action will be performed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **integration_id** | **str** | Integration ID | |
| **conversation_query** | [**AsyncConversationQuery**](AsyncConversationQuery.html) | Conversation Query. Note: After the recording is created, it might take up to 48 hours for the recording to be included in the submitted job query. | |
{: class="table table-striped"}


