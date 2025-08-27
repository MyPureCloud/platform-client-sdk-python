# CapacityPlanRequest

## CapacityPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the capacity plan | |
| **description** | str | Description of the capacity plan | [optional] |
| **start_business_unit_date** | date | The start date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **end_business_unit_date** | date | The end date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | The selected forecast for this capacity plan. Null when main forecast is used in the future | |
| **full_time_equivalent_weekly_hours** | float | The weekly hours used to calculate full time equivalent agents | |
| **staffing_group_allocations** | [list[CreateStaffingGroupAllocation]](CreateStaffingGroupAllocation) | List of staffing group allocations to be used for the capacity plan | |



_PureCloudPlatformClientV2 236.0.0_
