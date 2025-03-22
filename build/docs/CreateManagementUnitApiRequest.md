# CreateManagementUnitApiRequest

## CreateManagementUnitApiRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the management unit | |
| **time_zone** | str | The default time zone to use for this management unit.  Moving to Business Unit | [optional] |
| **start_day_of_week** | str | The configured first day of the week for scheduling and forecasting purposes. Moving to Business Unit | [optional] |
| **settings** | [CreateManagementUnitSettingsRequest](CreateManagementUnitSettingsRequest) | The configuration for the management unit.  If omitted, reasonable defaults will be assigned | [optional] |
| **division_id** | str | The id of the division to which this management unit belongs.  Defaults to home division ID | [optional] |
| **business_unit_id** | str | The id of the business unit to which this management unit belongs | |



_PureCloudPlatformClientV2 224.0.0_
