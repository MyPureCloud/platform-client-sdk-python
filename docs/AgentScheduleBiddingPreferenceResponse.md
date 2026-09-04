# AgentScheduleBiddingPreferenceResponse

## AgentScheduleBiddingPreferenceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **submitted** | bool | Whether the preference is submitted | |
| **assigned_schedule_set_id** | str | The schedule set assigned to the agent by the bid process. Will be set after bid is processed | [optional] |
| **overridden_schedule_set_id** | str | The schedule set that overrides the assigned schedule set for the agent | [optional] |
| **override_reason** | str | The reason why the assigned schedule set has been overridden. This must be null without an override schedule set | [optional] |
| **agent_schedule_bid_preferences** | [list[AgentScheduleBiddingPreferencePriority]](AgentScheduleBiddingPreferencePriority) | The schedule bidding preferences | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 266.0.0_
