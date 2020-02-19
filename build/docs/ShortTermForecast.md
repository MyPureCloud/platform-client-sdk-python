---
title: ShortTermForecast
---
## ShortTermForecast

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **week_date** | **str** | The weekDate of the short term forecast in yyyy-MM-dd format | |
| **description** | **str** | The description of the short term forecast | [optional] |
| **creation_method** | **str** | The method used to create this forecast | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | Metadata for this forecast | |
| **source_data** | [**ListWrapperForecastSourceDayPointer**](ListWrapperForecastSourceDayPointer.html) | The source data references and metadata for this forecast | [optional] |
| **reference_start_date** | **datetime** | ISO-8601 date that serves as the reference date for interval-based modifications | [optional] |
| **modifications** | [**ListWrapperWfmForecastModification**](ListWrapperWfmForecastModification.html) | The modifications that have been applied to this forecast | [optional] |
| **generation_results** | [**ForecastGenerationResult**](ForecastGenerationResult.html) | Forecast generation results, if applicable | [optional] |
{: class="table table-striped"}


