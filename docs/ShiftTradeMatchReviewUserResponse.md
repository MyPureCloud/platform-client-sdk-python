# ShiftTradeMatchReviewUserResponse

## ShiftTradeMatchReviewUserResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **weekly_minimum_paid_minutes** | int | The minimum weekly paid minutes for this user per the work plan tied to the agent schedule | [optional] |
| **weekly_maximum_paid_minutes** | int | The maximum weekly paid minutes for this user per the work plan tied to the agent schedule | [optional] |
| **pre_trade_schedule_paid_minutes** | int | The paid minutes on the week schedule for this user prior to the shift trade | [optional] |
| **post_trade_schedule_paid_minutes** | int | The paid minutes on the week schedule for this user if the shift trade is approved | [optional] |
| **post_trade_new_shift** | [ShiftTradePreviewResponse](ShiftTradePreviewResponse) | Preview of what the shift will look like for the opposite side of this trade after the match is approved | [optional] |



_PureCloudPlatformClientV2 235.0.0_
