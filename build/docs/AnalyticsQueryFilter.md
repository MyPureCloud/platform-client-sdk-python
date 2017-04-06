---
title: AnalyticsQueryFilter
---
## AnalyticsQueryFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Boolean operation to apply to the provided predicates and clauses | |
| **clauses** | [**list[AnalyticsQueryClause]**](AnalyticsQueryClause.html) | Boolean &#39;and/or&#39; logic with up to two-levels of nesting | [optional] |
| **predicates** | [**list[AnalyticsQueryPredicate]**](AnalyticsQueryPredicate.html) | Like a three-word sentence: (attribute-name) (operator) (target-value). These can be one of three types: dimension, property, metric. | [optional] |
{: class="table table-striped"}


