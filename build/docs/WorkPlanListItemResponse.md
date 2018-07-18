---
title: WorkPlanListItemResponse
---
## WorkPlanListItemResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **agent_count** | **int** | Number of agents in this work plan | [optional] |
| **weekly_minimum_paid_minutes** | **int** | Minimum weekly paid time in minutes defined in this work plan | [optional] |
| **weekly_maximum_paid_minutes** | **int** | Maximum weekly paid time in minutes defined in this work plan | [optional] |
| **maximum_days** | **int** | Maximum number of days in a week that can be scheduled using this work plan | [optional] |
| **enabled** | **bool** | Whether the work plan is enabled for scheduling | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for this work plan | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


