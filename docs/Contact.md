# Contact

## Contact

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **address** | str | Email address or phone number for this contact type | [optional] |
| **display** | str | Formatted version of the address property | [optional] |
| **media_type** | str |  | [optional] |
| **type** | str | The type of this contact entry. Note: the PRIMARY email address cannot be changed via PATCH /api/v2/users/{userId}; submitting a modified value for the PRIMARY entry returns a 400 error. | [optional] |
| **extension** | str | Use internal extension instead of address. Mutually exclusive with the address field. | [optional] |
| **country_code** | str |  | [optional] |
| **integration** | str | Integration tag value if this number is associated with an external integration. | [optional] |



_PureCloudPlatformClientV2 269.0.0_
