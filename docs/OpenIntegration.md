# OpenIntegration

## OpenIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique Integration Id. | |
| **name** | str | The name of the Open messaging integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **outbound_notification_webhook_url** | str | The outbound notification webhook URL for the Open messaging integration. | |
| **outbound_notification_webhook_signature_secret_token** | str | The outbound notification webhook signature secret token. | |
| **webhook_headers** | dict(str, str) | The user specified headers for the Open messaging integration. | [optional] |
| **status** | str | The status of the Open Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient associated to the Open messaging Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 227.1.0_
