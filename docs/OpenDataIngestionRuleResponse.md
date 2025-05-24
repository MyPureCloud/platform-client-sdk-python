# OpenDataIngestionRuleResponse

## OpenDataIngestionRuleResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | ID of the open data ingestion rule. | [optional] |
| **name** | str | The name of the data ingestion rule. | [optional] |
| **description** | str | A description of the data ingestion rule. | [optional] |
| **status** | str | The status of the data ingestion rule. | [optional] |
| **version** | int | The version number of the data ingestion rule. | [optional] |
| **date_created** | datetime | Timestamp indicating when the data ingestion rule was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Timestamp indicating when the data ingestion rule was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **platform** | str | The platform of the data ingestion rule. | [optional] |
| **external_source** | [DomainEntityRef](DomainEntityRef) | The external source associated with this open data ingestion rule, which is used when performing identity resolution | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 229.0.0_
