---
title: WfmAgent
---
## WfmAgent

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **user** | [**UserReference**](UserReference.html) | The user associated with this data | [optional] |
| **queues** | [**list[QueueReference]**](QueueReference.html) | List of queues to which the agent belongs and which are defined in the service goal groups in this management unit | [optional] |
| **languages** | [**list[LanguageReference]**](LanguageReference.html) | The list of languages | [optional] |
| **skills** | [**list[RoutingSkillReference]**](RoutingSkillReference.html) | The list of skills | [optional] |
| **work_plan** | [**WorkPlanReference**](WorkPlanReference.html) | The work plan associated with this agent | [optional] |
| **schedulable** | **bool** | Whether the agent has the permission to be included in schedule generation | [optional] |
| **time_zone** | [**WfmTimeZone**](WfmTimeZone.html) | The time zone for this agent. Defaults to the time zone of the management unit to which the agent belongs | [optional] |
| **accept_direct_shift_trades** | **bool** | Whether the agent accepts direct shift trade requests | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Metadata for this agent | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


