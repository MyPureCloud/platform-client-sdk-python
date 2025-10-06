# BuTimeOffPlanResponse

## BuTimeOffPlanResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | The name of this time-off plan | |
| **activity_code_ids** | list[str] | The IDs of activity codes associated with this time-off plan | |
| **time_off_limits** | [list[BuTimeOffLimitReference]](BuTimeOffLimitReference) | The IDs of time-off limits associated with this time-off plan | [optional] |
| **auto_approval_rule** | str | Auto approval rule for this time-off plan | |
| **days_before_start_to_expire_from_waitlist** | int | The number of days before the time-off request start date for when the request will be expired from the waitlist | |
| **hris_time_off_type** | [HrisTimeOffType](HrisTimeOffType) | Time-off type, if this time-off plan is associated with the integration | [optional] |
| **enabled** | bool | Whether this time-off plan is currently being used by agents | |
| **count_against_time_off_limits** | bool | Whether this time-off plan counts against time-off limits | |
| **business_unit_association** | [TimeOffPlanBusinessUnitAssociation](TimeOffPlanBusinessUnitAssociation) | Business unit association, if the time-off plan belongs to a business unit. managementUnitAssociation must not be set if this is populated | [optional] |
| **management_unit_association** | [TimeOffPlanManagementUnitAssociation](TimeOffPlanManagementUnitAssociation) | Management Unit association, if the time-off plan belongs to a management unit. businessUnitAssociation must not be set if this is populated | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time-off plan | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 240.0.0_
