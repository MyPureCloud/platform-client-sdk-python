# CreateVerifierRequest

## CreateVerifierRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **algorithm** | str | The hashing algorithm for the TOTP verifier. | [optional] |
| **digits** | int | The number of digits in the TOTP code. Must be between 6 and 12. | [optional] |
| **enabled** | bool | Indicates whether this verifier will be enabled. | [optional] |
| **name** | str | The name of the verifier. Maximum length is 100 characters. | |
| **period** | int | The time period in seconds for the TOTP code. | [optional] |
| **secret_size** | int | The size of the shared secret in bytes. Must be between 10 and 64. | [optional] |
| **default** | bool | Indicates whether this will be the default verifier. | [optional] |



_PureCloudPlatformClientV2 266.0.0_
