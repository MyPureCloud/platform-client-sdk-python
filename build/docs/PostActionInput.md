# PostActionInput

## PostActionInput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **category** | str | Category of action, Can be up to 256 characters long | |
| **name** | str | Name of action, Can be up to 256 characters long | |
| **integration_id** | str | The ID of the integration this action is associated to | |
| **config** | [ActionConfig](ActionConfig) | Configuration to support request and response processing | |
| **contract** | [ActionContractInput](ActionContractInput) | Action contract | |
| **secure** | bool | Indication of whether or not the action is designed to accept sensitive data | [optional] |



_PureCloudPlatformClientV2 227.1.0_
