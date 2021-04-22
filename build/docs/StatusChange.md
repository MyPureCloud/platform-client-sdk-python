---
title: StatusChange
---
## StatusChange

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **date_status_changed** | **datetime** | The date of this status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **status** | **str** | The status the change request transitioned to | [optional] |
| **previous_status** | **str** | The status the change request transitioned from | [optional] |
| **message** | **str** | A short message describing the status change | [optional] |
| **changed_by** | **str** | If applicable, the user who updated the change request to this status | [optional] |
| **reject_reason** | **str** | The reason for rejecting the limit override request | [optional] |
{: class="table table-striped"}


