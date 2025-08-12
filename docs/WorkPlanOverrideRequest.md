# WorkPlanOverrideRequest

## WorkPlanOverrideRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **action** | str | The action to perform on work plan override, defaults to add | [optional] |
| **start_date** | date | The start date in yyyy-MM-dd format for the updated work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **week_count** | int | The week count of the updated work plan, required if action is Add or Update | [optional] |
| **work_plan_id** | str | The updated work plan id | [optional] |



_PureCloudPlatformClientV2 235.0.0_
