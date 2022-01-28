---
title: DefaultObjective
---
## DefaultObjective

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **template_id** | **str** | The id of this objective&#39;s base template | [optional] |
| **zones** | [**list[ObjectiveZone]**](ObjectiveZone.html) | Objective zone specifies min,max points and values for the associated metric | [optional] |
| **enabled** | **bool** | A flag for whether this objective is enabled for the related metric | [optional] |
| **topics** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | A list of topic ids for detected topic metrics | [optional] |
| **topic_ids_filter_type** | **str** | A filter type for topic Ids. It&#39;s only used for objectives with topicIds. Default filter behavior is \&quot;or\&quot;. | [optional] |
{: class="table table-striped"}


