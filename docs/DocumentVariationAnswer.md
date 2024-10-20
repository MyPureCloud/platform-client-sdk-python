# DocumentVariationAnswer

## DocumentVariationAnswer

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the variation. | [optional] |
| **date_created** | datetime | The creation date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The last modification date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **document_version** | [AddressableEntityRef](AddressableEntityRef) | The version of the document. | [optional] |
| **contexts** | [list[DocumentVariationContext]](DocumentVariationContext) | The context values associated with the variation. | |
| **document** | [KnowledgeDocumentReference](KnowledgeDocumentReference) | The reference to document to which the variation is associated. | [optional] |
| **priority** | int | The priority of the variation. | [optional] |
| **name** | str | The name of the variation. | [optional] |
| **body** | [DocumentBodyWithHighlight](DocumentBodyWithHighlight) | The content for the variation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 214.0.0_
