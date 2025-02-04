# CreateAlternativeShiftTradeRequest

## CreateAlternativeShiftTradeRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **job_id** | str | The ID of this alternative shift job | |
| **drop_shift_reference_keys** | list[str] | A list of offered shift reference keys an agent wants to drop | [optional] |
| **pickup_shift_reference_keys** | list[str] | A list of offered shift reference keys an agent wants to pick up | [optional] |
| **alternative_shift_trade_granularity** | str | The granularity of alternative shifts to be traded | |
| **expiration_date** | datetime | The date when the trade will expire in ISO-8601 format. The trade cannot be approved after expiration | [optional] |



_PureCloudPlatformClientV2 221.0.0_
