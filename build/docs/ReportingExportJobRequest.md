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
| **period** | **str** | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **view_type** | **str** | The type of view export job to be created | |
| **filter** | [**ViewFilter**](ViewFilter.html) | Filters to apply to create the view | |
| **read** | **bool** | Indicates if the request has been marked as read | [optional] |
| **locale** | **str** | The locale use for localization of the exported data, i.e. en-us, es-mx   | |
| **has_format_durations** | **bool** | Indicates if durations are formatted in hh:mm:ss format instead of ms | [optional] |
| **has_split_filters** | **bool** | Indicates if filters will be split in aggregate detail exports | [optional] |
{: class="table table-striped"}


