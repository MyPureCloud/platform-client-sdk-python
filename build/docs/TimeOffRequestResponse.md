# TimeOffRequestResponse

## TimeOffRequestResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | |
| **user** | [UserReference](UserReference) | The user associated with this time off request | |
| **is_full_day_request** | bool | Whether this is a full day request (false means partial day) | |
| **marked_as_read** | bool | Deprecated - Always returns true. | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category | |
| **paid** | bool | Whether this is a paid time off request | [optional] |
| **status** | str | The status of this time off request | |
| **substatus** | str | The substatus of this time off request | [optional] |
| **partial_day_start_date_times** | list[datetime] | A set of start date-times in ISO-8601 format for partial day requests. Will be not empty if isFullDayRequest &#x3D;&#x3D; false | |
| **full_day_management_unit_dates** | list[str] | A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit&#39;s configured time zone. Will be not empty if isFullDayRequest &#x3D;&#x3D; true | |
| **daily_duration_minutes** | int | The daily duration of this time off request in minutes | |
| **duration_minutes** | list[int] | Daily durations for each day of this time off request in minutes | |
| **payable_minutes** | list[int] | Payable minutes for each day of this time off request | |
| **full_day_earliest_start_offset_minutes** | list[int] | Earliest start offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | |
| **full_day_latest_end_offset_minutes** | list[int] | Latest end offset in minutes for each full-day request date. Values may be null when time-off estimation is disabled or no estimate is available | |
| **notes** | str | Notes about the time off request | |
| **submitted_by** | [UserReference](UserReference) | The user who submitted this time off request. The id may be &#39;System&#39; if it was an automated process | |
| **submitted_date** | datetime | The timestamp when this request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **reviewed_by** | [UserReference](UserReference) | The user who reviewed this time off request. The id may be &#39;System&#39; if it was an automated process | [optional] |
| **reviewed_date** | datetime | The timestamp when this request was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who last modified this TimeOffRequestResponse | [optional] |
| **modified_date** | datetime | The timestamp when this request was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **sync_version** | int | The sync version of this time off request for which the scheduled activity is associated | |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | The version metadata of the time off request | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 264.0.0_
