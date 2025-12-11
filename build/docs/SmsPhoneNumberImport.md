# SmsPhoneNumberImport

## SmsPhoneNumberImport

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **phone_number** | str | A phone number to be used for SMS communications. E.g. +13175555555 or +34234234234 | |
| **phone_number_type** | str | Type of the phone number provisioned. | |
| **country_code** | str | The ISO 3166-1 alpha-2 country code of the country this phone number is associated with. | |
| **integration_id** | str | The id of the Genesys Cloud integration this phone number belongs to. | |
| **compliance** | [Compliance](Compliance) | Compliance configuration for short codes, including help, stop and opt in. | [optional] |
| **supported_content** | [SupportedContentReference](SupportedContentReference) | Defines the media SupportedContent profile configured for an MMS capable phone number. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 246.0.0_
