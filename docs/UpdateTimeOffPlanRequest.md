# UpdateTimeOffPlanRequest

## UpdateTimeOffPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of this time off plan. | [optional] |
| **activity_code_ids** | [SetWrapperString](SetWrapperString) | The set of activity code IDs to associate with this time off plan. | [optional] |
| **time_off_limit_ids** | [SetWrapperString](SetWrapperString) | The set of time off limit IDs to associate with this time off plan. | [optional] |
| **auto_approval_rule** | str | Auto approval rule for the time off plan. | [optional] |
| **days_before_start_to_expire_from_waitlist** | int | The number of days before the time off request start date for when the request will be expired from the waitlist. | [optional] |
| **hris_time_off_type** | [ValueWrapperHrisTimeOffType](ValueWrapperHrisTimeOffType) | Time off type, if this time off plan is associated with the integration. | [optional] |
| **active** | bool | Whether this time off plan should be used by agents. | [optional] |
| **metadata** | [WfmVersionedEntityMetadata](WfmVersionedEntityMetadata) | Version metadata for the time off plan | |



_PureCloudPlatformClientV2 211.0.0_
