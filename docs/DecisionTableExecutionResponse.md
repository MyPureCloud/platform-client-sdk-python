# DecisionTableExecutionResponse

## DecisionTableExecutionResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **table** | [DecisionTableVersionEntity](DecisionTableVersionEntity) | The decision table version entity that was executed. | [optional] |
| **total_match_row_count** | int | Total number of rows that matched execution input and would return results | [optional] |
| **top_match_rows** | [list[DecisionTableRowEntityRef]](DecisionTableRowEntityRef) | Top 5 rows matching execution input, excluding the one produced the result. | [optional] |
| **row_execution_outputs** | [list[DecisionTableRowExecutionOutput]](DecisionTableRowExecutionOutput) | The output data for each executed row for which output is collected. | [optional] |



_PureCloudPlatformClientV2 239.0.0_
