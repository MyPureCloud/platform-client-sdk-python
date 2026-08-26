# AdminAgentScheduleBidBiddingPreference

## AdminAgentScheduleBidBiddingPreference

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **agent** | [UserReference](UserReference) | The agent to whom this schedule bid preference applies | |
| **submitted** | bool | Indicates whether the preference has been submitted | |
| **assigned_schedule_set_id** | str | The schedule set assigned to the agent by the bid process. This will be set after bid is processed | [optional] |
| **overridden_schedule_set_id** | str | The schedule set that overrides the assigned schedule set for the agent | [optional] |
| **override_reason** | str | The reason the assigned schedule set has been overridden. This must be null if no override schedule is set | [optional] |
| **agent_schedule_bid_preference_priorities** | [list[AgentScheduleBiddingPreferencePriority]](AgentScheduleBiddingPreferencePriority) | The agent schedule set preferences | |
| **end_date** | date | The end date of this scheduling set preference relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |



_PureCloudPlatformClientV2 265.0.0_
