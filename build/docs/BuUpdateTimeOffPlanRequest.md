# BuUpdateTimeOffPlanRequest

## BuUpdateTimeOffPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of this time-off plan | [optional] |
| **activity_code_ids** | [SetWrapperString](SetWrapperString) | The IDs of activity codes to associate with this time-off plan | [optional] |
| **auto_approval_rule** | str | Auto approval rule for this time-off plan | [optional] |
| **days_before_start_to_expire_from_waitlist** | int | The number of days before the time-off request start date for when the request will be expired from the waitlist | [optional] |
| **auto_publish_approved_time_off_requests** | bool | Whether newly approved time-off requests with activity codes associated with this time-off plan should be automatically published to the schedule | [optional] |
| **restricted_activity_code_ids** | [SetWrapperString](SetWrapperString) | The IDs of non time-off activity codes to check for conflicts in case the auto approval rule specifies checking activity codes. If these activity codes are present in schedule and overlap with the time-off request duration, the request will not be auto approved | [optional] |
| **hris_time_off_type** | [ValueWrapperHrisTimeOffType](ValueWrapperHrisTimeOffType) | Time-off type, if this time-off plan is associated with the integration | [optional] |
| **enabled** | bool | Whether this time-off plan should be used by agents | [optional] |
| **count_against_time_off_limits** | bool | Whether this time-off plan should count against time-off limits | [optional] |
| **business_unit_association** | [UpdateTimeOffPlanBusinessUnitAssociation](UpdateTimeOffPlanBusinessUnitAssociation) | Business unit association, if the time-off plan belongs to a business unit. managementUnitAssociation must not be set if this is populated | [optional] |
| **management_unit_association** | [UpdateTimeOffPlanManagementUnitAssociation](UpdateTimeOffPlanManagementUnitAssociation) | Management unit association, if the time-off plan belongs to a management unit. businessUnitAssociation must not be set if this is populated | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for this time-off plan | |



_PureCloudPlatformClientV2 249.0.0_
