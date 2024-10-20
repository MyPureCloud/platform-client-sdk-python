# RecordingEncryptionConfiguration

## RecordingEncryptionConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **url** | str | When keyConfigurationType is LocalKeyManager, this should be the url for decryption and must specify the path to where GenesysCloud can requests decryption. When keyConfigurationType is KmsSymmetric, this should be the arn to the key alias for the master key | |
| **api_id** | str | The api id for Hawk Authentication. Null if keyConfigurationType is KmsSymmetric | [optional] |
| **api_key** | str | The api shared symmetric key used for hawk authentication. Null if keyConfigurationType is KmsSymmetric | [optional] |
| **key_configuration_type** | str | Type should be LocalKeyManager or KmsSymmetric when create or update Key configurations; &#39;Native&#39; for disabling configuration. | |
| **last_error** | [ErrorBody](ErrorBody) | The error message related to the configuration | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 214.0.0_
