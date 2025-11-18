# OutboundDomain

## OutboundDomain

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Unique Id of the domain such as: example.com | |
| **name** | str |  | [optional] |
| **cname_verification_result** | [VerificationResult](VerificationResult) | CNAME registration Status | [optional] |
| **dkim_verification_result** | [VerificationResult](VerificationResult) | DKIM registration Status | [optional] |
| **sender_type** | str | Sender Type | [optional] |
| **email_setting** | [EmailSetting](EmailSetting) | The email settings associated with this domain. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 243.0.0_
