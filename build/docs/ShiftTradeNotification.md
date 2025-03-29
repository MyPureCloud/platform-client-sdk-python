# ShiftTradeNotification

## ShiftTradeNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **week_date** | str | The start week date of the initiating shift of the shift trade in yyyy-MM-dd format | [optional] |
| **trade_id** | str | The ID of the shift trade | [optional] |
| **one_sided** | bool | Whether this is a one sided shift trade | [optional] |
| **new_state** | str | The new state of the shift trade, null if there was no change | [optional] |
| **initiating_user** | [UserReference](UserReference) | The user who initiated the shift trade | [optional] |
| **initiating_shift_date** | datetime | The start date and time of the initiating shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **receiving_user** | [UserReference](UserReference) | The user on the receiving side of this shift trade (null if not matched) | [optional] |
| **receiving_shift_date** | datetime | The start date and time of the receiving shift (null if not matched or if one-sided. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |



_PureCloudPlatformClientV2 224.1.0_
