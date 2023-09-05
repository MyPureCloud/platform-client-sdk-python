---
title: ServiceGoalTemplate
---
## ServiceGoalTemplate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **service_level** | [**BuServiceLevel**](BuServiceLevel.html) | Service level targets for this service goal template | [optional] |
| **average_speed_of_answer** | [**BuAverageSpeedOfAnswer**](BuAverageSpeedOfAnswer.html) | Average speed of answer targets for this service goal template | [optional] |
| **abandon_rate** | [**BuAbandonRate**](BuAbandonRate.html) | Abandon rate targets for this service goal template | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Version metadata for the service goal template | [optional] |
| **impact_override** | [**ServiceGoalTemplateImpactOverride**](ServiceGoalTemplateImpactOverride.html) | Settings controlling max percent increase and decrease of service goals for this service goal template | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


