# ReportingExportJobResponse

## ReportingExportJobResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **run_id** | str | The unique run id of the export schedule execute | |
| **status** | str | The current status of the export request | |
| **time_zone** | str | The requested timezone of the exported data. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | |
| **export_format** | str | The requested format of the exported data | |
| **interval** | str | The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **download_url** | str | The url to download the request if it&#39;s status is completed | [optional] |
| **view_type** | str | The type of view export job to be created | |
| **export_error_messages_type** | str | The error message in case the export request failed | [optional] |
| **period** | str | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **filter** | [ViewFilter](ViewFilter) | Filters to apply to create the view | |
| **read** | bool | Indicates if the request has been marked as read | |
| **created_date_time** | datetime | The created date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **modified_date_time** | datetime | The last modified date/time of the request. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **locale** | str | The locale use for localization of the exported data, i.e. en-us, es-mx   | |
| **percentage_complete** | float | The percentage of the job that has completed processing | |
| **has_format_durations** | bool | Indicates if durations are formatted in hh:mm:ss format instead of ms | [optional] |
| **has_split_filters** | bool | Indicates if filters will be split in aggregate detail exports | [optional] |
| **exclude_empty_rows** | bool | Excludes empty rows from the exports | [optional] |
| **has_split_by_media** | bool | Indicates if media type will be split in aggregate detail exports | [optional] |
| **has_summary_row** | bool | Indicates if summary row needs to be present in exports | [optional] |
| **csv_delimiter** | str | The user supplied csv delimiter string value either of type &#39;comma&#39; or &#39;semicolon&#39; permitted for the export request | [optional] |
| **selected_columns** | [list[SelectedColumns]](SelectedColumns) | The list of ordered selected columns from the export view by the user | [optional] |
| **has_custom_participant_attributes** | bool | Indicates if custom participant attributes will be exported | [optional] |
| **recipient_emails** | list[str] | The list of email recipients for the exports | [optional] |
| **email_statuses** | dict(str, str) | The status of individual email addresses as a map | [optional] |
| **email_error_description** | str | The optional error message in case the export fail to email | [optional] |
| **include_duration_format_in_header** | bool | Indicates whether to include selected duration format to the column headers | [optional] |
| **duration_format** | str | Indicates the duration format for the exports | [optional] |
| **export_allowed_to_rerun** | bool | Indicates whether the export run is allowed to rerun | [optional] |
| **enabled** | bool |  | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
