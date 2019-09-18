---
title: RecordingJobsQuery
---
## RecordingJobsQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | **str** | Operation to perform bulk task | |
| **action_date** | **datetime** | The date when the action will be performed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **integration_id** | **str** | IntegrationId to Access AWS S3 bucket for bulk recording exports. This field is for EXPORT only | [optional] |
| **include_screen_recordings** | **bool** | Include Screen recordings for export action, default value = true  | [optional] |
| **conversation_query** | [**AsyncConversationQuery**](AsyncConversationQuery.html) | Conversation Query. Note: After the recording is created, it might take up to 48 hours for the recording to be included in the submitted job query. | |
{: class="table table-striped"}


