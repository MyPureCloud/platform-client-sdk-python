# KnowledgeDocumentFeedback

## KnowledgeDocumentFeedback

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | str | The globally unique identifier for the object. | [optional] |
| **document_variation** | [EntityReference](EntityReference) | The variation of the document on which feedback was given. | |
| **rating** | str | Feedback rating. | |
| **reason** | str | Feedback reason. | [optional] |
| **comment** | str | Free-text comment of the feedback. Maximum length: 2000 characters. | [optional] |
| **search** | [EntityReference](EntityReference) | The search that surfaced the document on which feedback was given. | [optional] |
| **session_id** | str | Knowledge guest session ID. | [optional] |
| **date_created** | datetime | The date and time of the feedback. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **query_type** | str | The type of the query that surfaced the document on which the feedback was given. | [optional] |
| **surfacing_method** | str | The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.Generative: A generated answer in a snippet was shown. | [optional] |
| **state** | str | The state of the feedback. | [optional] |
| **document** | [KnowledgeDocumentVersionReference](KnowledgeDocumentVersionReference) | The document on which feedback was given. | |
| **application** | [KnowledgeSearchClientApplication](KnowledgeSearchClientApplication) | The client application from which feedback was given. | |
| **conversation_context** | [KnowledgeConversationContext](KnowledgeConversationContext) | Conversation context information if the feedback is given in the context of a conversation. | [optional] |
| **user_id** | str | The ID of the user who created the feedback. | [optional] |
| **self_uri** | str | The URI for this object | [optional] |



_PureCloudPlatformClientV2 247.0.0_
