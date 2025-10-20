# BulkContactsResponse

## BulkContactsResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **results** | [list[BulkResponseResultExternalContactExternalContactBulkEntityErrorExternalContact]](BulkResponseResultExternalContactExternalContactBulkEntityErrorExternalContact) | A list of results for all of the Bulk operations specified in the request. Includes both successes and failures. Ordering is NOT guaranteed - may be in a different order from the request. | [optional] |
| **error_count** | int | The number of failed operations in the results. | [optional] |
| **error_indexes** | list[int] | The indexes of all failed operations in the results field. | [optional] |



_PureCloudPlatformClientV2 241.0.0_
