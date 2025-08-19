# TwitterIntegrationUpdateRequest

## TwitterIntegrationUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Twitter messaging integration. | [optional] |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingRequestReference](MessagingSettingRequestReference) | Defines the message settings to be applied for this integration | [optional] |
| **signup_code** | str | The authorization code returned from the signup flow to request access tokens later on | [optional] |
| **code_challenge** | str | The codeChallenge used during the signup flow | [optional] |
| **redirect_uri** | str | The redirectUri used during the signup flow | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
