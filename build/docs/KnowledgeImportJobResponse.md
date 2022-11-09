---
title: KnowledgeImportJobResponse
---
## KnowledgeImportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Id of the import job | [optional] |
| **upload_key** | **str** | Upload key | |
| **file_type** | **str** | File type of the document | |
| **settings** | [**KnowledgeImportJobSettings**](KnowledgeImportJobSettings.html) | Additional optional settings | [optional] |
| **status** | **str** | Status of the import job | [optional] |
| **report** | [**KnowledgeImportJobReport**](KnowledgeImportJobReport.html) | Report of the import job | [optional] |
| **knowledge_base** | [**KnowledgeBase**](KnowledgeBase.html) | Knowledge base which document import does belong to | [optional] |
| **date_created** | **datetime** | Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


