# EffectiveConfiguration

## EffectiveConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **properties** | dict(str, object) | Key-value configuration settings described by the schema in the propertiesSchemaUri field. | |
| **advanced** | dict(str, object) | Advanced configuration described by the schema in the advancedSchemaUri field. | |
| **name** | str | The name of the integration, used to distinguish this integration from others of the same type. | |
| **notes** | str | Notes about the integration. | |
| **credentials** | [dict(str, CredentialInfo)](CredentialInfo) | Credentials required by the integration. The required keys are indicated in the credentials property of the Integration Type | |



_PureCloudPlatformClientV2 219.1.0_
