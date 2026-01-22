# AppleIntegration

## AppleIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique integration Id. | |
| **name** | str | The name of the Apple messaging integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **messages_for_business_id** | str | The Apple Messages for Business Id for the Apple messaging integration. | |
| **business_name** | str | The name of the business. | [optional] |
| **logo_url** | str | The url of the businesses logo. | [optional] |
| **status** | str | The status of the Apple Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient associated to the Apple messaging Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **apple_i_message_app** | [AppleIMessageApp](AppleIMessageApp) | Interactive Application (iMessage App) Settings. | [optional] |
| **apple_authentication** | [AppleAuthentication](AppleAuthentication) | The Apple Messages for Business authentication setting. | [optional] |
| **apple_pay** | [ApplePay](ApplePay) | Apple Pay settings. | [optional] |
| **identity_resolution** | [AppleIdentityResolutionConfig](AppleIdentityResolutionConfig) | The configuration to control identity resolution. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 249.0.0_
