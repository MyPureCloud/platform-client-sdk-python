# DialerRulesetConfigChangeDataActionConditionPredicate

## DialerRulesetConfigChangeDataActionConditionPredicate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **output_field** | str | The name of an output field from the data action&#39;s output to use for this condition | [optional] |
| **output_operator** | str | The operation with which to evaluate this condition | [optional] |
| **comparison_value** | str | The value to compare against for this condition | [optional] |
| **output_field_missing_resolution** | bool | The result of this predicate if the requested output field is missing from the data action&#39;s result | [optional] |
| **inverted** | bool | If true, inverts the result of evaluating this Predicate. Default is false. | [optional] |
| **additional_properties** | dict(str, object) |  | [optional] |



_PureCloudPlatformClientV2 219.0.0_
