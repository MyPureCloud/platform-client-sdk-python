---
title: DialerRule
---
## DialerRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The identifier of the rule | [optional] |
| **name** | **str** | The name of the rule | |
| **order** | **int** | The ranked order of the rule; rules are processed from lowest number to highest | [optional] |
| **category** | **str** | The category of the rule | |
| **conditions** | [**list[Condition]**](Condition.html) | The list of rule conditions; all must evaluate to true to trigger the rule actions | |
| **actions** | [**list[DialerAction]**](DialerAction.html) | The list of rule actions to be taken if the conditions are true | [optional] |
{: class="table table-striped"}


