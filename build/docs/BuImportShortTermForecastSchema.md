---
title: BuImportShortTermForecastSchema
---
## BuImportShortTermForecastSchema

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **description** | **str** | The description for the forecast | |
| **week_count** | **int** | The number of weeks covered by the forecast | |
| **planning_groups** | [**list[ForecastPlanningGroupData]**](ForecastPlanningGroupData.html) | The short term planning group data | |
| **long_term_planning_groups** | [**list[LongTermForecastPlanningGroupData]**](LongTermForecastPlanningGroupData.html) | The long term planning group data | [optional] |
| **can_use_for_scheduling** | **bool** | Whether this forecast can be used for scheduling | [optional] |
{: class="table table-striped"}


