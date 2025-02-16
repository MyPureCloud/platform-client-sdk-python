# BuFullDayTimeOffMarker

## BuFullDayTimeOffMarker

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **business_unit_date** | date | The date of the time off marker, interpreted in the business unit&#39;s time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **length_minutes** | int | The length of the time off marker in minutes | [optional] |
| **description** | str | The description of the time off marker | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the time off marker | [optional] |
| **paid** | bool | Whether the time off marker is paid | [optional] |
| **payable_minutes** | int | Payable minutes for the time off marker | [optional] |
| **time_off_request_id** | str | The ID of the time off request | [optional] |
| **time_off_request_sync_version** | int | The sync version of the full day time off request for which the scheduled activity is associated | [optional] |
| **delete** | bool | Set to &#39;true&#39; to delete this time off marker. Will always be null on responses, only has an effect on schedule update | [optional] |



_PureCloudPlatformClientV2 222.0.0_
