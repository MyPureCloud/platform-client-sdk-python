# CapacityPlanStaffingRequirementResult

## CapacityPlanStaffingRequirementResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **business_unit** | [BusinessUnitReference](BusinessUnitReference) | The business unit to which the capacity plan belongs | |
| **capacity_plan** | [CapacityPlanReference](CapacityPlanReference) | The capacity plan for which requirements are generated | |
| **status** | str | The status of the requirement generation of the capacity plan | |
| **reference_business_unit_date** | date | The reference date for interval-based data for the requirements. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | |
| **granularity** | str | Granularity of the intervals | |
| **error_code** | str | The error code when status is &#39;Failed&#39; | [optional] |
| **download_url** | str | The URL to get the requirements results for the capacity plan. It will be populated if the status is &#39;Complete&#39; | [optional] |
| **download_template** | [StaffingRequirementResultResponseTemplate](StaffingRequirementResultResponseTemplate) | Staffing requirement results always come through downloadUrl, the schema included here is just for documentation | [optional] |



_PureCloudPlatformClientV2 244.0.0_
