# CapacityPlanForecastInputsTemplate

## CapacityPlanForecastInputsTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **reference_business_unit_date** | date | The reference date for interval-based data relative to the business unit time zone for the forecast inputs. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **granularity** | str | Granularity of the intervals | |
| **months** | [list[YearMonth]](YearMonth) | The list of months covered by this capacity plan, formatted as yyyy-MM, populated for monthly granularity | [optional] |
| **planning_groups_forecast_data** | [list[ForecastInputPlanningGroupData]](ForecastInputPlanningGroupData) | The forecast data for the planning groups | |
| **capacity_plan_forecast_summary** | [CapacityPlanForecastMetrics](CapacityPlanForecastMetrics) | The summary of forecast inputs for this capacity plan, for the selected granularity | |



_PureCloudPlatformClientV2 262.0.0_
