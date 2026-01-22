# EvaluationSearchAggregationBucket

## EvaluationSearchAggregationBucket

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **key** | str | The key for this bucket | [optional] |
| **key_as_string** | str | The key as a string representation | [optional] |
| **document_count** | int | Number of documents in this bucket | [optional] |
| **key_value** | int | Numeric key value for date histograms | [optional] |
| **pcFrom** | float | Lower bound for range buckets | [optional] |
| **to** | float | Upper bound for range buckets | [optional] |
| **value** | float | Simple aggregation value | [optional] |
| **count** | int | Count of documents | [optional] |
| **minimum** | float | Minimum value in the aggregation | [optional] |
| **maximum** | float | Maximum value in the aggregation | [optional] |
| **average** | float | Average value in the aggregation | [optional] |
| **sum** | float | Sum of values in the aggregation | [optional] |
| **sub_aggregations** | [dict(str, EvaluationSearchAggregationResponse)](EvaluationSearchAggregationResponse) | Nested sub-aggregations | [optional] |



_PureCloudPlatformClientV2 249.0.0_
