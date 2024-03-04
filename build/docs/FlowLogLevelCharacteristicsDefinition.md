---
title: FlowLogLevelCharacteristicsDefinition
---
## FlowLogLevelCharacteristicsDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **minimum_level** | **str** | The minimum level required for this characteristic to be enabled. | [optional] |
| **depends_on** | [**FlowCharacteristics**](FlowCharacteristics.html) | If set, this is the id of the characteristic that this one depends on and it must be enabled for this to be enabled. | [optional] |
{: class="table table-striped"}


