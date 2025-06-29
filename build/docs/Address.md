# Address

## Address

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | This will be nameRaw if present, or a locality lookup of the address field otherwise. | [optional] |
| **name_raw** | str | The name as close to the bits on the wire as possible. | [optional] |
| **address_normalized** | str | The normalized address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table. | [optional] |
| **address_raw** | str | The address as close to the bits on the wire as possible. | [optional] |
| **address_displayable** | str | The displayable address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table. | [optional] |



_PureCloudPlatformClientV2 232.0.0_
