---
title: KnowledgeExportJobResponse
---
## KnowledgeExportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Id of the export job. | [optional] |
| **download_url** | **str** | The URL of the location at which the caller can download the export file, when available. | [optional] |
| **count_document_processed** | **int** | The current count of the number of records processed. | [optional] |
| **export_filter** | [**KnowledgeExportJobFilter**](KnowledgeExportJobFilter.html) | Filters to narrow down what to export. | [optional] |
| **status** | **str** | The status of the export job. | [optional] |
| **knowledge_base** | [**KnowledgeBase**](KnowledgeBase.html) | Knowledge base which document export belongs to. | [optional] |
| **date_created** | **datetime** | The timestamp of when the export began. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | The timestamp of when the export stopped. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **error_information** | [**ErrorBody**](ErrorBody.html) | Any error information, or null of the processing is not in failed state. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


