# WorkPlanRotationResponse

## WorkPlanRotationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **enabled** | bool | Whether the work plan rotation is enabled for scheduling | [optional] |
| **date_range** | [DateRangeWithOptionalEnd](DateRangeWithOptionalEnd) | The date range to which this work plan rotation applies | [optional] |
| **pattern** | [WorkPlanPatternResponse](WorkPlanPatternResponse) | Pattern with ordered list of work plans that rotate on a weekly basis | [optional] |
| **agent_count** | int | Number of agents in this work plan rotation | [optional] |
| **agents** | [list[WorkPlanRotationAgentResponse]](WorkPlanRotationAgentResponse) | Agents in this work plan rotation. Populate with expand&#x3D;agents for GET WorkPlanRotationsList (defaults to empty list) | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this work plan rotation | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.0.0_
