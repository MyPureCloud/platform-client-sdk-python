---
title: Flow
---
## Flow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The flow name | |
| **description** | **str** |  | [optional] |
| **division** | [**AuthzDivision**](AuthzDivision.html) |  | [optional] |
| **type** | **str** |  | [optional] |
| **locked_user** | [**User**](User.html) |  | [optional] |
| **active** | **bool** |  | [optional] |
| **system** | **bool** |  | [optional] |
| **deleted** | **bool** |  | [optional] |
| **published_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **saved_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **input_schema** | **object** | json schema describing the inputs for the flow | [optional] |
| **output_schema** | **object** | json schema describing the outputs for the flow | [optional] |
| **checked_in_version** | [**FlowVersion**](FlowVersion.html) |  | [optional] |
| **published_by** | [**User**](User.html) |  | [optional] |
| **current_operation** | [**Operation**](Operation.html) |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


