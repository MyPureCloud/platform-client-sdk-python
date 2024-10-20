# ContactListFilterRange

## ContactListFilterRange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **min** | str | The minimum value of the range. Required for the operator BETWEEN. | [optional] |
| **max** | str | The maximum value of the range. Required for the operator BETWEEN. | [optional] |
| **min_inclusive** | bool | Whether or not to include the minimum in the range. | [optional] |
| **max_inclusive** | bool | Whether or not to include the maximum in the range. | [optional] |
| **in_set** | list[str] | A set of values that the contact data should be in. Required for the IN operator. | [optional] |



_PureCloudPlatformClientV2 214.0.0_
