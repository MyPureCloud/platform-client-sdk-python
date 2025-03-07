# KnowledgeImport

## KnowledgeImport

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the import operation | [optional] |
| **name** | str | Name of the import operation | [optional] |
| **upload_key** | str | Upload key | |
| **file_type** | str | file type of the document | |
| **ignore_headers** | bool | Ignore headers for the specified file | [optional] |
| **status** | str | Status of the operation | [optional] |
| **report** | [ImportReport](ImportReport) | Report of the import operation | [optional] |
| **knowledge_base** | [KnowledgeBase](KnowledgeBase) | Knowledge base which document import does belong to | [optional] |
| **language_code** | str | Language code | [optional] |
| **date_created** | datetime | Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_
