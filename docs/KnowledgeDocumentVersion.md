# KnowledgeDocumentVersion

## KnowledgeDocumentVersion

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | Globally unique identifier for the document version. | [optional] |
| **date_published** | datetime | Published date of document version. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **document** | [KnowledgeDocumentResponse](KnowledgeDocumentResponse) | The document which is versioned. | [optional] |
| **restore_from_version_id** | str | The globally unique identifier for the document version. If the value is provided, the document is restored to the given version. If not, it publishes the draft changes as a new version of the document. | |
| **version_number** | int | Version Number of the document. | [optional] |
| **date_expires** | datetime | Expiry date of document version, applicable only to the &#39;Archived&#39; version of the document. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 216.0.0_
