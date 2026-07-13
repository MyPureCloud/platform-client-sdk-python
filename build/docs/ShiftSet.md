# ShiftSet

## ShiftSet

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The ID of the shift set | |
| **name** | str | The name given for the shift set | |
| **effective_work_plan** | [ShiftSetEffectiveWorkPlan](ShiftSetEffectiveWorkPlan) | The work plan or work plan rotation used for generating the shift set | |
| **shifts** | [list[ScheduleBidScheduledShift]](ScheduleBidScheduledShift) | The scheduled shifts | |
| **suggested_agent_count** | int | The suggested agent count | |
| **override_agent_count** | int | The override agent count. If it is null, it falls back to using the suggestedAgentCount | [optional] |



_PureCloudPlatformClientV2 262.0.0_
