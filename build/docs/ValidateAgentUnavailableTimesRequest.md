# ValidateAgentUnavailableTimesRequest

## ValidateAgentUnavailableTimesRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **validation_week_date** | date | The ID of the week to validate. Must correspond to the start day of week of the business unit to which the agent belongs in the format YYYY-MM-dd. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **unavailable_times** | [list[UpdateUnavailableTime]](UpdateUnavailableTime) | Proposed changes to agent&#39;s unavailable time spans to be validated | |



_PureCloudPlatformClientV2 248.0.0_
