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
| **date_start** | **date** | start date of the objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
{: class="table table-striped"}


