---
title: ForecastPlanningGroupData
---
## ForecastPlanningGroupData

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **planning_group_id** | **str** | The ID of the planning group to which this data applies. Note this is a snapshot of the planning group at the time of forecast creation and may not correspond to the current configuration | [optional] |
| **offered_per_interval** | **list[float]** | Forecast offered counts per interval for this week of the forecast | [optional] |
| **average_handle_time_seconds_per_interval** | **list[float]** | Forecast average handle time per interval in seconds | [optional] |
{: class="table table-striped"}


