# EncryptionKey

## EncryptionKey

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **create_date** | datetime | create date of the key pair. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **keydata_summary** | str | key data summary (base 64 encoded public key) | [optional] |
| **user** | [User](User) | user that requested generation of public key | [optional] |
| **local_encryption_configuration** | [LocalEncryptionConfiguration](LocalEncryptionConfiguration) | Local configuration | [optional] |
| **key_configuration_type** | str | Key type used in this configuration | [optional] |
| **kms_key_arn** | str | ARN of internal key to be wrapped by AWS KMS Symmetric key | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 214.0.0_
