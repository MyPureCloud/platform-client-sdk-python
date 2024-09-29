# BuQueryAdherenceExplanationsRequest

## BuQueryAdherenceExplanationsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start date of the range to query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **end_date** | datetime | The end date of the range to query. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **management_unit_ids** | list[str] | A filter for which management units to query. Leave empty or omit entirely for all management units in the business unit | [optional] |
| **agent_ids** | list[str] | A filter for which agents within the business unit to query. Leave empty or omit entirely for all agents in the business unit (or management units if specified) | [optional] |



_PureCloudPlatformClientV2 212.0.0_
