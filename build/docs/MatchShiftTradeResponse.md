# MatchShiftTradeResponse

## MatchShiftTradeResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **trade** | [ShiftTradeResponse](ShiftTradeResponse) | The associated shift trade | [optional] |
| **violations** | [list[ShiftTradeMatchViolation]](ShiftTradeMatchViolation) | Constraint violations which disallow this shift trade | [optional] |
| **admin_review_violations** | [list[ShiftTradeMatchViolation]](ShiftTradeMatchViolation) | Constraint violations for this shift trade which require shift trade administrator review | [optional] |
| **unevaluated_rules** | list[str] | Unevaluated rules for this shift trade which require shift trade administrator review | [optional] |



_PureCloudPlatformClientV2 233.0.0_
