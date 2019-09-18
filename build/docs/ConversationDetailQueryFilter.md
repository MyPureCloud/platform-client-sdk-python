---
title: ConversationDetailQueryFilter
---
## ConversationDetailQueryFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Boolean operation to apply to the provided predicates and clauses | |
| **clauses** | [**list[ConversationDetailQueryClause]**](ConversationDetailQueryClause.html) | Boolean &#39;and/or&#39; logic with up to two-levels of nesting | [optional] |
| **predicates** | [**list[ConversationDetailQueryPredicate]**](ConversationDetailQueryPredicate.html) | Like a three-word sentence: (attribute-name) (operator) (target-value). | [optional] |
{: class="table table-striped"}


