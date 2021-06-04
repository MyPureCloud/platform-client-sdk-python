---
title: QualityAuditQueryExecutionStatusResponse
---
## QualityAuditQueryExecutionStatusResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Id of the audit query execution request. | [optional] |
| **state** | **str** | Status of the audit query execution request. | [optional] |
| **date_start** | **datetime** | Start date and time of the audit query execution. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **interval** | **str** | Interval for the audit query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **filters** | [**list[QualityAuditQueryFilter]**](QualityAuditQueryFilter.html) | Filters for the audit query. | [optional] |
| **sort** | [**list[AuditQuerySort]**](AuditQuerySort.html) | Sort parameter for the audit query. | [optional] |
{: class="table table-striped"}


