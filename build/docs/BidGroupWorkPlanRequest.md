# BidGroupWorkPlanRequest

## BidGroupWorkPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **work_plan_id** | str | The ID of the work plan used in the bid group | |
| **override_agent_count** | int | The modified agent count for this work plan | [optional] |
| **suggested_agent_count** | int | The number of agents needed for this work plan to produce the optimal schedule | [optional] |
| **agent_count_range** | [AgentCountRange](AgentCountRange) | The range of agent slot count per work plan. The suggested slot count must be in agent count range | [optional] |



_PureCloudPlatformClientV2 217.0.0_
