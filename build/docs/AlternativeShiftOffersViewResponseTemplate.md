# AlternativeShiftOffersViewResponseTemplate

## AlternativeShiftOffersViewResponseTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **job_id** | str | The unique identifier of the async list job that created this file | |
| **business_unit_id** | str | The unique identifier of the business unit to which the user (agent) belongs at the time the offer is created | |
| **agent_id** | str | The unique identifier of the agent for whom the offer was made | |
| **management_unit_id** | str | The unique identifier of the management unit to which the user (agent) belongs at the time the offer is created | |
| **schedule** | [AlternativeShiftScheduleLookup](AlternativeShiftScheduleLookup) | The existing schedule information associated with the offer | |
| **offer_week_date** | date | The first date of the week for the schedule we are querying in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **shifts** | [list[AlternativeShiftAgentScheduledShift]](AlternativeShiftAgentScheduledShift) | The shifts the agent is scheduled for at the time the offer is created | |
| **alternative_days** | [list[AlternativeShiftAgentScheduledShift]](AlternativeShiftAgentScheduledShift) | The offered alternative shift days in this week at the time the offer is created | |



_PureCloudPlatformClientV2 217.0.0_
