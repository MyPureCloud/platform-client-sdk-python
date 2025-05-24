# DecisionTableRow

## DecisionTableRow

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **table** | [DecisionTableVersionEntity](DecisionTableVersionEntity) | The decision table to which this row belongs | |
| **row_index** | int | The absolute index of this row in the decision table, starting at 0 | [optional] |
| **date_created** | datetime | The date when this row was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The date when this row was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **inputs** | [dict(str, DecisionTableRowParameterValue)](DecisionTableRowParameterValue) | The map input values of the row being created. At least one value must be provided. The key for this map is the column ID the row value relates | [optional] |
| **outputs** | [dict(str, DecisionTableRowParameterValue)](DecisionTableRowParameterValue) | The map output values of the row being created. At least one value must be provided. The key for this map is the column ID the row value relates | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
