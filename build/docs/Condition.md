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
| **value** | **str** | A value associated with the condition. This could be text, a number, or a relative time. A value for relative time should follow the format PxxDTyyHzzM, where xx, yy, and zz specify the days, hours and minutes. For example, a value of P01DT08H30M corresponds to 1 day, 8 hours, and 30 minutes from now. To specify a time in the past, include a negative sign before each numeric value. For example, a value of P-01DT-08H-30M corresponds to 1 day, 8 hours, and 30 minutes in the past. You can also do things like P01DT00H-30M, which would correspond to 23 hours and 30 minutes from now (1 day - 30 minutes). | [optional] |
| **value_type** | **str** | Determines the type of the value associated with the condition | [optional] |
| **operator** | **str** | An operation type for condition evaluation | [optional] |
| **codes** | **list[str]** | List of wrap-up code identifiers (used only in conditions of type &#39;wrapupCondition&#39;) | [optional] |
| **property_type** | **str** | Determines the type of the property associated with the condition | [optional] |
| **pcProperty** | **str** | A value associated with the property type of this condition | [optional] |
{: class="table table-striped"}


