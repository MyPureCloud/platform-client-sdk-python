---
title: Condition
---
## Condition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of the condition. | [optional] |
| **inverted** | **bool** | If true, inverts the result of evaluating this Condition. Default is false. | [optional] |
| **attribute_name** | **str** | An attribute name associated with this Condition. Required for a contactAttributeCondition. | [optional] |
| **value** | **str** | A value associated with this Condition. This could be text, a number, or a relative time. Not used for a DataActionCondition. | [optional] |
| **value_type** | **str** | The type of the value associated with this Condition. Not used for a DataActionCondition. | [optional] |
| **operator** | **str** | An operation with which to evaluate the Condition. Not used for a DataActionCondition. | [optional] |
| **codes** | **list[str]** | List of wrap-up code identifiers. Required for a wrapupCondition. | [optional] |
| **pcProperty** | **str** | A value associated with the property type of this Condition. Required for a contactPropertyCondition. | [optional] |
| **property_type** | **str** | The type of the property associated with this Condition. Required for a contactPropertyCondition. | [optional] |
{: class="table table-striped"}


