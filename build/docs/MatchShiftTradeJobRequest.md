# MatchShiftTradeJobRequest

## MatchShiftTradeJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **week_date** | date | The start week date of the initiating shift in the business unit time zone (yyyy-MM-dd format). Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **receiving_schedule** | [ReceivingScheduleLookup](ReceivingScheduleLookup) | Associated schedule information for the receiving user | |
| **receiving_shift_id** | str | The ID of the shift the receiving user is giving up in trade, if applicable | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the shift trade | |



_PureCloudPlatformClientV2 256.0.0_
