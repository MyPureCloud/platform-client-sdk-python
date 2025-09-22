# DecisionTableRowExecutionOutput

## DecisionTableRowExecutionOutput

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **row_id** | str | Unique rule identifier. | |
| **row_index** | int | Unique rule identifier. | |
| **outputs** | dict(str, object) | The JSON output produced by this rule. Valid according to the execution output contract. In the case of enum decision table output columns, the enum options key will be provided as the value, not the enum options label as this can be changed. For business rules queue columns both “queue” and “id” keys will always be returned  regardless of the business rules queue attribute key and these do not change. | |



_PureCloudPlatformClientV2 237.0.0_
