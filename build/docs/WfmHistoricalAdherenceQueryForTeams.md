# WfmHistoricalAdherenceQueryForTeams

## WfmHistoricalAdherenceQueryForTeams

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | Beginning of the date range to query in ISO-8601 format | |
| **end_date** | datetime | End of the date range to query in ISO-8601 format. If it is not set, end date will be set to current time | [optional] |
| **time_zone** | str | The time zone, in olson format, to use in defining days when computing adherence. The results will be returned as UTC timestamps regardless of the time zone input. | |
| **user_ids** | list[str] | The userIds to report on. If null or not set, adherence will be computed for all the users in management unit or requested teamIds | [optional] |
| **include_exceptions** | bool | Whether user exceptions should be returned as part of the results | [optional] |



_PureCloudPlatformClientV2 222.0.0_
