---
title: Condition
---
## Condition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | The type of the condition | [optional] |
| **inverted** | **bool** | Indicates whether to evaluate for the opposite of the stated condition; default is false | [optional] |
| **attribute_name** | **str** | An attribute name associated with the condition (applies only to certain rule conditions) | [optional] |
| **value** | **str** | A value associated with the condition | [optional] |
| **value_type** | **str** | Determines the type of the value associated with the condition | [optional] |
| **operator** | **str** | An operation type for condition evaluation | [optional] |
| **codes** | **list[str]** | List of wrap-up code identifiers (used only in conditions of type &#39;wrapupCondition&#39;) | [optional] |
{: class="table table-striped"}


