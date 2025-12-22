# AgentMuScheduleItem

## AgentMuScheduleItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **agent** | [UserReference](UserReference) | The agent to whom this schedule applies. Note: selfUri will not be populated if retrieving result via downloadUrl | |
| **shifts** | [list[AgentMuScheduleShift]](AgentMuScheduleShift) | The shift definitions for this agent schedule | |
| **full_day_time_off_marker_dates** | list[date] | The full day time off marker dates which apply to this agent schedule, interpreted in the time zone of the relevant business unit | |



_PureCloudPlatformClientV2 246.1.0_
