# ConditionalGroupRoutingRule

## ConditionalGroupRoutingRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [DomainEntityRef](DomainEntityRef) | The queue being evaluated for this rule.  If null, the current queue will be used. | [optional] |
| **metric** | str | The queue metric being evaluated | [optional] |
| **operator** | str | The operator that compares the actual value against the condition value | [optional] |
| **condition_value** | float | The limit value, beyond which a rule evaluates as true | [optional] |
| **groups** | [list[MemberGroup]](MemberGroup) | The group(s) to activate if the rule evaluates as true | [optional] |
| **wait_seconds** | int | The number of seconds to wait in this rule, if it evaluates as true, before evaluating the next rule.  For the final rule, this is ignored, so need not be specified. | [optional] |



_PureCloudPlatformClientV2 212.0.0_
