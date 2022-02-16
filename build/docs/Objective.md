---
title: Objective
---
## Objective

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **template_id** | **str** | The id of this objective&#39;s base template | [optional] |
| **zones** | [**list[ObjectiveZone]**](ObjectiveZone.html) | Objective zone specifies min,max points and values for the associated metric | [optional] |
| **enabled** | **bool** | A flag for whether this objective is enabled for the related metric | [optional] |
| **media_types** | **list[str]** | A list of media types for the metric | [optional] |
| **queues** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | A list of queues for the metric | [optional] |
| **topics** | [**list[AddressableEntityRef]**](AddressableEntityRef.html) | A list of topic ids for detected topic metrics | [optional] |
| **topic_ids_filter_type** | **str** | A filter type for topic Ids. It&#39;s only used for objectives with topicIds. Default filter behavior is \&quot;or\&quot;. | [optional] |
| **date_start** | **date** | start date of the objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
{: class="table table-striped"}


