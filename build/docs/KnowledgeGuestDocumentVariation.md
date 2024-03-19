---
title: KnowledgeGuestDocumentVariation
---
## KnowledgeGuestDocumentVariation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the variation. | [optional] |
| **date_created** | **datetime** | The creation date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | The last modification date-time for the document variation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **document_version** | [**AddressableEntityRef**](AddressableEntityRef.html) | The version of the document. | [optional] |
| **contexts** | [**list[KnowledgeGuestDocumentVariationContext]**](KnowledgeGuestDocumentVariationContext.html) | The context values associated with the variation. | |
| **document** | [**AddressableEntityRef**](AddressableEntityRef.html) | The reference to document to which the variation is associated. | [optional] |
| **body** | [**DocumentBody**](DocumentBody.html) | The content for the variation. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


