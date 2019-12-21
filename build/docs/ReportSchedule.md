---
title: ReportSchedule
---
## ReportSchedule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **quartz_cron_expression** | **str** | Quartz Cron Expression | |
| **next_fire_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **description** | **str** |  | [optional] |
| **time_zone** | **str** |  | [optional] |
| **time_period** | **str** |  | [optional] |
| **interval** | **str** | Interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **report_format** | **str** |  | [optional] |
| **locale** | **str** |  | [optional] |
| **enabled** | **bool** |  | [optional] |
| **report_id** | **str** | Report ID | |
| **parameters** | **dict(str, object)** |  | [optional] |
| **last_run** | [**ReportRunEntry**](ReportRunEntry.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


