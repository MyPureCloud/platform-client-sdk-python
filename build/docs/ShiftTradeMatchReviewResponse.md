---
title: ShiftTradeMatchReviewResponse
---
## ShiftTradeMatchReviewResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **initiating_user** | [**ShiftTradeMatchReviewUserResponse**](ShiftTradeMatchReviewUserResponse.html) | Details for the initiatingUser side of the shift trade | [optional] |
| **receiving_user** | [**ShiftTradeMatchReviewUserResponse**](ShiftTradeMatchReviewUserResponse.html) | Details for the receivingUser side of the shift trade | [optional] |
| **violations** | [**list[ShiftTradeMatchViolation]**](ShiftTradeMatchViolation.html) | Constraint violations introduced after being matched that would normally disallow a trade, but which can still be overridden by the shift trade administrator | [optional] |
| **admin_review_violations** | [**list[ShiftTradeMatchViolation]**](ShiftTradeMatchViolation.html) | Constraint violations associated with this shift trade which require shift trade administrator review | [optional] |
{: class="table table-striped"}


