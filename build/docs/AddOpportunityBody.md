# AddOpportunityBody

## AddOpportunityBody

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_date** | datetime | The start date and time of the opportunity in ISO-8601 format | |
| **end_date** | datetime | The end date and time of the opportunity in ISO-8601 format | |
| **open_date** | datetime | The date and time when the opportunity opens for enrollment in ISO-8601 format. If not provided or in the past, it will be automatically updated to the current time when the opportunity is published | [optional] |
| **deadline_date** | datetime | The deadline date and time for enrollment in the opportunity in ISO-8601 format | |
| **name** | str | The name of the opportunity | |
| **description** | str | Additional details describing the purpose or context of this opportunity | [optional] |
| **activity_code_id** | str | The ID of the activity code associated with the opportunity | |
| **approval_type** | str | The approval type for enrollments | |
| **capacity** | int | The maximum capacity (enrollment slots) for this opportunity | |



_PureCloudPlatformClientV2 265.0.0_
