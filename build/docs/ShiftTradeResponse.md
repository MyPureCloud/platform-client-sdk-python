---
title: ShiftTradeResponse
---
## ShiftTradeResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The ID of this shift trade | [optional] |
| **week_date** | **date** | The start week date of the associated schedule in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **schedule** | [**WeekScheduleReference**](WeekScheduleReference.html) | The ID of the associated schedule | [optional] |
| **state** | **str** | The state of this shift trade | [optional] |
| **initiating_user** | [**UserReference**](UserReference.html) | The user who initiated this trade | [optional] |
| **initiating_shift_id** | **str** | The ID of the shift offered for trade by the initiating user | [optional] |
| **initiating_shift_start** | **datetime** | The start date/time of the shift being offered for trade. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **initiating_shift_end** | **datetime** | The end date/time of the shift being offered for trade. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **receiving_user** | [**UserReference**](UserReference.html) | The user matching the trade, or if the state is not Matched, the user to whom the trade request was sent | [optional] |
| **receiving_shift_id** | **str** | The ID of the shift being exchanged for the initiating shift, null if the receiving user is picking up a shift | [optional] |
| **receiving_shift_start** | **datetime** | The start date/time of the receiving shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **receiving_shift_end** | **datetime** | The end date/time of the receiving shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **expiration** | **datetime** | When this shift trade offer will expire if not matched or approved. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **one_sided** | **bool** | Whether this is a one-sided shift trade (e.g. the initiating user is not asking for a shift in return) | [optional] |
| **acceptable_intervals** | [**list[ShiftTradeResponseAcceptableIntervals]**](ShiftTradeResponseAcceptableIntervals.html) |  | [optional] |
| **reviewed_by** | [**UserReference**](UserReference.html) | The user who reviewed this shift trade | [optional] |
| **reviewed_date** | **datetime** | The timestamp when this shift trade was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version data for this trade | [optional] |
{: class="table table-striped"}


