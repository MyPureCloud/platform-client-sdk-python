# AdminAgentWorkPlanBiddingPreference

## AdminAgentWorkPlanBiddingPreference

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **agent** | [UserReference](UserReference) | The agent to whom this work plan bidding preference applies | |
| **submitted** | bool | Whether the preference is submitted | |
| **assigned_work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan assigned to the agent by the bid process | [optional] |
| **overridden_work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan that overrides the assigned work plan for the agent | [optional] |
| **override_reason** | str | The reason why the assigned work plan has been overridden. This must be null without an override work plan | [optional] |
| **priorities** | list[int] | The agent priorities for the list of work plans. The index of the priorities should match with the list of work plans that belong to bid group. It contains null if priority is not set for the work plan | [optional] |



_PureCloudPlatformClientV2 244.0.0_
