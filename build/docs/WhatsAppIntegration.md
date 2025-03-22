# WhatsAppIntegration

## WhatsAppIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | A unique Integration Id. | |
| **name** | str | The name of the WhatsApp integration. | |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the SupportedContent profile configured for an integration | [optional] |
| **messaging_setting** | [MessagingSettingReference](MessagingSettingReference) |  | [optional] |
| **phone_number** | str | The phone number associated to the WhatsApp integration. | |
| **available_phone_numbers** | [WhatsAppAvailablePhoneNumberDetailsListing](WhatsAppAvailablePhoneNumberDetailsListing) | The list of available WhatsApp phone numbers for this account. Please select one phone number from this list to use with the created integration. | [optional] |
| **status** | str | The status of the WhatsApp Integration | [optional] |
| **recipient** | [DomainEntityRef](DomainEntityRef) | The recipient associated to the WhatsApp Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | datetime | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [DomainEntityRef](DomainEntityRef) | User reference that created this Integration | [optional] |
| **modified_by** | [DomainEntityRef](DomainEntityRef) | User reference that last modified this Integration | [optional] |
| **version** | int | Version number required for updates. | |
| **activation_status_code** | str | The status code of WhatsApp Integration activation process | [optional] |
| **activation_error_info** | [ErrorBody](ErrorBody) | The error information of WhatsApp Integration activation process | [optional] |
| **create_status** | str | Status of asynchronous create operation | [optional] |
| **create_error** | [ErrorBody](ErrorBody) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 224.0.0_
