---
title: CreateManagementUnitApiRequest
---
## CreateManagementUnitApiRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of the management unit | |
| **time_zone** | **str** | The default time zone to use for this management unit | |
| **start_day_of_week** | **str** | The configured first day of the week for scheduling and forecasting purposes | |
| **settings** | [**CreateManagementUnitSettingsRequest**](CreateManagementUnitSettingsRequest.html) | The configuration for the management unit.  If omitted, reasonable defaults will be assigned | [optional] |
| **division_id** | **str** | The id of the division to which this management unit belongs.  Defaults to home division ID | [optional] |
{: class="table table-striped"}


