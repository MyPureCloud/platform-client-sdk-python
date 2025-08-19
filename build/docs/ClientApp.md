# ClientApp

## ClientApp

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the integration, used to distinguish this integration from others of the same type. | [optional] |
| **integration_type** | [IntegrationType](IntegrationType) | Type of the integration | [optional] |
| **notes** | str | Notes about the integration. | [optional] |
| **intended_state** | str | Configured state of the integration. | |
| **config** | [ClientAppConfigurationInfo](ClientAppConfigurationInfo) | Configuration information for the integration. | [optional] |
| **reported_state** | [IntegrationStatusInfo](IntegrationStatusInfo) | Last reported status of the integration. | [optional] |
| **attributes** | dict(str, str) | Read-only attributes for the integration. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
