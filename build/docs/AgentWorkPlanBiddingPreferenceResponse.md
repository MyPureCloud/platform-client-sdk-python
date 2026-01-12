# AgentWorkPlanBiddingPreferenceResponse

## AgentWorkPlanBiddingPreferenceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **submitted** | bool | Whether the preference is submitted | |
| **assigned_work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan assigned to the agent by the bid process | [optional] |
| **overridden_work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan that overrides the assigned work plan for the agent | [optional] |
| **override_reason** | str | The reason why the assigned work plan has been overridden. This must be null without an override work plan | [optional] |
| **agent_work_plan_bid_preferences** | [list[AgentWorkPlanBiddingPreference]](AgentWorkPlanBiddingPreference) | The list of work plan bidding preferences | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_
