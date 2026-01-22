# CopyCapacityPlanRequest

## CopyCapacityPlanRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | str | The name of the new capacity plan | |
| **description** | str | Description of the new capacity plan | [optional] |
| **start_business_unit_date** | date | The start date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **end_business_unit_date** | date | The end date for the capacity plan relative to the business unit time zone in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **forecast** | [ValueWrapperBuShortTermForecastReference](ValueWrapperBuShortTermForecastReference) | The selected forecast for this capacity plan. Uses forecast from original capacity plan if not specified | [optional] |



_PureCloudPlatformClientV2 249.0.0_
