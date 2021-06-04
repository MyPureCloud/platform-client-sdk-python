---
title: QualityAuditQueryExecutionResultsResponse
---
## QualityAuditQueryExecutionResultsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Id of the audit query execution request. | [optional] |
| **page_size** | **int** | Number of results in a page. | [optional] |
| **cursor** | **str** | Optional cursor to indicate where to resume the results. | [optional] |
| **entities** | [**list[QualityAuditLogMessage]**](QualityAuditLogMessage.html) | List of audit messages. | [optional] |
{: class="table table-striped"}


