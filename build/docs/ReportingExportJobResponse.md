---
title: ReportingExportJobResponse
---
## ReportingExportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **status** | **str** | The current status of the export request | |
| **time_zone** | [**TimeZone**](TimeZone.html) | The requested timezone of the exported data | |
| **export_format** | **str** | The requested format of the exported data | |
| **interval** | **str** | The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **download_url** | **str** | The url to download the request if it&#39;s status is completed | [optional] |
| **view_type** | **str** | The type of view export job to be created | |
| **export_error_messages_type** | **str** | The error message in case the export request failed | [optional] |
| **period** | **str** | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | [optional] |
| **filter** | [**ViewFilter**](ViewFilter.html) | Filters to apply to create the view | |
| **read** | **bool** | Indicates if the request has been marked as read | |
| **created_date_time** | **datetime** | The created date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **modified_date_time** | **datetime** | The last modified date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | |
| **locale** | **str** | The locale use for localization of the exported data, i.e. en-us, es-mx   | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


