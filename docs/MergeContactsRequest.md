# MergeContactsRequest

## MergeContactsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **contact_ids** | list[str] | The IDs of all contacts involved in the merge operation (must be between 2 and 25). | |
| **value_override** | [ExternalContact](ExternalContact) | Override data to set for specific Contact fields after a merge. Any null fields in &#x60;valueOverride&#x60; will not replace existing data. | [optional] |



_PureCloudPlatformClientV2 235.1.0_
