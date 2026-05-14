# ScheduledTrigger

## ScheduledTrigger

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the scheduled trigger. Can be up to 162 characters in length. | [optional] |
| **target** | [TriggerTarget](TriggerTarget) | The target to invoke when the scheduled trigger fires | [optional] |
| **version** | int | Version of this scheduled trigger | [optional] |
| **enabled** | bool | Whether or not the scheduled trigger is enabled | [optional] |
| **schedule** | [TriggerSchedule](TriggerSchedule) | The schedule configuration for when this trigger should fire | [optional] |
| **description** | str | Description of the trigger. Can be up to 512 characters in length. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 257.1.0_
