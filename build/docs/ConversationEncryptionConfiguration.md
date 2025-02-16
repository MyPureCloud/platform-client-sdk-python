# ConversationEncryptionConfiguration

## ConversationEncryptionConfiguration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **url** | str | keyConfigurationType is always KmsSymmetric, and should be the arn to the key alias for the master key | |
| **key_configuration_type** | str | Type should be &#39;KmsSymmetric&#39; when create or update Key configurations, &#39;None&#39; to disable configuration. | |
| **last_error** | [ErrorBody](ErrorBody) | The error message related to the configuration | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 222.0.0_
