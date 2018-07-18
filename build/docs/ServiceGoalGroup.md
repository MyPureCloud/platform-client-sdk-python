---
title: ServiceGoalGroup
---
## ServiceGoalGroup

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **goals** | [**ServiceGoalGroupGoals**](ServiceGoalGroupGoals.html) | Goals defined for this service goal group | [optional] |
| **queue_media_associations** | [**list[QueueMediaAssociation]**](QueueMediaAssociation.html) | List of queues and media types from that queue to associate with this service goal group | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the list of service goal groups for the associated management unit | |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


