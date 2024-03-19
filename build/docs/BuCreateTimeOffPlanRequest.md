---
title: BuCreateTimeOffPlanRequest
---
## BuCreateTimeOffPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of this time-off plan | |
| **activity_code_ids** | **list[str]** | The IDs of activity codes to associate with this time-off plan | [optional] |
| **auto_approval_rule** | **str** | Auto approval rule for this time-off plan. Default is Never | [optional] |
| **days_before_start_to_expire_from_waitlist** | **int** | The number of days before the time-off request start date for when the request will be expired from the waitlist. Default is 0 | [optional] |
| **hris_time_off_type** | [**HrisTimeOffType**](HrisTimeOffType.html) | Time-off type, if this time-off plan is associated with the integration | [optional] |
| **enabled** | **bool** | Whether this time-off plan should be used by agents. Default is true | [optional] |
| **count_against_time_off_limits** | **bool** | Whether this time-off plan should count against time-off limits. Default is false | [optional] |
| **business_unit_association** | [**CreateTimeOffPlanBusinessUnitAssociation**](CreateTimeOffPlanBusinessUnitAssociation.html) | Business unit association, if the time-off plan belongs to a business unit. managementUnitAssociation must not be set if this is populated | [optional] |
| **management_unit_association** | [**CreateTimeOffPlanManagementUnitAssociation**](CreateTimeOffPlanManagementUnitAssociation.html) | Management unit association, if the time-off plan belongs to a management unit. businessUnitAssociation must not be set if this is populated | [optional] |
{: class="table table-striped"}


