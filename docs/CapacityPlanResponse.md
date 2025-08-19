# CapacityPlanResponse

## CapacityPlanResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **description** | str | Description of the capacity plan | [optional] |
| **forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | The selected forecast for this capacity plan. Null when main forecast is used in the future | [optional] |
| **start_business_unit_date** | date | The start date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **end_business_unit_date** | date | The end date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **full_time_equivalent_weekly_hours** | float | The weekly hours used to calculate full time equivalent agents | |
| **metadata** | [CapacityPlanMetadata](CapacityPlanMetadata) | The metadata of this capacity plan | |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 235.1.0_
