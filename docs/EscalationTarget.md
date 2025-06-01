# EscalationTarget

## EscalationTarget

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **target_type** | str | Defines the target that the message will be escalated to. | |
| **destination** | str | Defines the destination of the escalation.SourceIntegration means use the SocialMedia Source Integration as the destination.OverrideIntegration means the set integration will be used regardless of the source. | |
| **override** | [OverrideEscalationTarget](OverrideEscalationTarget) | Set the integration ID.Only valid when type is OverrideIntegration. | [optional] |



_PureCloudPlatformClientV2 230.0.0_
