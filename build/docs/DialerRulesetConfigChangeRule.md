---
title: DialerRulesetConfigChangeRule
---
## DialerRulesetConfigChangeRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **conditions** | [**list[DialerRulesetConfigChangeCondition]**](DialerRulesetConfigChangeCondition.html) | The list of rule conditions; all must evaluate to true to trigger the rule actions | [optional] |
| **additional_properties** | **dict(str, object)** |  | [optional] |
| **id** | **str** | The identifier of the rule | [optional] |
| **name** | **str** | The name of the rule | [optional] |
| **order** | **int** | The ranked order of the rule; rules are processed from lowest number to highest | [optional] |
| **category** | **str** | The category of the rule | [optional] |
| **actions** | [**list[DialerRulesetConfigChangeAction]**](DialerRulesetConfigChangeAction.html) | The list of rule actions to be taken if the conditions are true | [optional] |
{: class="table table-striped"}


