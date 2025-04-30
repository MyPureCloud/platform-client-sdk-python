# IntegrationConfiguration

## IntegrationConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the integration, used to distinguish this integration from others of the same type. | |
| **version** | int | Version number required for updates. | |
| **properties** | object | Key-value configuration settings described by the schema in the propertiesSchemaUri field. | |
| **advanced** | object | Advanced configuration described by the schema in the advancedSchemaUri field. | |
| **notes** | str | Notes about the integration. | |
| **credentials** | [dict(str, CredentialInfo)](CredentialInfo) | Credentials required by the integration. The required keys are indicated in the credentials property of the Integration Type | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.0.0_
