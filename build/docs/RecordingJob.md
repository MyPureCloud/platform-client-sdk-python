---
title: RecordingJob
---
## RecordingJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **state** | **str** | The current state of the job. | |
| **recording_jobs_query** | [**RecordingJobsQuery**](RecordingJobsQuery.html) | Original query of the job. | [optional] |
| **date_created** | **datetime** | Date when the job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **total_conversations** | **int** | Total number of conversations affected. | [optional] |
| **total_recordings** | **int** | Total number of recordings affected. | [optional] |
| **total_processed_recordings** | **int** | Total number of recordings have been processed. | [optional] |
| **percent_progress** | **int** | Progress in percentage based on the number of recordings | [optional] |
| **error_message** | **str** | Error occurred during the job execution | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


