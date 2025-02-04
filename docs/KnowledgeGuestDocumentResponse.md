# KnowledgeGuestDocumentResponse

## KnowledgeGuestDocumentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **title** | str | Document title, having a limit of 500 words. | [optional] |
| **visible** | bool | Indicates if the knowledge document should be included in search results. | [optional] |
| **alternatives** | [list[KnowledgeDocumentAlternative]](KnowledgeDocumentAlternative) | List of alternate phrases related to the title which improves search results. | [optional] |
| **state** | str | State of the document. | [optional] |
| **date_created** | datetime | Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | datetime | Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_imported** | datetime | Document import date-time, or null if was not imported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **last_published_version_number** | int | The last published version number of the document. | [optional] |
| **date_published** | datetime | The date on which the document was last published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [UserReference](UserReference) | The user who created the document. | [optional] |
| **modified_by** | [UserReference](UserReference) | The user who modified the document. | [optional] |
| **document_version** | [AddressableEntityRef](AddressableEntityRef) | The version of the document. | [optional] |
| **session_id** | str | ID of the guest session. | [optional] |
| **category** | [GuestCategoryReference](GuestCategoryReference) | The reference to category associated with the document. | [optional] |
| **variations** | [list[KnowledgeGuestDocumentVariation]](KnowledgeGuestDocumentVariation) | Variations of the document. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 221.0.0_
