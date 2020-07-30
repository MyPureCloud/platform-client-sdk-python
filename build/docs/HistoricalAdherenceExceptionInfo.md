---
title: HistoricalAdherenceExceptionInfo
---
## HistoricalAdherenceExceptionInfo

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **start_offset_seconds** | **int** | Exception start offset in seconds relative to query start time | [optional] |
| **end_offset_seconds** | **int** | Exception end offset in seconds relative to query start time | [optional] |
| **scheduled_activity_code_id** | **str** | The ID of the scheduled activity for this user | [optional] |
| **scheduled_activity_category** | **str** | Activity for which the user is scheduled | [optional] |
| **actual_activity_category** | **str** | Activity for which the user is actually engaged | [optional] |
| **system_presence** | **str** | Actual underlying system presence value | [optional] |
| **routing_status** | [**RoutingStatus**](RoutingStatus.html) | Actual underlying routing status, used to determine whether a user is actually in adherence when OnQueue | [optional] |
| **impact** | **str** | The impact of the current adherence state for this user | [optional] |
| **secondary_presence_lookup_id** | **str** | The lookup ID used to retrieve secondary status from map of lookup ID to corresponding secondary presence ID | [optional] |
{: class="table table-striped"}


