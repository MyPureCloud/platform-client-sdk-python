---
title: QMAuditQueryRequest
---
## QMAuditQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Date and time range of data to query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **filters** | [**list[QualityAuditQueryFilter]**](QualityAuditQueryFilter.html) | List of filters for the query. | |
| **sort** | [**list[AuditQuerySort]**](AuditQuerySort.html) | Sort parameter for the query. | [optional] |
{: class="table table-striped"}


