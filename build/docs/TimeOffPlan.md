---
title: TimeOffPlan
---
## TimeOffPlan

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of this time off plan. | [optional] |
| **activity_code_ids** | **list[str]** | The set of activity code IDs associated with this time off plan. | [optional] |
| **time_off_limits** | [**list[TimeOffLimitReference]**](TimeOffLimitReference.html) | The set of time off limit IDs associated with this time off plan. | [optional] |
| **auto_approval_rule** | **str** | Auto approval rule for this time off plan | [optional] |
| **days_before_start_to_expire_from_waitlist** | **int** | The number of days before the time off request start date for when the request will be expired from the waitlist. | [optional] |
| **active** | **bool** | Whether this time off plan is currently being used by agents. | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the time off plan. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


