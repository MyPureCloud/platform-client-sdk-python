# AgentPossibleWorkShiftsResponse

## AgentPossibleWorkShiftsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **week_start_date** | date | Start date of requested effective work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **pattern** | list[int] | Each element is the ID of an effective work plan for a specific week | [optional] |
| **weekly_possible_work_shifts** | [list[PossibleWorkShiftsForWeek]](PossibleWorkShiftsForWeek) | Each element is a weekly effective work plan that can be used for multiple weeks | [optional] |
| **scheduler_interval_length_minutes** | int | Number of minutes in each interval in the intervalScheduleProbabilities | [optional] |
| **time_zone** | str | The time zone of the business unit | [optional] |



_PureCloudPlatformClientV2 238.0.0_
