# BuForecastStaffingRequirementsResult

## BuForecastStaffingRequirementsResult

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **week_number** | int | The week number represented by this response | |
| **download_url** | str | The url to get the requirements results for this week | |
| **download_url_expiration_date** | datetime | The expiration date of the download url, as an ISO-8601 string | |
| **planning_group_staffing_requirements** | [list[StaffingRequirementsPlanningGroupData]](StaffingRequirementsPlanningGroupData) | Results will always come via downloadUrl, however the schema is included for documentation | [optional] |



_PureCloudPlatformClientV2 232.0.0_
