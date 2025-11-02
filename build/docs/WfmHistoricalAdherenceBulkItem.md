# WfmHistoricalAdherenceBulkItem

## WfmHistoricalAdherenceBulkItem

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit_id** | str | The ID of the management unit to query | |
| **start_date** | datetime | Beginning of the date range to query in ISO-8601 format | |
| **end_date** | datetime | End of the date range to query in ISO-8601 format | |
| **user_ids** | list[str] | The IDs of the users to query. If not included, will query every user in the management unit | [optional] |
| **include_exceptions** | bool | Whether user exceptions should be returned as part of the results. Defaults to false if not specified. | [optional] |
| **include_actuals** | bool | Whether user actual activities should be returned as part of the results. Defaults to false if not specified. | [optional] |



_PureCloudPlatformClientV2 242.0.0_
