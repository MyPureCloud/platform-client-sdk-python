# ConditionalGroupActivation

## ConditionalGroupActivation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **pilot_rule** | [ConditionalGroupActivationPilotRule](ConditionalGroupActivationPilotRule) | The pilot rule for this queue, which executes periodically to determine queue health | [optional] |
| **rules** | [list[ConditionalGroupActivationRule]](ConditionalGroupActivationRule) | The set of rules to be periodically executed on the queue (if the pilot rule evaluates as true or there is no pilot rule) | [optional] |



_PureCloudPlatformClientV2 228.0.0_
