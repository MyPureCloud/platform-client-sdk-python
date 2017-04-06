---
title: AnalyticsQueryPredicate
---
## AnalyticsQueryPredicate

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **type** | **str** | Optional type, can usually be inferred | [optional] |
| **dimension** | **str** | Left hand side for dimension predicates | [optional] |
| **property_type** | **str** | Left hand side for property predicates | [optional] |
| **pcProperty** | **str** | Left hand side for property predicates | [optional] |
| **metric** | **str** | Left hand side for metric predicates | [optional] |
| **operator** | **str** | Optional operator, default is matches | [optional] |
| **value** | **str** | Right hand side for dimension, property, or metric predicates | [optional] |
| **range** | [**NumericRange**](NumericRange.html) | Right hand side for property or metric predicates | [optional] |
{: class="table table-striped"}


