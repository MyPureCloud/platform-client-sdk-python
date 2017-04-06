---
title: DomainEdgeSoftwareUpdateDto
---
## DomainEdgeSoftwareUpdateDto

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **version** | [**DomainEdgeSoftwareVersionDto**](DomainEdgeSoftwareVersionDto.html) | Version | |
| **max_download_rate** | **int** |  | [optional] |
| **download_start_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **execute_start_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **execute_stop_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **execute_on_idle** | **bool** |  | [optional] |
| **status** | **str** |  | [optional] |
| **edge_uri** | **str** |  | [optional] |
| **call_draining_wait_time_seconds** | **int** |  | [optional] |
| **current** | **bool** |  | [optional] |
{: class="table table-striped"}


