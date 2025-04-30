# MinerExecuteRequest

## MinerExecuteRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_start** | date | Start date for the date range to mine. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end** | date | End date for the date range to mine. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **upload_key** | str | Location of input conversations. | [optional] |
| **media_type** | str | Media type for filtering conversations. | [optional] |
| **participant_type** | str | Type of the participant, either agent, customer or both. | [optional] |
| **queue_ids** | list[str] | List of queue IDs for filtering conversations. | [optional] |



_PureCloudPlatformClientV2 227.0.0_
