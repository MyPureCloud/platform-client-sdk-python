# WfmAgent

## WfmAgent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **user** | [UserReference](UserReference) | The user associated with this data | [optional] |
| **work_plan** | [WorkPlanReference](WorkPlanReference) | The work plan associated with this agent, if applicable | [optional] |
| **work_plan_rotation** | [WorkPlanRotationReference](WorkPlanRotationReference) | The work plan rotation associated with this agent, if applicable | [optional] |
| **accept_direct_shift_trades** | bool | Whether the agent accepts direct shift trade requests | [optional] |
| **work_plan_overrides** | [list[WorkPlanOverride]](WorkPlanOverride) | The work plan overrides associated with this agent. Populate with expand&#x3D;workPlanOverrides | [optional] |
| **queues** | [list[QueueReference]](QueueReference) | List of queues to which this agent is capable of handling | [optional] |
| **languages** | [list[LanguageReference]](LanguageReference) | The list of languages this agent is capable of handling | [optional] |
| **skills** | [list[RoutingSkillReference]](RoutingSkillReference) | The list of skills this agent is capable of handling | [optional] |
| **schedulable** | bool | Whether the agent can be included in schedule generation | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Metadata for this agent | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.1.0_
