# UpdateCapacityPlanRequest

## UpdateCapacityPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the capacity plan | [optional] |
| **description** | str | Description of the capacity plan | [optional] |
| **start_business_unit_date** | date | The start date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **end_business_unit_date** | date | The end date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **forecast** | [ValueWrapperBuShortTermForecastReference](ValueWrapperBuShortTermForecastReference) | The selected forecast for this capacity plan | [optional] |
| **full_time_equivalent_weekly_hours** | float | The weekly hours used to calculate full time equivalent agents | [optional] |
| **use_latest_planning_group_staffing_group_association** | bool | Whether to use latest staffing group to planning group association | [optional] |
| **metadata** | [CapacityPlanMetadata](CapacityPlanMetadata) | The metadata of this capacity plan | |



_PureCloudPlatformClientV2 236.0.0_
