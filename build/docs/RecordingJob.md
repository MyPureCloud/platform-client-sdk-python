# RecordingJob

## RecordingJob

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **state** | str | The current state of the job. | |
| **recording_jobs_query** | [RecordingJobsQuery](RecordingJobsQuery) | Original query of the job. | [optional] |
| **date_created** | datetime | Date when the job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **total_conversations** | int | Total number of conversations affected. | [optional] |
| **total_recordings** | int | Total number of recordings affected. | [optional] |
| **total_skipped_recordings** | int | Total number of recordings that have been skipped. | [optional] |
| **total_failed_recordings** | int | Total number of recordings that the bulk job failed to process. | [optional] |
| **total_processed_recordings** | int | Total number of recordings have been processed. | [optional] |
| **percent_progress** | int | Progress in percentage based on the number of recordings | [optional] |
| **error_message** | str | Error occurred during the job execution | [optional] |
| **failed_recordings** | str | Get IDs of recordings that the bulk job failed for | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **user** | [AddressableEntityRef](AddressableEntityRef) | Details of the user created the job | [optional] |



_PureCloudPlatformClientV2 234.0.0_
