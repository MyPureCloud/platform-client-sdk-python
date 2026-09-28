# BuQueryAdherenceAdjustmentsRequest

## BuQueryAdherenceAdjustmentsRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start timestamp of the range to query in ISO-8601 format | |
| **end_date** | datetime | The end timestamp of the range to query in ISO-8601 format | |
| **reason_code_ids** | list[str] | A filter for the reason codes to include. Leave empty or omit entirely for all reason codes | [optional] |
| **statuses** | list[str] | A filter for which adherence adjustment statuses to include. Leave empty or omit entirely for all statuses | [optional] |
| **user_ids** | list[str] | A filter for which users within the business unit to query. Leave empty or omit entirely for all users | [optional] |
| **management_unit_ids** | list[str] | A filter for which management units to query. Leave empty or omit entirely for all management units in the business unit | [optional] |



_PureCloudPlatformClientV2 268.0.0_
