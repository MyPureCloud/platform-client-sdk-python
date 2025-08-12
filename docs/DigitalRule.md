# DigitalRule

## DigitalRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The identifier of the rule. | [optional] |
| **name** | str | The name of the rule. | |
| **order** | int | The ranked order of the rule. Rules are processed from lowest number to highest. | |
| **category** | str | The category of the rule. | |
| **conditions** | [list[DigitalCondition]](DigitalCondition) | A list of conditions to evaluate. All of the Conditions must evaluate to true to trigger the actions. | |
| **actions** | [list[DigitalAction]](DigitalAction) | The list of actions to be taken if all conditions are true. | |



_PureCloudPlatformClientV2 235.0.0_
