# BuForecastStaffingRequirementsResultResponse

## BuForecastStaffingRequirementsResultResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **business_unit_id** | str | The ID of the business unit to which the forecast staffing requirements belongs | |
| **forecast** | [BuShortTermForecastReference](BuShortTermForecastReference) | The forecast reference | |
| **reference_start_date** | datetime | The reference start date for interval-based data for this forecast as an ISO-8601 string | |
| **week_count** | int | The number of weeks in this forecast | |
| **interval_length_minutes** | int | The period/interval in minutes for which to aggregate the data | |
| **state** | str | The state of the staffing requirements generation | |
| **results** | [list[BuForecastStaffingRequirementsResult]](BuForecastStaffingRequirementsResult) | The forecast staffing requirement results, Will be populated when state &#x3D;&#x3D; &#39;Complete&#39; | [optional] |



_PureCloudPlatformClientV2 231.0.0_
