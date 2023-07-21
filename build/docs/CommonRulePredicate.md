---
title: CommonRulePredicate
---
## CommonRulePredicate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metric_type** | **str** | The type of metric being evaluated. | |
| **metric_value_type** | **str** | The type of metric value being evaluated. | |
| **comparison_operator** | **str** | The comparison operator being performed on the metric. | |
| **value** | **float** | The value the metric will be compared to. | |
| **status** | **str** | The status of the entity corresponding to the metric. | [optional] |
| **entity** | [**CommonRulePredicateEntity**](CommonRulePredicateEntity.html) | The entity whose metric is being represented. | |
| **media_type** | **str** | The media type of the conversation the metric describes. | [optional] |
| **metric** | **str** | The metric being evaluated. | |
{: class="table table-striped"}


