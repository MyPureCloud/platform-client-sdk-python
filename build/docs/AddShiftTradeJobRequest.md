# AddShiftTradeJobRequest

## AddShiftTradeJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **initiating_shift** | [InitiatingShiftRequestItem](InitiatingShiftRequestItem) | The shift that the initiating user wants to give up in this trade | |
| **acceptable_intervals** | [list[RequiredDateRange]](RequiredDateRange) | Time frames when the initiating user is willing to accept a shift in exchange. Empty means giving up the shift without taking on another one | [optional] |
| **target** | [ShiftTradeTargetRequestItem](ShiftTradeTargetRequestItem) | Optional shift trade target, can be used for example for direct user to user trade | [optional] |
| **expiration_date** | datetime | When this shift trade will expire. Date time is represented as an ISO-8601 string | [optional] |



_PureCloudPlatformClientV2 256.0.0_
