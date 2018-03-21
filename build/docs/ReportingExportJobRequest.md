---
title: ReportingExportJobRequest
---
## ReportingExportJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The user supplied name of the export request | |
| **time_zone** | [**TimeZone**](TimeZone.html) | The requested timezone of the exported data | |
| **export_format** | **str** | The requested format of the exported data | |
| **interval** | **str** | The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **data_columns** | [**list[DataColumn]**](DataColumn.html) | The data columns included in the export | |
| **period** | **str** | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **view_type** | **str** | The type of view export job to be created | |
| **filter** | [**ViewFilter**](ViewFilter.html) | Filters to apply to create the view | |
| **read** | **bool** | Indicates if the request has been marked as read | [optional] |
{: class="table table-striped"}


