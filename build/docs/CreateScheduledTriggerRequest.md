# CreateScheduledTriggerRequest

## CreateScheduledTriggerRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **target** | [TriggerTarget](TriggerTarget) | The target to invoke when the scheduled trigger fires | |
| **enabled** | bool | Boolean indicating if scheduled trigger is enabled | |
| **name** | str | The name of the scheduled trigger. Can be up to 162 characters in length. | |
| **schedule** | [TriggerSchedule](TriggerSchedule) | The schedule configuration for when this trigger should fire | |
| **description** | str | Description of the trigger. Can be up to 512 characters in length. | [optional] |



_PureCloudPlatformClientV2 257.0.0_
