# BuAgentScheduleActivity

## BuAgentScheduleActivity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start date/time of this activity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **length_minutes** | int | The length of this activity in minutes | |
| **description** | str | The description of this activity | |
| **activity_code_id** | str | The ID of the activity code associated with this activity | |
| **paid** | bool | Whether this activity is paid | [optional] |
| **payable_minutes** | int | Payable minutes for this activity | [optional] |
| **time_off_request_id** | str | The ID of the time off request associated with this activity, if applicable | [optional] |
| **time_off_request_sync_version** | int | The sync version of the partial day time off request for which the scheduled activity is associated, if applicable | [optional] |
| **external_activity_id** | str | The ID of the external activity associated with this activity, if applicable | [optional] |
| **external_activity_type** | str | The type of the external activity associated with this activity, if applicable | [optional] |



_PureCloudPlatformClientV2 243.0.0_
