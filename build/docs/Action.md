# Action

## Action

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **integration_id** | str | The ID of the integration for which this action is associated | [optional] |
| **category** | str | Category of Action | [optional] |
| **contract** | [ActionContract](ActionContract) | Action contract | [optional] |
| **version** | int | Version of this action | [optional] |
| **secure** | bool | Indication of whether or not the action is designed to accept sensitive data | [optional] |
| **config** | [ActionConfig](ActionConfig) | Configuration to support request and response processing | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
