# WfmAgentHistoricalAdherenceResult

## WfmAgentHistoricalAdherenceResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **user** | [UserReference](UserReference) | The user who submitted the agent historical adherence query | [optional] |
| **start_date** | datetime | Beginning of the date range that was queried, in ISO-8601 format | |
| **end_date** | datetime | End of the date range that was queried, in ISO-8601 format. If it was not set, end date will be set to the queried time | |
| **calculations_completed_date** | datetime | Completed date of calculations that was queried, in ISO-8601 format. | |
| **target_adherence_percentage** | float | Target percentage for this user, in the scale of 0 - 100 | |
| **adherence_percentage** | float | Adherence percentage for this user, in the scale of 0 - 100 | [optional] |
| **conformance_percentage** | float | Conformance percentage for this user, in the scale of 0 - 100. Conformance percentage can be greater than 100 when the actual on queue time is greater than the scheduled on queue time for the same period. | [optional] |
| **impact** | str | The impact of the current adherence state for this user | |
| **exception_info** | [list[HistoricalAdherenceExceptionInfo]](HistoricalAdherenceExceptionInfo) | List of adherence exceptions for this user | [optional] |
| **day_metrics** | [list[AgentAdherenceDayMetrics]](AgentAdherenceDayMetrics) | Adherence and conformance metrics for days in query range | |
| **actuals** | [list[HistoricalAdherenceActuals]](HistoricalAdherenceActuals) | List of actual activity with offset for this user | [optional] |
| **scheduled_activities** | [list[AgentAdherenceScheduledActivity]](AgentAdherenceScheduledActivity) | List of scheduled activities for this user | [optional] |
| **secondary_presence_lookup_items** | [list[SecondaryPresenceLookupItem]](SecondaryPresenceLookupItem) | List of secondary presence lookup ID to corresponding secondary presence ID item | |



_PureCloudPlatformClientV2 246.1.0_
