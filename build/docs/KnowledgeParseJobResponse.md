# KnowledgeParseJobResponse

## KnowledgeParseJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Id of the parse job | [optional] |
| **download_url** | str | The URL of the location at which the caller can download the original html file. | [optional] |
| **hints** | list[str] | Hinted titles for the parser. | [optional] |
| **status** | str | Status of the parse job | [optional] |
| **parse_results** | [list[KnowledgeParseRecord]](KnowledgeParseRecord) | Results of the parse | [optional] |
| **import_result** | [KnowledgeParseImportResult](KnowledgeParseImportResult) | Result of the import phase | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the operation | [optional] |
| **date_created** | datetime | Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_
