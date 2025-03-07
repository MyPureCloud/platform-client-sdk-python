# SmsAddress

## SmsAddress

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The id of this address. | [optional] |
| **name** | str |  | [optional] |
| **street** | str | The number and street address where this address is located. | [optional] |
| **city** | str | The city in which this address is in | [optional] |
| **region** | str | The state or region this address is in | [optional] |
| **postal_code** | str | The postal code this address is in | [optional] |
| **country_code** | str | The ISO country code of this address | [optional] |
| **validated** | bool | In some countries, addresses are validated to comply with local regulation. In those countries, if the address you provide does not pass validation, it will not be accepted as an Address. This value will be true if the Address has been validated, or false for countries that don&#39;t require validation or if the Address is non-compliant. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 223.0.0_
