# ReportingExportJobRequest

## ReportingExportJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The user supplied name of the export request | |
| **time_zone** | str | The requested timezone of the exported data. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | |
| **export_format** | str | The requested format of the exported data | |
| **interval** | str | The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **period** | str | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **view_type** | str | The type of view export job to be created | |
| **filter** | [ViewFilter](ViewFilter) | Filters to apply to create the view | |
| **read** | bool | Indicates if the request has been marked as read | [optional] |
| **locale** | str | The locale used for localization of the exported data, i.e. en-US, es | |
| **has_format_durations** | bool | Indicates if durations are formatted in hh:mm:ss format instead of ms | [optional] |
| **has_split_filters** | bool | Indicates if filters will be split in aggregate detail exports | [optional] |
| **exclude_empty_rows** | bool | Excludes empty rows from the exports | [optional] |
| **has_split_by_media** | bool | Indicates if media type will be split in aggregate detail exports | [optional] |
| **has_summary_row** | bool | Indicates if summary row needs to be present in exports | [optional] |
| **csv_delimiter** | str | The user supplied csv delimiter string value either of type &#39;comma&#39; or &#39;semicolon&#39; permitted for the export request | [optional] |
| **selected_columns** | [list[SelectedColumns]](SelectedColumns) | The list of ordered selected columns from the export view by the user | [optional] |
| **has_custom_participant_attributes** | bool | Indicates if custom participant attributes will be exported | [optional] |
| **recipient_emails** | list[str] | The list of email recipients for the exports | [optional] |
| **include_duration_format_in_header** | bool | Indicates whether to include selected duration format to the column headers | [optional] |
| **duration_format** | str | Indicates the duration format for the exports | [optional] |
| **chart_columns** | [list[ChartColumn]](ChartColumn) | The list of columns for which chart is going to be displayed in export | [optional] |



_PureCloudPlatformClientV2 230.0.0_
