---
title: AddShiftTradeRequest
---
## AddShiftTradeRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **schedule_id** | **str** | The ID of the schedule to which the initiating and receiving shifts belong | |
| **initiating_shift_id** | **str** | The ID of the shift that the initiating user wants to give up | |
| **receiving_user_id** | **str** | The ID of the user to whom to send the request (for use in direct trade requests) | [optional] |
| **expiration** | **datetime** | When this shift trade request should expire. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **acceptable_intervals** | [**list[ShiftTradeResponseAcceptableIntervals]**](ShiftTradeResponseAcceptableIntervals.html) |  | [optional] |
{: class="table table-striped"}


