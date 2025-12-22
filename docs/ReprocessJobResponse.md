# ReprocessJobResponse

## ReprocessJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | The description of the job. | [optional] |
| **date_start** | datetime | The date from which the reprocessing should begin. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **date_end** | datetime | The date at which the reprocessing should end. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **media_types** | list[str] | Media types used to filter interactions. | |
| **programs** | list[str] | The mapped programs to be included in the job. | |
| **dialects** | list[str] | Language dialects used to filter interactions. | [optional] |
| **created_by** | [AddressableEntityRef](AddressableEntityRef) | The user who created the job. | |
| **date_created** | datetime | The date the job was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **job_status** | str | The status of the job. | |
| **queue_order** | int | The position of the job in the queued jobs. | [optional] |
| **processed_interactions_count** | int | The amount of interactions successfully reprocessed. | |
| **failed_interactions_count** | int | The amount of failed interactions. | |
| **total_interactions_count** | int | The amount of interactions in the job. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
