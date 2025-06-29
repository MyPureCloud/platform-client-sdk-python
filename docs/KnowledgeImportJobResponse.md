# KnowledgeImportJobResponse

## KnowledgeImportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the import job | [optional] |
| **download_url** | str | The URL of the location at which the caller can download the imported file. | [optional] |
| **failed_entities_url** | str | The URL of the location at which the caller can download the entities in json format that failed during the import. | [optional] |
| **upload_key** | str | Upload key | |
| **file_type** | str | File type of the document | |
| **settings** | [KnowledgeImportJobSettings](KnowledgeImportJobSettings) | Additional optional settings | [optional] |
| **status** | str | Status of the import job | [optional] |
| **report** | [KnowledgeImportJobReport](KnowledgeImportJobReport) | Report of the import job | [optional] |
| **knowledge_base** | [KnowledgeBase](KnowledgeBase) | Knowledge base which document import does belong to | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the operation | [optional] |
| **date_created** | datetime | Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **skip_confirmation_step** | bool | If enabled pre-validation step will be skipped. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 232.0.0_
