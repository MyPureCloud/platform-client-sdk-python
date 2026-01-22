# EvaluationSearchAggregationResponse

## EvaluationSearchAggregationResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **value** | float | Simple aggregation value (for SUM, COUNT, AVERAGE, etc.) | [optional] |
| **count** | int | Count of documents | [optional] |
| **minimum** | float | Minimum value | [optional] |
| **maximum** | float | Maximum value | [optional] |
| **average** | float | Average value | [optional] |
| **sum** | float | Total Sum | [optional] |
| **document_count_error_upper_bound** | int | Upper bound estimate of the error in document count for this aggregation | [optional] |
| **sum_other_document_count** | int | Total document count for buckets not included in the response due to size limits | [optional] |
| **buckets** | [list[EvaluationSearchAggregationBucket]](EvaluationSearchAggregationBucket) | List of aggregation buckets | [optional] |



_PureCloudPlatformClientV2 249.0.0_
