# PhoneNumber

## PhoneNumber

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **display** | str | The displayed form of the phone number string. Users should input the phone number in this field, but it will be altered by the API on write. If the phone number can be read as E164, the value will be replaced with international formatted-version of the number. If the number cannot be read as E164, the value will be preserved as-is. In both cases, the provided input string will be copied to the userInput field. | [optional] |
| **extension** | int | An optional extension for the provided phone number. | [optional] |
| **accepts_sms** | bool | Whether this phone number can accept SMS messages. | [optional] |
| **normalization_country_code** | str | The country code that will be used for E164 conversion of a provided phone number. If the country code is omitted from the provided phone number, the country code provided in this field will be used during the E164 conversion attempt. If this field is left empty, the default country code for any provided phone number that does not explicitly include a country code is assumed to be +1 (North America). | [optional] |
| **user_input** | str | The user-inputted phone number string that was provided to the display field on write. This field is not user-writeable and will always be set by the system. | [optional] |
| **e164** | str | The E164-formatted form of the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164. | [optional] |
| **country_code** | str | The detected country code from the provided phone number. This field is not user-writeable and will only be set when the provided phone number could be read as E164. | [optional] |



_PureCloudPlatformClientV2 235.1.0_
