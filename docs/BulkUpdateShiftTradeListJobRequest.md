# BulkUpdateShiftTradeListJobRequest

## BulkUpdateShiftTradeListJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **management_unit_ids** | list[str] | The IDs of the management units from which to update shift trades | |
| **week_dates** | list[date] | The start week dates in which the shift trades being updated occur in the business unit time zone (yyyy-MM-dd format) | |
| **entities** | [list[BulkUpdateShiftTradeStateRequestItem]](BulkUpdateShiftTradeStateRequestItem) | The shift trades that are being updated | |



_PureCloudPlatformClientV2 255.0.0_
