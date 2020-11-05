---
title: WorkPlanRotationResponse
---
## WorkPlanRotationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **enabled** | **bool** | Whether the work plan rotation is enabled for scheduling | [optional] |
| **date_range** | [**DateRangeWithOptionalEnd**](DateRangeWithOptionalEnd.html) | The date range to which this work plan rotation applies | [optional] |
| **pattern** | [**WorkPlanPatternResponse**](WorkPlanPatternResponse.html) | Pattern with ordered list of work plans that rotate on a weekly basis | [optional] |
| **agent_count** | **int** | Number of agents in this work plan rotation | [optional] |
| **agents** | [**list[WorkPlanRotationAgentResponse]**](WorkPlanRotationAgentResponse.html) | Agents in this work plan rotation. Populate with expand=agents for GET WorkPlanRotationsList (defaults to empty list) | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for this work plan rotation | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


