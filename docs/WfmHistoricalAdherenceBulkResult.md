# WfmHistoricalAdherenceBulkResult

## WfmHistoricalAdherenceBulkResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | Beginning of the date range for this result in ISO-8601 format | [optional] |
| **end_date** | datetime | End of the date range for this result in ISO-8601 format | [optional] |
| **management_unit_id** | str | The ID of the management unit for this result | [optional] |
| **user_results** | [list[WfmHistoricalAdherenceBulkUserResult]](WfmHistoricalAdherenceBulkUserResult) | The individual results for each user | [optional] |
| **lookup_id_to_secondary_presence_id** | dict(str, str) | Map of secondary presence lookup ID to corresponding secondary presence ID | [optional] |



_PureCloudPlatformClientV2 237.0.0_
