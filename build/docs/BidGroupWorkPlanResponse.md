# BidGroupWorkPlanResponse

## BidGroupWorkPlanResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **management_unit** | [ManagementUnitReference](ManagementUnitReference) | The management unit to which this work plan belongs.  Nullable in some routes | [optional] |
| **override_agent_count** | int | The modified agent count for this work plan | [optional] |
| **suggested_agent_count** | int | The number of agents needed for this work plan to produce the optimal schedule | [optional] |
| **agent_count_range** | [AgentCountRange](AgentCountRange) | The range of agent slot count per work plan. The suggested slot count must be in agent count range | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_
