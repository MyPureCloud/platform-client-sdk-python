# AppleIntegrationRequest

## AppleIntegrationRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Apple messaging integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingRequestReference](MessagingSettingRequestReference) | Defines the message settings to be applied for this integration | [optional] |
| **messages_for_business_id** | str | The Apple Messages for Business Id for the Apple messaging integration. | |
| **business_name** | str | The name of the business. | [optional] |
| **logo_url** | str | The url of the businesses logo. | [optional] |
| **apple_i_message_app** | [AppleIMessageApp](AppleIMessageApp) | Interactive Application (iMessage App) Settings. | [optional] |
| **apple_authentication** | [AppleAuthentication](AppleAuthentication) | The Apple Messages for Business authentication setting. | [optional] |
| **apple_pay** | [ApplePay](ApplePay) | Apple Pay settings. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.1.0_
