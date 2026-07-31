# CreateVerifierRequest

## CreateVerifierRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **algorithm** | str | The hashing algorithm for the TOTP verifier. | |
| **digits** | int | The number of digits in the TOTP code. Must be between 6 and 12. | |
| **enabled** | bool | Indicates whether this verifier will be enabled. | |
| **name** | str | The name of the verifier. Maximum length is 100 characters. | |
| **period** | int | The time period in seconds for the TOTP code. | |
| **secret_size** | int | The size of the shared secret in bytes. Must be between 10 and 64. | |
| **default** | bool | Indicates whether this will be the default verifier. | |



_PureCloudPlatformClientV2 263.0.0_
