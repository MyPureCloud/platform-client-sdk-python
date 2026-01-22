# StaffingGroupMetricChangeResponse

## StaffingGroupMetricChangeResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **number_of_weeks** | int | The number of weeks to which the metric change applies | |
| **week_start_number** | int | The start number of the week (starting from 1) to which the metric change applies, related to numberOfWeeks | |
| **value** | float | The value of the metric | |
| **metric** | str | The metric which is going to be modified for the selected staffing groups | |
| **notes** | str | Notes about the staffing groups metric changes | [optional] |
| **staffing_groups** | [list[StaffingGroupReference]](StaffingGroupReference) | The staffing groups affected by the metric change | |
| **created_by** | [UserReference](UserReference) | The user who created the metric change | |
| **created_date** | datetime | The date the entity was created, in ISO-8601 format | |



_PureCloudPlatformClientV2 249.0.0_
