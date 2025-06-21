# DecisionTable

## DecisionTable

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str |  | [optional] |
| **division** | [Division](Division) | The division to which this entity belongs. | [optional] |
| **description** | str | The decision table description. | [optional] |
| **date_created** | datetime | UTC date time indicating when this decision table was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | UTC date time indicating when this decision table was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_published** | datetime | UTC date time indicating when this decision table was published. Null if never published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **published** | [DecisionTableVersionEntity](DecisionTableVersionEntity) | The entity reference to the most recently published decision table version. Null if never published. | [optional] |
| **latest** | [DecisionTableVersionEntity](DecisionTableVersionEntity) | The entity reference to the most recently created decision table version. | [optional] |
| **columns** | [DecisionTableColumns](DecisionTableColumns) | The column definitions of this decision table. | [optional] |
| **published_contract** | [DecisionTableContract](DecisionTableContract) | The published contract information for this decision table. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 231.0.0_
