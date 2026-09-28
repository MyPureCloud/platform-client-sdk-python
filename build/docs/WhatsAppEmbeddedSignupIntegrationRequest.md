# WhatsAppEmbeddedSignupIntegrationRequest

## WhatsAppEmbeddedSignupIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the WhatsApp Integration. Required for Embedded Signup v2; optional for v4 (set later via PATCH). | [optional] |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingRequestReference](MessagingSettingRequestReference) | Defines the message settings to be applied for this integration | [optional] |
| **embedded_signup_access_token** | str | The access token returned from the embedded signup flow. Not required for versions v4 or later. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 268.0.0_
