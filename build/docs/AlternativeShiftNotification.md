---
title: AlternativeShiftNotification
---
## AlternativeShiftNotification

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **week_date** | **date** | The start date of the schedule with which this trade is associated. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **granularity** | **str** | The granularity of alternative shifts to be traded | |
| **new_state** | **str** | The new state of the alternative shift trade, null if there was no change | [optional] |
| **initiating_user** | [**UserReference**](UserReference.html) | The user who initiated the alternative shift trade | |
| **initiating_shift_date** | **datetime** | The start date and time of the initiating shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | |
| **receiving_user** | [**UserReference**](UserReference.html) | The user on the receiving this alternative shift trade | [optional] |
| **receiving_shift_date** | **datetime** | The start date and time of the receiving alternative shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


