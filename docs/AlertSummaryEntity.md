# AlertSummaryEntity

## AlertSummaryEntity

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **entity_type** | str | Specifies the type of entity being evaluated | |
| **user** | [AddressableEntityRef](AddressableEntityRef) | User id of the entity being monitored | [optional] |
| **group** | [AddressableEntityRef](AddressableEntityRef) | Group id of the entity being monitored | [optional] |
| **queue** | [AddressableEntityRef](AddressableEntityRef) | Queue id of the entity being monitored | [optional] |
| **team** | [AddressableEntityRef](AddressableEntityRef) | Team id of the entity being monitored | [optional] |
| **alerting** | bool | Flag that indicated if the entity is current causing the alert to be triggered | |



_PureCloudPlatformClientV2 216.0.0_
