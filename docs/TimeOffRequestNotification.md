# TimeOffRequestNotification

## TimeOffRequestNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **time_off_request_id** | str | The ID of this time off request | [optional] |
| **user** | [UserReference](UserReference) | The user associated with this time off request | [optional] |
| **is_full_day_request** | bool | Whether this is a full day request (false means partial day) | [optional] |
| **status** | str | The status of this time off request | [optional] |
| **partial_day_start_date_times** | list[datetime] | A set of start date-times in ISO-8601 format for partial day requests.  Will be not empty if isFullDayRequest &#x3D;&#x3D; false | [optional] |
| **full_day_management_unit_dates** | list[str] | A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit&#39;s configured time zone.  Will be not empty if isFullDayRequest &#x3D;&#x3D; true | [optional] |



_PureCloudPlatformClientV2 221.0.0_
