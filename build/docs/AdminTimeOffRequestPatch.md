---
title: AdminTimeOffRequestPatch
---
## AdminTimeOffRequestPatch

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **status** | **str** | The status of this time off request | [optional] |
| **activity_code_id** | **str** | The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category | [optional] |
| **paid** | **bool** | Whether this is a paid time off request | [optional] |
| **notes** | **str** | Notes about the time off request | [optional] |
| **full_day_management_unit_dates** | **list[str]** | A set of dates in yyyy-MM-dd format. Should be interpreted in the management unit&#39;s configured time zone. | [optional] |
| **partial_day_start_date_times** | **list[datetime]** | A set of start date-times in ISO-8601 format for partial day requests. | [optional] |
| **daily_duration_minutes** | **int** | The daily duration of this time off request in minutes | [optional] |
| **duration_minutes** | **list[int]** | Daily durations for each day of this time off request in minutes | [optional] |
| **payable_minutes** | **list[int]** | Payable minutes for each day of this time off request | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the time off request | |
{: class="table table-striped"}


