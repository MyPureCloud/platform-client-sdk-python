---
title: ConditionalGroupRoutingRule
---
## ConditionalGroupRoutingRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [**DomainEntityRef**](DomainEntityRef.html) | The queue being evaluated for this rule.  For rule 1, this is always the current queue. | [optional] |
| **metric** | **str** | The queue metric being evaluated | [optional] |
| **operator** | **str** | The operator that compares the actual value against the condition value | [optional] |
| **condition_value** | **float** | The limit value, beyond which a rule evaluates as true | [optional] |
| **groups** | [**list[MemberGroup]**](MemberGroup.html) | The group(s) to activate if the rule evaluates as true | [optional] |
| **wait_seconds** | **int** | The number of seconds to wait in this rule, if it evaluates as true, before evaluating the next rule | [optional] |
{: class="table table-striped"}


