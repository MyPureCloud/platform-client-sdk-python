# SkillExpressionValidationResult

## SkillExpressionValidationResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **valid** | bool | Whether the expression is valid | [optional] |
| **expression** | str | Normalized SpEL expression (null if validation failed) | [optional] |
| **skills** | [list[SkillReference]](SkillReference) | List of skill references extracted from the expression (empty if no skills found and/or invalid expression) | [optional] |
| **errors** | [list[SkillExpressionValidationError]](SkillExpressionValidationError) | List of validation errors (empty if valid) | [optional] |
| **hint** | str | Optional hint message (e.g., if expression is non-optimal or system is near capacity) | [optional] |



_PureCloudPlatformClientV2 263.0.0_
