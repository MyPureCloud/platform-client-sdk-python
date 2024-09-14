# OpenIntegrationUpdateRequest

## OpenIntegrationUpdateRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of the Open messaging integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingRequestReference](MessagingSettingRequestReference) | Defines the message settings to be applied for this integration | [optional] |
| **outbound_notification_webhook_url** | str | The outbound notification webhook URL for the Open messaging integration. | [optional] |
| **outbound_notification_webhook_signature_secret_token** | str | The outbound notification webhook signature secret token. | [optional] |
| **webhook_headers** | dict(str, str) | The user specified headers for the Open messaging integration. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 211.1.0_
