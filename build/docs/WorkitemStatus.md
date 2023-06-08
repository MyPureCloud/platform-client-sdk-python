---
title: WorkitemStatus
---
## WorkitemStatus

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **category** | **str** | The Category of the Status. | [optional] |
| **destination_statuses** | [**list[WorkitemStatusReference]**](WorkitemStatusReference.html) | The Statuses the Status can transition to. | [optional] |
| **description** | **str** | The description of the Status. | [optional] |
| **default_destination_status** | [**WorkitemStatusReference**](WorkitemStatusReference.html) | Default destination status to which this Status will transition to if auto status transition enabled. | [optional] |
| **status_transition_delay_seconds** | **int** | Delay in seconds for auto status transition | [optional] |
| **status_transition_time** | [**LocalTime**](LocalTime.html) | Time in HH:MM:SS format at which auto status transition will occur after statusTransitionDelaySeconds delay. To set Time, the statusTransitionDelaySeconds must be equal to or greater than 86400 i.e. a day | [optional] |
| **worktype** | [**WorktypeReference**](WorktypeReference.html) | The Worktype containing the Status. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


