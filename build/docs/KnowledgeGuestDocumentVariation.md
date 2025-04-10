# KnowledgeGuestDocumentVariation

## KnowledgeGuestDocumentVariation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the variation. | [optional] |
| **date_created** | datetime | The creation date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | The last modification date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **document_version** | [AddressableEntityRef](AddressableEntityRef) | The version of the document. | [optional] |
| **contexts** | [list[KnowledgeGuestDocumentVariationContext]](KnowledgeGuestDocumentVariationContext) | The context values associated with the variation. | |
| **document** | [AddressableEntityRef](AddressableEntityRef) | The reference to document to which the variation is associated. | [optional] |
| **body** | [DocumentBodyResponse](DocumentBodyResponse) | The content for the variation. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 225.0.0_
