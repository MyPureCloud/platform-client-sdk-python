# BuCurrentAgentScheduleSearchResponse

## BuCurrentAgentScheduleSearchResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **agent_schedules** | [list[BuAgentScheduleSearchResponse]](BuAgentScheduleSearchResponse) | The requested agent schedules | [optional] |
| **business_unit_time_zone** | str | The time zone configured for the business unit to which this schedule applies | [optional] |
| **published_schedules** | [list[BuAgentSchedulePublishedScheduleReference]](BuAgentSchedulePublishedScheduleReference) | References to all published week schedules overlapping the start/end date query parameters | [optional] |
| **start_date** | datetime | The start date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **end_date** | datetime | The end date of the schedules. Only populated on notifications. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **updates** | [list[BuAgentScheduleUpdate]](BuAgentScheduleUpdate) | The list of updates for the schedule. Only used in notifications | [optional] |



_PureCloudPlatformClientV2 232.0.0_
