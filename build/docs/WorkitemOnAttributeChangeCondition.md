# WorkitemOnAttributeChangeCondition

## WorkitemOnAttributeChangeCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **attribute** | str | The name of the workitem attribute whose change will be evaluated as part of the rule. | |
| **new_value** | str | The value the attribute&#39;s new value is compared against. Compared for equality unless an operator is supplied. Null matches the attribute having been cleared, on clearable attributes. | [optional] |
| **old_value** | str | The value the attribute is transitioning from. Not permitted for the priority attribute. Omitted or null matches any previous value. | [optional] |
| **operator** | str | How the attribute&#39;s new value is compared against newValue. Required for the priority attribute; not permitted otherwise. | [optional] |



_PureCloudPlatformClientV2 270.0.0_
