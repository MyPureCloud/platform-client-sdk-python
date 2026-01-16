# DialerRule

## DialerRule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The identifier of the rule. | [optional] |
| **name** | str | The name of the rule. | |
| **order** | int | The ranked order of the rule. Rules are processed from lowest number to highest. | [optional] |
| **category** | str | The category of the rule. | |
| **conditions** | [list[Condition]](Condition) | A list of Conditions. All of the Conditions must evaluate to true to trigger the actions. | |
| **actions** | [list[DialerAction]](DialerAction) | The list of actions to be taken if the conditions are true. | [optional] |



_PureCloudPlatformClientV2 248.0.0_
