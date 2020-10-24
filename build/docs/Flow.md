---
title: Flow
---
## Flow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The flow identifier | [optional] |
| **name** | **str** | The flow name | |
| **division** | [**WritableDivision**](WritableDivision.html) | The division to which this entity belongs. | [optional] |
| **description** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **locked_user** | [**User**](User.html) | User that has the flow locked. | [optional] |
| **locked_client** | [**DomainEntityRef**](DomainEntityRef.html) | OAuth client that has the flow locked. | [optional] |
| **active** | **bool** |  | [optional] |
| **system** | **bool** |  | [optional] |
| **deleted** | **bool** |  | [optional] |
| **published_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **saved_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **input_schema** | **object** | json schema describing the inputs for the flow | [optional] |
| **output_schema** | **object** | json schema describing the outputs for the flow | [optional] |
| **checked_in_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **debug_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **published_by** | [**User**](User.html) |  | [optional] |
| **current_operation** | [**Operation**](Operation.html) |  | [optional] |
| **nlu_info** | [**NluInfo**](NluInfo.html) | Information about the NLU domain version for the flow | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


