# DecisionTableJobValidationError

## DecisionTableJobValidationError

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **message** | str |  | [optional] |
| **code** | str |  | [optional] |
| **status** | int |  | [optional] |
| **entity_id** | str |  | [optional] |
| **entity_name** | str |  | [optional] |
| **message_with_params** | str |  | [optional] |
| **message_params** | dict(str, str) |  | [optional] |
| **context_id** | str |  | [optional] |
| **details** | [list[Detail]](Detail) |  | [optional] |
| **errors** | [list[ErrorBody]](ErrorBody) |  | [optional] |
| **limit** | [Limit](Limit) |  | [optional] |
| **row_number** | int | Row number in the import file when applicable (1-based for data rows; 0 may be used for file-level issues such as headers) | [optional] |



_PureCloudPlatformClientV2 265.0.0_
