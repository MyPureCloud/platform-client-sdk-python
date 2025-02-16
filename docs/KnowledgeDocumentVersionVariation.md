# KnowledgeDocumentVersionVariation

## KnowledgeDocumentVersionVariation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the variation. | [optional] |
| **date_created** | datetime | The creation date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The last modification date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **contexts** | [list[DocumentVariationContext]](DocumentVariationContext) | The context values associated with the variation. | |
| **priority** | int | The priority of the variation. | [optional] |
| **name** | str | The name of the variation. | [optional] |
| **body** | [DocumentBodyResponse](DocumentBodyResponse) | The content for the variation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |
| **document_version** | [AddressableEntityRef](AddressableEntityRef) | Reference to the document version to which the variation is associated with. | [optional] |



_PureCloudPlatformClientV2 222.0.0_
