# SmsAvailablePhoneNumber

## SmsAvailablePhoneNumber

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **phone_number** | str | A phone number available for provisioning in E.164 format. E.g. +13175555555 or +34234234234 | [optional] |
| **country_code** | str | The ISO 3166-1 alpha-2 country code of the country this phone number is associated with. | [optional] |
| **region** | str | The region/province/state the phone number is associated with. | [optional] |
| **city** | str | The city the phone number is associated with. | [optional] |
| **capabilities** | list[str] | The capabilities of the phone number available for provisioning. | [optional] |
| **phone_number_type** | str | The type of phone number available for provisioning. | [optional] |
| **address_requirement** | str | The address requirement needed for provisioning this number. If there is a requirement, the address must be the residence or place of business of the individual or entity using the phone number. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 242.0.0_
