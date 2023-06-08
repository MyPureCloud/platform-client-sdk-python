---
title: WorkitemStatusUpdate
---
## WorkitemStatusUpdate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The name of the Status. Valid length between 3 and 256 characters. | [optional] |
| **destination_status_ids** | **list[str]** | A list of destination Statuses where a Workitem with this Status can transition to. If the list is empty Workitems with this Status can transition to all other Statuses defined on the Worktype. A Status can have a maximum of 24 destinations. | [optional] |
| **description** | **str** | The description of the Status. Maximum length of 4096 characters. | [optional] |
| **default_destination_status_id** | **str** | Default destination status to which this Status will transition to if auto status transition enabled. | [optional] |
| **status_transition_delay_seconds** | **int** | Delay in seconds for auto status transition. Required if defaultDestinationStatusId is provided. | [optional] |
| **status_transition_time** | [**LocalTime**](LocalTime.html) | Time in HH:MM:SS format at which auto status transition will occur after statusTransitionDelaySeconds delay. To set Time, the statusTransitionDelaySeconds must be equal to or greater than 86400 i.e. a day | [optional] |
{: class="table table-striped"}


