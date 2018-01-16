---
title: ActivityCode
---
## ActivityCode

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the activity code. Default activity codes will be created with an empty name | [optional] |
| **is_active** | **bool** | Whether this activity code is active or has been deleted | [optional] |
| **is_default** | **bool** | Whether this is a default activity code | [optional] |
| **category** | **str** | The activity code&#39;s category. | [optional] |
| **length_in_minutes** | **int** | The default length of the activity in minutes | [optional] |
| **counts_as_paid_time** | **bool** | Whether an agent is paid while performing this activity | [optional] |
| **counts_as_work_time** | **bool** | Indicates whether or not the activity should be counted as contiguous work time for calculating daily constraints | [optional] |
| **agent_time_off_selectable** | **bool** | Whether an agent can select this activity code when creating or editing a time off request. Null if the activity&#39;s category is not time off. | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the associated management unit&#39;s list of activity codes | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


