---
title: MetricDefinition
---
## MetricDefinition

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **unit_type** | **str** | The type of associated metric unit | [optional] |
| **short_name** | **str** | An alternate name for this metric definition, often abbreviation | [optional] |
| **dividend_metrics** | **list[str]** | Metric names used as dividend | [optional] |
| **divisor_metrics** | **list[str]** | Metric names used as divisor | [optional] |
| **default_objective** | [**DefaultObjective**](DefaultObjective.html) | A predefined default objective for this metric | [optional] |
| **lock_template_id** | **str** | An optional field to specify if this metric definition is locked to certain template. e.g. punctuality | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


