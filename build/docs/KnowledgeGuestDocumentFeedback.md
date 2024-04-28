---
title: KnowledgeGuestDocumentFeedback
---
## KnowledgeGuestDocumentFeedback

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **document_variation** | [**EntityReference**](EntityReference.html) | The variation of the document on which feedback was given. | |
| **rating** | **str** | Feedback rating. | |
| **reason** | **str** | Feedback reason. | [optional] |
| **comment** | **str** | Free-text comment of the feedback. Maximum length: 2000 characters. | [optional] |
| **search** | [**EntityReference**](EntityReference.html) | The search that surfaced the document on which feedback was given. | [optional] |
| **session_id** | **str** | Knowledge guest session ID. | [optional] |
| **date_created** | **datetime** | The date and time of the feedback. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **query_type** | **str** | The type of the query that surfaced the document on which the feedback was given. | [optional] |
| **surfacing_method** | **str** | The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown. | [optional] |
| **state** | **str** | The state of the feedback. | [optional] |
| **document** | [**KnowledgeGuestDocumentVersionReference**](KnowledgeGuestDocumentVersionReference.html) | The document on which feedback was given. | |
| **application** | [**KnowledgeGuestSearchClientApplication**](KnowledgeGuestSearchClientApplication.html) | The client application from which feedback was given. | [optional] |
{: class="table table-striped"}


