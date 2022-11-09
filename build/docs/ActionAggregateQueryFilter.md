---
title: ActionAggregateQueryFilter
---
## ActionAggregateQueryFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Boolean operation to apply to the provided predicates and clauses | |
| **clauses** | [**list[ActionAggregateQueryClause]**](ActionAggregateQueryClause.html) | Boolean &#39;and/or&#39; logic with up to two-levels of nesting | [optional] |
| **predicates** | [**list[ActionAggregateQueryPredicate]**](ActionAggregateQueryPredicate.html) | Like a three-word sentence: (attribute-name) (operator) (target-value). | [optional] |
{: class="table table-striped"}


