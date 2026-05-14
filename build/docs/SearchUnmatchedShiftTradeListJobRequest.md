# SearchUnmatchedShiftTradeListJobRequest

## SearchUnmatchedShiftTradeListJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit_ids** | list[str] | The IDs of management units from which to query shift trades | |
| **week_dates** | list[date] | The start week dates in which to query shift trades in the business unit time zone (yyyy-MM-dd format) | |
| **receiving_schedule** | [ReceivingScheduleLookup](ReceivingScheduleLookup) | Associated schedule information for the receiving user | |
| **receiving_shift_ids** | list[str] | The IDs of shifts that the receiving user would potentially be willing to trade. If empty, only returns one-sided trades | [optional] |



_PureCloudPlatformClientV2 257.1.0_
