# DecisionTableVersion

## DecisionTableVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **version** | int | The decision table version. | [optional] |
| **status** | str | Current status of this decision table version | [optional] |
| **description** | str | The decision table description. | [optional] |
| **row_count** | int | The number of rows in this decision table version. | [optional] |
| **rows_uri** | str | The rows URI for this decision table version. | [optional] |
| **date_created** | datetime | UTC date time indicating when this decision table version was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | UTC date time indicating when this decision table version was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_published** | datetime | UTC date time indicating when this decision table version was published. Null if never published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **columns** | [DecisionTableColumns](DecisionTableColumns) | The column definitions of this decision table version. | [optional] |
| **contract** | [DecisionTableContract](DecisionTableContract) | The contract information for this decision table version. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 237.0.0_
