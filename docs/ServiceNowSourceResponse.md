# ServiceNowSourceResponse

## ServiceNowSourceResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **name** | str | Name of the source. | [optional] |
| **date_created** | datetime | Source creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Source last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **type** | str | The source type. | [optional] |
| **integration** | [KnowledgeIntegrationReference](KnowledgeIntegrationReference) | The reference to the integration associated with the source. | [optional] |
| **schedule_period** | int | The schedule period of the source in hours. | [optional] |
| **last_sync** | [SourceLastSync](SourceLastSync) | Additional information about the last synchronization of the source. | [optional] |
| **settings** | [ServiceNowSettings](ServiceNowSettings) | The settings of the source. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 215.0.0_
