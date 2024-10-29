# UserListScheduleRequestBody

## UserListScheduleRequestBody

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user_ids** | list[str] | The user ids for which to fetch schedules | |
| **start_date** | datetime | Beginning of the range of schedules to fetch, in ISO-8601 format | |
| **end_date** | datetime | End of the range of schedules to fetch, in ISO-8601 format | |
| **load_full_weeks** | bool | Whether to load the full week&#39;s schedule (for the requested users) of any week overlapping the start/end date query parameters, defaults to false | [optional] |



_PureCloudPlatformClientV2 215.0.0_
