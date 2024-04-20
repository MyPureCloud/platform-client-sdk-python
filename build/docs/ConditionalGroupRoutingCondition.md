---
title: ConditionalGroupRoutingCondition
---
## ConditionalGroupRoutingCondition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue** | [**DomainEntityRef**](DomainEntityRef.html) | The queue being evaluated for this rule.  If null, the current queue will be used. | [optional] |
| **metric** | **str** | The queue metric being evaluated | [optional] |
| **operator** | **str** | The operator that compares the actual value against the condition value | [optional] |
| **value** | **float** | The limit value, beyond which a rule evaluates as true | [optional] |
{: class="table table-striped"}


