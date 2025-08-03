# KnowledgeSyncJobResponse

## KnowledgeSyncJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the sync job. | [optional] |
| **upload_key** | str |  | [optional] |
| **status** | str | The status of the export job. | [optional] |
| **report** | [KnowledgeSyncJobReport](KnowledgeSyncJobReport) | Report of the sync job | [optional] |
| **knowledge_base** | [KnowledgeBaseReference](KnowledgeBaseReference) | Knowledge base which document export belongs to. | [optional] |
| **date_created** | datetime | The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The timestamp of when the export stopped. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the operation | [optional] |
| **download_url** | str | The URL of the location at which the caller can download the sync file, when available. | [optional] |
| **failed_entities_url** | str | The URL of the location at which the caller can download the entities in json format that failed during the sync. | [optional] |
| **source** | [KnowledgeOperationSource](KnowledgeOperationSource) | Source of the sync job. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 234.0.0_
