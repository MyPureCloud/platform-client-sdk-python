---
title: AuditQueryRequest
---
## AuditQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Date and time range of data to query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ssZ/YYYY-MM-DDThh:mm:ssZ | |
| **service_name** | **str** | Name of the service to query audits for. | |
| **filters** | [**list[AuditQueryFilter]**](AuditQueryFilter.html) | Additional filters for the query. | [optional] |
| **sort** | [**list[AuditQuerySort]**](AuditQuerySort.html) | Sort parameter for the query. | [optional] |
{: class="table table-striped"}


